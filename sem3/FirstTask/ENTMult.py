import time
import math
from multiprocessing import Pool
from collections import Counter

start_time = time.time()

def uniq_count(message):
    return list(Counter(message).values())

def ent(message):
    return -sum([e/len(message)*math.log2(e/len(message)) for e in uniq_count(message)])



if __name__ == '__main__':
	
    file_name = 'newfile.txt'
    bs = 10000
    bs2 = 1
    full_ent = 0
    buffer_list = []

    with open(file_name, 'rb') as f:
        for i in range(2):
            buffer = f.read(bs)
            buffer_list.append(buffer)
            del buffer
    print(len(buffer_list))

    with Pool(2) as p:
        print((sum(p.map(ent,buffer_list)))/len(buffer_list))
    print("%s seconds" % (time.time() - start_time))