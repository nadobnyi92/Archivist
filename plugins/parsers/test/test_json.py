import unittest
from json_loader import JsonLoader
import pathlib
pathlib.Path(__file__).parent.resolve()
from os import path

class TestJsonLoader(unittest.TestCase):
    def setUp(self) -> None:
        json_path = path.join(pathlib.Path(__file__).parent.resolve(), 'data.json')
        self.loader = JsonLoader(json_path)
        return super().setUp()

    def test_load( self ):
        records = self.loader.importRecords()
        self.assertEqual(len(records), 3)
        self.assertEqual(list(records.keys()), ['2020', '2021', '2022'])
        self.assertEqual(list(records['2020']), )

if __name__ == '__main__':
    unittest.main()
