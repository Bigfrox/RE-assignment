'''
NOT using RE
Bio Computing Assignment 1, String Manipulation with Regular Expression
2016253072
명수환(Myeong Suhwan)
2에서 5 사이의 크기의 시퀀스 세그먼트가 3회 이상 연속적으로 반복될 때 저복잡도 영역이 정의된다
ex) TAA TAA TAA 
GTA GTA GTA
끝에 패턴이 있는 경우 잡아야함
'''
import random

genes = ['T','A','G','C']

data_rand = ""
num = 5 # * How many genes you wanna make?
while num:
    data_rand += genes[random.randint(0,3)]
    num -= 1

data_rand += "AGCAGCAGCAGCTATATGCGCGCAGCAGCAGCTAGTAGTA G T GGTCC GGTCC G GT C C"
#print(data)

data = ""
data += data_rand

#!
data = "AGAGAGTTATAAGTGGTAGTAGTAGG"
print(data)



index = 0

# * 2개짜리 TATAT AGCTA
# if buffer[0] == buffer[2] == buffer[4] and buffer[1] == buffer[3] == tmp_buffer[0]:
#     print("!!")
#     pattern_found += buffer[0]
#     pattern_found += buffer[1]
#     pattern_found *= 3
#     print(pattern_found)

pattern_size = 5 # 초기화
start_pos = 0
while start_pos + 5< len(data):
    # 초기화
    buffer = [0,0,0,0,0]
    tmp_buffer = [0,0,0,0,0]
    pattern_found = ""
    print("시작")
    index = start_pos
    print(index)
    
    
    
    # * 처음 10개 데이터
    for i in range(len(buffer)):
        
        buffer[i] = data[index]
        index += 1
        if index == len(data):
            break
    for i in range(len(tmp_buffer)):
        tmp_buffer[i] = data[index]
        index += 1
        if index == len(data):
            break
    print(buffer)
    print(tmp_buffer)
    if buffer == tmp_buffer: # * 첫 5개 패턴이 같은 경우
        for i in range(len(tmp_buffer)):
            tmp_buffer[i] = data[index]
            index += 1
        if buffer == tmp_buffer: #! size-5 패턴 found
            for v in buffer:
                pattern_found += v
            print("[Pattern Found]")
            print(pattern_found)
        
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
                print(tmp_buffer)
                for i in range(5-pattern_size):
                    tmp_buffer.pop(-1)
                print(tmp_buffer)
                #print(data[index])
                if buffer == tmp_buffer:
                    for v in buffer:
                        pattern_found += v
                    print("[Pattern Found]")
                    print(pattern_found)
                    break
        if pattern_size <= 2:
            print("Couldn't find a pattern")

    start_pos += 1


    
        



# while(index < len(data)):
#     for i in range(len(buffer)):
#         buffer[i] = data[index]
#         index += 1
        
    
    
    
#     if tmp_buffer == buffer:
#         buffer.pop(0)

#     break


# if tmp_buffer == buffer:
#     print("!!")
# buffer.pop(0)
# print(buffer)
# buffer.append('X')
# print(buffer)