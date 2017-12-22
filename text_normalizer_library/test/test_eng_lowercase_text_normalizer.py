# -*- coding: utf-8 -*-

from unittest import TestCase
from ..eng_lowercase_text_normalizer import (
    eng_lowercase_text_normalizer,
)


class EngLowercaseTextNormalizerTestCase(TestCase):

    def test_normalize_n_denormalize_0(self):
        result = eng_lowercase_text_normalizer.normalize(
            '哈囉 AAB 123 Cddef 哈囉 >< ???',
        )
        self.assertEqual(
            ('哈囉 aab 123 cddef 哈囉 >< ???',
             [
                 {
                     'before': 'AAB',
                     'after': 'aab',
                 },
                 {
                     'before': 'Cddef',
                     'after': 'cddef',
                 },
             ],
             ),
            result,
        )
        result = eng_lowercase_text_normalizer.denormalize(
            sentence=result[0],
            meta=result[1],
        )
        self.assertEqual(
            '哈囉 AAB 123 Cddef 哈囉 >< ???',
            result,
        )

    def test_normalize_n_denormalize_1(self):
        result = eng_lowercase_text_normalizer.normalize(
            'AAB 123 哈囉 Cddef 456 ffecI',
        )
        self.assertEqual(
            ('aab 123 哈囉 cddef 456 ffeci',
             [
                 {
                     'before': 'AAB',
                     'after': 'aab',
                 },
                 {
                     'before': 'Cddef',
                     'after': 'cddef',
                 },
                 {
                     'before': 'ffecI',
                     'after': 'ffeci',
                 },
             ],
             ),
            result,
        )
        result = eng_lowercase_text_normalizer.denormalize(
            sentence=result[0],
            meta=result[1],
        )
        self.assertEqual(
            'AAB 123 哈囉 Cddef 456 ffecI',
            result,
        )
