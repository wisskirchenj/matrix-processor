import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

from matrix.processor import main


class TestProcessor(unittest.TestCase):

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_same_dim(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['2 2', '1 2', '3 4', '2 2', '5 6', '7 8']
        main()
        self.assertEqual(mock_stdout.getvalue(), '6 8\n10 12\n')
