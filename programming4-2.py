# -*- coding: utf-8 -*-
from operator import itemgetter


def read_weblog(filename):
	fp=open(filename,"r")
	fp.readline()
	index=0
	while True:
		tmp_lis=[]
		one_line=fp.readline().split("\n")[0]
		if not one_line:
			break
		ip,time,url,status=one_line.split(",")
		log_info=[ip,time,url,status]
		weblog_list.append(log_info)
		index+=1
	fp.close()



weblog_list=[]

def main():
	while True :
		string = input("$ ")
		command_lis=string.split()
		command1=command_lis[0]



		if command1 == "exit":
			break
		# ip,time,url,status
		if command1 == "sort" and len(command_lis)==2:
			command2=command_lis[1]
			if command2 == "-ip":
				weblog_list.sort(key=itemgetter(0))
			elif command2 == "-t":
				weblog_list.sort(key=itemgetter(1))
			elif command2 == "-url":
				weblog_list.sort(key=itemgetter(2))
			elif command2 == "-status":
				weblog_list.sort(key=itemgetter(3))
		if command1 == "read" and len(command_lis)==2:
			command2=command_lis[1]
			read_weblog(command2)

		if command1 == "print":
			for content in weblog_list:
				print(content[0])
				print(content[1])
				print(content[2])
				print(content[3])
				print("\n-------------------\n")


main()

