# -*- coding: utf-8 -*-
from unittest import TestCase

from ..charactor_text_normalizer_collection import (
    chinese_charactor_text_normalizer_collection_1,
    chinese_charactor_text_normalizer_collection_2,
    chinese_charactor_text_normalizer_collection_3,
    chinese_charactor_text_normalizer_collection_4,
)


class CharactorTextNormalizerCollectionTestCase(TestCase):

    def _run_test(self, test_cases, normalizer, normalizer_name):
        for test_case in test_cases:
            with self.subTest(test_case=(normalizer_name, test_case[0])):
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

    def test_chinese_charactor_text_normalizer_collection_1(self):
        test_cases = [
            (
                "   我在85.33度C買了一杯900──1000元的咖啡《ohoh》？？ m_m",
                "我在_float_度c買了一杯_int_-_int_元的咖啡(ohoh)?? m_m",
                "我在85.33度C買了一杯900──1000元的咖啡《ohoh》？？ m_m",
            ),
            (
                "買5──8年五門車    ～～",
                "買_int_-_int_年五門車 --",
                "買5──8年五門車 ～～",
            ),
            (
                "2001 ~ 2007年紅色\藍色的Benz    OHOHOH",
                "_int_ - _int_年紅色,藍色的benz ohohoh",
                "2001 ~ 2007年紅色\藍色的Benz OHOHOH",
            ),
        ]
        self._run_test(
            test_cases=test_cases,
            normalizer=chinese_charactor_text_normalizer_collection_1,
            normalizer_name="chinese_charactor_text_normalizer_collection_1",
        )

    def test_chinese_charactor_text_normalizer_collection_2(self):
        test_cases = [
            (
                "   我在85.33度C買了一杯900──1000元的咖啡    《ohoh》？？ m_m",
                "我在_float_度c買了一杯_int_-_int_元的咖啡 <ohoh>?? m_m",
                "我在85.33度C買了一杯900──1000元的咖啡 《ohoh》？？ m_m",
            ),
            (
                "買5-8年五門車  ～～    ",
                "買_int_-_int_年五門車 ~~",
                "買5-8年五門車 ～～",
            ),
            (
                "2001 ~ 2007年紅色\藍色的Benz    OHOHOH    ",
                "_int_ ~ _int_年紅色\藍色的benz ohohoh",
                "2001 ~ 2007年紅色\藍色的Benz OHOHOH",
            ),
        ]
        self._run_test(
            test_cases=test_cases,
            normalizer=chinese_charactor_text_normalizer_collection_2,
            normalizer_name="chinese_charactor_text_normalizer_collection_2",
        )

    def test_chinese_charactor_text_normalizer_collection_3(self):
        test_cases = [
            (
                "   我在85.33度C買了一杯900-1000元的咖啡{ohoh}",
                "我在_2float2_度c買了一杯_3int_-_4int_元的咖啡(ohoh)",
                "我在85.33度C買了一杯900-1000元的咖啡{ohoh}",
            ),
            (
                "   買5 - 80年     五門車~    ",
                "買_1int_ - _2int_年 五門車-",
                "買5 - 80年 五門車~",
            ),
        ]
        self._run_test(
            test_cases=test_cases,
            normalizer=chinese_charactor_text_normalizer_collection_3,
            normalizer_name="chinese_charactor_text_normalizer_collection_3",
        )

    def test_chinese_charactor_text_normalizer_collection_4(self):
        test_cases = [
            (
                "    我在85.333度C買了一杯900──1000元的咖啡《ohoh》？？ m_m  ",
                "我在_2float3_度c買了一杯_3int_-_4int_元的咖啡<ohoh>?? m_m",
                "我在85.333度C買了一杯900──1000元的咖啡《ohoh》？？ m_m",
            ),
            (
                "買5-800年   五門車  ～～    ",
                "買_1int_-_3int_年 五門車 ~~",
                "買5-800年 五門車 ～～",
            ),
            (
                "    2001 ~ 2007年紅色\藍色的Benz    OHOHOH",
                "_4int_ ~ _4int_年紅色\藍色的benz ohohoh",
                "2001 ~ 2007年紅色\藍色的Benz OHOHOH",
            ),
        ]
        self._run_test(
            test_cases=test_cases,
            normalizer=chinese_charactor_text_normalizer_collection_4,
            normalizer_name="chinese_charactor_text_normalizer_collection_4",
        )
