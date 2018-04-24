# -*- coding: utf-8 -*-
from unittest import TestCase
from ..eng_lowercase_text_normalizer import EngLowercaseTextNormalizer


class EngLowercaseTextNormalizerTestCase(TestCase):

    def setUp(self):
        self.eng_lowercase_text_normalizer = EngLowercaseTextNormalizer()

    def test_lowercase(self):
        test_cases = [
            (
                "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ",
                "abcdefghijklmnopqrstuvwxyz",
            ),
            (
                "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ",
                "abcdefghijklmnopqrstuvwxyz",
            ),
            (
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "abcdefghijklmnopqrstuvwxyz",
            ),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    self.eng_lowercase_text_normalizer.lowercase(
                        sentence=test_case[0],
                    ),
                )

    def test_normalize_n_denormalize_0(self):
        test_cases = [
            (
                "哈囉 AAB 123 Cddef 哈囉 >< ???",
                (
                    "哈囉 aab 123 cddef 哈囉 >< ???",
                    [
                        {
                            "before": "AAB",
                            "after": "aab",
                        },
                        {
                            "before": "Cddef",
                            "after": "cddef",
                        },
                    ],
                ),
                "哈囉 AAB 123 Cddef 哈囉 >< ???",
            ),
            (
                "AAB 123 哈囉 Cddef 456 ffecI",
                (
                    "aab 123 哈囉 cddef 456 ffeci",
                    [
                        {
                            "before": "AAB",
                            "after": "aab",
                        },
                        {
                            "before": "Cddef",
                            "after": "cddef",
                        },
                        {
                            "before": "ffecI",
                            "after": "ffeci",
                        },
                    ],
                ),
                "AAB 123 哈囉 Cddef 456 ffecI",
            ),
            (
                "家豪大大亂入吃雞排",
                ("家豪大大亂入吃雞排", None),
                "家豪大大亂入吃雞排",
            ),
            (
                "ａbc",
                (
                    "abc",
                    [
                        {
                            "before": "ａbc",
                            "after": "abc",
                        },
                    ],
                ),
                "ａbc",
            ),
        ]

        for test_case in test_cases:
            with self.subTest(
                test_case="normalize {}".format(test_case[0]),
            ):
                self.assertEqual(
                    test_case[1],
                    self.eng_lowercase_text_normalizer.normalize(
                        sentence=test_case[0],
                    ),
                )
            with self.subTest(
                test_case="denormalize {}".format(test_case[0]),
            ):
                self.assertEqual(
                    test_case[2],
                    self.eng_lowercase_text_normalizer.denormalize(
                        sentence=test_case[1][0],
                        meta=test_case[1][1],
                    ),
                )
