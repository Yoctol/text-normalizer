from typing import List
import re

from .base_text_normalizer import BaseTextNormalizer


INT_PATTERN = re.compile(r"[0-9０１２３４５６７８９]+(?!float|\_|\d)")
FLOAT_PATTERN = re.compile(
    r"(?<!\.|\d)[0-9０１２３４５６７８９]+\.[0-9０１２３４５６７８９]+(?!\.|\d)",
)


def gen_float_token_with_digit(floats: List[str], token: str = "_{}float{}_"):
    output = []
    for float_str in floats:
        digit_lst = INT_PATTERN.findall(float_str)
        float_token = token.format(len(digit_lst[0]), len(digit_lst[1]))
        output.append(float_token)
    return output


def gen_int_token_with_digit(ints: List[str], token: str = "_{}int_"):
    output = []
    for int_str in ints:
        int_token = token.format(len(int_str))
        output.append(int_token)
    return output


def sub_token_with_value_sequentially(
        sentence: str,
        token: str,
        value_list: List[str],
    ) -> str:
    split_prog = re.compile(
        '{}|{}'.format(
            token,
            token.strip(),
        ),
    )
    splited_sentence = split_prog.split(sentence)
    if len(splited_sentence) != len(value_list) + 1:
        raise ValueError(
            "Number of tokens in sentence should be equal to that of values",
            "original sentence = {}".format(sentence),
            "token = {}".format(token),
            "value_list = {}".format(value_list),
        )

    output_sent = []
    for i, segment in enumerate(splited_sentence):
        output_sent.append(segment)
        if i != len(splited_sentence) - 1:
            output_sent.append(value_list[i])
    return ''.join(output_sent)


CASES = {
    "_int_": {
        "pattern": INT_PATTERN,
    },
    "_float_": {
        "pattern": FLOAT_PATTERN,
    },
    "_{}int_": {
        "pattern": INT_PATTERN,
        "gen_token_with_digit": gen_int_token_with_digit,
    },
    "_{}float{}_": {
        "pattern": FLOAT_PATTERN,
        "gen_token_with_digit": gen_float_token_with_digit,
    },
    " _int_ ": {
        "pattern": INT_PATTERN,
    },
    " _float_ ": {
        "pattern": FLOAT_PATTERN,
    },
    " _{}int_ ": {
        "pattern": INT_PATTERN,
        "gen_token_with_digit": gen_int_token_with_digit,
    },
    " _{}float{}_ ": {
        "pattern": FLOAT_PATTERN,
        "gen_token_with_digit": gen_float_token_with_digit,
    },
}


class NumberTokenTextNormalizer(BaseTextNormalizer):

    def __init__(
            self,
            token: str,
            denormalizable: bool = True,
            name: str = None,
        ) -> None:
        super().__init__(name=name, denormalizable=denormalizable)
        if token not in CASES:
            raise KeyError(
                "This case [{}] is not handled".format(token),
                "Handle cases {} only".format(CASES.keys()),
            )
        self.token = token

    def normalize(
            self,
            sentence: str,
        ) -> (str, dict):
        revised_sentence = CASES[self.token]["pattern"].sub(
            repl=self.token,
            string=sentence,
        )
        value_list = CASES[self.token]["pattern"].findall(string=sentence)
        if "gen_token_with_digit" not in CASES[self.token]:
            if not self.denormalizable:
                return revised_sentence, None
            return revised_sentence, {self.token: value_list}

        #### token with digits ####
        tokens_with_digit = CASES[self.token]["gen_token_with_digit"](
            value_list,
            token=self.token,
        )
        revised_sentence = sub_token_with_value_sequentially(
            sentence=revised_sentence,
            token=self.token,
            value_list=tokens_with_digit,
        )
        if not self.denormalizable:
            return revised_sentence, None

        meta = {}
        for token, value in zip(tokens_with_digit, value_list):
            if token in meta:
                meta[token].append(value)
            else:
                meta[token] = [value]
        return revised_sentence, meta

    def denormalize(
            self,
            sentence: str,
            meta: dict = None,
        ) -> str:
        if meta is None:
            meta = {}
        if (not self.denormalizable) or (len(meta) == 0):
            # Case1: self.denormalizable = False
            return sentence

        for token, values in meta.items():
            sentence = sub_token_with_value_sequentially(
                sentence=sentence,
                token=token,
                value_list=values,
            )
        return sentence
