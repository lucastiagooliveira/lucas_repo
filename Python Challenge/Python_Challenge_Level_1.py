# import string
string  = ('''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.''')


def str_to_list(string):
	new_string = []
	for i in string:
		j = ord(i)
		if j < 96:
			new_string.append(j)
		elif j == 121:
			new_string.append(97)
		elif  j == 122:
			new_string.append(98)
		else: 
			new_string.append(j+2)
	new_string = list(map(lambda x: chr(x), new_string))
	new_string = ''.join(new_string)
	print(new_string)
	return new_string
new_string = str_to_list(string)
var = 'map'.maketrans(string, new_string)
print('map'.translate(var))

