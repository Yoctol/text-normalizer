from typing import List


class BaseTextNormalizerCollection(object):

    def __init__(self):
        self.text_normalizers = []

    def add_text_normalizers(
            self,
            text_normalizers: List[object],
        ) -> None:
        '''
        TODO: Ensure text normalizer is a subclass of BaseTextNormalizer
        '''
        for text_normalizer in text_normalizers:
            self.text_normalizers.append(text_normalizer)

    def clear_text_normalizers(self):
        self.text_normalizers = []

    def normalize(
            self,
            sentence: str,
        )-> (str, List[dict]):
        meta = []
        for text_normalizer in self.text_normalizers:
            sentence, meta_data = text_normalizer.normalize(sentence=sentence)
            meta.append({
                'name': text_normalizer.name,
                'revised_sentence': sentence,
                'meta_data': meta_data,
            })
        return sentence, meta

    def denormalize(
            self,
            sentence: str,
            meta: List[dict],
        ) -> str:
        for text_normalizer, record in zip(
                self.text_normalizers[::-1],
                meta[::-1],
            ):
            if record['name'] == text_normalizer.name:
                sentence = text_normalizer.denormalize(
                    sentence=sentence,
                    meta=record['meta_data'],
                )
        return sentence.strip()

    # def ldenormalize(
    #         self,
    #         sentence: List[str],
    #         meta: List[dict],
    #     ):
    #     for text_normalizer, record in zip(self.text_normalizers[::-1], meta[::-1]):
    #         if record['name'] == text_normalizer.name:
    #             sentence = text_normalizer.lretrieve(
    #                 sentence=sentence,
    #                 meta=record['meta_data'],
    #             )
    #     return sentence
