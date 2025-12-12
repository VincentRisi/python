in_file_name = 'D:/vlab/python/laz/wordle/collins2019.txt'

words = list()
with open(in_file_name, 'rt') as in_file:
    lines = in_file.readlines()
    for line in lines:
        for word in line.split():
             words.append(word)
print (words)