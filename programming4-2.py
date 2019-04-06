# -*- coding: utf-8 -*-
from operator import itemgetter


def month_to_int(month):
	dic = {'Jan' : '1', 'Feb' : '2', 'Mar':'3', 'Apr': '4', 'May' : '5', 'Jun':'6', 'Jul':'7',
		'Aug':'8','Sep':'9','Oct':'10','Nov':'11','Dec':'12'}

	return dic[month]

def int_to_month(month):
	dic = {'1' : 'Jan', '2' : 'Feb', '3':'Mar', '4': 'Apr', '5' : 'May', '6':'Jun', '7':'Jul',
		'8':'Aug','9':'Sep','10':'Oct','11':'Nov','12':'Dec'}
	return dic[month]


def read_weblog(filename):
	fp = open(filename, "r")
	fp.readline()
	index = 0
	while True:
		tmp_lis = []
		one_line = fp.readline().split("\n")[0]
		if not one_line:
			break
		ip, time, url, status = one_line.split(",")
		time = time.split('[')[1]
		time = time.split('/')
		day, month = time[0],month_to_int(time[1])
		time = time[2].split(':')
		year, hour, minute, seconds = time[0],time[1],time[2],time[3]
		log_info = [ip, day,month,year,hour,minute,seconds, url, status]
		weblog_list.append(log_info)
		index+=1
	fp.close()
	

# time = day, month, year, hour,min,seconds
# ip = A,B,C,D
weblog_list = []

def main():
	sort_flag = 0
	while True :
		string = input("$ ")
		command_lis = string.split()
		command1 = command_lis[0]

		if command1 == "exit":
			break
		# ip,time,url,status
		if command1 == "sort" and len(command_lis)==2:
			command2=command_lis[1]
			if command2 == "-ip":
				
				weblog_list.sort(key = lambda elem: elem[0])
				#print(weblog_list[0],weblog_list[1],weblog_list[2],weblog_list[3])
				sort_flag='ip'
			
			elif command2 == "-t":
				
				for i in [6 ,5 ,4 ,1 ,2 , 3]:
					weblog_list.sort(key= lambda elem: elem[i])
				sort_flag='time'
		if command1 == "read" and len(command_lis)==2:
			command2=command_lis[1]
			read_weblog(command2)

		if command1 == "print":
			if sort_flag == 0:
				print("No Sort...\n")
			if sort_flag == 'ip':
				for content in weblog_list:
					print(content[0])
					print('\t'+content[1]+'/'+int_to_month(content[2])+'/'+content[3]+':'+content[4]+':'+content[5]+':'+content[6])
					print('\t'+content[7])
					print('\t'+content[8])
					print("\n-------------------\n")
			if sort_flag == 'time':
				for content in weblog_list:
					print(content[1]+'/'+int_to_month(content[2])+'/'+content[3]+':'+content[4]+':'+content[5]+':'+content[6])
					print('\t'+content[0])
					print('\t'+content[7])
					print('\t'+content[8])
					print("\n-------------------\n")

main()

