from typing import List


class BaseTextNormalizer(object):

    def __init__(
            self,
            denormalizable: bool = False,
            name: str = None,
        ) -> None:
        self.denormalizable = denormalizable
        if name is None:
            self.name = self.__class__.__name__
        else:
            self.name = name

    def normalize(
            self,
            sentence: str,
        ) -> (str, List[dict]):
        raise NotImplementedError

    def denormalize(
            self,
            sentence: str,
            meta: dict = None,
        ) -> str:
        '''
        If the text normalizer is denormalizable, then this method should be implemented.
        '''
        if not self.denormalizable:
            return sentence

    # def ldenormalize(
    #         self,
    #         sentence: List[str],
    #         meta: dict = None,
    #     ) -> str:
    #     if not self.denormalizable:
    #         return sentence
