import unittest

from nest import read_input, missing_levels, parse_json
import sys
from io import StringIO


class TestSum(unittest.TestCase):

    def test_read_input_from_stdin(self):
        ''' Test the return from calling this class method '''
        test_input = [
            {
                "country": "US",
                "city": "Boston",
                "currency": "USD",
                "amount": 100
            },
            {
                "country": "FR",
                "city": "Paris",
                "currency": "EUR",
                "amount": 20
            },
            {
                "country": "FR",
                "city": "Lyon",
                "currency": "EUR",
                "amount": 11.4
            },
            {
                "country": "ES",
                "city": "Madrid",
                "currency": "EUR",
                "amount": 8.9
            },
            {
                "country": "UK",
                "city": "London",
                "currency": "GBP",
                "amount": 12.2
            },
            {
                "country": "UK",
                "city": "London",
                "currency": "FBP",
                "amount": 10.9
            }
        ]

        self.assertEqual(read_input(), test_input)

    def test_missing_levels(self):
        nlevels = ['currency', 'country']
        data =  {
            'country': 'US',
            'city': 'London',
            'currency': 'GPB',
            'amount': 12
        }
        result = missing_levels(nlevels, data)
        expected_result = [{'city': 'London'}, {'amount': 12}]
        self.assertEqual(result, expected_result)

    def test_parse_json(self):

        nlevels = ['currency', 'country']
        data = [
            {
                "country": "US",
                "city": "Boston",
                "currency": "USD",
                "amount": 100
            },
            {
                "country": "FR",
                "city": "Paris",
                "currency": "EUR",
                "amount": 20
            },
            {
                "country": "FR",
                "city": "Lyon",
                "currency": "EUR",
                "amount": 11.4
            },
            {
                "country": "ES",
                "city": "Madrid",
                "currency": "EUR",
                "amount": 8.9
            },
            {
                "country": "UK",
                "city": "London",
                "currency": "GBP",
                "amount": 12.2
            },
            {
                "country": "UK",
                "city": "London",
                "currency": "FBP",
                "amount": 10.9
            }
        ]
        result = parse_json(data, nlevels)
        expected_result = {'USD': {'US': [{'city': 'Boston'}, {'amount': 100}]}, 'EUR': {'FR': [{'city': 'Lyon'}, {'amount': 11.4}], 'ES': [{'city': 'Madrid'}, {'amount': 8.9}]}, 'GBP': {'UK': [{'city': 'London'}, {'amount': 12.2}]}, 'FBP': {'UK': [{'city': 'London'}, {'amount': 10.9}]}}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
