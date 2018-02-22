# -*- coding: utf-8 -*-
from unittest import TestCase

from ..punctuation_keeping_text_normalizer_collection import (
    punctuation_keeping_text_normalizer_collection,
)


class PunctuationKeepingTextNormalizerCollectionTestCase(TestCase):

    def test_punctuation_keeping_text_normalizer_collection(self):
        test_cases = [
            (
                "我在85.33度C買了一杯900-1000元的咖啡{ohoh}",
                "我在 _float_ 度c買了一杯 _int_ - _int_ 元的咖啡(ohoh)",
            ),
            (
                "買5-8年五門車~",
                "買 _int_ - _int_ 年五門車-",

            )
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                revised_sentence, meta = punctuation_keeping_text_normalizer_collection.normalize(
                    sentence=test_case[0],
                )
                self.assertEqual(
                    test_case[1],
                    revised_sentence,
                )
                recovered_sentence = punctuation_keeping_text_normalizer_collection.denormalize(
                    sentence=test_case[1],
                    meta=meta,
                )
                self.assertEqual(
                    test_case[0],
                    recovered_sentence,
                )
