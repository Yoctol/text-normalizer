from unittest import TestCase
from ..strip import Strip


class StripTemplate:

    def test_normalize(self):
        for i in range(len(self.test_cases)):
            test_case = self.test_cases[i]
            with self.subTest(i=test_case):
                result = self.normalizer.normalize(
                    test_case['input'],
                )
                self.assertEqual(
                    test_case['output'],
                    result[0],
                )
                self.assertEqual(
                    test_case['meta'],
                    result[1],
                )

    def test_invertible(self):
        for i in range(len(self.test_cases)):
            test_case = self.test_cases[i]
            with self.subTest(i=test_case):
                result = self.normalizer.normalize(
                    test_case['input'],
                )
                output = self.normalizer.denormalize(
                    result[0],
                    result[1],
                )
                self.assertEqual(
                    test_case['input'],
                    output,
                )


class StripDefaultTestCase(StripTemplate, TestCase):

    @classmethod
    def setUpClass(cls):
        cls.normalizer = Strip()
        cls.test_cases = [
            {
                'input': ' \n\t\n HAHA\t \t \n \n ',
                'output': 'HAHA',
                'meta': {
                    'forward': [(0, 6, ' \n\t\n H'), (8, 17, 'A\t \t \n \n ')],
                    'backward': [(0, 1, 'H'), (3, 4, 'A')],
                },
            },
            {
                'input': ' \n \t \t \n',
                'output': '',
                'meta': {
                    'forward': [(0, 8, ' \n \t \t \n')],
                    'backward': [(0, 0, '')],
                },
            },
            {
                'input': '黃金曼特寧好苦QAQ\t\t\n\n ',
                'output': '黃金曼特寧好苦QAQ',
                'meta': {
                    'forward': [(9, 15, 'Q\t\t\n\n ')],
                    'backward': [(9, 10, 'Q')],
                },
            },
            {
                'input': '\t\t   \n\n我的空白在前面ㄏㄏ',
                'output': '我的空白在前面ㄏㄏ',
                'meta': {
                    'forward': [(0, 8, '\t\t   \n\n我')],
                    'backward': [(0, 1, '我')],
                },
            },
            {
                'input': '隼興大大是專業HR',
                'output': '隼興大大是專業HR',
                'meta': {
                    'forward': [],
                    'backward': [],
                },
            },
        ]


class StripLeftTestCase(StripTemplate, TestCase):

    @classmethod
    def setUpClass(cls):
        cls.normalizer = Strip(direction='left')
        cls.test_cases = [
            {
                'input': ' \n\t\n HAHA\t \t \n \n ',
                'output': 'HAHA\t \t \n \n ',
                'meta': {
                    'forward': [(0, 6, ' \n\t\n H')],
                    'backward': [(0, 1, 'H')],
                },
            },
            {
                'input': ' \n \t \t \n',
                'output': '',
                'meta': {
                    'forward': [(0, 8, ' \n \t \t \n')],
                    'backward': [(0, 0, '')],
                },
            },
            {
                'input': '黃金曼特寧好苦QAQ\t\t\n\n ',
                'output': '黃金曼特寧好苦QAQ\t\t\n\n ',
                'meta': {
                    'forward': [],
                    'backward': [],
                },
            },
            {
                'input': '\t\t   \n\n我的空白在前面ㄏㄏ',
                'output': '我的空白在前面ㄏㄏ',
                'meta': {
                    'forward': [(0, 8, '\t\t   \n\n我')],
                    'backward': [(0, 1, '我')],
                },
            },
            {
                'input': '隼興大大是專業HR',
                'output': '隼興大大是專業HR',
                'meta': {
                    'forward': [],
                    'backward': [],
                },
            },
        ]


class StripRightTestCase(StripTemplate, TestCase):

    @classmethod
    def setUpClass(cls):
        cls.normalizer = Strip(direction='right')
        cls.test_cases = [
            {
                'input': ' \n\t\n HAHA\t \t \n \n ',
                'output': ' \n\t\n HAHA',
                'meta': {
                    'forward': [(8, 17, 'A\t \t \n \n ')],
                    'backward': [(8, 9, 'A')],
                },
            },
            {
                'input': ' \n \t \t \n',
                'output': '',
                'meta': {
                    'forward': [(0, 8, ' \n \t \t \n')],
                    'backward': [(0, 0, '')],
                },
            },
            {
                'input': '黃金曼特寧好苦QAQ\t\t\n\n ',
                'output': '黃金曼特寧好苦QAQ',
                'meta': {
                    'forward': [(9, 15, 'Q\t\t\n\n ')],
                    'backward': [(9, 10, 'Q')],
                },
            },
            {
                'input': '\t\t   \n\n我的空白在前面ㄏㄏ',
                'output': '\t\t   \n\n我的空白在前面ㄏㄏ',
                'meta': {
                    'forward': [],
                    'backward': [],
                },
            },
            {
                'input': '隼興大大是專業HR',
                'output': '隼興大大是專業HR',
                'meta': {
                    'forward': [],
                    'backward': [],
                },
            },
        ]
