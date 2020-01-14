import os
from sys import argv
import zipfile
from shutil import copyfile, move

gtest_files = os.listdir(os.curdir + '/gtest')
gtest_path = 'gtest/'

solution_file = argv[3]
solution_path = os.curdir + '/'

homework_dir = argv[1] + ('/' if not argv[1].endswith('/') else '')
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
    move(argv[2], submission_dir)
    with zipfile.ZipFile(submission_dir + argv[2]) as zip:
        zip.extractall(submission_dir)
    os.remove(submission_dir + argv[2])


unzip_submissions()

count = 0
for i in os.listdir(submission_dir):
    if ".zip" in i:
        print(f"Extracting: {submission_dir + i}")

        folder_name = submission_dir + i.split('.zip')[0] + '/'
        zip_file = submission_dir + i

        if not os.path.isdir(folder_name):
            print(f'Creating: {folder_name}')
            os.mkdir(folder_name)

        with zipfile.ZipFile(zip_file, 'r') as zip:
            print(f'Extracting files to: {folder_name}')
            zip.extractall(folder_name)
        
        copy_gstest(folder_name)
        copy_solution(folder_name)
        
        open(folder_name + 'grade.txt', 'w')
        print('Success!')
        os.remove(zip_file)
        count += 1

print(f'\nExtracted {count} directories')

