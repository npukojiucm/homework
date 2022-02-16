import os
from pathlib import Path


path_file = Path(Path.cwd(), '..', 'Read and write file', 'Files')
filename_list = []

for path in Path(path_file).glob('*.txt'):
    filename_list.append(path)

file_att = {}
file_len = []

for file in filename_list:
    with open(file, encoding='UTF-8') as f:
        len_ = len(f.readlines())
        if len_ in file_att.keys():
            file_att[len_] += [file]
        else:
            file_att[len_] = [file]

for key_ in file_att:
    file_len.append(key_)
    file_len.sort()

path_job = Path(Path.cwd(), '..', 'Read and write file', Path('my_job.txt'))
with open(path_job, 'w') as f:
    for len_ in file_len:
        for name_file in file_att.get(len_):
            f.write(os.path.basename(name_file) + '\n')
            f.write(str(len_) + '\n')
            with open(name_file, encoding='utf-8') as r:
                for line in r:
                    f.write(line.strip() + '\n')
