
# No other modules apart from 'csv' need to be imported
# as they aren't required to solve the assignment
# Import required module/s
import csv

def readScoreSheet(file_name):
	name_score_mapping  = {}
	input_file_obj = open(file_name, 'r')
	for line in input_file_obj:
		reader=csv.reader(input_file_obj)
		name_score_mapping=dict(reader)
	input_file_obj.close()
	for values in name_score_mapping:
		name_score_mapping[values]=float(name_score_mapping[values])
	return name_score_mapping

def getTheTopper(mapping_dict):
	name_with_max_score=max(mapping_dict,key=mapping_dict.get)
	return name_with_max_score

if __name__ == "__main__":
	csv_file_name = 'week4_assignment2_sample.csv'
	name_score_mapping = readScoreSheet(csv_file_name)
	print(name_score_mapping)
	topper_name = getTheTopper(name_score_mapping)
	print(topper_name)
