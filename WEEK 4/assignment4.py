

# No other modules apart from 'csv' need to be imported
# as they aren't required to solve the assignment
# Import required module/s
import csv
def readMarkSheet(file_name):
	name_marks_mapping = {}
	input_file_obj = open(file_name, 'r')
	reader=csv.reader(input_file_obj)
	next(reader)
	for row in reader:
		name_marks_mapping[row[0]]={'marks':[float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5])]}
	input_file_obj.close()
	return name_marks_mapping

def generateGradeCard(mapping_dict):
	grade_card = {}
	for key in mapping_dict:
		total=0
		for i in mapping_dict[key]:
			for j in range(0,len(mapping_dict[key][i])):
				total=total+(mapping_dict[key][i][j])
			total=(total/500)*100
			if(total>=90):
				grade='O'
			elif(total>=70):
				grade='A'
			elif(total>=60):
				grade='B'
			elif(total>=50):
				grade='C'
			elif(total>=40):
				grade='D'
			else:
				grade='Fail'
		grade_card[key]={'subject_wise_marks': mapping_dict[key][i], 'grade_received': grade}
	return grade_card

if __name__ == "__main__":
	csv_file_name = 'week4_assignment4_sample.csv'
	name_marks_mapping = readMarkSheet(csv_file_name)
	print(name_marks_mapping)
	grade_card = generateGradeCard(name_marks_mapping)
	print(grade_card)
