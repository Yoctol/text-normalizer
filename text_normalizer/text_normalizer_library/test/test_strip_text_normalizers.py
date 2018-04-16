# -*- coding: utf-8 -*-
from unittest import TestCase
from ..strip_text_normalizers import (
    pure_strip_text_normalizer,
)


class StripTextNormalizerTestCase(TestCase):

    def normalize(self):
        result = pure_strip_text_normalizer.normalize(
            sentence='   \n\n\t\t    LALALA 拉拉 xddd \n\n\t\t\t   ')
        self.assertEqual(
            ('LALALA 拉拉 xddd', None),
            result,
        )
