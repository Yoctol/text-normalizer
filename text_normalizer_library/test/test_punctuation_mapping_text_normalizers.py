# -*- coding: utf-8 -*-
from unittest import TestCase

from ..punctuation_mapping_text_normalizers import (
    full_punctuation_mapping_text_normalizer,
    simplified_punctuation_mapping_text_normalizer,
)


class PunctuationMappingTextNormalizerTestCase(TestCase):

    def run_test(self, test_cases, normalizer):
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                revised_sentence, meta = normalizer.normalize(
                    sentence=test_case[0],
                )
                self.assertEqual(
                    test_case[1],
                    revised_sentence,
                )
                recovered_sentence = normalizer.denormalize(
                    sentence=test_case[1],
                    meta=meta,
                )
                self.assertEqual(
                    test_case[0],
                    recovered_sentence,
                )

    def test_full_punctuation_mapping_text_normalizer(self):
        test_cases = [
            (
                "符號， 、 。 ． ？ ！ ～ ＄ ％ ＠ ＆ ＃ ＊ ‧ ， 、 。 ． ？ ！ ～ ＄ ％ ＠ ＆ ＃ ＊ ‧",
                "符號, , . . ? ! ~ $ % @ & # * . , , . . ? ! ~ $ % @ & # * .",
            ),
            (
                "； ︰ … ﹐ ﹒ ˙ · ﹔ ﹕ ‘ ’ “ ” 〝 〞 ； ︰ … ﹐ ﹒ ˙ · ﹔ ﹕ ‘ ’ “ ” 〝 〞",
                "; : ... , . . . ; : \" \" \" \" \" \" ; : ... , . . . ; : \" \" \" \" \" \"",
            ),
            (
                "括號符號； 〔 〕 【 】 ﹝ ﹞ 〈 〉 ﹙ ﹚ 《 》 （ ） ； 〔 〕 【 】 ﹝ ﹞ 〈 〉 ﹙ ﹚ 《 》 （ ）",
                "括號符號; [ ] [ ] [ ] < > ( ) < > ( ) ; [ ] [ ] [ ] < > ( ) < > ( )",
            ),
            (
                "｛ ｝ ﹛ ﹜ 『 』 「 」 ＜ ＞ ≦ ≧ ﹤ ﹥ ｛ ｝ ﹛ ﹜ 『 』 「 」 ＜ ＞ ≦ ≧ ﹤ ﹥",
                "{ } { } \" \" \" \" < > < > < > { } { } \" \" \" \" < > < > < >",
            ),
            (
                "括號符號； ︵ ︶ ︷ ︸ ︹ ︺ ︻ ︼ ︽ ︾ ︿ ﹀ ﹁ ﹂ ﹃ ﹄  ︵ ︶ ︷ ︸ ︹ ︺ ︻ ︼ ︽ ︾ ︿ ﹀ ﹁ ﹂ ﹃ ﹄",
                "括號符號; ( ) { } [ ] [ ] < > < > \" \" \" \"  ( ) { } [ ] [ ] < > < > \" \" \" \"",
            ),
            (
                "線段符號； ﹣ ﹦ ≡ ｜ ∣ ∥ – ︱ — ︳ ╴ ¯ ￣ ﹉ ﹣ ﹦ ≡ ｜ ∣ ∥ – ︱ — ︳ ╴ ¯ ￣ ﹉",
                "線段符號; - = = | | / - | - | - - - - - = = | | / - | - | - - - -",
            ),
            (
                "﹊ ﹍ ﹎ ﹋ ﹌ ﹏ ︴ ﹨ ∕ ╲ ╱ ＼ ／ ﹊ ﹍ ﹎ ﹋ ﹌ ﹏ ︴ ﹨ ∕ ╲ ╱ ＼ ／",
                "- _ _ - - _ | \ / \ / \ / - _ _ - - _ | \ / \ / \ /",
            ),
            (
                "+ ＋ ＋ ﹢ * ＊ × ╳",
                "+ + + + * * * *",
            ),
        ]
        self.run_test(test_cases, normalizer=full_punctuation_mapping_text_normalizer)

    def test_simplified_punctuation_mapping_text_normalizer(self):
        test_cases = [
            (
                "符號， 、 。 ． ？ ！ ～ ＄ ％ ＠ ＆ ＃ ＊ ‧ ， 、 。 ． ？ ！ ～ ＄ ％ ＠ ＆ ＃ ＊ ‧",
                "符號, , . . ? ! - $ % @ & # * . , , . . ? ! - $ % @ & # * .",
            ),
            (
                "； ︰ … ﹐ ﹒ ˙ · ﹔ ﹕ ‘ ’ “ ” 〝 〞  ︰ … ﹐ ﹒ ˙ · ﹔ ﹕ ‘ ’ “ ” 〝 〞",
                "; : ... , . . . ; : \" \" \" \" \" \"  : ... , . . . ; : \" \" \" \" \" \"",
            ),
            (
                "括號符號； 〔 〕 【 】 ﹝ ﹞ 〈 〉 ﹙ ﹚ 《 》 （ ） 〔 〕 【 】 ﹝ ﹞ 〈 〉 ﹙ ﹚ 《 》 （ ）",
                "括號符號; ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( ) ( )",
            ),
            (
                "｛ ｝ ﹛ ﹜ 『 』 「 」 ＜ ＞ ≦ ≧ ﹤ ﹥ ｛ ｝ ﹛ ﹜ 『 』 「 」 ＜ ＞ ≦ ≧ ﹤ ﹥",
                "( ) ( ) \" \" \" \" ( ) ( ) ( ) ( ) ( ) \" \" \" \" ( ) ( ) ( )",
            ),
            (
                "括號符號； ︵ ︶ ︷ ︸ ︹ ︺ ︻ ︼ ︽ ︾ ︿ ﹀ ﹁ ﹂ ﹃ ﹄ ︵ ︶ ︷ ︸ ︹ ︺ ︻ ︼ ︽ ︾ ︿ ﹀ ﹁ ﹂ ﹃ ﹄",
                "括號符號; ( ) ( ) ( ) ( ) ( ) ( ) \" \" \" \" ( ) ( ) ( ) ( ) ( ) ( ) \" \" \" \"",
            ),
            (
                "線段符號； ﹣ ﹦ ≡ ｜ ∣ ∥ – ︱ — ︳ ╴ ¯ ￣ ﹉ ﹣ ﹦ ≡ ｜ ∣ ∥ – ︱ — ︳ ╴ ¯ ￣ ﹉",
                "線段符號; - = = , , , - , - , - - - - - = = , , , - , - , - - - -",
            ),
            (
                "﹊ ﹍ ﹎ ﹋ ﹌ ﹏ ︴ ﹨ ∕ ╲ ╱ ＼ ／ ﹊ ﹍ ﹎ ﹋ ﹌ ﹏ ︴ ﹨ ∕ ╲ ╱ ＼ ／",
                "- _ _ - - _ , , , , , , , - _ _ - - _ , , , , , , ,",
            ),
        ]
        self.run_test(test_cases, normalizer=simplified_punctuation_mapping_text_normalizer)
