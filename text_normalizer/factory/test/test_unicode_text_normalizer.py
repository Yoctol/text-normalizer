from unittest import TestCase
from os.path import abspath, dirname, join

from ..unicode_text_normalizer import UnicodeTextNormalizer


ROOT_DIR = dirname(abspath(__file__))


class UnicodeTextNormalizerTestCase(TestCase):

    def setUp(self):
        self.normalizer = UnicodeTextNormalizer(
            unicode_mapping_path=join(
                ROOT_DIR,
                "example_unicode_mapping.txt",
            ),
        )

    def test_attributes(self):
        table = self.normalizer.mapping_table
        self.assertEqual(
            {
                '0xff11': '1',
                '0x31': '1',
                '0xff0c': ',',
                '0xff10': '０',
                '0x2c': ',',
            },
            table,
        )
        unicode_other = self.normalizer.u_other
        self.assertEqual("0x20", unicode_other)

        other = self.normalizer.other
        self.assertEqual(" ", other)

    def test_normalize(self):
        result = self.normalizer.normalize(
            sentence='，，HAHA０1０1 1１',
        )
        self.assertEqual(
            (
                ',,    ０1０1 11',
                {
                    '０': ['０', '０'],
                    ',': ['，', '，'],
                    ' ': ['H', 'A', 'H', 'A', ' '],
                    '1': ['1', '1', '1', '１'],
                },
            ),
            result,
        )

    def test_denormalize(self):
        nor_result = self.normalizer.normalize(
            sentence='，，HAHA０1０1 1１',
        )
        de_result = self.normalizer.denormalize(
            sentence=nor_result[0],
            meta=nor_result[1],
        )
        self.assertEqual(
            '，，HAHA０1０1 1１',
            de_result,
        )
