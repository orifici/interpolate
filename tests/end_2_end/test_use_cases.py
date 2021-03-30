import mock
import unittest
from interpolate.interpolate import main


class MockFileManager():
    """Mock class to test the happy path use case.
    This class mocks the FileManager() class so
    that we don't need to read/write to the file system
    """

    def __init__(self, mock_matrix):
        self.mock_matrix = mock_matrix
        self.final_matrix = None

    def read_matrix_from_file(self):
        return self.mock_matrix

    def write_matrix_to_file(self, matrix, path_to_file):
        self.final_matrix = matrix


class TestHappyPath(unittest.TestCase):
    """Class to test the happy path.
    From the matrix `matrix` we should obtain
    the matrix `expected_res`, after `nan`
    substitutions
    """
    @classmethod
    def setUpClass(cls):
        """Prepares an input matrix and
        the corresponding expected matrix
        """
        cls.matrix = [
            [float('nan'), 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, float('nan'), 12],
            [13, 14, 15, 16],
        ]
        cls.expected_res = [
            [3.5, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]

    @mock.patch('interpolate.interpolate.FileManager')
    def test_happy_path(self, file_manager):
        """Test of the main() function as an unknown "box"

        By mocking the FileManger() class we can test the
        main() function of our package fully, with the only
        exception of I/O
        """
        file_manager.return_value = MockFileManager(mock_matrix=self.matrix)
        main()
        self.assertEqual(
            file_manager.return_value.final_matrix,
            self.expected_res
        )
