from typing import List
import re

from .base_text_normalizer import BaseTextNormalizer


class EngLowercaseTextNormalizer(BaseTextNormalizer):

    def __init__(self, name='eng_lowercase'):
        super().__init__(name=name, denormalizable=True)
        self.pattern = '[a-zA-Z]+'
        self.findall_prog = re.compile(self.pattern)

    def normalize(
            self,
            sentence: str,
        ) -> (str, List[dict]):
        eng_words = self.findall_prog.findall(sentence)
        if len(eng_words) == 0:
            return sentence.lower(), None
        else:
            meta = []
            for eng_word in eng_words:
                meta.append({'before': eng_word, 'after': eng_word.lower()})
            return sentence.lower(), meta

    def denormalize(
            self,
            sentence: str,
            meta: List[dict] = None,
        ):
        if meta is None:
            return sentence
        else:
            begin_index = 0
            output = []
            for single_meta in meta:
                start = sentence.find(single_meta['after'], begin_index)
                if start != -1:
                    if begin_index != start:
                        output.append(sentence[begin_index: start])
                        begin_index = start
                    output.append(single_meta['before'])
                    begin_index += len(single_meta['before'])
            if begin_index != len(sentence):
                output.append(sentence[begin_index:])
            return ''.join(output)
