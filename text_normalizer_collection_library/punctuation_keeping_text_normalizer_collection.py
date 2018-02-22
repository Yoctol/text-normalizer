from ..base_text_normalizer_collection import BaseTextNormalizerCollection
from ..text_normalizer_library.punctuation_mapping_text_normalizers import (
    simplified_punctuation_mapping_text_normalizer,
)
from ..text_normalizer_library.basic_text_normalizers import (
    whitespace_char_text_normalizer,
    float_text_normalizer,
    int_text_normalizer,
)
from ..text_normalizer_library.strip_text_normalizers import (
    pure_strip_text_normalizer,
)
from ..text_normalizer_library.eng_lowercase_text_normalizer import (
    eng_lowercase_text_normalizer,
)


punctuation_keeping_text_normalizer_collection = BaseTextNormalizerCollection()
punctuation_keeping_text_normalizer_collection.add_text_normalizers(
    text_normalizers=[
        eng_lowercase_text_normalizer,
        simplified_punctuation_mapping_text_normalizer,
        float_text_normalizer,
        int_text_normalizer,
        whitespace_char_text_normalizer,
        pure_strip_text_normalizer,
    ],
)
