# -*- coding: utf-8 -*-
from unittest import TestCase

from ..unicode_text_normalizer_collection import (
    u_zh_text_normalizer_collection_1,
    u_zh_text_normalizer_collection_2,
    u_zh_text_normalizer_collection_3,
    u_zh_text_normalizer_collection_4,
    u_en_text_normalizer_collection_1,
    u_en_text_normalizer_collection_2,
    u_en_text_normalizer_collection_3,
    u_zh_en_text_normalizer_collection_1,
    u_zh_en_text_normalizer_collection_2,
    u_zh_en_text_normalizer_collection_3,
    u_zh_en_text_normalizer_collection_4,
)


class UnicodeTextNormalizerCollectionTestCase(TestCase):

    def unit_test(self, normalizer, test_cases):
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

    def test_u_zh_text_normalizer_collection_1(self):
        normalizer = u_zh_text_normalizer_collection_1
        test_cases = [
            (
                '我在85.33度C買了一杯900──1000元的咖啡《ohoh》？？',
                '我在 度 買了一杯 元的咖啡 ',
            ),
            (
                '買5──8年五門車～～',
                '買 年五門車 ',
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_u_zh_text_normalizer_collection_2(self):
        normalizer = u_zh_text_normalizer_collection_2
        test_cases = [
            (
                '我在85.33度C買了一杯900 1000元的咖啡《ohoh》？？',
                '我在85.33度 買了一杯900 1000元的咖啡 ',
            ),
            (
                '買5──8年五門車～～',
                '買5 8年五門車 ',
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_u_zh_text_normalizer_collection_3(self):
        normalizer = u_zh_text_normalizer_collection_3
        test_cases = [
            (
                '我在85.33度C買了一杯900 1000元的咖啡《ohoh》？？',
                '我在_float_度 買了一杯_int_ _int_元的咖啡 ',
            ),
            (
                '買5──8年五門車～～',
                '買_int_ _int_年五門車 ',
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_u_zh_text_normalizer_collection_4(self):
        normalizer = u_zh_text_normalizer_collection_4
        test_cases = [
            (
                '我在85.333度C買了一杯900 1000元的咖啡《ohoh》？？',
                '我在_2float3_度 買了一杯_3int_ _4int_元的咖啡 ',
            ),
            (
                '買5──8年五門車～～',
                '買_1int_ _1int_年五門車 ',
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_u_en_text_normalizer_collection_1(self):
        normalizer = u_en_text_normalizer_collection_1
        test_cases = [
            (
                'I want to buy 300 cups of $10.7 coffee. OHOH@@',
                'i want to buy 300 cups of $10.7 coffee. ohoh@@',
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_u_en_text_normalizer_collection_2(self):
        normalizer = u_en_text_normalizer_collection_2
        test_cases = [
            (
                'I want    to buy 300 cups of $10.7 coffee. OHOH',
                'i want to buy _int_ cups of $_float_ coffee. ohoh',
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_u_en_text_normalizer_collection_3(self):
        normalizer = u_en_text_normalizer_collection_3
        test_cases = [
            (
                'I want    to buy 300 cups of $10.7 coffee. OHOH',
                'i want to buy _3int_ cups of $_2float1_ coffee. ohoh',
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_u_zh_en_text_normalizer_collection_1(self):
        normalizer = u_zh_en_text_normalizer_collection_1
        test_cases = [
            (
                '我在85.333度C買了a cup of900-1000元的咖啡《ohoh》？？',
                '我在_float_度c買了a cup of_int_-_int_元的咖啡<ohoh>??',
            ),
            (
                '+1~~',
                '+_int_~~',
            ),
            (
                '，買5～80年五門車～～',
                ',買_int_~_int_年五門車~~',
            ),
            (
                '<><>@@##',
                '<><>@@##',
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_u_zh_en_text_normalizer_collection_2(self):
        normalizer = u_zh_en_text_normalizer_collection_2
        test_cases = [
            (
                '我在85.333度C買了a cup of900-1000元的咖啡《ohoh》？？',
                '我在_2float3_度c買了a cup of_3int_-_4int_元的咖啡<ohoh>??',
            ),
            (
                '+1~~',
                '+_1int_~~',
            ),
            (
                '，買5～80年五門車～～',
                ',買_1int_~_2int_年五門車~~',
            ),
            (
                '<><>@@##',
                '<><>@@##',
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_u_zh_en_text_normalizer_collection_3(self):
        normalizer = u_zh_en_text_normalizer_collection_3
        test_cases = [
            (
                '我在85.333度C買了a cup of900～1000元的咖啡《ohoh》？？',
                '我在_float_度c買了a cup of_int_-_int_元的咖啡 ohoh ',
            ),
            (
                '+1~~',
                '+_int_--',
            ),
            (
                '<><>@@##',
                ' ',
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_u_zh_en_text_normalizer_collection_4(self):
        normalizer = u_zh_en_text_normalizer_collection_4
        test_cases = [
            (
                '我在85.333度C買了a cup of900～1000元的咖啡《OhoH》？？',
                '我在_2float3_度c買了a cup of_3int_-_4int_元的咖啡 ohoh ',
            ),
            (
                '+1~~',
                '+_1int_--',
            ),
            (
                '，買5～80年五門車～～',
                ',買_1int_-_2int_年五門車--',
            ),
            (
                '<><>@@##',
                ' ',
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )
