from unittest import TestCase
from ..base_factory import BaseFactory


class TestBaseFactory(TestCase):

    def setUp(self):
        self.base_text_normalizer_class = BaseFactory()
        self.base_text_normalizer_class_with_name = BaseFactory(name='123')

    def test_attributes(self):
        self.assertEqual(
            {
                'denormalizable': False,
                'name': 'BaseFactory',
            },
            self.base_text_normalizer_class.__dict__,
        )

        self.assertEqual(
            {
                'denormalizable': False,
                'name': '123',
            },
            self.base_text_normalizer_class_with_name.__dict__,
        )

    def test_denormalize(self):
        self.assertEqual(
            'HAHA',
            self.base_text_normalizer_class.denormalize(sentence='HAHA'),
        )
        self.assertEqual(
            'HAHA',
            self.base_text_normalizer_class_with_name.denormalize(sentence='HAHA'),
        )
