# -*- coding: utf-8 -*-
from unittest import TestCase

from ..punctuation_keeping_text_normalizer_collection import (
    full_punctuation_keeping_text_normalizer_collection,
    simplified_punctuation_keeping_text_normalizer_collection,
    number_with_digits_n_simplified_punctuation_text_normalizer_collection,
)


class PunctuationKeepingTextNormalizerCollectionTestCase(TestCase):

    def test_full_punctuation_keeping_text_normalizer_collection(self):
        normalizer = full_punctuation_keeping_text_normalizer_collection
        test_cases = [
            (
                "我在85.33度C買了一杯900──1000元的咖啡《ohoh》？？",
                "我在 _float_ 度c買了一杯 _int_ - _int_ 元的咖啡<ohoh>??",
            ),
            (
                "買5──8年五門車～～",
                "買 _int_ - _int_ 年五門車~~",
            ),
        ]
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

    def test_simplified_punctuation_keeping_text_normalizer_collection(self):
        normalizer = simplified_punctuation_keeping_text_normalizer_collection
        test_cases = [
            (
                "我在85.33度C買了一杯900-1000元的咖啡{ohoh}",
                "我在 _float_ 度c買了一杯 _int_ - _int_ 元的咖啡(ohoh)",
            ),
            (
                "買5-8年五門車~",
                "買 _int_ - _int_ 年五門車-",
            ),
        ]
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

    def test_number_with_digits_n_simplified_punctuation_text_normalizer_collection(self):
        normalizer = number_with_digits_n_simplified_punctuation_text_normalizer_collection
        test_cases = [
            (
                "我在85.33度C買了一杯900-1000元的咖啡{ohoh}",
                "我在 _2float2_ 度c買了一杯 _3int_ - _4int_ 元的咖啡(ohoh)",
            ),
            (
                "買5-8年五門車~",
                "買 _1int_ - _1int_ 年五門車-",
            ),
        ]
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
