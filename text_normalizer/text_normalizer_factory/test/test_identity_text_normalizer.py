# -*- coding: utf-8 -*-
from unittest import TestCase
from ..identity_text_normalizer import IdentityTextNormalizer


class IdentityTextNormalizerTestCase(TestCase):

    def setUp(self):
        self.identity_text_normalizer = IdentityTextNormalizer()

    def test_attributes(self):
        self.assertEqual(
            {
                'denormalizable': False,
                'name': 'identity',
            },
            self.identity_text_normalizer.__dict__,
        )

    def test_normalize(self):
        result = self.identity_text_normalizer.normalize(
            '不管你測什麼 我都會回傳原本的句子給你 呵呵',
        )
        self.assertEqual(
            ('不管你測什麼 我都會回傳原本的句子給你 呵呵', None),
            result,
        )

    def test_denormalize(self):
        result = self.identity_text_normalizer.denormalize(
            '不管你測什麼 我都會回傳原本的句子給你 呵呵',
        )
        self.assertEqual(
            '不管你測什麼 我都會回傳原本的句子給你 呵呵',
            result,
        )
