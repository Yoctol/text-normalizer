# -*- coding: utf-8 -*-
from unittest import TestCase

from ..basic_text_normalizer_collection import basic_text_normalizer_collection


class BasicNormalizerCollectionTestCase(TestCase):

    def test_basic_text_normalizer_collection(self):
        revised_sentence, history = basic_text_normalizer_collection.normalize(
            sentence='2017-01-01我在85.33度C買了一杯(*999*)的咖啡--10:30',
            lowercase=True,
        )
        self.assertEqual(
            '_date_我在_float_度c買了一杯 _int_ 的咖啡 _time_',
            revised_sentence,
        )
        recovered_sentence = basic_text_normalizer_collection.denormalize(
            sentence='_date_我在_float_度c買了一杯_int_的咖啡_time_',
            history=history,
        )
        self.assertEqual(
            '2017-01-01我在85.33度c買了一杯999的咖啡10:30',
            recovered_sentence,
        )
