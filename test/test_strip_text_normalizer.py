# -*- coding: utf-8 -*-
from unittest import TestCase
from ..strip_text_normalizer import StripTextNormalizer


class StripTextNormalizerTestCase(TestCase):

    def setUp(self):
        self.strip_text_normalizer_default = StripTextNormalizer()
        self.strip_text_normalizer_left = StripTextNormalizer(
            direction='left',
            chars=['#', ' '],
        )
        self.strip_text_normalizer_right = StripTextNormalizer(
            direction='right',
            chars=['/', ' '],
        )

    def test_attributes(self):
        self.assertEqual(
            {
                'chars': None,
                'chars_str': None,
                'direction': 'both',
                'denormalizable': False,
                'name': 'strip_both_None',
            },
            self.strip_text_normalizer_default.__dict__,
        )
        self.assertEqual(
            {
                'chars': ['#', ' '],
                'chars_str': '# ',
                'direction': 'left',
                'denormalizable': False,
                'name': 'strip_left_# ',
            },
            self.strip_text_normalizer_left.__dict__,
        )
        self.assertEqual(
            {
                'chars': ['/', ' '],
                'chars_str': '/ ',
                'direction': 'right',
                'denormalizable': False,
                'name': 'strip_right_/ ',
            },
            self.strip_text_normalizer_right.__dict__,
        )

    def test_normalize(self):
        result = self.strip_text_normalizer_default.normalize(
            sentence='         HAHA               ',
        )
        self.assertEqual(
            ('HAHA', None),
            result,
        )
        result = self.strip_text_normalizer_left.normalize(
            sentence='##  \t\tHAHA',
        )
        self.assertEqual(
            ('\t\tHAHA', None),
            result,
        )
        result = self.strip_text_normalizer_right.normalize(
            sentence='HAHA\t\t///  ',
        )
        self.assertEqual(
            ('HAHA\t\t', None),
            result,
        )
