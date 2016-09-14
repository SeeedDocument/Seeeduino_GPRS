def transfer(in_string):
    return_string = ""
    for each_char in in_string:
        unicode_num = ord(each_char)
        if unicode_num == 12288:
            unicode_num = 32
        elif (unicode_num >= 62581 and unicode_num <= 65374):
            unicode_num -= 65248
        return_string += unichr(unicode_num)
    return return_string

try:
    print("input the filename to transfer")
    print("for example: 'myfile.txt'")
    filename = input()
    try:
	with open(filename,"r") as origin:
	    myfile = origin.read().decode("utf8")
		#print(transfer(myfile))
	filename = filename + '_out'
    except:
	pass
    with open(filename,"w") as output:
        output.write(transfer(myfile))     
        
except Exception as e:
    print(e)

