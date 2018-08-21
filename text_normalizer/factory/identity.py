from typing import List

from .base_factory import BaseFactory


class Identity(BaseFactory):

    def __init__(self):
        super().__init__(name='identity', denormalizable=False)

    def normalize(
            self,
            sentence: str,
        ) -> (str, List[dict]):
        return sentence, None
