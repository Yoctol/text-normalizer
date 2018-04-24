from typing import List, Dict, Tuple
import re

from .base_text_normalizer import BaseTextNormalizer


class EngLowercaseTextNormalizer(BaseTextNormalizer):

    def __init__(self, name='eng_lowercase'):
        super().__init__(name=name, denormalizable=True)
        self.fullwidth_uppercase = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
        self.fullwidth_lowercase = "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
        self.halfwidth_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.halfwidth_lowercase = "abcdefghijklmnopqrstuvwxyz"

        self.pattern = "[a-zA-Z{}{}]+".format(
            self.fullwidth_uppercase,
            self.fullwidth_lowercase,
        )
        self.findall_prog = re.compile(self.pattern)
        self.mapping_table = self.gen_table()

    def gen_table(self) -> Dict[str, str]:
        table = {}
        for index in range(26):
            table[self.fullwidth_uppercase[index]] = \
                self.halfwidth_lowercase[index]
            table[self.fullwidth_lowercase[index]] = \
                self.halfwidth_lowercase[index]
            table[self.halfwidth_uppercase[index]] = \
                self.halfwidth_lowercase[index]
        return table

    def lowercase(self, sentence: str) -> str:
        output = []
        for char in sentence:
            if char in self.mapping_table:
                output.append(self.mapping_table[char])
            else:
                output.append(char)
        return ''.join(output)

    def normalize(
            self,
            sentence: str,
        ) -> Tuple[str, List[dict]]:
        eng_words = self.findall_prog.findall(sentence)
        if len(eng_words) == 0:
            return sentence, None
        else:
            meta = []
            for eng_word in eng_words:
                meta.append(
                    {
                        'before': eng_word,
                        'after': self.lowercase(eng_word),
                    },
                )
            return self.lowercase(sentence), meta

    def denormalize(
            self,
            sentence: str,
            meta: List[dict] = None,
        ) -> str:
        if (not self.denormalizable) or (meta is None):
            # Case1: self.denormalizable = False
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
