# -*- coding: utf-8 -*-
from unittest.mock import Mock, call

from unittest import TestCase
from ..base_text_normalizer_collection import BaseTextNormalizerCollection


class TestBaseTextNormalizerCollection(TestCase):

    def setUp(self):
        self.base_text_normalizer_collection = BaseTextNormalizerCollection()
        self.example_sentence = "0123456789"
        self.text_normalizers = Mock()
        self.text_normalizer_0 = Mock()
        self.text_normalizer_0.normalize = Mock(return_value=("我123456789", {"我": ["0"]}))
        self.text_normalizer_0.denormalize = Mock(return_value="023456789")
        self.text_normalizer_0.name = "text_normalizer_0"
        self.text_normalizer_1 = Mock()
        self.text_normalizer_1.normalize = Mock(return_value=("我23456789", None))
        self.text_normalizer_1.denormalize = Mock(return_value="我23456789")
        self.text_normalizer_1.name = "text_normalizer_1"
        self.text_normalizer_2 = Mock()
        self.text_normalizer_2.normalize = Mock(return_value=("我要3456789", {"要": ["2"]}))
        self.text_normalizer_2.denormalize = Mock(return_value="我23456789")
        self.text_normalizer_2.name = "text_normalizer_2"
        self.text_normalizers.f0, self.text_normalizers.f1, self.text_normalizers.f2 = \
            self.text_normalizer_0, self.text_normalizer_1, self.text_normalizer_2

    def test_attributes(self):
        self.assertEqual(
            {
                'text_normalizers': [],
            },
            self.base_text_normalizer_collection.__dict__,
        )

    def test_add_text_normalizers(self):
        self.base_text_normalizer_collection.add_text_normalizers([self.text_normalizer_0])
        self.assertEqual(
            [self.text_normalizer_0],
            self.base_text_normalizer_collection.text_normalizers,
        )
        self.base_text_normalizer_collection.add_text_normalizers([self.text_normalizer_1])
        self.assertEqual(
            [self.text_normalizer_0, self.text_normalizer_1],
            self.base_text_normalizer_collection.text_normalizers,
        )
        self.base_text_normalizer_collection.add_text_normalizers([self.text_normalizer_2])
        self.assertEqual(
            [self.text_normalizer_0, self.text_normalizer_1, self.text_normalizer_2],
            self.base_text_normalizer_collection.text_normalizers,
        )
        self.base_text_normalizer_collection.clear_text_normalizers()
        self.base_text_normalizer_collection.add_text_normalizers(
            [self.text_normalizer_0, self.text_normalizer_1, self.text_normalizer_2],
        )
        self.assertEqual(
            [self.text_normalizer_0, self.text_normalizer_1, self.text_normalizer_2],
            self.base_text_normalizer_collection.text_normalizers,
        )

    def test_call(self):
        self.base_text_normalizer_collection.add_text_normalizers([self.text_normalizer_0])
        self.base_text_normalizer_collection.normalize(
            sentence=self.example_sentence,
        )
        self.text_normalizers.assert_has_calls(
            [call.f0.normalize(sentence=self.example_sentence)],
        )

        self.base_text_normalizer_collection.add_text_normalizers([self.text_normalizer_1])
        self.base_text_normalizer_collection.normalize(
            sentence=self.example_sentence,
        )
        self.text_normalizers.assert_has_calls(
            [
                call.f0.normalize(sentence=self.example_sentence),
                call.f1.normalize(sentence="我123456789"),
            ],
        )
        self.base_text_normalizer_collection.add_text_normalizers([self.text_normalizer_2])
        self.base_text_normalizer_collection.normalize(
            sentence=self.example_sentence,
        )
        self.text_normalizers.assert_has_calls(
            [
                call.f0.normalize(sentence=self.example_sentence),
                call.f1.normalize(sentence="我123456789"),
                call.f2.normalize(sentence="我23456789"),
            ],
        )

    def test_denormalize(self):
        self.base_text_normalizer_collection.add_text_normalizers([self.text_normalizer_0])
        self.base_text_normalizer_collection.denormalize(
            sentence="我123456789",
            meta=[
                {
                    'name': "text_normalizer_0",
                    'revised_sentence': "XDDD",
                    'meta_data': {"我": ["0"]},
                },
            ],
        )
        self.text_normalizers.assert_has_calls(
            [
                call.f0.denormalize(
                    sentence="我123456789",
                    meta={"我": ["0"]},
                ),
            ],
        )

        self.base_text_normalizer_collection.add_text_normalizers([self.text_normalizer_1])
        self.base_text_normalizer_collection.denormalize(
            sentence="我123456789",
            meta=[
                {
                    'name': "text_normalizer_0",
                    'revised_sentence': "XDDD",
                    'meta_data': {"我": ["0"]},
                },
                {
                    'name': "text_normalizer_1",
                    "revise_sentence": ">O<",
                    "meta_data": None,
                },
            ],
        )
        self.text_normalizers.assert_has_calls(
            [
                call.f1.denormalize(
                    sentence="我123456789",
                    meta=None,
                ),
                call.f0.denormalize(
                    sentence="我23456789",
                    meta={"我": ["0"]},
                ),
            ],
        )

        self.base_text_normalizer_collection.add_text_normalizers([self.text_normalizer_2])
        self.base_text_normalizer_collection.denormalize(
            sentence="我要3456789",
            meta=[
                {
                    'name': "text_normalizer_0",
                    'revised_sentence': "XDDD",
                    'meta_data': {"我": ["0"]},
                },
                {
                    'name': "text_normalizer_1",
                    "revise_sentence": ">O<",
                    "meta_data": None,
                },
                {
                    'name': "text_normalizer_2",
                    "revised_sentence": "M_M",
                    "meta_data": {"要": ["2"]},
                },
            ],
        )

        self.text_normalizers.assert_has_calls(
            [
                call.f2.denormalize(
                    sentence="我要3456789",
                    meta={"要": ["2"]},
                ),
                call.f1.denormalize(
                    sentence="我23456789",
                    meta=None,
                ),
                call.f0.denormalize(
                    sentence="我23456789",
                    meta={"我": ["0"]},
                ),
            ],
        )
