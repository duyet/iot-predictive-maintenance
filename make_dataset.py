#!/bin/python

import argparse
from glob import glob
from os.path import basename, join
import pandas as pd
import numpy as np

def parse_files(file_pattern, columns, label_data = False):
    """Parse a set of raw data files into a single DataFrame object.
        Parameters
        ----------
        file_pattern : str
            pattern to match filenames for parsing
        columns : list
            names of columns to assign to the parsed file
        label_data : bool (optional, default = False)
            flag to indicate that we're reading RUL label files
        Returns
        -------
        pandas.DataFrame
            dataframe representation of all files matching file_pattern, with appropriate column names
    """
    # get all of the data files from the input directory
    data_sets = []
    for data_file in glob(file_pattern):
        if label_data:
            # read in contents as a DataFrame
            subset_df = pd.read_csv(data_file, header=None)
            # need to create a unit_id column explicitly
            unit_id = range(1, subset_df.shape[0] + 1)
            subset_df.insert(0, 'unit_id', unit_id)
        else:
            # read in contents as a DataFrame
            subset_df = pd.read_csv(data_file, sep=' ', header=None, usecols=range(26))
        # extract the id of the dataset from the name and add as a column
        dataset_id = basename(data_file).split("_")[1][:5]
        subset_df.insert(0, 'dataset_id', dataset_id)
        # add to list
        data_sets.append(subset_df)
    # combine dataframes
    df = pd.concat(data_sets)
    df.columns = columns
    # return the result
    return df

def main():
	# parse command line arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("input_path", help="path to the raw data files")
	parser.add_argument("output_path", help="location to store output data files")
	args = parser.parse_args()
	# define column names
	sensor_columns = ["sensor {}".format(s) for s in range(1,22)]
	info_columns = ['dataset_id', 'unit_id','cycle','setting 1', 'setting 2', 'setting 3']
	label_columns = ['dataset_id', 'unit_id', 'rul']
	# process all data sets
	for set_type in ['train', 'test', 'RUL']:
		# construct the input file path
		base_input_pattern = set_type + '_*.txt'
		full_input_pattern = join(args.input_path, base_input_pattern)
		# parse raw files
		if set_type == 'RUL':
			df = parse_files(full_input_pattern, label_columns, label_data = True)
		else:
			df = parse_files(full_input_pattern, info_columns + sensor_columns)
		# construct the output file path
		base_output_name = set_type + '.csv'
		full_output_path = join(args.output_path, base_output_name)
		# write to csv
		df.to_csv(full_output_path, index=False)

if __name__ == '__main__':
  main()
