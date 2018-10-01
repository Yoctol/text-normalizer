from unittest import TestCase

from ..transform import transform


class TransfromTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_cases = [
            {
                "input_str": "隼興喜歡希臘神話",
                "forward_annotations": [(4, 6, "希臘")],
                "backward_annotations": [(4, 6, "羅馬")],
                "result": "隼興喜歡羅馬神話",
            },
            {
                "input_str": "隼興喜歡希臘神話",
                "forward_annotations": [(4, 6, "希臘")],
                "backward_annotations": [(4, 10, "羅馬OHOH")],
                "result": "隼興喜歡羅馬OHOH神話",
            },


        ]

    def test_transform(self):
        for i in range(len(self.test_cases)):
            with self.subTest(i=i):
                test_case = self.test_cases[i]
                result = transform(
                    input_str=test_case["input_str"],
                    forward_annotations=test_case["forward_annotations"],
                    backward_annotations=test_case["backward_annotations"],
                )
                self.assertEqual(
                    test_case["result"],
                    result,
                )
