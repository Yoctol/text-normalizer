from ..replace_pattern_with_token import ReplacePatternWithToken


date_text_normalizer_yymmdd = ReplacePatternWithToken(
    name='date_yymmdd',
    denormalizable=True,
    target_pattern=r'[0-2]*\d\d\d-[0-1]*\d-[0-3]*\d',
    prefix_pattern=r'[^\d-]{1}|\A',
    suffix_pattern=r'[^\d-]{1}|\Z',
    token=' _date_ ',
)
