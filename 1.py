#-*- coding: utf-8 -*-
L = ['Hello', 'World', 18, 'IBM', 'AAAAAAAAAA']
L1 = [s.lower() if isinstance(s, str) == True else s for s in L]
#处理后的L仍保留非字符串
L2 = [s.lower() for s in L if isinstance(s, str)]
#处理后的L不保留非字符串

print('L = ', L)
print('L1 = ', L1)
print('L2 = ', L2)