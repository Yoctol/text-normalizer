from typing import List

from .base_text_normalizer import BaseTextNormalizer


class StripTextNormalizer(BaseTextNormalizer):

    def __init__(
            self,
            chars: List[str] = None,
            direction: str = 'both',
            name: str = 'strip',
        ):
        self.chars = chars
        if self.chars is None:
            self.chars_str = None
        else:
            self.chars_str = ''.join(chars)
        if direction not in ['both', 'left', 'right']:
            raise ValueError(
                'WRONG direction input! '
                'Direction has three options [both, left, right]',
                'Your input is {}'.format(direction),
            )
        else:
            self.direction = direction
        super().__init__(
            name=name + '_' + self.direction + '_' + str(self.chars_str),
            denormalizable=False,
        )

    def normalize(
            self,
            sentence: str,
        ) -> (str, List[dict]):
        if self.direction == 'both':
            return sentence.strip(self.chars_str), None
        elif self.direction == 'left':
            return sentence.lstrip(self.chars_str), None
        elif self.direction == 'right':
            return sentence.rstrip(self.chars_str), None
