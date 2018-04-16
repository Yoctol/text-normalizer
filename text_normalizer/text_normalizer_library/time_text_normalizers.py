from text_normalizer.text_normalizer_factory import ReplacePatternWithToken


time_text_normalizer_hhmm = ReplacePatternWithToken(
    name='time_hhmm',
    denormalizable=True,
    target_pattern=r'[0-2]*\d:[0-5]*\d',
    prefix_pattern=r'[^\d:]{1}|\A',
    suffix_pattern=r'[^\d:]{1}|\Z',
    token=' _time_ ',
)
