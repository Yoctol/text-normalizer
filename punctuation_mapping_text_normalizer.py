from typing import List
import re

import pandas as pd
from .base_text_normalizer import BaseTextNormalizer

SpecialCases = {
    '\\': '\\\\',
}


class PunctuationMappingTextNormalizer(BaseTextNormalizer):

    def __init__(
            self,
            normalization_table_path: str,
            denormalizable: bool = True,
            name: str = 'punctuation_normalizer',
        ) -> None:
        super().__init__(name=name, denormalizable=True)
        remove_space = re.compile(r"\s+")
        table_df = pd.read_csv(normalization_table_path).astype(str)
        for column in table_df.columns.tolist():
            table_df[column] = table_df[column].str.strip()
        table_dict = table_df.to_dict(orient='index')

        self.patterns = []
        for idx, mapping in table_dict.items():
            cleaned_before_pattern = remove_space.sub(" ", mapping["before"])
            before_pattern_list = cleaned_before_pattern.split(" ")
            escaped_before_pattern_list = [
                re.escape(pat) for pat in list(set(before_pattern_list))]
            escaped_after_pattern = re.escape(mapping["after"])
            self.patterns.append(
                {
                    "normalization_pattern": re.compile(
                        r"{}".format("|".join(escaped_before_pattern_list)),
                    ),
                    "denormalization_pattern": re.compile(
                        r"{}".format(escaped_after_pattern),
                    ),
                    "replacement": mapping["after"],
                },
            )

    def normalize(
            self,
            sentence: str,
        ) -> (str, List[dict]):
        revised_sentence = sentence
        meta = []
        for pattern in self.patterns:
            if pattern["replacement"] in SpecialCases:
                pattern["replacement"] = SpecialCases[pattern["replacement"]]
            # if pattern["replacement"] == '"':
            #     pattern["replacement"] = '\"'
            revised_sentence = pattern["normalization_pattern"].sub(
                repl=pattern["replacement"],
                string=revised_sentence,
            )
            meta.append(
                {
                    "before": pattern["normalization_pattern"].findall(
                        string=sentence,
                    ),
                    "after": pattern["replacement"],
                }
            )
        return revised_sentence, meta

    def denormalize(
            self,
            sentence: str,
            meta: List[List[str]],
        ) -> str:
        if super().denormalize(sentence=sentence):
            # Case1: self.denormalizable = False
            return sentence

        for single_meta, pattern in zip(meta[::-1], self.patterns[::-1]):
            if single_meta["after"] != pattern["replacement"]:
                KeyError(
                    "WRONG META !!!",
                    "The AFTER token should be the same as REPLACEMENT in patterns",
                    "Now, AFTER token is {} and REPLACEMENT is {}".format(
                        single_meta["after"],
                        self.pattern["replacement"],
                    )
                )
            punct_to_be_denormalized = pattern["denormalization_pattern"].findall(
                string=sentence,
            )
            if len(punct_to_be_denormalized) != len(single_meta["before"]):
                raise KeyError(
                    "The number of punctuation to be denormalized is not equal to",
                    "the number of that in meta data \n",
                    "# of punctuations to be denormalized = {}\n".format(
                        len(punct_to_be_denormalized)
                    ),
                    "punctuations in meta = {}".format(single_meta["before"]),
                )
            for punct in single_meta["before"]:
                sentence = pattern["denormalization_pattern"].sub(
                    repl=punct,
                    string=sentence,
                    count=1,
                )
        return sentence
