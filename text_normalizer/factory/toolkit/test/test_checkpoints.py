from unittest import TestCase

from ..checkpoints import (
    is_equal_length,
    is_input_str_valid,
)


class CheckpointsTestCase(TestCase):

    def test_not_equal_length(self):
        output = is_equal_length(
            [1, 2, 3],
            [4, 5],
        )
        self.assertFalse(output)

    def test_equal_length_false(self):
        output = is_equal_length(
            [1, 2, 3],
            [4, 5, 6],
        )
        self.assertTrue(output)

    def test_valid_input_str(self):
        output = is_input_str_valid(
            input_str="隼興喜歡希臘神話",
            forward_annotations=[(4, 6, "希臘")],
        )
        self.assertTrue(output)

    def test_invalid_input_str(self):
        output = is_input_str_valid(
            input_str="隼興喜歡希臘神話",
            forward_annotations=[(4, 6, "埃及")],
        )
        self.assertFalse(output)
