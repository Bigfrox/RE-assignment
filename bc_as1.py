'''
Bio Computing Assignment 1, String Manipulation with Regular Expression
2016253072
명수환(Myeong Suhwan)
2에서 5 사이의 크기의 시퀀스 세그먼트가 3회 이상 연속적으로 반복될 때 저복잡도 영역이 정의된다
ex) TAA TAA TAA 
GTA GTA GTA
'''

import re
import random

genes = ['T','A','G','C']

data_rand = ""
num = 20 # * How many genes you wanna make?
while num:
    data_rand += genes[random.randint(0,3)]
    num -= 1

data_rand += "AGCAGCAGCAGCTATATGCGCGCAGCAGCAGCTAGTAGTA G T GGTCC GGTCC G GT C C"
#print(data)

data_re = re.compile(r'([AGCT]{2,5})\1{2,}') # 왜 {2,}로 해야 잡힐까

#test file
data = ""
filename = 'assignment1_input.txt'
input_file = open(filename, 'r')

with open(filename, 'r') as file:
    line = None
    line = file.readline() # comment
    if(line[0] == '>'):
        print("This is comment")
    while line != '':
        line = file.readline()
        data += line.strip('\n')

data += data_rand
data = data.replace(" ", "")
print(">>>>",data)

found_list = data_re.findall(data)

print(found_list)


start_offset = 0
for v in found_list:
    index = data.find(v*3, start_offset)
    print("[index]", index, end=" ")
    print("[pattern]", v*3)
    print("\n")
    start_offset = index + len(v)*3
#print(index)
