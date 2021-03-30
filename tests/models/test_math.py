import unittest
from libs.models.math import MainMatrix, Nan


class TestMainMatrix(unittest.TestCase):
    """Class to test basic methods of the
    MainMatrix() class
    """
    @classmethod
    def setUpClass(cls):
        """Prepares 5 different matrices and
        their `nan`s coordinates (i, j) as global
        attributes
        """
        cls.matrix_1 = MainMatrix(data_in=[
            [1, 2],
            [3, 4],
            [5, 6]
        ])
        cls.m1_nans = []

        cls.matrix_2 = MainMatrix(data_in=[
            [1, 2, float('nan')],
            [3, float('nan'), 4],
            [float('nan'), 6, 7]
        ])
        cls.m2_nans = [(0, 2), (1, 1), (2, 0)]

        cls.matrix_3 = MainMatrix([
            [1, 2, float('nan')],
        ])
        cls.m3_nans = [(0, 2)]

        cls.matrix_4 = MainMatrix(data_in=[
            [1, ],
            [2, ],
            [float('nan')]
        ])
        cls.m4_nans = [(2, 0)]

        cls.matrix_5 = MainMatrix([
            [float('nan'), float('nan'), float('nan')],
            [float('nan'), float('nan'), float('nan')]
        ])
        cls.m5_nans = [
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2)
        ]

    def test_find_nans(self):
        """Tests the MainMatrix find_nans method
        using 5 different input matrices
        """
        # matrix 1 is (2x3) and has no nans
        nans = self.matrix_1.find_nans()
        self.assertEqual(len(nans), 0)
        self.assertEqual(self.matrix_1.max_r, 3)
        self.assertEqual(self.matrix_1.max_c, 2)

        # matrix 2 is (3x3) and has 3 nans
        nans = self.matrix_2.find_nans()
        self.assertEqual(len(nans), 3)
        self.assertEqual(self.matrix_2.max_r, 3)
        self.assertEqual(self.matrix_2.max_c, 3)
        coords = []
        for n in nans:
            coords.append((n.i, n.j))
        self.assertEqual(coords, self.m2_nans)

        # matrix 3 is (1x3) and has 1 nans
        nans = self.matrix_3.find_nans()
        self.assertEqual(len(nans), 1)
        self.assertEqual(self.matrix_3.max_r, 1)
        self.assertEqual(self.matrix_3.max_c, 3)
        coords = []
        for n in nans:
            coords.append((n.i, n.j))
        self.assertEqual(coords, self.m3_nans)

        # matrix 4 is (3x1) and has 1 nans
        nans = self.matrix_4.find_nans()
        self.assertEqual(len(nans), 1)
        self.assertEqual(self.matrix_4.max_r, 3)
        self.assertEqual(self.matrix_4.max_c, 1)
        coords = []
        for n in nans:
            coords.append((n.i, n.j))
        self.assertEqual(coords, self.m4_nans)

        # matrix 5 is (2x3) and has 6 nans
        nans = self.matrix_5.find_nans()
        self.assertEqual(len(nans), 6)
        self.assertEqual(self.matrix_5.max_r, 2)
        self.assertEqual(self.matrix_5.max_c, 3)
        coords = []
        for n in nans:
            coords.append((n.i, n.j))
        self.assertEqual(coords, self.m5_nans)


class TestNan(unittest.TestCase):
    """Class to test basic methods of
    the Nan() class
    """
    @classmethod
    def setUpClass(cls):
        """Prepares 5 `nan`s location
        and the corresponding nearest_neighbors
        expected coordinates (i, j)
        """
        cls.nan_locations = [
            (0, 0, 2, 2), (0, 3, 4, 4),
            (3, 0, 4, 4), (3, 3, 4, 4),
            (1, 1, 3, 3)
        ]
        cls.expected_nn = [
            [(1, 0), (0, 1)], [(0, 2), (1, 3)],
            [(2, 0), (3, 1)], [(2, 3), (3, 2)],
            [(0, 1), (1, 2), (1, 0), (1, 2)]
        ]

    def test_nn_pairs(self):
        """Test that from the nan_locations the
        expected nearest_neighbors are as in expected_nn
        """
        nans = []
        for i in self.nan_locations:
            nans.append(Nan(*i))
        for i, n in enumerate(nans):
            expected_pairs = self.expected_nn[i]
            # For each nan, test the number of
            # nearest neighbors is correct
            self.assertEqual(
                len(expected_pairs),
                len([x for x in n.pairs if x != ()])
            )
            # Test nearest neighbors coordinates
            for pair in expected_pairs:
                self.assertIn(pair, n.pairs)
