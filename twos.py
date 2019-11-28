def flip(c):
	return '1' if (c == '0') else '0'


def TwosComplement(n):
 binn = '{0:016b}'.format( int(bin(~n)[2:]) ) 
 n = len(binn)
 ones = ""
	# for ones complement flip every bit
 for i in range(n):
  ones += flip(binn[i])
 ones = list(ones.strip(""))
 return ''.join(ones)
n = -1
print(TwosComplement(n))
