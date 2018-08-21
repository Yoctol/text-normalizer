from .base_collection import BaseCollection
from ..library import (
    whitespace_reduction_text_normalizer,
    eng_lowercase_text_normalizer,
    float_text_normalizer,
    int_text_normalizer,
    int_with_digit_text_normalizer,
    float_with_digit_text_normalizer,
    unicode__chinese_characters_text_normalizer,
    unicode__chinese_characters_and_digits_text_normalizer,
    unicode__english_digits_and_full_punctuations_text_normalizer,
    unicode__chinese_english_digits_and_full_punctuations_text_normalizer,
    unicode__chinese_english_digits_and_simplified_punctuations_1_text_normalizer,
)


u_zh_text_normalizer_collection_1 = BaseCollection()
u_zh_text_normalizer_collection_1.add_text_normalizers(
    text_normalizers=[
        unicode__chinese_characters_text_normalizer,
        unicode__chinese_characters_and_digits_text_normalizer,
        whitespace_reduction_text_normalizer,
    ],
)

u_zh_text_normalizer_collection_2 = BaseCollection()
u_zh_text_normalizer_collection_2.add_text_normalizers(
    text_normalizers=[
        unicode__chinese_characters_and_digits_text_normalizer,
        whitespace_reduction_text_normalizer,
    ],
)

u_zh_text_normalizer_collection_3 = BaseCollection()
u_zh_text_normalizer_collection_3.add_text_normalizers(
    text_normalizers=[
        unicode__chinese_characters_and_digits_text_normalizer,
        float_text_normalizer,
        int_text_normalizer,
        whitespace_reduction_text_normalizer,
    ],
)

u_zh_text_normalizer_collection_4 = BaseCollection()
u_zh_text_normalizer_collection_4.add_text_normalizers(
    text_normalizers=[
        unicode__chinese_characters_and_digits_text_normalizer,
        float_with_digit_text_normalizer,
        int_with_digit_text_normalizer,
        whitespace_reduction_text_normalizer,
    ],
)

u_en_text_normalizer_collection_1 = BaseCollection()
u_en_text_normalizer_collection_1.add_text_normalizers(
    text_normalizers=[
        unicode__english_digits_and_full_punctuations_text_normalizer,
        eng_lowercase_text_normalizer,
        whitespace_reduction_text_normalizer,
    ],
)

u_en_text_normalizer_collection_2 = BaseCollection()
u_en_text_normalizer_collection_2.add_text_normalizers(
    text_normalizers=[
        unicode__english_digits_and_full_punctuations_text_normalizer,
        eng_lowercase_text_normalizer,
        float_text_normalizer,
        int_text_normalizer,
        whitespace_reduction_text_normalizer,
    ],
)

u_en_text_normalizer_collection_3 = BaseCollection()
u_en_text_normalizer_collection_3.add_text_normalizers(
    text_normalizers=[
        unicode__english_digits_and_full_punctuations_text_normalizer,
        eng_lowercase_text_normalizer,
        float_with_digit_text_normalizer,
        int_with_digit_text_normalizer,
        whitespace_reduction_text_normalizer,
    ],
)

u_zh_en_text_normalizer_collection_1 = BaseCollection()
u_zh_en_text_normalizer_collection_1.add_text_normalizers(
    text_normalizers=[
        unicode__chinese_english_digits_and_full_punctuations_text_normalizer,
        eng_lowercase_text_normalizer,
        float_text_normalizer,
        int_text_normalizer,
        whitespace_reduction_text_normalizer,
    ],
)

u_zh_en_text_normalizer_collection_2 = BaseCollection()
u_zh_en_text_normalizer_collection_2.add_text_normalizers(
    text_normalizers=[
        unicode__chinese_english_digits_and_full_punctuations_text_normalizer,
        eng_lowercase_text_normalizer,
        float_with_digit_text_normalizer,
        int_with_digit_text_normalizer,
        whitespace_reduction_text_normalizer,
    ],
)

u_zh_en_text_normalizer_collection_3 = BaseCollection()
u_zh_en_text_normalizer_collection_3.add_text_normalizers(
    text_normalizers=[
        unicode__chinese_english_digits_and_simplified_punctuations_1_text_normalizer,
        eng_lowercase_text_normalizer,
        float_text_normalizer,
        int_text_normalizer,
        whitespace_reduction_text_normalizer,
    ],
)

u_zh_en_text_normalizer_collection_4 = BaseCollection()
u_zh_en_text_normalizer_collection_4.add_text_normalizers(
    text_normalizers=[
        unicode__chinese_english_digits_and_simplified_punctuations_1_text_normalizer,
        eng_lowercase_text_normalizer,
        float_with_digit_text_normalizer,
        int_with_digit_text_normalizer,
        whitespace_reduction_text_normalizer,
    ],
)
