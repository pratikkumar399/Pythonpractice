import csv

hello = open('Sample.txt','r')
print(hello)

data = hello.read(100)
# data
# data1 = hello.readline()
# data1

with open('Sample.txt', 'r') as file_obj:
    data1 = file_obj.readline()
print(data1)

with open('Bill2.csv') as fileobj:
    file_data = csv.reader(fileobj)
    for row in file_data:
        print(row)
print(file_data)
