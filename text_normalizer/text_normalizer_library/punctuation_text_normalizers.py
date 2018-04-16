from text_normalizer.text_normalizer_factory import ReplacePatternWithToken

CHINESE_PUNCTUATIONS = r"。「」﹁﹂『 』、‧（ ）《》〈〉 ﹏﹏﹏……—～，？；：［］【 】！"
ENGLISH_PUNCTUATIONS = \
    r"\!\#\$\%\&\(\)\*\+\,\-\.\/\:\;\?\@\[\]\{\}\|\~\`\_\^\<\>\=\'\"\\"
ENGLISH_PUNCTUATIONS_WITHOUT_ENDPOINT = ENGLISH_PUNCTUATIONS.replace("\.", "")
ENGLISH_PUNCTUATIONS_WITHOUT_UNDERSCORE = ENGLISH_PUNCTUATIONS.replace("\_", "")


chinese_punctuation_text_normalizer = ReplacePatternWithToken(
    name='chinese_punctuation',
    denormalizable=False,
    target_pattern=r'[{}]+'.format(CHINESE_PUNCTUATIONS),
    prefix_pattern=None,
    suffix_pattern=None,
    token=' ',
)

english_punctuation_text_normalizer = ReplacePatternWithToken(
    name='english_punctuation',
    denormalizable=False,
    target_pattern=r'[{}]+'.format(ENGLISH_PUNCTUATIONS),
    prefix_pattern=None,
    suffix_pattern=None,
    token=' ',
)

all_punctuation_text_normalizer = ReplacePatternWithToken(
    name='all_punctuation',
    denormalizable=False,
    target_pattern=r'[{}]+'.format(ENGLISH_PUNCTUATIONS + CHINESE_PUNCTUATIONS),
    prefix_pattern=None,
    suffix_pattern=None,
    token=' ',
)

all_punctuation_without_endpoint_text_normalizer = ReplacePatternWithToken(
    name='all_punctuation_without_endpoint',
    denormalizable=False,
    target_pattern=r'[{}]+'.format(
        CHINESE_PUNCTUATIONS + ENGLISH_PUNCTUATIONS_WITHOUT_ENDPOINT,
    ),
    prefix_pattern=None,
    suffix_pattern=None,
    token=' ',
)
all_punctuation_without_underscore_text_normalizer = ReplacePatternWithToken(
    name='all_punctuation_without_underscore',
    denormalizable=False,
    target_pattern=r'[{}]+'.format(
        CHINESE_PUNCTUATIONS + ENGLISH_PUNCTUATIONS_WITHOUT_UNDERSCORE,
    ),
    prefix_pattern=None,
    suffix_pattern=None,
    token=' ',
)
