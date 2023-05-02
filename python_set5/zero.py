#Find the number of integers from 1 to n which contains digits 0's in Python
# input the value of N
n=int(input('Enter the value of n: '))

s=str(n)
z=str(0)

if z in s:
    print('Zero is found in {}'.format(n))
else:
    print('Zero is not found in {}'.format(n))
