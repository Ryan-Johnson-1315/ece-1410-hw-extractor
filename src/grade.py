import argparse
import os
import csv

parser = argparse.ArgumentParser()

#parser.add_argument('-p', '--path', help='Path to graded directories')
parser.add_argument('-c', '--csv', help='Path and filename to csv file')

args = parser.parse_args()
#
#if not args.csv.endswith('.csv'):
#    exit('csv must contain the full path to file with a name')
#
#if not args.path.endswith('/'):
#    args.path += '/'
#
#grades = {}
#
#for directory in os.listdir(args.path):
#    late = False
#    student_id = directory.split('_')[1]
#    print(student_id)
#    if student_id == 'LATE'
#        late = True
#        student_id = directory.split('_')[2]
#    
#    
#    if late:
#        grades[student_id] = 0
#    else
#        g = open(args.path + directory + '/grade.txt').readline()
#        grades[student_id] = int(g)
#
#

reader = csv.reader(open(args.csv, 'r'))
writer = csv.writer(open('updated_' + args.csv, 'w'))

headers = next(reader)
writer.writerow(headers)
GRADE = 6
ID    = 1

while True:
    line = next(reader)
    line[GRADE] = 25
    print(line)
    exit(0)    
print(headers)
