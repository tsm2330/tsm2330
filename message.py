import datetime
import os

path = os.getcwd()

input_list = []
this_input = ""
this_input += ">"
message = ""
today = datetime.datetime.today()
now = today.strftime("%Y/%m/%d %H:%M:%S")
    
while message != 'exit':
    message = input(this_input)
    if message != 'exit' :
        input_list.append(message)
        
path = path+'/log.txt'
f = open(path, 'a',encoding = 'utf-8')
for this_input in input_list:
    f.write(now +' ' + str(this_input) +'\n')
f.close()
