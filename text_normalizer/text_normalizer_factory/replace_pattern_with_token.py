from typing import List
import re

from .base_text_normalizer import BaseTextNormalizer


class ReplacePatternWithToken(BaseTextNormalizer):

    def __init__(
            self,
            target_pattern: str,
            token: str,
            prefix_pattern: str = None,
            suffix_pattern: str = None,
            denormalizable: bool = False,
            name: str = None,
        ):
        super().__init__(name=name, denormalizable=denormalizable)
        self.token = token
        if prefix_pattern and suffix_pattern:
            self.findall_pattern = "(?:{})({})(?={})".format(
                prefix_pattern,
                target_pattern,
                suffix_pattern,
            )
            self.sub_pattern = "({}){}(?={})".format(
                prefix_pattern,
                target_pattern,
                suffix_pattern,
            )
            self.sub_replacement = "\g<1>{}".format(token)
        else:
            self.findall_pattern = target_pattern
            self.sub_pattern = target_pattern
            self.sub_replacement = token

        self.findall_prog = re.compile(self.findall_pattern)
        self.sub_prog = re.compile(self.sub_pattern)
        self.split_prog = re.compile(
            '{}|{}|{}|{}'.format(
                self.token,
                self.token.rstrip(),
                self.token.lstrip(),
                self.token.strip(),
            ),
        )

    def normalize(
            self,
            sentence: str,
        ) -> (str, List[dict]):
        revised_sentence = self.sub_prog.sub(
            repl=self.sub_replacement,
            string=sentence,
        )
        if self.denormalizable:
            meta = self.findall_prog.findall(
                string=sentence,
            )
            return revised_sentence, {self.token: meta}
        else:
            return revised_sentence, None

    def denormalize(
            self,
            sentence: str,
            meta: dict = None,
        ) -> str:
        if not self.denormalizable:
            # Case1: self.denormalizable = False
            return sentence

        if self.token not in meta:
            # Case2: meta = {'a': ['XX', 'cc']}, 'a' != self.token
            raise KeyError(
                'Wrong meta :{} !!!'.format(meta),
                'Meta should be { %s: [...]}.' % self.token,
            )

        splited_sentence = self.split_prog.split(sentence)
        if (len(splited_sentence) == 1) and (len(meta[self.token]) == 0):
            # Case3: no token in sentence and meta is empty
            return sentence
        elif len(splited_sentence) - 1 != len(meta[self.token]):
            # Case4: # of token in sentence != # of token in meta
            raise ValueError(
                '# of tokens in sentence is not equal to that in meta'
                'sentence = {}'.format(sentence),
                'meta = {}'.format(meta),
            )
        else:
            output_sentence = ''
            idx = 0
            for s_idx, segment in enumerate(splited_sentence, start=1):
                output_sentence += segment
                if s_idx != len(splited_sentence):
                    output_sentence += meta[self.token][idx]
                    idx += 1
            return output_sentence

    # def ldenormalize(
    #         self,
    #         sentence: List[str],
    #         meta: dict = None,
    #     ) -> List[str]:

    #     super().ldenormalize(sentence=sentence)
    #     if self.token not in meta:
    #         raise KeyError('Wrong meta :{} !!!'.format(meta))

    #     '''
    #     Each segment should not contain more than one token.
    #     '''
    #     idx = 0
    #     output_sentence = []
    #     for segment in sentence:
    #         if self.token in segment:
    #             denormalized_segment = re.sub(self.token, meta[self.token][idx], segment)
    #             output_sentence.append(denormalized_segment)
    #             idx += 1
    #         else:
    #             output_sentence.append(segment)
    #     return output_sentence
