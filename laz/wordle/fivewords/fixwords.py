with open('word5.txt','rt') as in_list:
  all_words = in_list.readlines()
words = list()
for word in all_words:
  pair = word.split()
  if pair[1] != '2':
    words.append(pair[0])
last_letter = ''
line = ''
for word in words:
  if word[0] != last_letter:
    if len(line) > 0:
      print (line)
      line = ''
    last_letter = word[0]
    count = 0
  line = line + f', "{word}"'
  count = count + 1
  if count > 10:
    count = 0
    print (line) 
    line = ''
print (line)      
