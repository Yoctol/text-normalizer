# -*- coding: utf-8 -*-
from unittest import TestCase

from ..basic_text_normalizer_collection import (
    basic_text_normalizer_collection,
    number_with_digits_text_normalizer_collection,
)


class BasicNormalizerCollectionTestCase(TestCase):

    def test_basic_text_normalizer_collection(self):
        normalizer = basic_text_normalizer_collection
        test_cases = [
            (
                '我在85.33度C買了一杯(*999*)的咖啡--',
                '我在 _float_ 度c買了一杯 _int_ 的咖啡',
                '我在85.33度C買了一杯999的咖啡',
            ),
            (
                '++',
                '',
                '',
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
                    test_case[2],
                    recovered_sentence,
                )

    def test_number_with_digits_text_normalizer_collection(self):
        normalizer = number_with_digits_text_normalizer_collection
        test_cases = [
            (
                '我在85.33度C買了一杯(*999*)的咖啡--',
                '我在 _2float2_ 度c買了一杯 _3int_ 的咖啡',
                '我在85.33度C買了一杯999的咖啡',
            ),
            (
                '++??',
                '',
                '',
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
                    test_case[2],
                    recovered_sentence,
                )
