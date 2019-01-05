cdef void is_annotations_valid_in_c(  # noqa: E999
    list annotations,
) except *


cdef int is_position_valid_in_c(  # noqa: E999
    list annotations
)


cdef int segment_has_correct_length_in_c(  # noqa: E999
    list annotations,
)


cdef int is_overlapped_in_c(  # noqa: E999
    list annotations,
)
