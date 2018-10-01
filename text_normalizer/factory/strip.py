from typing import List, Tuple
import re

from .toolkit.search_all import search_all
from .toolkit.transform import transform
from .base_factory import BaseFactory


PATTERNS = {
    "left": re.compile(r"\A\s+.{0,1}"),
    "right": re.compile(r".{0,1}\s+\Z"),
    "both": re.compile(r"\A\s+.{0,1}|.{0,1}\s+\Z"),
    "rep": re.compile(r"[^\s]+"),
}


class Strip(BaseFactory):

    def __init__(
            self,
            direction: str = 'both',
            name: str = 'strip',
        ):
        if direction not in ['both', 'left', 'right']:
            raise ValueError(
                'WRONG direction input! '
                'Direction has three options [both, left, right]',
                'Your input is {}'.format(direction),
            )
        else:
            self.direction = direction
            self.pattern = PATTERNS[direction]

        super().__init__(
            name=name + '_' + self.direction,
            denormalizable=True,
        )


    @staticmethod
    def gen_backward_annotations(
        forward_annotations: List[Tuple[int, int, str]]):
        output = []
        offset = 0
        for anno in forward_annotations:
            rep = PATTERNS["rep"].findall(anno[2])
            if len(rep) > 0:
                rep = rep[0]
            else:
                rep = ""
            new_start = offset + anno[0]
            new_end = new_start + len(rep)
            output.append(
                (
                    new_start,
                    new_end,
                    rep,
                ),
            )
            offset = new_end - anno[1]
        return output


    def normalize(
            self,
            sentence: str,
        ) -> (str, List[dict]):

        forward_annotations = search_all(
            input_str=sentence,
            reg_pattern=self.pattern,
        )
        backward_annotations = self.gen_backward_annotations(
            forward_annotations)

        output_str = transform(
            input_str=sentence,
            forward_annotations=forward_annotations,
            backward_annotations=backward_annotations,
        )
        return output_str, {
            'for': forward_annotations,
            'back': backward_annotations,
        }

    def denormalize(
            self,
            sentence: str,
            meta: dict,
        ) -> str:
        forward_annotations = meta['for']
        backward_annotations = meta['back']
        output_str = transform(
            input_str=sentence,
            forward_annotations=backward_annotations,
            backward_annotations=forward_annotations,
        )
        return output_str
