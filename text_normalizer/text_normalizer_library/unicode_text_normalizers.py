from os.path import join

from text_normalizer.text_normalizer_factory import UnicodeTextNormalizer
from text_normalizer import ROOT_DIR


unicode__chinese_characters_text_normalizer = UnicodeTextNormalizer(
    unicode_mapping_path=join(
        ROOT_DIR,
        'data/unicode/chinese_characters_only.txt',
    ),
)

unicode__chinese_characters_and_digits_text_normalizer = UnicodeTextNormalizer(
    unicode_mapping_path=join(
        ROOT_DIR,
        'data/unicode/chinese_characters_and_digits.txt',
    ),
)

unicode__english_characters_and_digits_text_normalizer = UnicodeTextNormalizer(
    unicode_mapping_path=join(
        ROOT_DIR,
        'data/unicode/english_characters_and_digits.txt',
    ),
)

unicode__english_digits_and_full_punctuations_text_normalizer = UnicodeTextNormalizer(
    unicode_mapping_path=join(
        ROOT_DIR,
        'data/unicode/english_digits_and_full_punctuations.txt',
    ),
)

unicode__chinese_english_digits_and_full_punctuations_text_normalizer = UnicodeTextNormalizer(
    unicode_mapping_path=join(
        ROOT_DIR,
        'data/unicode/chinese_english_digits_and_full_punctuations.txt',
    ),
)

unicode__chinese_english_digits_and_simplified_punctuations_1_text_normalizer = \
    UnicodeTextNormalizer(
        unicode_mapping_path=join(
            ROOT_DIR,
            'data/unicode/chinese_english_digits_and_simplified_punctuations_1.txt',
        ),
    )
