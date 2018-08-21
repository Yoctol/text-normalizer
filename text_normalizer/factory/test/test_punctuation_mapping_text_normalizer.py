# -*- coding: utf-8 -*-
from os.path import abspath, dirname, join
from unittest import TestCase

from ..punctuation_mapping_text_normalizer import PunctuationMappingTextNormalizer

ROOT_DIR = dirname(abspath(__file__))


class PunctMappingTextNormalizerTestCase(TestCase):

    def setUp(self):
        self.punct_normalizer = PunctuationMappingTextNormalizer(
            normalization_table_path=join(
                ROOT_DIR, "example_punctuation_mapping.csv"),
        )

    def test_normalize_n_denormalize(self):
        result = self.punct_normalizer.normalize(
            "❨哈囉❩，（（❩） ） ,,,﹙﹚() ❨",
        )
        self.assertEqual(
            ("(哈囉),(()) ) ,,,()() (",
             [
                 {
                     "before": ["❨", "（", "（", "﹙", "(", "❨"],
                     "after": "(",
                 },
                 {
                     "before": ["❩", "❩", "）", "）", "﹚", ")"],
                     "after": ")",
                 },
                 {
                     "before": ["，", ",", ",", ","],
                     "after": ",",
                 },
             ],
             ),
            result,
        )
        result = self.punct_normalizer.denormalize(
            sentence=result[0],
            meta=result[1],
        )
        self.assertEqual(
            "❨哈囉❩，（（❩） ） ,,,﹙﹚() ❨",
            result,
        )
