import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

from matrix.processor import main, add, scale, mult, trans


class TestProcessor(unittest.TestCase):

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_same_dim(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['2 2', '1 2', '3 4', '2 2', '5 6', '7 8']
        add()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('6 8\n10 12\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_diff_dim(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['2 2', '1 2', '3 4', '3 3', '5 6 7', '8 9 10', '11 12 13']
        add()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('ERROR\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_scale(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['2 2', '1 2', '3 4', '3']
        scale()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('3 6\n9 12\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_scale_with_zero(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['2 2', '1 2', '3 4', '0']
        scale()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('0 0\n0 0\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_mult(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['2 2', '1 2', '3 4', '2 2', '5 6', '7 8']
        mult()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('19 22\n43 50\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_mult_with_diff_dim(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['1 2', '1 2', '2 3', '5 6 7', '8 9 10']
        mult()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('21 24 27\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_mult_with_incompatible_dim(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['1 2', '1 2', '3 2', '5 6', '7 8', '9 10']
        mult()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('ERROR\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['1', '2 2', '1 2', '3 4', '2 2', '5 6', '7 8', '0']
        main()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('6 8\n10 12\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_with_floats(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['2 2', '1.1 2.2', '3.3 4.4', '2 2', '5.5 6.6', '7.7 8.8']
        add()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('6.6 8.8\n11 13.2\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_transpose_main_diag(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['1', '3 3', '1 2 3', '4 5 6', '7 8 9']
        trans()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('1 4 7\n2 5 8\n3 6 9\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_transpose_side_diag(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['2', '3 3', '1 2 3', '4 5 6', '7 8 9']
        trans()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('9 6 3\n8 5 2\n7 4 1\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_transpose_vertical(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['3', '3 3', '1 2 3', '4 5 6', '7 8 9']
        trans()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('3 2 1\n6 5 4\n9 8 7\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_transpose_horizontal(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['4', '3 3', '1 2 3', '4 5 6', '7 8 9']
        trans()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('7 8 9\n4 5 6\n1 2 3\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_transpose_main_diag_non_square(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['1', '3 2', '1 2', '3 4', '5 6']
        trans()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('1 3 5\n2 4 6\n'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_transpose_side_diag_non_square(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['2', '3 2', '1 2', '3 4', '5 6']
        trans()
        self.assertNotEqual(-1, mock_stdout.getvalue().find('6 4 2\n5 3 1\n'))
