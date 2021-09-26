'''
NOT using RE
Bio Computing Assignment 1, String Manipulation "without" Regular Expression
2016253072
명수환(Myeong Suhwan)
Suppose a low-complexity region is defined when the sequence segment of size between 2 and 5 is repeated consecutively at least 3 times.
ex) TAA TAA TAA 
GTA GTA GTA
'''
import random
import time

start_time = time.time()
genes = ['T','A','G','C']

data_rand = ""
num = 100 # * How many genes you wanna make?
while num:
    data_rand += genes[random.randint(0,3)]
    num -= 1

data_rand += "CCCCCCTATATAAGCAGCAGCAGCTATATGCGCGCAGCAGCAGCTAGTAGTA G T GGTCC GGTCC G GT C CTTTTTTGGGG GGGG"
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

pattern_size = 5 # initialize
start_pos = 0
while start_pos + 5 < len(data):
    # initialize
    buffer = [0,0,0,0,0]
    tmp_buffer = [0,0,0,0,0]
    pattern_found = ""
    index = start_pos
    pattern_size = 5
    #print("start _ :",start_pos)
    
    
    # * from dataset, first 5 data is into buffer.
    # * next 5 data is into temporary buffer.
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
    # print(len(data))
    if buffer == tmp_buffer: # * Case of the pattern size is 5
        tmp_buffer = [0,0,0,0,0]
        for i in range(len(tmp_buffer)):
            tmp_buffer[i] = data[index]
            
            index += 1
            
        if buffer == tmp_buffer: #! size-5 pattern is found
            for v in buffer:
                pattern_found += v
            print("[index]", start_pos, end = " ")
            print("[Pattern]", pattern_found*3)
            print("\n")
            
            start_pos += pattern_size*3
            start_pos -= 1
    elif buffer[0] == buffer[1] == buffer[2] == buffer[3] == buffer[4] == tmp_buffer[0]:
        pattern_size = 2
        pattern_found += buffer[0]*2
        start_pos += pattern_size*3
        start_pos -= 1
        print("[index]", start_pos, end = " ")
        print("[Pattern]", pattern_found*3)
        print("\n")
        
    else: # * Case of the pattern size is less than 5
        
        while pattern_size > 2:
        
            pattern_size -= 1
            tmp_buffer.pop(-1)
            tmp_buffer.insert(0, buffer[-1]) #Push out
            buffer.pop(-1)
            index -= 1
            
            if buffer[:pattern_size] == tmp_buffer[:pattern_size]: # * Comparison : p-size
                #print("=> p-size", pattern_size)
                
                index -= (5-pattern_size-1)
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