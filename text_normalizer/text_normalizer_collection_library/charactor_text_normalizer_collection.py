from .base_text_normalizer_collection import BaseTextNormalizerCollection
from text_normalizer.text_normalizer_library import (
    whitespace_char_text_normalizer,
    float_text_normalizer,
    int_text_normalizer,
    int_with_digit_text_normalizer,
    float_with_digit_text_normalizer,
    full_punctuation_mapping_text_normalizer,
    simplified_punctuation_mapping_text_normalizer,
    pure_strip_text_normalizer,
    eng_lowercase_text_normalizer,
)


chinese_charactor_text_normalizer_collection_1 = BaseTextNormalizerCollection()
chinese_charactor_text_normalizer_collection_1.add_text_normalizers(
    text_normalizers=[
        eng_lowercase_text_normalizer,
        simplified_punctuation_mapping_text_normalizer,
        float_text_normalizer,
        int_text_normalizer,
        whitespace_char_text_normalizer,
        pure_strip_text_normalizer,
    ],
)


chinese_charactor_text_normalizer_collection_2 = BaseTextNormalizerCollection()
chinese_charactor_text_normalizer_collection_2.add_text_normalizers(
    text_normalizers=[
        eng_lowercase_text_normalizer,
        full_punctuation_mapping_text_normalizer,
        float_text_normalizer,
        int_text_normalizer,
        whitespace_char_text_normalizer,
        pure_strip_text_normalizer,
    ],
)


chinese_charactor_text_normalizer_collection_3 = BaseTextNormalizerCollection()
chinese_charactor_text_normalizer_collection_3.add_text_normalizers(
    text_normalizers=[
        eng_lowercase_text_normalizer,
        simplified_punctuation_mapping_text_normalizer,
        float_with_digit_text_normalizer,
        int_with_digit_text_normalizer,
        whitespace_char_text_normalizer,
        pure_strip_text_normalizer,
    ],
)


chinese_charactor_text_normalizer_collection_4 = BaseTextNormalizerCollection()
chinese_charactor_text_normalizer_collection_4.add_text_normalizers(
    text_normalizers=[
        eng_lowercase_text_normalizer,
        full_punctuation_mapping_text_normalizer,
        float_with_digit_text_normalizer,
        int_with_digit_text_normalizer,
        whitespace_char_text_normalizer,
        pure_strip_text_normalizer,
    ],
)
