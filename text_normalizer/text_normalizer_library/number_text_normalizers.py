from text_normalizer.text_normalizer_factory import NumberTokenTextNormalizer


int_text_normalizer = NumberTokenTextNormalizer(token="_int_")
float_text_normalizer = NumberTokenTextNormalizer(token="_float_")
int_with_digit_text_normalizer = NumberTokenTextNormalizer(token="_{}int_")
float_with_digit_text_normalizer = NumberTokenTextNormalizer(token="_{}float{}_")

int_with_space_text_normalizer = NumberTokenTextNormalizer(token=" _int_ ")
float_with_space_text_normalizer = NumberTokenTextNormalizer(token=" _float_ ")
int_with_digit_n_space_text_normalizer = NumberTokenTextNormalizer(token=" _{}int_ ")
float_with_digit_n_space_text_normalizer = NumberTokenTextNormalizer(token=" _{}float{}_ ")
