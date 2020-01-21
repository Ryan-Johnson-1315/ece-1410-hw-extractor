from os import path
import subprocess


if __name__ == "__main__":
    if path.exists('a.out'):
        print('Compile sucess')
        subprocess.call("./a.out", shell=True)
    else:
        print('Compile failed')

    with open('files.txt', 'r') as f:
        tmp = f.readlines()

        for i in tmp:
            subprocess.call(f'less {i}', shell=True)
        
    with open('grade.txt', 'w') as f:
        g = input('Grade: ')
        i = input('Comment: ')

        f.write(g + '\n')
        f.write(i + '\n')
