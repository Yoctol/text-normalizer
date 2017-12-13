from typing import List


class BaseTextNormalizerCollection(object):

    def __init__(self):
        self.text_normalizers = []

    def add_text_normalizer(
            self,
            text_normalizer: object,
        ) -> None:
        '''
        TODO: Ensure str_filter is a subclass of BaseFilter
        '''
        self.text_normalizers.append(text_normalizer)

    def clear_text_normalizers(self):
        self.text_normalizers = []

    def normalize(
            self,
            sentence: str,
        )-> (str, List[dict]):
        sentence = sentence.strip()
        history = []
        for text_normalizer in self.text_normalizers:
            sentence, meta_data = text_normalizer.normalize(sentence=sentence)
            history.append({
                'name': text_normalizer.name,
                'revised_sentence': sentence,
                'meta_data': meta_data,
            })
        return sentence.strip(), history

    def denormalize(
            self,
            sentence: str,
            history: List[dict],
        ) -> str:
        for text_normalizer, record in zip(
                self.text_normalizers[::-1],
                history[::-1],
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
    #         history: List[dict],
    #     ):
    #     for str_filter, record in zip(self.filters[::-1], history[::-1]):
    #         if record['name'] == str_filter.name:
    #             sentence = str_filter.lretrieve(
    #                 sentence=sentence,
    #                 meta=record['meta_data'],
    #             )
    #     return sentence
