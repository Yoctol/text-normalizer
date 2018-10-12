from typing import List, Tuple
import re

from .toolkit.search_all import search_all
from .toolkit.transform import transform
from .base_factory import BaseFactory


PATTERNS = {
    "left": re.compile(r"\A\s+"),
    "right": re.compile(r"\s+\Z"),
    "both": re.compile(r"\A\s+|\s+\Z"),
    "rep": '',
}


class Strip(BaseFactory):

    def __init__(
            self,
            direction: str = 'both',
            name: str = 'strip',
        ):
        if direction not in ['both', 'left', 'right']:
            raise ValueError(
                'Not Supported Yet!!'
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
            # rep = PATTERNS["rep"].findall(anno[2])
            # if len(rep) > 0:
            #     rep = rep[0]
            # else:
            #     rep = ""
            new_start = offset + anno[0]
            new_end = new_start + len(PATTERNS["rep"])
            output.append(
                (
                    new_start,
                    new_end,
                    PATTERNS["rep"],
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
            'forward': forward_annotations,
            'backward': backward_annotations,
        }

    def denormalize(
            self,
            sentence: str,
            meta: dict,
        ) -> str:
        forward_annotations = meta['forward']
        backward_annotations = meta['backward']
        output_str = transform(
            input_str=sentence,
            forward_annotations=backward_annotations,
            backward_annotations=forward_annotations,
        )
        return output_str
