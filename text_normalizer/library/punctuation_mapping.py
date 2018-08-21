from os.path import join

from ..factory import PunctuationMapping
from text_normalizer import ROOT_DIR


full_punctuation_mapping_text_normalizer = PunctuationMapping(
    normalization_table_path=join(
        ROOT_DIR,
        'data/punctuation/punctuation_mapping_0221.csv',
    ),
)

simplified_punctuation_mapping_text_normalizer = PunctuationMapping(
    normalization_table_path=join(
        ROOT_DIR,
        'data/punctuation/punctuation_mapping_0221_simplified.csv',
    ),
)
