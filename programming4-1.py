#-*- coding : utf-8 -*-
import random
import sys
import time


def input_random(size):
    sort_list=[]
    for i in range(0, size):
        sort_list.append(random.randint(1, size))
    return sort_list


def input_reverse(size):
    sort_list=[]
    for i in range(size, 0, -1):
        sort_list.append(i)
    return sort_list


def swap(sort_list, i, j):
    tmp = sort_list[i]
    sort_list[i] = sort_list[j]
    sort_list[j] = tmp
    return sort_list



def MAX_HEAPIFY(sort_list,i):
    heap_size=len(sort_list)
    # 만약 sort_list[i]의 자식노드가 없으면 종료
    if (2*i+1) > heap_size-1 or (2*i+2) > heap_size-1:
        return
    if sort_list[2*i+1] < sort_list[(2*i)+2]:
        k=2*i+2
    else:
        k=2*i+1

    if sort_list[i] >= sort_list[k]:
        return
    swap(sort_list,i,k)
    MAX_HEAPIFY(sort_list,k)

def Build_MAX_HEAP(sort_list):
    heap_size=len(sort_list)
    for i in range(int(heap_size/2),0,-1):
        MAX_HEAPIFY(sort_list,i)

def Heapsort(sort_list):
    Build_MAX_HEAP(sort_list)
    heap_size=len(sort_list)
    for i in range(heap_size-1,1,-1):
        swap(sort_list,0,i)
        heap_size-=1
        MAX_HEAPIFY(sort_list,0)




def main():
	unsort_list=[]
	time_list=[[],[]]
	
	print("\t\t\t\tRandom1000\t\t\tReverse1000\t\t\tRandom10000\t\t\tReverse10000\t\t\tRandom100000\t\t\tReverse100000")



	    #힙 정렬
 
	print("Heap\t\t\t\t\t", end='')
	for i in [1000,10000,100000]:
		unsort_list = input_random(i)
		start_time = time.time()
		Heapsort(unsort_list)
		end_time1 = time.time() - start_time
		time_list[0].append(end_time1)

		unsort_list = input_reverse(i)
		start_time = time.time()
		Heapsort(unsort_list)
		end_time2 = time.time() - start_time
		time_list[0].append(end_time2)

	for t in time_list[0]:
		print("%0.3f" % t, end='\t\t\t\t')
	print("\n")

    # 파이썬 정렬 함수

	print("python\t\t\t\t\t", end='')

	for i in [1000,10000,100000]:

		unsort_list = input_random(i)
		start_time=time.time()
		unsort_list = sorted(unsort_list)
		end_time1 = time.time() - start_time
		time_list[1].append(end_time1)

		unsort_list = input_reverse(i)
		start_time=time.time()
		unsort_list = sorted(unsort_list)
		end_time2 = time.time() - start_time
		time_list[1].append(end_time2)

	for t in time_list[1]:
		print("%0.3f" % t, end='\t\t\t\t')
	print("\n")




main()
