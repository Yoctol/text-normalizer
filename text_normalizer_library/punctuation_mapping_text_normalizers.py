from os.path import join

from ..punctuation_mapping_text_normalizer import PunctuationMappingTextNormalizer
from flow.global_vars import RESOURCES_PATH


full_punctuation_mapping_text_normalizer = PunctuationMappingTextNormalizer(
    normalization_table_path=join(
        RESOURCES_PATH,
        'punctuation/punctuation_mapping_0221.csv',
    )
)

simplified_punctuation_mapping_text_normalizer = PunctuationMappingTextNormalizer(
    normalization_table_path=join(
        RESOURCES_PATH,
        'punctuation/punctuation_mapping_0221_simplified.csv',
    )
)
