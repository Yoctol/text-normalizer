from ..base_text_normalizer_collection import BaseTextNormalizerCollection

from ..text_normalizer_library.basic_text_normalizers import (
    whitespace_char_text_normalizer,
    float_text_normalizer,
    int_text_normalizer,
    chinese_punctuation_text_normalizer,
    english_punctuation_text_normalizer,
)
from ..text_normalizer_library.date_text_normalizers import (
    date_text_normalizer_yymmdd,
)
from ..text_normalizer_library.time_text_normalizers import (
    time_text_normalizer_hhmm,
)

basic_text_normalizer_collection = BaseTextNormalizerCollection()
basic_text_normalizer_collection.add_text_normalizers(
    text_normalizers=[
        whitespace_char_text_normalizer,
        float_text_normalizer,
        date_text_normalizer_yymmdd,
        time_text_normalizer_hhmm,
        int_text_normalizer,
        chinese_punctuation_text_normalizer,
        english_punctuation_text_normalizer,
        whitespace_char_text_normalizer,
    ],
)
