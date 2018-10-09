

def transform(
        input_str: str,
        forward_annotations: list[tuple(int, int, str)],
        backward_annotations: list[tuple(int, int, str)],
    ) -> str:
    """Transform string based on annotations

    Args:
        input_str: string to be transformed

        forward_annotations: a list of forward annotations which
            indicates the substring of the above should be
            replaced.

        backward_annotations: a list of backward annotations which
            indicates the substring of the result should be
            restored.

        Note that each annotation should comply with the format below
            (start pos(int), end pos(int), original segment(str)).


    Returns:
        a string

    """
    return transform_in_c(
        input_str=input_str,
        forward_annotations=forward_annotations,
        backward_annotations=backward_annotations,
    )


cdef str transform_in_c(  # noqa: E999
        str input_str,
        list forward_annotations,
        list backward_annotations,
    ):

    cdef unsigned int i, n_modif, current_pt
    cdef list output_list
    cdef str output_str

    n_modif = len(forward_annotations)

    if n_modif == 0:
        # no modification return input str
        return input_str

    output_list = [""] * (2 * n_modif + 1)
    current_pt = 0
    for i in range(n_modif):
        output_list[2 * i] = input_str[current_pt: forward_annotations[i][0]]
        output_list[2 * i + 1] = backward_annotations[i][2]
        current_pt = forward_annotations[i][1]

    output_list[-1] = input_str[forward_annotations[-1][1]:]

    output_str = ''.join(output_list)
    return output_str
