import argparse
import os
import csv

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--path', help='Path to graded directories')
parser.add_argument('-c', '--csv', help='Path and filename to csv file')

args = parser.parse_args()

if not args.csv.endswith('.csv'):
    exit('csv must contain the full path to file with a name')

if not args.path.endswith('/'):
    args.path += '/'

grades = {}

for directory in os.listdir(args.path):
    student_id = directory.split('_')[1]
    print(student_id)
    if student_id == 'LATE':
        student_id = directory.split('_')[2]
        grades[student_id] = '0'
    else:
        g = open(args.path + directory + '/grade.txt').readline()
        grades[student_id] = g


reader = csv.reader(open(args.csv, 'r'))
writer = csv.writer(open('updated_' + args.csv, 'w'))

headers = next(reader)
writer.writerow(headers)
headers = next(reader)
writer.writerow(headers)
GRADE = 6
ID    = 1
keys = grades.keys()
while True:
    try:
        line = next(reader)
        if line[ID] in keys:
            line[GRADE] = grades[line[ID]].strip()
        else:
            line[GRADE] = '0'
        writer.writerow(line)
    except StopIteration:
        break

print('Done')
