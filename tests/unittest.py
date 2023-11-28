import unittest
import pandas as pd
from src.loader import SlackDataLoader

class TestSlackDataLoader(unittest.TestCase):

    def setUp(self):
        self.data_loader = SlackDataLoader()

    def test_load_slack_data(self):
        df = self.data_loader.load_slack_data('path/to/slack_channel_data')
        expected_columns = ['user', 'timestamp', 'message']
        self.assertListEqual(df.columns.tolist(), expected_columns)

if __name__ == '__main__':
    unittest.main()


