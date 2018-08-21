from .base_collection import BaseCollection
from ..library import (
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


chinese_charactor_text_normalizer_collection_1 = BaseCollection()
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


chinese_charactor_text_normalizer_collection_2 = BaseCollection()
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


chinese_charactor_text_normalizer_collection_3 = BaseCollection()
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


chinese_charactor_text_normalizer_collection_4 = BaseCollection()
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
