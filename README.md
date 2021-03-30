# Interpolate

Command line utility that allows a user to
interpolate missing values in a
two-dimensional matrix from a csv file


## Requirements

To install and run the utility the only
requirement is **python 3** (or newer)

## Installation

Copy the archive interpolate.tgz into a
`<working_dir>` and then install the
utility using `pip` as shown below
```bash
cd <working_dir>
pip install interpolate.tgz
```
make sure that you can see the below
message as confirmation of a successful
install
```
Successfully installed interpolate-0.0.1
```

## Run the utility
Once installed, the utility will be available
as a command line executable similar to any
other OS command.

Copy an appropriate input file in your
`<working_dir>` and run the utility against
it. Usage example:
```bash
cd <working_dir>
interpolate input_test_data.csv
```
The output will be created in the same
`<working_dir>` with the name
`interpolated_test_data.csv` and the utility
will also print a "success" message to
stdout as below
```
Successfully created file <file_name> under <working_dir>
```

## Uninstall the utility

To uninstall the utility just run
```bash
pip uninstall interpolate
```



# Dev Section

## Requirements

To develop and contribute to the utility,
besides the **python 3** interpreter, you
will need some additional modules installed.
The list of required packages can be found
in the requirements_dev.txt file.

To install the dev packages one can unpack
the interpolate archive and then run
```bash
cd <working_dir>
tar -xzvf interpolate.tgz
cd interpolate
pip install -r requirements_dev.txt
```
the packages installed are required to
- create new versions of the interpolate package
- run the tests

## Install in development mode

To install this software in development
mode you can simply issue
```bash
cd <project_root> # where setup.py is
pip install -e .
```
The `-e` (editable) mode will allow you to modify
the utility and see the changes reflected in the
installed package without having to re-run `pip install`

Once installed in *editable* mode, you can start
developing straight away.

## Running the tests
The utility comes with some basic tests
to help avoid regressions while adding
new features. These tests are of two types
- PEP8 linting
- unit/functional tests

Functional tests can be found under the
`tests` dir.

**PLEASE NOTE:** the below commands requires
you to have installed the
requirements_dev.txt as mentioned in
the previous section

To run **all** tests
```bash
cd <project_root> # where setup.py is
tox
```
To run your linting tests only
```bash
tox -e flake8
```

To run **all** your unit/functional tests
```bash
tox -e unit_tests
```

To speed up testing while developing,
one can also run a single test using
`py.test <path_to_test_file>` as shows below
```bash
py.test tests/models/test_math.py
```
