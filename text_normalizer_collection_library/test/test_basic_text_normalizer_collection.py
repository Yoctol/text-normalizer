# -*- coding: utf-8 -*-
from unittest import TestCase

from ..basic_text_normalizer_collection import basic_text_normalizer_collection


class BasicNormalizerCollectionTestCase(TestCase):

    def test_basic_text_normalizer_collection(self):
        revised_sentence, meta = basic_text_normalizer_collection.normalize(
            sentence='我在85.33度C買了一杯(*999*)的咖啡--',
        )
        self.assertEqual(
            '我在 _float_ 度c買了一杯 _int_ 的咖啡',
            revised_sentence,
        )
        recovered_sentence = basic_text_normalizer_collection.denormalize(
            sentence='我在 _float_ 度c買了一杯 _int_ 的咖啡',
            meta=meta,
        )
        self.assertEqual(
            '我在85.33度C買了一杯999的咖啡',
            recovered_sentence,
        )
