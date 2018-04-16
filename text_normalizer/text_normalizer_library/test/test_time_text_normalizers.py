# -*- coding: utf-8 -*-
from unittest import TestCase

from ..time_text_normalizers import (
    time_text_normalizer_hhmm,
)


class TimeTextNormalizersTestCase(TestCase):

    def test_time_hhmm_normalize(self):
        test_cases = [
            ('12:18', (' _time_ ', {' _time_ ': ['12:18']})),
            ('現在時間12:18', ('現在時間 _time_ ', {' _time_ ': ['12:18']})),
            ('12:18XD', (' _time_ XD', {' _time_ ': ['12:18']})),
            ('現在時間12:18XD', ('現在時間 _time_ XD', {' _time_ ': ['12:18']})),
            ('12:18:00', ('12:18:00', {' _time_ ': []})),
            ('12:1828', ('12:1828', {' _time_ ': []})),
            ('1233:18', ('1233:18', {' _time_ ': []})),
            ('12:18和19:37', (' _time_ 和 _time_ ', {' _time_ ': ['12:18', '19:37']})),
            ('12:1819:37', ('12:1819:37', {' _time_ ': []})),
            ('家豪大大亂入', ('家豪大大亂入', {' _time_ ': []})),
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[1],
                    time_text_normalizer_hhmm.normalize(sentence=test_case[0]),
                )

    def test_time_hhmm_denormalize(self):
        normal_test_cases = [
            (' _time_ ', {' _time_ ': ['12:18']}, '12:18'),
            ('現在時間 _time_ ', {' _time_ ': ['12:18']}, '現在時間12:18'),
            (' _time_ XD', {' _time_ ': ['12:18']}, '12:18XD'),
            ('現在時間 _time_ XD', {' _time_ ': ['12:18']}, '現在時間12:18XD'),
            (' _time_ 和 _time_ ', {' _time_ ': ['12:18', '19:37']}, '12:18和19:37'),
            (' _time_  _time_ ', {' _time_ ': ['12:18', '19:37']}, '12:1819:37'),
            ('家豪大大亂入', {' _time_ ': []}, '家豪大大亂入'),
        ]
        for test_case in normal_test_cases:
            with self.subTest(test_case=test_case):
                self.assertEqual(
                    test_case[2],
                    time_text_normalizer_hhmm.denormalize(
                        sentence=test_case[0],
                        meta=test_case[1],
                    ),
                )
        with self.assertRaises(KeyError):
            time_text_normalizer_hhmm.denormalize(
                sentence='家豪大大亂入',
                meta={'_雞排_': ['大雞排']},
            ),
        with self.assertRaises(ValueError):
            time_text_normalizer_hhmm.denormalize(
                sentence=' _time_ 和 _time_ 這兩個時間都沒有雞排',
                meta={' _time_ ': ['12:18']},
            )
