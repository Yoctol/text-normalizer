from .base_text_normalizer_collection import BaseTextNormalizerCollection
from text_normalizer.text_normalizer_library import (
    whitespace_char_text_normalizer,
    float_with_space_text_normalizer,
    int_with_space_text_normalizer,
    float_with_digit_n_space_text_normalizer,
    int_with_digit_n_space_text_normalizer,
    full_punctuation_mapping_text_normalizer,
    simplified_punctuation_mapping_text_normalizer,
    pure_strip_text_normalizer,
    eng_lowercase_text_normalizer,
)


full_punctuation_keeping_text_normalizer_collection = BaseTextNormalizerCollection()
full_punctuation_keeping_text_normalizer_collection.add_text_normalizers(
    text_normalizers=[
        eng_lowercase_text_normalizer,
        full_punctuation_mapping_text_normalizer,
        float_with_space_text_normalizer,
        int_with_space_text_normalizer,
        whitespace_char_text_normalizer,
        pure_strip_text_normalizer,
    ],
)


simplified_punctuation_keeping_text_normalizer_collection = BaseTextNormalizerCollection()
simplified_punctuation_keeping_text_normalizer_collection.add_text_normalizers(
    text_normalizers=[
        eng_lowercase_text_normalizer,
        simplified_punctuation_mapping_text_normalizer,
        float_with_space_text_normalizer,
        int_with_space_text_normalizer,
        whitespace_char_text_normalizer,
        pure_strip_text_normalizer,
    ],
)


number_with_digits_n_simplified_punctuation_text_normalizer_collection = \
    BaseTextNormalizerCollection()
number_with_digits_n_simplified_punctuation_text_normalizer_collection.add_text_normalizers(
    text_normalizers=[
        eng_lowercase_text_normalizer,
        simplified_punctuation_mapping_text_normalizer,
        float_with_digit_n_space_text_normalizer,
        int_with_digit_n_space_text_normalizer,
        whitespace_char_text_normalizer,
        pure_strip_text_normalizer,
    ],
)
