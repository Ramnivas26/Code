# LIST TASK - 1

'''
List
List is a collection which is ordered and changeable.
Allows duplicate  members. Denoted by []
Indexes are Present in List
'''

a = [1,2.33,"hi",True,'alpha','beta','theta',33.44,666,100,12.33]

print(a) # ---> [1,2.33,'hi',True,'alpha','beta','theta',33.44,666,100,12.33]
print (a[7]) # ---> 33.44
print (a[-2]) # ---> 100
print (a[1:9]) # ---> [2.33,"hi",True,'alpha','beta','theta',33.44,666]
print (a[3:-1]) # ---> [True,'alpha','beta','theta',33.44,666,100]
print (a[4:]) # ---> ['alpha','beta','theta',33.44,666,100,12.33]
print (a[:9]) # ---> [1,2.33,"hi",True,'alpha','beta','theta',33.44,666]
print (a[:]) # ---> [1,2.33,"hi",True,'alpha','beta','theta',33.44,666,100,12.33]
print(a[0:11:2]) # ---> [1,'hi','alpha','theta',666,12.33]
print(a[::3]) # ---> [1,True,'theta',100]
print(a[::-1]) # ---> [12.33, 100, 666, 33.44, 'theta', 'beta', 'alpha', True, 'hi', 2.33, 1]
