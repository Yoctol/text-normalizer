from .base_text_normalizer_collection import BaseTextNormalizerCollection
from text_normalizer.text_normalizer_library import (
    whitespace_char_text_normalizer,
    pure_strip_text_normalizer,
    eng_lowercase_text_normalizer,
)


eng_basic_text_normalizer_collection = BaseTextNormalizerCollection()
eng_basic_text_normalizer_collection.add_text_normalizers(
    text_normalizers=[
        eng_lowercase_text_normalizer,
        whitespace_char_text_normalizer,
        pure_strip_text_normalizer,
    ],
)
