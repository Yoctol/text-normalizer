from os.path import join

from text_normalizer.text_normalizer_factory import PunctuationMappingTextNormalizer
from text_normalizer import ROOT_DIR


full_punctuation_mapping_text_normalizer = PunctuationMappingTextNormalizer(
    normalization_table_path=join(
        ROOT_DIR,
        'data/punctuation/punctuation_mapping_0221.csv',
    ),
)

simplified_punctuation_mapping_text_normalizer = PunctuationMappingTextNormalizer(
    normalization_table_path=join(
        ROOT_DIR,
        'data/punctuation/punctuation_mapping_0221_simplified.csv',
    ),
)
