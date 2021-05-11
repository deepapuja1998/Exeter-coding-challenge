import csv

find_words_file = open('find_words.txt', 'r')
filedata = find_words_file.read()
list = filedata.split()
french = dict()
file = open('french_dictionary.csv', 'r')
csvfile = csv.reader(file)
for row in csvfile:
    french[row[0]] = row[1]
output = dict()
with open('t8.shakespeare.txt', 'r') as main:
    maindata = main.read()
shakespeare = open('t8.shakespeare.txt', 'r')
for line in shakespeare:
    words = line.split()
    for word in words:
        if word in list:
            if word in output:
                output[word] += 1
            else:
                output[word] = 1
                maindata = maindata.replace(word, french[word])
with open('translated.txt', 'w') as outputfile:
    outputfile.write(maindata)
with open('frequency.csv', 'w', newline='') as csvfile:
    fieldnames = ['English', 'French', 'Occurrence']
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    thewriter.writeheader()
    for i in output:
        thewriter.writerow({'English': i, 'French': french[i], 'Occurrence': output[i]})
