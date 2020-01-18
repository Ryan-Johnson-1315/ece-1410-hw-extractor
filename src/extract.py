import os
from sys import argv
import zipfile
from shutil import copyfile, move
import subprocess
import argparse

parser = argparse.ArgumentParser('Program that extracts all files in zip folders and compiles them')

parser.add_argument('--submissions', help='Path the submissions zip folder', required=True)
parser.add_argument('--solutions', help='Path to test.cpp file', required=True)
parser.add_argument('--compile', help='Whether to compile the code while extracting', action='store_true')
parser.add_argument('--folder', help='Name of the folder to create (i.e hw3)', required=True)

args = parser.parse_args()


gtest_files = os.listdir(os.curdir + '/gtest')
gtest_path = 'gtest/'

solution_file = args.solutions
solution_path = os.curdir + '/'

homework_dir = args.folder + ('/' if not args.folder.endswith('/') else '')
submission_dir = homework_dir + 'submissions/'

# Make all the dirs
if not os.path.isdir(homework_dir):
    print(f'Creating {homework_dir}')
    os.mkdir(homework_dir)

if not os.path.isdir(submission_dir):
    print(f'Creating {submission_dir}')
    os.mkdir(submission_dir)


def copy_solution(dest):
    copyfile(solution_path + solution_file, dest + solution_file)

def copy_gstest(dest):
    for i in gtest_files:
        copyfile(gtest_path + i, dest + i)

def unzip_submissions():
    move(args.submissions, submission_dir)
    with zipfile.ZipFile(submission_dir + args.submissions) as zip:
        zip.extractall(submission_dir)
    os.remove(submission_dir + args.submissions)
    return len(os.listdir(submission_dir))
def extract_sub_dirs(directory, destination):
    files_copied = open(f'{destination}files.txt', 'a')
    for file in os.listdir(directory):
        #print(f'Checking: {directory + file}...', end='')
        #print(f'if os.path.isfile({file})[{os.path.isfile(file)}] and (".cpp" in {file} or ".hpp" in {file} or ".h" in {file}[{(".cpp" in file or ".hpp" in file or ".h" in file)}])')
        if os.path.isfile(directory + file) and (".cpp" in file or ".hpp" in file or ".h" in file) and ("gtest" not in file and "test.cpp" not in file):
            #print(f'is a source file')
            files_copied.write(file + '\n')
            if directory != destination:
             #   print(f'Copying to {destination}')
                copyfile(directory + file, destination + file)
        elif os.path.isdir(directory + file + '/'):
            #print('is a directory')
            extract_sub_dirs(directory + file + '/', destination)
        #input('')
total = unzip_submissions()

count = 0
not_compiled = list()
for i in os.listdir(submission_dir):
    if ".zip" in i:
        print(f"\nExtracting: {submission_dir + i}")

        folder_name = submission_dir + i.split('.zip')[0] + '/'
        zip_file = submission_dir + i

        if not os.path.isdir(folder_name):
            print(f'\tCreating: {folder_name}')
            os.mkdir(folder_name)

        with zipfile.ZipFile(zip_file, 'r') as zip:
            print(f'\tExtracting files to: {folder_name}')
            zip.extractall(folder_name)
        
        extract_sub_dirs(folder_name, folder_name)

        copy_gstest(folder_name)
        copy_solution(folder_name)
        
        print(f'Extracted {len(os.listdir(folder_name))} files')
        open(folder_name + 'grade.txt', 'w')
        os.remove(zip_file)

        if args.compile:
            print('Compiling code...', end='')

            subprocess.call(f'g++ *.cpp', shell=True, cwd=folder_name, stderr=open(f'{folder_name}error.txt', 'w'))  
            if not os.path.exists(f'{folder_name}a.out'):
                not_compiled.append(folder_name)
                print('failed')
            else:
                os.remove(f'{folder_name}error.txt')
                print('success')
                
            
        count += 1
        print(f'Extracted {count}/{total}')

if args.compile:
    print(f'Compiled {total - len(not_compiled)}/{total} directories')

