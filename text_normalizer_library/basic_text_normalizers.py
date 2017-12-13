from ..replace_pattern_with_token import ReplacePatternWithToken


whitespace_char_text_normalizer = ReplacePatternWithToken(
    name='whitespace_char',
    denormalizable=False,
    target_pattern=r'\s+',
    prefix_pattern=None,
    suffix_pattern=None,
    token=' ',
)

chinese_punctuation_text_normalizer = ReplacePatternWithToken(
    name='chinese_punctuation',
    denormalizable=False,
    target_pattern=r'[。「」﹁﹂『 』、‧（ ）《》〈〉 ﹏﹏﹏……—～，？；：［］【 】！]+',
    prefix_pattern=None,
    suffix_pattern=None,
    token=' ',
)

english_punctuation_text_normalizer = ReplacePatternWithToken(
    name='english_punctuation',
    denormalizable=False,
    target_pattern=r'[\.,\<\>\(\)\"\'\{\}\[\]\*\^\!\?\=\+\-\~]+',
    prefix_pattern=None,
    suffix_pattern=None,
    token=' ',
)

int_text_normalizer = ReplacePatternWithToken(
    name='int',
    denormalizable=True,
    target_pattern=r'[0-9]+',
    prefix_pattern=None,
    suffix_pattern=None,
    token='_int_',
)

float_text_normalizer = ReplacePatternWithToken(
    name='float',
    denormalizable=True,
    target_pattern=r'[0-9]+\.[0-9]+',
    prefix_pattern=r'[^\.\d]{1}|\A',
    suffix_pattern=r'[^\.\d]{1}|\Z',
    token='_float_',
)
