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

grades = []

for directory in os.listdir(args.path):
    g = open(args.path + directory + '/grade.txt').readline()
    if g == '':
        g = 'Not Graded'

    grades.append(g)
    print(f'Grades: {grades}')


