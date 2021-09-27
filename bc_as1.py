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
import time

def getDataFromFile(filename):
    data = ""
    try:
        with open(filename, 'r') as file:
            line = None
            line = file.readline() # comment
            if(line[0] == '>'): # * must accept only first FASTA format.
                print("[Comment]")
                print(line)
            else:
                print("No correct format . . .")
            while line != '':
                line = file.readline()
                if line:
                    if(line[0] == '>'):
                        break
                data += line.strip('\n')
    except FileNotFoundError:
        print("No input file . . .")
        
    return data


def getRandomData(num):
    
    genes = ['T','A','G','C']
    if num < 1:
        print("Not generated random sequences . . .")
        
    data_rand = ""
    
    while num:
        data_rand += genes[random.randint(0,3)]
        num -= 1
    
    return data_rand


def main():
    start_time = time.time()

    data_re = re.compile(r'([AGCT]{2,5})\1{2,}') # 왜 {2,}로 해야 잡힐까
    data_not = re.compile(r'[^AGCT]')
    data = ""
    filename = 'assignment1_input.txt'
    #filename = 'no_exist_file.txt'
    #filename = 'multiple.txt'
    data += getDataFromFile(filename)
    num = 500000 # * Generate num DNA Sequences.
    data += getRandomData(num)
    #data += "AGCAGCAGCAGCTATATGCGCGCAGCAGCAGCTAGTAGTA G T GGTCC GGTCC G GT C CtTtTtT" # ? for Exception Check
    data += "AGCT"
    data = data.replace(" ", "")
    data = data.upper()
    if not data:
        print("No DNA Sequences . . .")
        exit(1)
    
    print(">>>>",data)
    no_dna = data_not.findall(data)
    if no_dna:
        print("No DNA Sequences . . .")
        print(no_dna)
        exit(1)
    
    found_list = data_re.findall(data)
    if not found_list:
        print("There is no Low Complexity . . .")
        return

    print(found_list)


    start_offset = 0
    for v in found_list:
        index = data.find(v*3, start_offset)
        print("[index]", index, end=" ")
        print("[pattern]", v*3)
        print("\n")
        start_offset = index + len(v)*3
    #print(index)


    print("Time Elapsed : ", time.time() - start_time)

if __name__ == '__main__':
    main()