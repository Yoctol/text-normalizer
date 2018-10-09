

def is_annotations_valid(
        annotations: list[tuple[int, int, str]],
    ) -> None:
    is_annotations_valid_in_c(annotations=annotations)


def is_position_valid(
        annotations: list[tuple[int, int, str]],
    ) -> int:
    return is_position_valid_in_c(annotations=annotations)


def segment_has_correct_length(
        annotations: list[tuple[int, int, str]],
    ) -> int:
    return segment_has_correct_length_in_c(annotations=annotations)


def is_overlapped(
        annotations: list[tuple[int, int, str]],
    ) -> int:
    return is_overlapped_in_c(annotations=annotations)


cdef void is_annotations_valid_in_c(  # noqa: E999
        list annotations,
    ) except *:

    cdef int check

    check = is_position_valid_in_c(annotations=annotations)
    if check > 0:
        raise ValueError(
            'start position is bigger than end position at [{}]'.format(check),
        )

    check = segment_has_correct_length_in_c(annotations=annotations)
    if check > 0:
        raise ValueError(
            'len of segment is not correct at [{}]'.format(check),
        )

    check = is_overlapped_in_c(annotations=annotations)
    if check > 0:
        raise ValueError(
            'annotations is overlapped at [{}]'.format(check),
        )


cdef int is_position_valid_in_c(  # noqa: E999
        list annotations
    ):
    cdef unsigned int n_anno, i, start_pos, end_pos
    cdef int output = -1

    n_anno = len(annotations)
    for i in range(n_anno):
        start_pos = annotations[i][0]
        end_pos = annotations[i][1]
        if start_pos > end_pos:
            output = i
            break
    return output


cdef int segment_has_correct_length_in_c(  # noqa: E999
        list annotations,
    ):
    cdef unsigned int i, n_anno, length, s_len
    cdef int output = -1

    n_anno = len(annotations)
    for i in range(n_anno):
        length = annotations[i][1] - annotations[i][0]
        s_len = len(annotations[i][2])
        if s_len != length:
            output = i
            break
    return output


cdef int is_overlapped_in_c(  # noqa: E999
        list annotations,
    ):
    cdef unsigned int i, n_anno, pt
    cdef bint output = -1

    n_anno = len(annotations)
    pt = annotations[0][1]
    for i in range(1, n_anno):
        if pt > annotations[i][0]:
            output = i
            break
        pt = annotations[i][1]
    return output
