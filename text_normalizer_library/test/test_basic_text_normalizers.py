# -*- coding: utf-8 -*-

from unittest import TestCase
from ..basic_text_normalizers import (
    whitespace_char_text_normalizer,
    chinese_punctuation_text_normalizer,
    english_punctuation_text_normalizer,
    int_text_normalizer,
    float_text_normalizer,
)


class BasicTextNormalizersTestCase(TestCase):

    def test_whitespace_char_text_normalizer_normalize(self):
        test_cases = [
            ('      ', (' ', None)),
            ('              ', (' ', None)),
            ('\n\n\n\n\n', (' ', None)),
            ('我有很多      空白', ('我有很多 空白', None)),
            ('我有很多          tab', ('我有很多 tab', None)),
            ('我有很多\n\n\n\n\n分行', ('我有很多 分行', None)),
            ('家豪大大亂入', ('家豪大大亂入', None)),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    whitespace_char_text_normalizer.normalize(sentence=test_case[0]),
                )

    def test_chinese_punctuation_text_normalizer_normalize(self):
        test_cases = [
            ('勤彥大大喜歡吃《變態》糖果！！！', ('勤彥大大喜歡吃 變態 糖果 ', None)),
            ('。「」﹁﹂『 』、‧（ ）《》〈〉 ﹏﹏﹏……—～，？；：［］【 】！', (' ', None)),
            ('家豪大大亂入', ('家豪大大亂入', None)),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    chinese_punctuation_text_normalizer.normalize(sentence=test_case[0]),
                )

    def test_english_punctuation_text_normalizer_normalize(self):
        test_cases = [
            ('勤彥大大喜歡吃<變態>糖果!!!', ('勤彥大大喜歡吃 變態 糖果 ', None)),
            ('.,<>(){}[]*^!?=+-~', (' ', None)),
            ('家豪大大亂入', ('家豪大大亂入', None)),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    english_punctuation_text_normalizer.normalize(sentence=test_case[0]),
                )

    def test_int_text_normalizer_normalize(self):
        test_cases = [
            ('100', (' _int_ ', {' _int_ ': ['100']})),
            ('340分', (' _int_ 分', {' _int_ ': ['340']})),
            ('薄餡大大1個打10個', ('薄餡大大 _int_ 個打 _int_ 個', {' _int_ ': ['1', '10']})),
            ('0800-22-44-66', (' _int_ - _int_ - _int_ - _int_ ',
                               {' _int_ ': ['0800', '22', '44', '66']})),
            ('家豪大大亂入', ('家豪大大亂入', {' _int_ ': []})),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    int_text_normalizer.normalize(sentence=test_case[0]),
                )

    def test_int_text_normalizer_denormalize(self):
        normal_test_cases = [
            (' _int_ ', {' _int_ ': ['100']}, '100'),
            (' _int_ 分', {' _int_ ': ['340']}, '340分'),
            ('薄餡大大 _int_ 個打 _int_ 個', {' _int_ ': ['1', '10']}, '薄餡大大1個打10個'),
            (' _int_ - _int_ - _int_ - _int_ ',
             {' _int_ ': ['0800', '22', '44', '66']}, '0800-22-44-66'),
            ('家豪大大亂入', {' _int_ ': []}, '家豪大大亂入'),
        ]
        for test_case in normal_test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[2],
                    int_text_normalizer.denormalize(
                        sentence=test_case[0],
                        meta=test_case[1],
                    ),
                )
        with self.assertRaises(KeyError):
            int_text_normalizer.denormalize(
                sentence='家豪大大亂入',
                meta={'_雞排_': ['大雞排']},
            ),
        with self.assertRaises(ValueError):
            int_text_normalizer.denormalize(
                sentence=' _int_ 和 _int_ 這兩個日期都沒有雞排',
                meta={' _int_ ': ['12']},
            )

    def test_float_text_normalizer_normalize(self):
        test_cases = [
            ('100.000', (' _float_ ', {' _float_ ': ['100.000']})),
            ('94.87分', (' _float_ 分', {' _float_ ': ['94.87']})),
            ('薄餡大大1.5個打10.7個', ('薄餡大大 _float_ 個打 _float_ 個', {' _float_ ': ['1.5', '10.7']})),
            ('123.456.789', ('123.456.789', {' _float_ ': []})),
            ('家豪大大亂入', ('家豪大大亂入', {' _float_ ': []})),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    float_text_normalizer.normalize(sentence=test_case[0]),
                )

    def test_float_text_normalizer_denormalize(self):
        normal_test_cases = [
            (' _float_ ', {' _float_ ': ['100.000']}, '100.000'),
            (' _float_ 分', {' _float_ ': ['340.87']}, '340.87分'),
            ('薄餡大大 _float_ 個打 _float_ 個', {' _float_ ': ['1.5', '10.7']}, '薄餡大大1.5個打10.7個'),
            ('家豪大大亂入', {' _float_ ': []}, '家豪大大亂入'),
        ]
        for test_case in normal_test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[2],
                    float_text_normalizer.denormalize(
                        sentence=test_case[0],
                        meta=test_case[1],
                    ),
                )
        with self.assertRaises(KeyError):
            float_text_normalizer.denormalize(
                sentence='家豪大大亂入',
                meta={'_雞排_': ['大雞排']},
            ),
        with self.assertRaises(ValueError):
            float_text_normalizer.denormalize(
                sentence=' _float_ 和 _float_ 這兩個價錢都買不到雞排',
                meta={' _float_ ': ['12']},
            )
