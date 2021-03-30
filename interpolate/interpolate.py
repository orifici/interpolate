#!/usr/bin/env python
import sys
import os
from libs.models.math import MainMatrix
from libs.io.file_rw import FileManager


def main():
    # Basic input checks
    if len(sys.argv) != 2:
        sys.exit(f"Wrong program invocation "
                 f"`{' '.join(map(os.path.basename, (sys.argv)))}`\n"
                 f"Please call the program as `interpolate <path_to_file>`")
    if not os.path.exists(sys.argv[1]):
        sys.exit(f"Wrong file path/name: {sys.argv[1]}\n"
                 f"Please check and re-run the program")

    # Read input data
    io_manager = FileManager(path_to_file=sys.argv[1])
    in_matrix = io_manager.read_matrix_from_file()

    # Find nans
    matrix = MainMatrix(data_in=in_matrix)
    nans = matrix.find_nans()

    # Get nearest neighbors for each nan
    # and replace it with their average
    for nan in nans:
        for coords in nan.pairs:
            if coords:
                nan.nearest_neighbors.append(matrix.get_element(*coords))
        nan.set_nn_mean_value()
        matrix.set_element(i=nan.i, j=nan.j, value=nan.nn_mean_value)

    # write output to file
    out_filename = "interpolated_test_data.csv"
    io_manager.write_matrix_to_file(
        matrix=matrix.matrix, path_to_file=out_filename)
    print(f"Successfully created file {out_filename} under {os.getcwd()}")


if __name__ == "__main__":
    sys.exit(main())
