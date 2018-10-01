

def search_all(input_str, reg_pattern):
    return search_all_in_c(
        input_str,
        reg_pattern,
    )


cdef list search_all_in_c(  # noqa: E999
        str input_str,
        reg_pattern,
    ):
    cdef unsigned int i, str_len
    cdef list output_list

    i = 0
    str_len = len(input_str)
    output_list = []
    while (i < str_len):
        output = reg_pattern.search(input_str[i:])
        if output is None:
            break
        start, end = output.span()
        output_list.append(
            (start + i, end + i, input_str[start + i: end + i]),
        )
        i += end
    return output_list
