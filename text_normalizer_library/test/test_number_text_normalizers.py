from unittest import TestCase
from ..number_text_normalizers import (
    int_text_normalizer,
    float_text_normalizer,
    int_with_digit_text_normalizer,
    float_with_digit_text_normalizer,
    int_with_space_text_normalizer,
    float_with_space_text_normalizer,
    int_with_digit_n_space_text_normalizer,
    float_with_digit_n_space_text_normalizer,
)


class NumberTextNormalizersTestCase(TestCase):

    def test_int_text_normalizer(self):
        revised_sentence, meta = int_text_normalizer.normalize(sentence="123")
        recovered_sentence = int_text_normalizer.denormalize(
            sentence=revised_sentence,
            meta=meta,
        )
        self.assertEqual("_int_", revised_sentence)
        self.assertEqual({"_int_": ["123"]}, meta)
        self.assertEqual("123", recovered_sentence)

    def test_float_text_normalizer(self):
        revised_sentence, meta = float_text_normalizer.normalize(sentence="123.33")
        recovered_sentence = float_text_normalizer.denormalize(
            sentence=revised_sentence,
            meta=meta,
        )
        self.assertEqual("_float_", revised_sentence)
        self.assertEqual({"_float_": ["123.33"]}, meta)
        self.assertEqual("123.33", recovered_sentence)

    def test_int_with_digit_text_normalizer(self):
        revised_sentence, meta = int_with_digit_text_normalizer.normalize(sentence="123")
        recovered_sentence = int_with_digit_text_normalizer.denormalize(
            sentence=revised_sentence,
            meta=meta,
        )
        self.assertEqual("_3int_", revised_sentence)
        self.assertEqual({"_3int_": ["123"]}, meta)
        self.assertEqual("123", recovered_sentence)

    def test_float_with_digit_text_normalizer(self):
        revised_sentence, meta = float_with_digit_text_normalizer.normalize(
            sentence="123.33",
        )
        recovered_sentence = float_with_digit_text_normalizer.denormalize(
            sentence=revised_sentence,
            meta=meta,
        )
        self.assertEqual("_3float2_", revised_sentence)
        self.assertEqual({"_3float2_": ["123.33"]}, meta)
        self.assertEqual("123.33", recovered_sentence)

    def test_int_with_space_text_normalizer(self):
        revised_sentence, meta = int_with_space_text_normalizer.normalize(sentence="123")
        recovered_sentence = int_with_space_text_normalizer.denormalize(
            sentence=revised_sentence,
            meta=meta,
        )
        self.assertEqual(" _int_ ", revised_sentence)
        self.assertEqual({" _int_ ": ["123"]}, meta)
        self.assertEqual("123", recovered_sentence)

    def test_float_with_space_text_normalizer(self):
        revised_sentence, meta = float_with_space_text_normalizer.normalize(sentence="123.33")
        recovered_sentence = float_with_space_text_normalizer.denormalize(
            sentence=revised_sentence,
            meta=meta,
        )
        self.assertEqual(" _float_ ", revised_sentence)
        self.assertEqual({" _float_ ": ["123.33"]}, meta)
        self.assertEqual("123.33", recovered_sentence)

    def test_int_with_digit_n_space_text_normalizer(self):
        revised_sentence, meta = int_with_digit_n_space_text_normalizer.normalize(
            sentence="123",
        )
        recovered_sentence = int_with_digit_n_space_text_normalizer.denormalize(
            sentence=revised_sentence,
            meta=meta,
        )
        self.assertEqual(" _3int_ ", revised_sentence)
        self.assertEqual({" _3int_ ": ["123"]}, meta)
        self.assertEqual("123", recovered_sentence)

    def test_float_with_digit_n_space_text_normalizer(self):
        revised_sentence, meta = float_with_digit_n_space_text_normalizer.normalize(
            sentence="123.33",
        )
        recovered_sentence = float_with_digit_n_space_text_normalizer.denormalize(
            sentence=revised_sentence,
            meta=meta,
        )
        self.assertEqual(" _3float2_ ", revised_sentence)
        self.assertEqual({" _3float2_ ": ["123.33"]}, meta)
        self.assertEqual("123.33", recovered_sentence)
