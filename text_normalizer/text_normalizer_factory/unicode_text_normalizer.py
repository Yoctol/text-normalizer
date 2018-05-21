from typing import List, Dict, Tuple
import re

from .base_text_normalizer import BaseTextNormalizer


PROG = re.compile(r"([0-9A-Z\s\-]+)\:([0-9A-Za-z]+)")
PROG_DASH = re.compile(r"([0-9A-Z]+)\-([0-9A-Z]+)")


class UnicodeTextNormalizer(BaseTextNormalizer):

    def __init__(
            self,
            unicode_mapping_path: str,
            other: hex = "0x20",
            name: str = 'unicode_normalizer',
            denormalizable: bool = True,
        ) -> None:

        self.denormalizable = denormalizable
        self.mapping_table = self._gen_unicode_mapping_table(
            unicode_mapping_path=unicode_mapping_path,
        )
        if len(other) > 0:
            self.u_other = other
            self.other = chr(int(other, 16))
        else:
            self.u_other = None
            self.other = other
            self.denormalizable = False

        super().__init__(
            name=name,
            denormalizable=self.denormalizable,
        )

    @staticmethod
    def _gen_unicode_mapping_table(
            unicode_mapping_path: str,
        ) -> Dict[hex, str]:

        with open(unicode_mapping_path, "r") as filep:
            mapping_list = filep.read().split("\n")

        mapping_table = {}
        for map_ in mapping_list:

            if len(map_) == 0:
                continue

            input_, output = PROG.findall(map_)[0]

            range_or_not = PROG_DASH.findall(input_)

            if len(range_or_not) > 0:
                for uninum in range(
                    int(range_or_not[0][0], 16),
                    int(range_or_not[0][1], 16) + 1,
                ):
                    if output == "one2one":
                        output_token = chr(uninum)
                    else:
                        output_token = chr(int(output, 16))
                    mapping_table[hex(uninum)] = output_token
            else:
                for uninum in input_.split(" "):
                    mapping_table[hex(int(uninum, 16))] = chr(int(output, 16))

        return mapping_table

    @staticmethod
    def _check_utf8_encoding(sentence: str):

        try:
            output_sentence = sentence.encode('utf-8').decode('utf-8')
        except UnicodeEncodeError as e:
            print("sentence: {}, error: {}".format(sentence, e))
            return False
        if output_sentence != sentence:
            return False

        return True

    def normalize(
            self,
            sentence: str,
        ) -> Tuple[str, Dict[str, List[str]]]:

        if not self._check_utf8_encoding(sentence):
            raise ValueError(
                "sentence: {} can not be encoded by UTF-8".format(sentence),
            )

        output_sentence = []
        meta = {}
        for char in sentence:
            uchar = hex(ord(char))
            if uchar in self.mapping_table:
                output_char = self.mapping_table[uchar]
            else:
                output_char = self.other
            if output_char not in meta:
                meta[output_char] = [char]
            else:
                meta[output_char].extend(char)
            output_sentence.append(output_char)

        return "".join(output_sentence), meta

    def denormalize(
            self,
            sentence: str,
            meta: Dict[str, List[str]],
        ) -> str:

        if not self.denormalizable:
            return sentence

        for org_o, org_i in meta.items():
            splited_sent = sentence.split(org_o)
            output_sentence = []
            for i, token in enumerate(splited_sent):
                output_sentence.append(token)
                if i != len(org_i):
                    output_sentence.append(org_i[i])
            sentence = "".join(output_sentence)

        return sentence
