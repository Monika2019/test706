# -*- coding: UTF-8 -*-
'''
s1="hello"
s2="world"
s3=" "
print(s1+s3+s2)

for i in range(1,5):
    print(i)
'''

times=3
for i in range(1,times):
    print("\ti=%d"%(i))
    for j in range(1,times):
        print("\t\tj=%d"%(j))
        for k in range(1,times):
            print("\t\t\tk=%d"%(k))
