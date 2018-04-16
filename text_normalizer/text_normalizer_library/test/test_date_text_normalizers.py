# -*- coding: utf-8 -*-
from unittest import TestCase

from ..date_text_normalizers import (
    date_text_normalizer_yymmdd,
)


class DateTextNormalizersTestCase(TestCase):

    def test_date_yymmdd_normalize(self):
        test_cases = [
            ('2017-12-07', (' _date_ ', {' _date_ ': ['2017-12-07']})),
            ('2017-1-3', (' _date_ ', {' _date_ ': ['2017-1-3']})),
            ('2017-1-30', (' _date_ ', {' _date_ ': ['2017-1-30']})),
            ('2017-12-3', (' _date_ ', {' _date_ ': ['2017-12-3']})),
            ('3017-12-07', ('3017-12-07', {' _date_ ': []})),
            ('2017-22-07', ('2017-22-07', {' _date_ ': []})),
            ('2017-12-47', ('2017-12-47', {' _date_ ': []})),
            ('今天日期是2017-12-07', ('今天日期是 _date_ ', {' _date_ ': ['2017-12-07']})),
            ('2017-12-07XD', (' _date_ XD', {' _date_ ': ['2017-12-07']})),
            ('現在日期2017-12-07XD', ('現在日期 _date_ XD', {' _date_ ': ['2017-12-07']})),
            ('2017-12-07-00', ('2017-12-07-00', {' _date_ ': []})),
            ('2017-12-0708', ('2017-12-0708', {' _date_ ': []})),
            ('2017-1208-07', ('2017-1208-07', {' _date_ ': []})),
            ('2017-12-07和2018-01-10', (' _date_ 和 _date_ ',
                                       {' _date_ ': ['2017-12-07', '2018-01-10']})),
            ('2017-12-072018-01-10', ('2017-12-072018-01-10', {' _date_ ': []})),
            ('家豪大大亂入', ('家豪大大亂入', {' _date_ ': []})),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    date_text_normalizer_yymmdd.normalize(sentence=test_case[0]),
                )

    def test_date_yymmdd_denormalize(self):
        normal_test_cases = [
            (' _date_ ', {' _date_ ': ['2017-12-18']}, '2017-12-18'),
            ('現在日期 _date_ ', {' _date_ ': ['2017-12-18']}, '現在日期2017-12-18'),
            (' _date_ XD', {' _date_ ': ['2017-12-18']}, '2017-12-18XD'),
            ('現在日期 _date_ XD', {' _date_ ': ['2017-12-18']}, '現在日期2017-12-18XD'),
            (' _date_ 和 _date_ ',
             {' _date_ ': ['2017-12-18', '2018-01-02']}, '2017-12-18和2018-01-02'),
            (' _date_  _date_ ',
             {' _date_ ': ['2017-12-18', '2018-01-02']}, '2017-12-182018-01-02'),
            ('家豪大大亂入', {' _date_ ': []}, '家豪大大亂入'),
        ]
        for test_case in normal_test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[2],
                    date_text_normalizer_yymmdd.denormalize(
                        sentence=test_case[0],
                        meta=test_case[1],
                    ),
                )
        with self.assertRaises(KeyError):
            date_text_normalizer_yymmdd.denormalize(
                sentence='家豪大大亂入',
                meta={'_雞排_': ['大雞排']},
            ),
        with self.assertRaises(ValueError):
            date_text_normalizer_yymmdd.denormalize(
                sentence=' _date_ 和 _date_ 這兩個日期都沒有雞排',
                meta={' _date_ ': ['2017-12-18']},
            )
