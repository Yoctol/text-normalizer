# -*- coding: utf-8 -*-

from unittest import TestCase
from ..unicode_text_normalizers import (
    unicode__chinese_characters_text_normalizer,
    unicode__chinese_characters_and_digits_text_normalizer,
    unicode__english_characters_and_digits_text_normalizer,
    unicode__english_digits_and_full_punctuations_text_normalizer,
    unicode__chinese_english_digits_and_full_punctuations_text_normalizer,
    unicode__chinese_english_digits_and_simplified_punctuations_1_text_normalizer,
)


class PunctuationTextNormalizersTestCase(TestCase):

    def unit_test(self, normalizer, test_cases):
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    normalizer.normalize(
                        sentence=test_case[0],
                    ),
                )
                self.assertEqual(
                    test_case[0],
                    normalizer.denormalize(
                        sentence=test_case[1][0],
                        meta=test_case[1][1],
                    ),
                )

    def test_unicode__chinese_characters_text_normalizer(self):
        normalizer = unicode__chinese_characters_text_normalizer
        test_cases = [
            (
                '><我想喝100.3元可樂xd～～',
                (
                    '  我想喝     元可樂    ',
                    {
                        '想': ['想'],
                        ' ': ['>', '<', '1', '0', '0', '.', '3',
                              'x', 'd', '～', '～'],
                        '我': ['我'],
                        '喝': ['喝'],
                        '樂': ['樂'],
                        '可': ['可'],
                        '元': ['元'],
                    },
                ),
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_unicode__chinese_characters_and_digits_text_normalizer(self):
        normalizer = unicode__chinese_characters_and_digits_text_normalizer
        test_cases = [
            (
                '><我想喝100.3元可樂xd～～',
                (
                    '  我想喝100.3元可樂    ',
                    {
                        '0': ['0', '0'],
                        '想': ['想'],
                        ' ': ['>', '<', 'x', 'd', '～', '～'],
                        '我': ['我'],
                        '喝': ['喝'],
                        '樂': ['樂'],
                        '可': ['可'],
                        '元': ['元'],
                        '1': ['1'],
                        '.': ['.'],
                        '3': ['3'],
                    },
                ),
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_unicode__english_characters_and_digits_text_normalizer(self):
        normalizer = unicode__english_characters_and_digits_text_normalizer
        test_cases = [
            (
                'hate cola 123!',
                (
                    'hate cola 123 ',
                    {
                        'h': ['h'],
                        'a': ['a', 'a'],
                        't': ['t'],
                        'e': ['e'],
                        'c': ['c'],
                        'o': ['o'],
                        'l': ['l'],
                        '1': ['1'],
                        '2': ['2'],
                        '3': ['3'],
                        ' ': [' ', ' ', '!'],
                    },
                ),
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_unicode__english_digits_and_full_punctuations_text_normalizer(self):
        normalizer = unicode__english_digits_and_full_punctuations_text_normalizer
        test_cases = [
            (
                'hate cola 123!',
                (
                    'hate cola 123!',
                    {
                        'h': ['h'],
                        'a': ['a', 'a'],
                        't': ['t'],
                        'e': ['e'],
                        'c': ['c'],
                        'o': ['o'],
                        'l': ['l'],
                        '1': ['1'],
                        '2': ['2'],
                        '3': ['3'],
                        '!': ['!'],
                        ' ': [' ', ' '],
                    },
                ),
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_unicode__chinese_english_digits_and_full_punctuations_text_normalizer(self):
        normalizer = unicode__chinese_english_digits_and_full_punctuations_text_normalizer
        test_cases = [
            (
                '～我想喝100元『可樂』，cola xd~。',
                (
                    '~我想喝100元"可樂",cola xd~.',
                    {
                        '0': ['0', '0'],
                        '想': ['想'],
                        ' ': [' '],
                        '~': ['～', '~'],
                        ',': ['，'],
                        '.': ['。'],
                        '"': ['『', '』'],
                        '我': ['我'],
                        '喝': ['喝'],
                        '樂': ['樂'],
                        '可': ['可'],
                        '元': ['元'],
                        '1': ['1'],
                        'c': ['c'],
                        'o': ['o'],
                        'l': ['l'],
                        'a': ['a'],
                        'x': ['x'],
                        'd': ['d'],
                    },
                ),
            ),
            (
                '。「」﹁﹂『 』、‧（ ）《》〈〉 ﹏﹏﹏……—～，？；：［］【 】！',
                (
                    '.""  " ", ( )<><>       ~,?;:[][ ]!',
                    {
                        ' ': ['﹁', '﹂', ' ', '‧', ' ', ' ', '﹏',
                              '﹏', '﹏', '…', '…', '—', ' '],
                        '!': ['！'],
                        '"': ['「', '」', '『', '』'],
                        '(': ['（'],
                        ')': ['）'],
                        ',': ['、', '，'],
                        '.': ['。'],
                        ':': ['：'],
                        ';': ['；'],
                        '<': ['《', '〈'],
                        '>': ['》', '〉'],
                        '?': ['？'],
                        '[': ['［', '【'],
                        ']': ['］', '】'],
                        '~': ['～'],
                    },
                ),
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )

    def test_unicode__chinese_english_digits_and_simplified_punctuations_1_text_normalizer(self):
        normalizer = unicode__chinese_english_digits_and_simplified_punctuations_1_text_normalizer
        test_cases = [
            (
                '><我想喝100元可樂/cola xd～～',
                (
                    '  我想喝100元可樂,cola xd--',
                    {
                        '0': ['0', '0'],
                        '想': ['想'],
                        ' ': ['>', '<', ' '],
                        '-': ['～', '～'],
                        ',': ['/'],
                        '我': ['我'],
                        '喝': ['喝'],
                        '樂': ['樂'],
                        '可': ['可'],
                        '元': ['元'],
                        '1': ['1'],
                        'c': ['c'],
                        'o': ['o'],
                        'l': ['l'],
                        'a': ['a'],
                        'x': ['x'],
                        'd': ['d'],
                    },
                ),
            ),
            (
                '。「」﹁﹂『 』、‧（ ）《》〈〉 ﹏﹏﹏……—～，？；：［］【 】！',
                (
                    '.       ,               -, ,       ',
                    {
                        ' ': ['「', '」', '﹁', '﹂', '『', ' ', '』',
                              '‧', '（', ' ', '）', '《', '》', '〈', '〉',
                              ' ', '﹏', '﹏', '﹏', '…', '…', '—', '？', '：',
                              '［', '］', '【', ' ', '】', '！'],
                        ',': ['、', '，', '；'],
                        '-': ['～'],
                        '.': ['。'],
                    },
                ),
            ),
        ]
        self.unit_test(
            normalizer=normalizer,
            test_cases=test_cases,
        )
