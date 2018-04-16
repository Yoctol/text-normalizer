# -*- coding: utf-8 -*-
from unittest import TestCase

from ..eng_basic_text_normalizer_collection import eng_basic_text_normalizer_collection


class EngBasicNormalizerCollectionTestCase(TestCase):

    def test_eng_basic_text_normalizer_collection(self):
        test_cases = [
            (
                'Hoa DADA loves to eat chicken pie.',
                'hoa dada loves to eat chicken pie.',
                'Hoa DADA loves to eat chicken pie.',
            ),
            (
                'CPH DA    DA want to hang    out  with Hoa \t\t DADA! \n\n',
                'cph da da want to hang out with hoa dada!',
                'CPH DA DA want to hang out with Hoa DADA!',
            ),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                revised_sentence, meta = eng_basic_text_normalizer_collection.normalize(
                    sentence=test_case[0],
                )
                self.assertEqual(test_case[1], revised_sentence)
                recovered_sentence = eng_basic_text_normalizer_collection.denormalize(
                    sentence=revised_sentence,
                    meta=meta,
                )
                self.assertEqual(test_case[2], recovered_sentence)
