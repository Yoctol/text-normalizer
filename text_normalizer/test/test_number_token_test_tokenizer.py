# -*- coding: utf-8 -*-
from unittest import TestCase
from ..number_token_text_normalizer import (
    gen_float_token_with_digit,
    gen_int_token_with_digit,
    sub_token_with_value_sequentially,
    NumberTokenTextNormalizer,
)


class NumberTokenTextNormalizerTestCase(TestCase):

    def run_test_denormalizable(self, test_cases, normalizer):
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    normalizer.normalize(test_case[0]),
                )
                self.assertEqual(
                    test_case[0],
                    normalizer.denormalize(
                        sentence=test_case[1][0],
                        meta=test_case[1][1],
                    ),
                )

    def run_test_not_denormalizable(self, test_cases, normalizer):
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    normalizer.normalize(test_case[0]),
                )
                self.assertEqual(
                    test_case[1][0],
                    normalizer.denormalize(
                        sentence=test_case[1][0],
                        meta=test_case[1][1],
                    ),
                )

    def test_gen_float_token_with_digit(self):
        self.assertEqual(
            ["_1float1_", "_1float5_", "_3float4_", "_4float2_"],
            gen_float_token_with_digit(
                ["2.0", "0.00003", "300.1113", "5000.05"]),
        )

    def test_gen_int_token_with_digit(self):
        self.assertEqual(
            ["_1int_", "_2int_", "_3int_", "_7int_"],
            gen_int_token_with_digit(["1", "20", "300", "5000.05"]),
        )

    def test_sub_token_with_value_sequentially(self):
        test_cases = [
            (
                {
                    "sentence": "A@A@@A@@@AA",
                    "token": "A",
                    "value_list": ["1", "2", "3", "4", "5"],
                },
                "1@2@@3@@@45",
            ),
            (
                {
                    "sentence": "來亂的",
                    "token": "bla",
                    "value_list": [],
                },
                "來亂的",
            ),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    sub_token_with_value_sequentially(**test_case[0]),
                )

    def test_unhandle_case(self):
        with self.assertRaises(KeyError):
            NumberTokenTextNormalizer(token="_ohoh_")

    def test_pure_int(self):
        int_text_normalizer = NumberTokenTextNormalizer(token="_int_")
        test_cases = [
            ("123", ("_int_", {"_int_": ["123"]})),
            ("23.35", ("_int_._int_", {"_int_": ["23", "35"]})),
            ("23 0000", ("_int_ _int_", {"_int_": ["23", "0000"]})),
            ("OHOH 23", ("OHOH _int_", {"_int_": ["23"]})),
            ("122223333 OHOH", ("_int_ OHOH", {"_int_": ["122223333"]})),
            ("１００", ("_int_", {"_int_": ["１００"]})),
            ("3４0分", ("_int_分", {"_int_": ["3４0"]})),
            ("薄餡大大１個打10個", ("薄餡大大_int_個打_int_個", {"_int_": ["１", "10"]})),
            ("0８00-２２-44-６６",
                ("_int_-_int_-_int_-_int_", {"_int_": ["0８00", "２２", "44", "６６"]})),
            ("來亂的", ("來亂的", {"_int_": []})),
        ]
        self.run_test_denormalizable(
            normalizer=int_text_normalizer,
            test_cases=test_cases,
        )

    def test_pure_int_not_denormalizable(self):
        int_text_normalizer_not_denormalizable = NumberTokenTextNormalizer(
            token="_int_",
            denormalizable=False,
        )
        test_cases = [
            ("123", ("_int_", None)),
            ("23.35", ("_int_._int_", None)),
            ("23 0000", ("_int_ _int_", None)),
            ("OHOH 23", ("OHOH _int_", None)),
            ("122223333 OHOH", ("_int_ OHOH", None)),
            ("１００", ("_int_", None)),
            ("3４0分", ("_int_分", None)),
            ("薄餡大大１個打10個", ("薄餡大大_int_個打_int_個", None)),
            ("0８00-２２-44-６６", ("_int_-_int_-_int_-_int_", None)),
            ("來亂的", ("來亂的", None)),
        ]
        self.run_test_not_denormalizable(
            normalizer=int_text_normalizer_not_denormalizable,
            test_cases=test_cases,
        )

    def test_pure_float(self):
        float_text_normalizer = NumberTokenTextNormalizer(token="_float_")
        test_cases = [
            ("49.3", ("_float_", {"_float_": ["49.3"]})),
            ("12.33 456.0", ("_float_ _float_", {"_float_": ["12.33", "456.0"]})),
            ("123", ("123", {"_float_": []})),
            ("94.87分", ("_float_分", {"_float_": ["94.87"]})),
            ("薄餡大大1.5個打10.7個",
                ("薄餡大大_float_個打_float_個", {"_float_": ["1.5", "10.7"]})),
            ("123.456.789", ("123.456.789", {"_float_": []})),
            ("1０0.0００", ("_float_", {"_float_": ["1０0.0００"]})),
            ("９4.87分", ("_float_分", {"_float_": ["９4.87"]})),
            ("薄餡大大1.5個打１０.７個",
                ("薄餡大大_float_個打_float_個", {"_float_": ["1.5", "１０.７"]})),
            ("１２３.４５６.７８９", ("１２３.４５６.７８９", {"_float_": []})),
            ("來亂的", ("來亂的", {"_float_": []})),
        ]
        self.run_test_denormalizable(
            normalizer=float_text_normalizer,
            test_cases=test_cases,
        )

    def test_pure_float_not_denormalizable(self):
        float_text_normalizer = NumberTokenTextNormalizer(
            token="_float_",
            denormalizable=False,
        )
        test_cases = [
            ("49.3", ("_float_", None)),
            ("12.33 456.0", ("_float_ _float_", None)),
            ("123", ("123", None)),
            ("94.87分", ("_float_分", None)),
            ("薄餡大大1.5個打10.7個", ("薄餡大大_float_個打_float_個", None)),
            ("123.456.789", ("123.456.789", None)),
            ("1０0.0００", ("_float_", None)),
            ("９4.87分", ("_float_分", None)),
            ("薄餡大大1.5個打１０.７個", ("薄餡大大_float_個打_float_個", None)),
            ("１２３.４５６.７８９", ("１２３.４５６.７８９", None)),
            ("來亂的", ("來亂的", None)),
        ]
        self.run_test_not_denormalizable(
            normalizer=float_text_normalizer,
            test_cases=test_cases,
        )

    def test_int_with_digit(self):
        intd_text_normalizer = NumberTokenTextNormalizer(token="_{}int_")
        test_cases = [
            ("123", ("_3int_", {"_3int_": ["123"]})),
            ("098765431389", ("_12int_", {"_12int_": ["098765431389"]})),
            ("1 4567890103",
                ("_1int_ _10int_", {"_1int_": ["1"], "_10int_": ["4567890103"]})),
            ("_12float733_", ("_12float733_", {})),
            ("ohoh 000 _33float0_ 1",
             ("ohoh _3int_ _33float0_ _1int_", {"_3int_": ["000"], "_1int_": ["1"]})),
            ("123 345 678 901",
                ("_3int_ _3int_ _3int_ _3int_", {"_3int_": ["123", "345", "678", "901"]})),
            ("１００", ("_3int_", {"_3int_": ["１００"]})),
            ("3４0分", ("_3int_分", {"_3int_": ["3４0"]})),
            ("薄餡大大１個打10個", ("薄餡大大_1int_個打_2int_個", {"_1int_": ["１"], "_2int_": ["10"]})),
            ("0８00-２２-44-６６",
                ("_4int_-_2int_-_2int_-_2int_",
                    {"_4int_": ["0８00"], "_2int_": ["２２", "44", "６６"]})),
            ("來亂的", ("來亂的", {})),
        ]
        self.run_test_denormalizable(
            test_cases=test_cases,
            normalizer=intd_text_normalizer,
        )

    def test_int_with_digit_not_denormalizable(self):
        intd_text_normalizer = NumberTokenTextNormalizer(
            token="_{}int_",
            denormalizable=False,
        )
        test_cases = [
            ("123", ("_3int_", None)),
            ("098765431389", ("_12int_", None)),
            ("1 4567890103", ("_1int_ _10int_", None)),
            ("_12float733_", ("_12float733_", None)),
            ("ohoh 000 _33float0_ 1", ("ohoh _3int_ _33float0_ _1int_", None)),
            ("１００", ("_3int_", None)),
            ("3４0分", ("_3int_分", None)),
            ("薄餡大大１個打10個", ("薄餡大大_1int_個打_2int_個", None)),
            ("0８00-２２-44-６６", ("_4int_-_2int_-_2int_-_2int_", None)),
            ("來亂的", ("來亂的", None)),
        ]
        self.run_test_not_denormalizable(
            test_cases=test_cases,
            normalizer=intd_text_normalizer,
        )

    def test_float_with_digit(self):
        floatd_text_normalizer = NumberTokenTextNormalizer(
            token="_{}float{}_",
        )
        test_cases = [
            ("123.33", ("_3float2_", {"_3float2_": ["123.33"]})),
            ("123", ("123", {})),
            ("1234567890.123456789011",
             ("_10float12_", {"_10float12_": ["1234567890.123456789011"]})),
            ("1.3 224.00", ("_1float1_ _3float2_",
                            {"_1float1_": ["1.3"], "_3float2_": ["224.00"]})),
            ("12.3 34.5 67.8 90.1",
                ("_2float1_ _2float1_ _2float1_ _2float1_",
                    {"_2float1_": ["12.3", "34.5", "67.8", "90.1"]})),
            ("_3int_", ("_3int_", {})),
            ("94.87分", ("_2float2_分", {"_2float2_": ["94.87"]})),
            ("薄餡大大1.5個打10.7個",
                ("薄餡大大_1float1_個打_2float1_個",
                    {"_1float1_": ["1.5"], "_2float1_": ["10.7"]})),
            ("123.456.789", ("123.456.789", {})),
            ("1０0.0００", ("_3float3_", {"_3float3_": ["1０0.0００"]})),
            ("９4.87分", ("_2float2_分", {"_2float2_": ["９4.87"]})),
            ("薄餡大大1.5個打１０.７個",
                ("薄餡大大_1float1_個打_2float1_個",
                    {"_1float1_": ["1.5"], "_2float1_": ["１０.７"]})),
            ("１２３.４５６.７８９", ("１２３.４５６.７８９", {})),
            ("來亂的", ("來亂的", {})),
        ]
        self.run_test_denormalizable(
            test_cases=test_cases,
            normalizer=floatd_text_normalizer,
        )

    def test_float_with_digit_not_denrmalizable(self):
        floatd_text_normalizer = NumberTokenTextNormalizer(
            token="_{}float{}_",
            denormalizable=False,
        )
        test_cases = [
            ("123.33", ("_3float2_", None)),
            ("123", ("123", None)),
            ("1234567890.123456789011", ("_10float12_", None)),
            ("1.3 224.00", ("_1float1_ _3float2_", None)),
            ("_3int_", ("_3int_", None)),
            ("94.87分", ("_2float2_分", None)),
            ("薄餡大大1.5個打10.7個", ("薄餡大大_1float1_個打_2float1_個", None)),
            ("123.456.789", ("123.456.789", None)),
            ("1０0.0００", ("_3float3_", None)),
            ("９4.87分", ("_2float2_分", None)),
            ("薄餡大大1.5個打１０.７個", ("薄餡大大_1float1_個打_2float1_個", None)),
            ("１２３.４５６.７８９", ("１２３.４５６.７８９", None)),
            ("來亂的", ("來亂的", None)),
        ]
        self.run_test_not_denormalizable(
            test_cases=test_cases,
            normalizer=floatd_text_normalizer,
        )

    def test_int_text_normalizer_with_space(self):
        int_text_normalizer_with_space = NumberTokenTextNormalizer(token=" _int_ ")
        test_cases = [
            ("12345678900", (" _int_ ", {" _int_ ": ["12345678900"]})),
            ("340分", (" _int_ 分", {" _int_ ": ["340"]})),
            ("薄餡大大1個打10個", ("薄餡大大 _int_ 個打 _int_ 個", {" _int_ ": ["1", "10"]})),
            ("0800-22-44-66", (" _int_ - _int_ - _int_ - _int_ ",
                               {" _int_ ": ["0800", "22", "44", "66"]})),
            ("１００", (" _int_ ", {" _int_ ": ["１００"]})),
            ("3４0分", (" _int_ 分", {" _int_ ": ["3４0"]})),
            ("薄餡大大１個打10個", ("薄餡大大 _int_ 個打 _int_ 個", {" _int_ ": ["１", "10"]})),
            ("0８00-２２-44-６６", (" _int_ - _int_ - _int_ - _int_ ",
                               {" _int_ ": ["0８00", "２２", "44", "６６"]})),
            ("家豪大大亂入", ("家豪大大亂入", {" _int_ ": []})),
        ]
        self.run_test_denormalizable(
            test_cases=test_cases,
            normalizer=int_text_normalizer_with_space,
        )
        with self.assertRaises(ValueError):
            int_text_normalizer_with_space.denormalize(
                sentence=" _int_ 和 _int_ 這兩個日期都沒有雞排",
                meta={" _int_ ": ["12"]},
            )

    def test_float_text_normalizer_with_space(self):
        float_text_normalizer_with_space = NumberTokenTextNormalizer(token=" _float_ ")
        test_cases = [
            ("100.000", (" _float_ ", {" _float_ ": ["100.000"]})),
            ("94.87分", (" _float_ 分", {" _float_ ": ["94.87"]})),
            ("薄餡大大1.5個打10.7個", ("薄餡大大 _float_ 個打 _float_ 個", {" _float_ ": ["1.5", "10.7"]})),
            ("123.456.789", ("123.456.789", {" _float_ ": []})),
            ("1０0.0００", (" _float_ ", {" _float_ ": ["1０0.0００"]})),
            ("９4.87分", (" _float_ 分", {" _float_ ": ["９4.87"]})),
            ("薄餡大大1.5個打１０.７個", ("薄餡大大 _float_ 個打 _float_ 個", {" _float_ ": ["1.5", "１０.７"]})),
            ("１２３.４５６.７８９", ("１２３.４５６.７８９", {" _float_ ": []})),
            ("家豪大大亂入", ("家豪大大亂入", {" _float_ ": []})),
        ]
        self.run_test_denormalizable(
            test_cases=test_cases,
            normalizer=float_text_normalizer_with_space,
        )

    def test_int_with_digit_n_space(self):
        intd_text_normalizer_with_space = NumberTokenTextNormalizer(token=" _{}int_ ")
        test_cases = [
            ("123", (" _3int_ ", {" _3int_ ": ["123"]})),
            ("098765431389", (" _12int_ ", {" _12int_ ": ["098765431389"]})),
            ("1 4567890103",
                (" _1int_   _10int_ ",
                    {" _1int_ ": ["1"], " _10int_ ": ["4567890103"]})),
            ("_12float733_", ("_12float733_", {})),
            ("ohoh 000 _33float0_ 1",
                ("ohoh  _3int_  _33float0_  _1int_ ",
                    {" _3int_ ": ["000"], " _1int_ ": ["1"]})),
            ("123 345 678 901",
                (" _3int_   _3int_   _3int_   _3int_ ",
                    {" _3int_ ": ["123", "345", "678", "901"]})),
            ("１００", (" _3int_ ", {" _3int_ ": ["１００"]})),
            ("3４0分", (" _3int_ 分", {" _3int_ ": ["3４0"]})),
            ("薄餡大大１個打10個",
                ("薄餡大大 _1int_ 個打 _2int_ 個",
                    {" _1int_ ": ["１"], " _2int_ ": ["10"]})),
            ("0８00-２２-44-６６",
                (" _4int_ - _2int_ - _2int_ - _2int_ ",
                    {" _4int_ ": ["0８00"], " _2int_ ": ["２２", "44", "６６"]})),
            ("來亂的", ("來亂的", {})),
        ]
        self.run_test_denormalizable(
            test_cases=test_cases,
            normalizer=intd_text_normalizer_with_space,
        )

    def test_float_with_digit_n_space(self):
        floatd_text_normalizer_with_space = NumberTokenTextNormalizer(
            token=" _{}float{}_ ",
        )
        test_cases = [
            ("123.33", (" _3float2_ ", {" _3float2_ ": ["123.33"]})),
            ("123", ("123", {})),
            ("1234567890.123456789011",
             (" _10float12_ ", {" _10float12_ ": ["1234567890.123456789011"]})),
            ("1.3 224.00", (" _1float1_   _3float2_ ",
                            {" _1float1_ ": ["1.3"], " _3float2_ ": ["224.00"]})),
            ("12.3 34.5 67.8 90.1",
                (" _2float1_   _2float1_   _2float1_   _2float1_ ",
                    {" _2float1_ ": ["12.3", "34.5", "67.8", "90.1"]})),
            ("_3int_", ("_3int_", {})),
            ("94.87分", (" _2float2_ 分", {" _2float2_ ": ["94.87"]})),
            ("薄餡大大1.5個打10.7個",
                ("薄餡大大 _1float1_ 個打 _2float1_ 個",
                    {" _1float1_ ": ["1.5"], " _2float1_ ": ["10.7"]})),
            ("123.456.789", ("123.456.789", {})),
            ("1０0.0００", (" _3float3_ ", {" _3float3_ ": ["1０0.0００"]})),
            ("９4.87分", (" _2float2_ 分", {" _2float2_ ": ["９4.87"]})),
            ("薄餡大大1.5個打１０.７個",
                ("薄餡大大 _1float1_ 個打 _2float1_ 個",
                    {" _1float1_ ": ["1.5"], " _2float1_ ": ["１０.７"]})),
            ("１２３.４５６.７８９", ("１２３.４５６.７８９", {})),
            ("來亂的", ("來亂的", {})),
        ]
        self.run_test_denormalizable(
            test_cases=test_cases,
            normalizer=floatd_text_normalizer_with_space,
        )
