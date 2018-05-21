from text_normalizer.text_normalizer_factory import ReplacePatternWithToken


whitespace_char_text_normalizer = ReplacePatternWithToken(
    name='whitespace_char',
    denormalizable=False,
    target_pattern=r'\s+',
    prefix_pattern=None,
    suffix_pattern=None,
    token=' ',
)

whitespace_reduction_text_normalizer = ReplacePatternWithToken(
    name='whitespaces2one',
    denormalizable=True,
    target_pattern=r'\s+',
    prefix_pattern=None,
    suffix_pattern=None,
    token=' ',
)
