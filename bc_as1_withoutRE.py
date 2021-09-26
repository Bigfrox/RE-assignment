'''
NOT using RE
Bio Computing Assignment 1, String Manipulation "without" Regular Expression
2016253072
명수환(Myeong Suhwan)
2에서 5 사이의 크기의 시퀀스 세그먼트가 3회 이상 연속적으로 반복될 때 저복잡도 영역이 정의된다
ex) TAA TAA TAA 
GTA GTA GTA
'''
import random
import time

start_time = time.time()
genes = ['T','A','G','C']

data_rand = ""
num = 5000000 # * How many genes you wanna make?
while num:
    data_rand += genes[random.randint(0,3)]
    num -= 1

data_rand += "AGCAGCAGCAGCTATATGCGCGCAGCAGCAGCTAGTAGTA G T GGTCC GGTCC G GT C C"
#print(data)
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
#data = data.replace("\n", "")
#!
#data = "GCTCTCTATATACGTCCCGTCCCGTCCA"
print(data)
print("data length : ",len(data))



index = 0

pattern_size = 5 # 초기화
start_pos = 0
while start_pos + 5< len(data):
    # 초기화
    buffer = [0,0,0,0,0]
    tmp_buffer = [0,0,0,0,0]
    pattern_found = ""
    index = start_pos
    pattern_size = 5
    #print("start _ :",start_pos)
    
    
    # * 처음 10개 데이터
    for i in range(len(buffer)):
        
        buffer[i] = data[index]
        index += 1
        if index >= len(data):
            break
    for i in range(len(tmp_buffer)):
        tmp_buffer[i] = data[index]
        index += 1
        if index >= len(data):
            break
    # print(buffer)
    # print(tmp_buffer)
    if buffer == tmp_buffer: # * 첫 5개 패턴이 같은 경우
        for i in range(len(tmp_buffer)):
            tmp_buffer[i] = data[index]
            index += 1
        if buffer == tmp_buffer: #! size-5 패턴 found
            for v in buffer:
                pattern_found += v
            print("[index]", start_pos, end = " ")
            print("[Pattern]", pattern_found*3)
            print("\n")
            
            start_pos += pattern_size*3
        
    else: # * 패턴이 5개가 아닐 경우
        
        while pattern_size > 2:
            pattern_size -= 1
            tmp_buffer.pop(-1)
            tmp_buffer.insert(0, buffer[-1]) #밀어내기
            buffer.pop(-1)
            index -= 1
            
            if buffer[:pattern_size] == tmp_buffer[:pattern_size]: # * p-size개 비교
                #print("=> p-size", pattern_size)
                
                index -= (5-pattern_size)
                #print(index)
                #tmp_buffer = [0,0,0,0,0]
                for i in range(len(buffer)):
                    tmp_buffer[i] = data[index]
                    index += 1
                #print(tmp_buffer)
                for i in range(5-pattern_size):
                    tmp_buffer.pop(-1)
                #print(tmp_buffer)
                #print(data[index])
                if buffer == tmp_buffer:
                    for v in buffer:
                        pattern_found += v
                    print("[index]", start_pos, end = " ")
                    print("[Pattern]", pattern_found*3)
                    print("\n")
                    start_pos += pattern_size*3
                    break
        

    start_pos += 1

print("Time Elapsed : ", time.time() - start_time)