from ..factory import NumberToken


int_text_normalizer = NumberToken(token="_int_")
float_text_normalizer = NumberToken(token="_float_")
int_with_digit_text_normalizer = NumberToken(token="_{}int_")
float_with_digit_text_normalizer = NumberToken(token="_{}float{}_")

int_with_space_text_normalizer = NumberToken(token=" _int_ ")
float_with_space_text_normalizer = NumberToken(token=" _float_ ")
int_with_digit_n_space_text_normalizer = NumberToken(token=" _{}int_ ")
float_with_digit_n_space_text_normalizer = NumberToken(token=" _{}float{}_ ")
