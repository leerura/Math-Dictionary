import csv

data = []
with open('contents.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

English = data[0]
Korean = data[1]

What = input("모르는 영어단어를 쳐주세용")

if What in English:
    num = English.index(What)
    result = Korean[num]
    print(result)