from unittest import TestCase

from ..label_propagation import (
    # propagate_label,
    backpropagate_label,
)


class LabelPropagationTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        """
        input str: 我想買10元的100c.c.飲料
        result of normalization:
        我想買_int_元的_int_c.c.飲料
        meta = {
            'forward': [(3,5, '10'), (7, 10, '100')],
            'backward': [(3,8, '_int_'), (10, 15, '_int_')],
        }

        """
        cls.meta = {
            'forward': [(3, 5, '10'), (7, 10, '100')],
            'backward': [(3, 8, '_int_'), (10, 15, '_int_')],
        }
        cls.label = [0, 0, 0, 1, 1, 1, 1, 1, 1,
                     0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0]
        cls.expected_label = [0, 0, 0, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0]

    def test_backpropagate_label(self):
        output = backpropagate_label(
            label=self.label,
            annotations=[self.meta],
        )
        self.assertEqual(self.expected_label, output)
