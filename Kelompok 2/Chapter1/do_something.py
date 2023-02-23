#function yang akan dipangil di file lain
import random

def do_something(count,out_list):
	for i in range(count):
		out_list.append(random.random())
