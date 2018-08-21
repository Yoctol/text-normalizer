from .base_collection import BaseCollection
from ..library import (
    whitespace_char_text_normalizer,
    pure_strip_text_normalizer,
    eng_lowercase_text_normalizer,
)


eng_basic_text_normalizer_collection = BaseCollection()
eng_basic_text_normalizer_collection.add_text_normalizers(
    text_normalizers=[
        eng_lowercase_text_normalizer,
        whitespace_char_text_normalizer,
        pure_strip_text_normalizer,
    ],
)
