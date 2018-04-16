# -*- coding: utf-8 -*-

from unittest import TestCase
from ..identity_text_normalizer import (
    identity_text_normalizer,
)


class IdentityTextNormalizersTestCase(TestCase):

    def test_identity_text_normalizer_normalize(self):
        result = identity_text_normalizer.normalize(
            sentence='我超懶惰 我就是想耍廢 KerKer ><',
        )
        self.assertEqual(
            ('我超懶惰 我就是想耍廢 KerKer ><', None),
            result,
        )
        result = identity_text_normalizer.denormalize(
            sentence=result[0],
            meta=result[1],
        )
        self.assertEqual(
            '我超懶惰 我就是想耍廢 KerKer ><',
            result,
        )
