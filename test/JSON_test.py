import unittest
from JSON import JSON


class JSONTest(unittest.TestCase):
    def test_init_no_exception(self):
        query = JSON("123.123.123.123")
        try:
            query.parse_json()
        except KeyError:
            self.fail()

    def test_parse_key_exception(self):
        query = JSON("!")
        self.assertRaises(KeyError, query.parse_json())


if __name__ == '__main__':
    unittest.main()
