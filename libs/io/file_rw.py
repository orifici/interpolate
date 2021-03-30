import os


class FileManager():
    """Utility class to manage read/writes to files

    Parameters
    ----------
    path_to_file : string
        absolute path to the input/output file
    """

    def __init__(self, path_to_file):
        self.path_to_file = os.path.abspath(path_to_file)

    def read_matrix_from_file(self):
        """Reads a matrix from an input file.
        Casts each element from string to float.

        Returns
        -------
        matrix : list of lists
            returns the matrix as a list of lists
        """
        matrix = []
        with open(self.path_to_file, "r") as file_in:
            for line in file_in:
                matrix.append(list(map(float, line.rstrip().split(","))))
        return matrix

    def write_matrix_to_file(self, matrix, path_to_file):
        """Write a matrix to an output file.
        Casts each element from float to string.
        """
        with open(path_to_file, 'w') as file_out:
            for row in matrix:
                file_out.write(",".join(map(str, row)))
                file_out.write('\n')
