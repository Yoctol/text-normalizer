# -*- coding: utf-8 -*-

from unittest import TestCase
from ..basic_text_normalizers import (
    whitespace_char_text_normalizer,
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
                    whitespace_char_text_normalizer.normalize(
                        sentence=test_case[0],
                    ),
                )
