import math


class MainMatrix():
    """Class that represents the input matrix

    Parameters
    ----------
    data_in : list of lists
        pythonic way to represent a matrix Aij

    Attributes
    ----------
    matrix : list of lists
        pythonic way to represent a matrix Aij
    max_r : int
        max number of rows
    max_c : int
        max number of columns
    """

    def __init__(self, data_in):
        self.matrix = data_in
        self.max_r = len(self.matrix)
        self.max_c = len(self.matrix[0])

    def pretty_print(self):
        """Prints the matrix in a human-readable
        format
        """
        for row in self.matrix:
            print(row)

    def get_element(self, i, j):
        """Get element aij of matrix Aij"""
        return self.matrix[i][j]

    def set_element(self, i, j, value):
        """Set element aij of matrix Aij.
        This is needed to replace the
        `nan` values
        """
        self.matrix[i][j] = value

    def find_nans(self):
        """Traverse the matrix to find all
        `nan` elements and returns them as
        Nan() objects

        Returns
        -------
        nans : list[Nan()]
            returns a list of Nan() objects
        """
        nans = []
        for i, row in enumerate(self.matrix):
            for j, element in enumerate(row):
                if math.isnan(element):
                    nans.append(
                        Nan(i=i, j=j, max_r=self.max_r, max_c=self.max_c))
        return nans


class Nan():
    """Class which represents a `nan` defined by:
    - The nan position in the original matrix (i, j)
    - The nan's 4 nearest neighbors and their positions (i, j)
    - the average of its nearest neighbors

    Parameters
    ----------
    i : int
        row index of the Aij matrix
    j : int
        column index of the Aij matrix
    max_r : int
        number of rows
    max_c : type
        number of columns

    Attributes
    ----------
    nan_coordinates : tuple(int, int)
        a tuple with the row and column
        indexes pair (i, j)
    pairs : list[(i, j), .., (i, j)]
        a list of index couples (i, j)
        of all elements aij around the `nan`s
    nearest_neighbors : list[float, .., float]
        a list of float which are the elements
        aij around the `nans`
    nn_mean_value : float
        arithmetic average of the nearest_neighbors
    _set_nearest_neighbors_coord : list[(i, j), ..,(i, j)]
        sets four pairs of indexes (i, j)
        representing the positions of the `nan`'s
        nearest neighbors. If the `nan` is on
        an edge, the pair can be an empty tuple ()
    """

    def __init__(self, i, j, max_r, max_c):
        self.nan_coordinates = (i, j)
        self.i = i
        self.j = j
        self.max_r = max_r
        self.max_c = max_c
        self.pairs = []
        self.nearest_neighbors = []
        self.nn_mean_value = 0.0
        self._set_nearest_neighbors_coord()

    def _set_nearest_neighbors_coord(self):
        """Works out the 4 nearest neighbors
        relative to the `nan` position at (i, j)
        """
        # left
        self.pairs.append([(self.i-1, self.j) if self.i-1 >= 0 else ()].pop())
        # right
        self.pairs.append(
            [(self.i+1, self.j) if self.i+1 <= self.max_r-1 else ()].pop())
        # up
        self.pairs.append(
            [(self.i, self.j-1) if self.j-1 >= 0 else ()].pop())
        # down
        self.pairs.append(
            [(self.i, self.j+1) if self.j+1 <= self.max_c-1 else ()].pop())

    def set_nn_mean_value(self):
        """Sets nn_mean_value to the average
        of the nearest_neighbors.

        The result is rounded to 6 digits
        """
        den = float(len(self.nearest_neighbors))
        self.nn_mean_value = round(sum(self.nearest_neighbors) / den, 6)

    def __repr__(self):
        """String representation of the `nan`"""
        return str(self.nan_coordinates)
