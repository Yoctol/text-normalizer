from unittest import TestCase
import re

from ..search_all import search_all


class SearchAllTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_cases = [
            {
                "input_str": "   買5 - 80年     五門車~    ",
                "reg_pattern": re.compile(r"\A\s+.{0,1}|.{0,1}\s+\Z"),
                "result": [
                    (0, 4, "   買"),
                    (19, 24, "~    "),
                ],
            },
        ]

    def test_search_all(self):
        for i in range(len(self.test_cases)):
            with self.subTest(i=i):
                test_case = self.test_cases[i]
                result = search_all(
                    input_str=test_case["input_str"],
                    reg_pattern=test_case["reg_pattern"],
                )
                self.assertEqual(
                    test_case["result"],
                    result,
                )
