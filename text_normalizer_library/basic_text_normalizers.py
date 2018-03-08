from ..replace_pattern_with_token import ReplacePatternWithToken


whitespace_char_text_normalizer = ReplacePatternWithToken(
    name='whitespace_char',
    denormalizable=False,
    target_pattern=r'\s+',
    prefix_pattern=None,
    suffix_pattern=None,
    token=' ',
)
