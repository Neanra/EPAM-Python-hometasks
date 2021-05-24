"""
File `data/students.csv` stores information about students in CSV format.
This file contains the student’s names, age and average mark.

1. Implement a function get_top_performers which receives file path and
returns names of top performer students.
Example:
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))

Result:
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia',
'Joseph Head']

2. Implement a function write_students_age_desc which receives the file path
with students info and writes CSV student information to the new file in
descending order of age.
Example:
def write_students_age_desc(file_path, output_file):
    pass

Content of the resulting file:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""

import csv

def get_top_performers(file_path, number_of_top_students=5):
    list_of_students = []
    with open(file_path, 'r') as file_handle:
        csv_f = csv.reader(file_handle)
        next(csv_f)
        for row in csv_f:
            name, age, average = row
            list_of_students.append((name, float(average)))
    return list(map(lambda x: x[0], sorted(list_of_students, key = lambda x: x[1], 
                                      reverse=True)[:number_of_top_students]))


def write_students_age_desc(file_path, output_file):
    list_of_students = []
    with open(file_path, 'r') as file_handle:
        reader = csv.reader(file_handle)
        next(reader)
        for row in reader:
            name, age, average = row
            list_of_students.append([name,age,average])
    list_of_students = sorted(list_of_students, key = lambda x: int(x[1]), reverse=True)
    
    with open(output_file, 'w') as output_handle:
        writer = csv.writer(output_handle)
        writer.writerow(['student name', 'age', 'average mark'])
        writer.writerows(list_of_students)
    
