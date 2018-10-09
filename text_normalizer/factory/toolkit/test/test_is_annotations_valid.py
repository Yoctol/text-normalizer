from unittest import TestCase

from ..is_annotations_valid import (
    is_position_valid,
    segment_has_correct_length,
    is_overlapped,
)


class IsAnnotationsValidTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.normal_annotations = [(4, 6, "希臘"), (10, 17, "abcdgfh")]

    def test_is_position_valid_normal(self):
        output = is_position_valid(self.normal_annotations)
        self.assertEqual(-1, output)

    def test_invalid_position(self):
        output = is_position_valid(
            [(0, 7, '1234'), (3, 2, 'o'), (10, -1, '5678')],
        )
        self.assertEqual(output, 1)

    def test_segment_has_correct_length_normal(self):
        output = segment_has_correct_length(self.normal_annotations)
        self.assertEqual(output, -1)

    def test_segment_has_incorrect_length(self):
        output = segment_has_correct_length(
            [(0, 7, '1234'), (3, 2, 'o'), (10, -1, '5678')],
        )
        self.assertEqual(output, 0)

    def test_is_overlapped(self):
        output = is_overlapped(self.normal_annotations)
        self.assertEqual(output, -1)

    def test_overlapped(self):
        output = is_overlapped(
            [(0, 7, '1234'), (7, 10, 'o'), (9, 13, '5678')],
        )
        self.assertEqual(output, 2)
