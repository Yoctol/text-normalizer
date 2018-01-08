# -*- coding: utf-8 -*-

from unittest import TestCase
from ..punctuation_text_normalizers import (
    chinese_punctuation_text_normalizer,
    english_punctuation_text_normalizer,
    all_punctuation_text_normalizer,
    all_punctuation_without_endpoint_text_normalizer,
    all_punctuation_without_underscore_text_normalizer,
)


class PunctuationTextNormalizersTestCase(TestCase):

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

    def test_all_punctuation_text_normalizer_normalize(self):
        test_cases = [
            ('勤彥大大：喜歡吃《》<變態>《》糖果!!!', ('勤彥大大 喜歡吃 變態 糖果 ', None)),
            ('.,<>(){}[]*^!?=+-~。「」﹁﹂『 』、‧（ ）《》〈〉 ﹏﹏﹏……—～，？；：［］【 】！', (' ', None)),
            ('家豪大大亂入', ('家豪大大亂入', None)),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    all_punctuation_text_normalizer.normalize(sentence=test_case[0]),
                )

    def test_all_punctuation_without_endpoint_text_normalizer_normalize(self):
        test_cases = [
            ('勤彥大大：喜歡吃87.9《》<變態>《》糖果!!!',
             ('勤彥大大 喜歡吃87.9 變態 糖果 ', None)),
            ('.,<>(){}[]*^!?=+-~。「」﹁﹂『 』、‧（ ）《》〈〉 ﹏﹏﹏……—～，？；：［］【 】！',
             ('. ', None)),
            ('家豪大大亂入', ('家豪大大亂入', None)),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    all_punctuation_without_endpoint_text_normalizer.normalize(
                        sentence=test_case[0],
                    ),
                )

    def test_all_punctuation_without_underscore_text_normalizer_normalize(self):
        test_cases = [
            ('勤彥大大：喜歡吃87.9《》_<變態>_《》糖果!!!', ('勤彥大大 喜歡吃87 9 _ 變態 _ 糖果 ', None)),
            ('_.,<>(){}[]*^!?=+-~。「」﹁﹂『 』、‧（ ）《》〈〉 ﹏﹏﹏……—～，？；：［］【 】！', ('_ ', None)),
            ('家豪大大亂入', ('家豪大大亂入', None)),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    all_punctuation_without_underscore_text_normalizer.normalize(
                        sentence=test_case[0],
                    ),
                )
