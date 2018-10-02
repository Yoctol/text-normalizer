

def propagate_label(
        label: list[int],
        annotations: list[dict],
    ) -> list[int]:
    return propagate_label_in_c(
        label=label,
        annotations=annotations,
    )


def backpropagate_label(
        label: list[int],
        annotations: list[dict],
    ) -> list[int]:
    return backpropagate_label_in_c(
        label=label,
        annotations=annotations,
    )


cdef list propagate_label_in_c(  # noqa: E999
        list label,
        list annotations,  # list of dict
    ):
    cdef unsigned int i, n_anno

    n_anno = len(annotations)
    for i in range(n_anno):
        label = propagate_label_for_a_pair_of_annotations_in_c(
            label=label,
            forward_annotations=annotations[i]['forward'],
            backward_annotations=annotations[i]['backward'],
        )
    return label


cdef list backpropagate_label_in_c(  # noqa: E999
        list label,
        list annotations,
    ):
    cdef unsigned int i, j, n_anno

    n_anno = len(annotations)
    for i in range(n_anno - 1, -1, -1):
        label = propagate_label_for_a_pair_of_annotations_in_c(
            label=label,
            forward_annotations=annotations[i]['backward'],
            backward_annotations=annotations[i]['forward'],
        )
    return label


cdef list propagate_label_for_a_pair_of_annotations_in_c(  # noqa: E999
        list label,
        list forward_annotations,  # list of tuples
        list backward_annotations,  # list of tuples
    ):

    cdef unsigned int i, n_fmodif, n_bmodif, current_pt
    cdef list output_label

    n_fmodif = len(forward_annotations)
    n_bmodif = len(backward_annotations)

    if n_fmodif != n_bmodif:
        raise ValueError(
            f'number of forward and backward modifications is not the same')

    if n_bmodif == 0:
        # no modification return label
        return label

    output_label = [0] * (2 * n_fmodif + 1)
    current_pt = 0
    for i in range(n_fmodif):
        # before annotations
        output_label[2 * i] = label[current_pt: forward_annotations[i][0]]

        # annotate
        merged_label = get_high_freq_label(
            label[forward_annotations[i][0]: forward_annotations[i][1]])
        n_labels = backward_annotations[i][1] - backward_annotations[i][0]
        output_label[2 * i + 1] = [merged_label] * n_labels

        current_pt = forward_annotations[i][1]

    output_label[-1] = label[forward_annotations[-1][1]:]

    output_label = sum(output_label, [])
    return output_label


cdef unsigned int get_high_freq_label(  # noqa: E999
    list label):

    cdef unsigned int max_f, label_f
    cdef dict record = {}

    max_f = 0
    label_f = 0
    for l in label:
        if l not in record:
            record[l] = 1
        else:
            record[l] += 1

        if record[l] > max_f:
            max_f = record[l]
            label_f = l
    return label_f
