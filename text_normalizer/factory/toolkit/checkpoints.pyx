

def is_equal_length(
        forward_annotations: list[tuple[int, int, str]],
        backward_annotations: list[tuple[int, int, str]],
    ) -> bool:
    return is_equal_length_in_c(
        forward_annotations=forward_annotations,
        backward_annotations=backward_annotations,
    )


def is_input_str_valid(
        input_str: str,
        forward_annotations: list[tuple[int, int, str]],
    ) -> bool:
    return is_input_str_valid_in_c(
        input_str=input_str,
        forward_annotations=forward_annotations,
    )


cdef bint is_equal_length_in_c(  # noqa: E999
        list forward_annotations,
        list backward_annotations,
    ):
    cdef unsigned int f_len, b_len
    f_len = len(forward_annotations)
    b_len = len(backward_annotations)

    if f_len != b_len:
        return False
    else:
        return True


cdef bint is_input_str_valid_in_c(  # noqa: E999
        str input_str,
        list forward_annotations,
    ):
    cdef unsigned int i, start_pos, end_pos, n_anno
    cdef str substring
    cdef bint output

    n_anno = len(forward_annotations)
    output = True
    for i in range(n_anno):
        start_pos = forward_annotations[i][0]
        end_pos = forward_annotations[i][1]
        substring = forward_annotations[i][2]

        if input_str[start_pos: end_pos] != substring:
            output = False
            break

    return output
