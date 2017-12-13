# -*- coding: utf-8 -*-

from unittest import TestCase
from ..basic_text_normalizers import (
    whitespace_char_text_normalizer,
    chinese_punctuation_text_normalizer,
    english_punctuation_text_normalizer,
    num_text_normalizer,
)


class BasicTextNormalizersTestCase(TestCase):

    def test_whitespace_char_text_normalizer_normalize(self):
        test_cases = [
            ('      ', ('', None)),
            ('              ', ('', None)),
            ('\n\n\n\n\n', ('', None)),
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
            ('勤彥大大喜歡吃《變態》糖果！！！', ('勤彥大大喜歡吃 變態 糖果', None)),
            ('～﹁？。？﹂～、', ('', None)),
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
            ('勤彥大大喜歡吃<變態>糖果!!!', ('勤彥大大喜歡吃 變態 糖果', None)),
            ('~>??<,==++', ('', None)),
            ('家豪大大亂入', ('家豪大大亂入', None)),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    english_punctuation_text_normalizer.normalize(sentence=test_case[0]),
                )

    def test_num_text_normalizer_normalize(self):
        test_cases = [
            ('100', ('_num_', {'_num_': ['100']})),
            ('340分', ('_num_分', {'_num_': ['340']})),
            ('薄餡大大1個打10個', ('薄餡大大_num_個打_num_個', {'_num_': ['1', '10']})),
            ('0800-22-44-66', ('_num_-_num_-_num_-_num_',
                               {'_num_': ['0800', '22', '44', '66']})),
            ('家豪大大亂入', ('家豪大大亂入', {'_num_': []})),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    num_text_normalizer.normalize(sentence=test_case[0]),
                )

    def test_num_text_normalizer_denormalize(self):
        normal_test_cases = [
            ('_num_', {'_num_': ['100']}, '100'),
            ('_num_分', {'_num_': ['340']}, '340分'),
            ('薄餡大大_num_個打_num_個', {'_num_': ['1', '10']}, '薄餡大大1個打10個'),
            ('_num_-_num_-_num_-_num_',
             {'_num_': ['0800', '22', '44', '66']}, '0800-22-44-66'),
            ('家豪大大亂入', {'_num_': []}, '家豪大大亂入'),
        ]
        for test_case in normal_test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[2],
                    num_text_normalizer.denormalize(
                        sentence=test_case[0],
                        meta=test_case[1],
                    ),
                )
        with self.assertRaises(KeyError):
            num_text_normalizer.denormalize(
                sentence='家豪大大亂入',
                meta={'_雞排_': ['大雞排']},
            ),
        with self.assertRaises(ValueError):
            num_text_normalizer.denormalize(
                sentence='_num_和_num_這兩個日期都沒有雞排',
                meta={'_num_': ['12']},
            )
