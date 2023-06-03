import sys
R, C = [int(x) for x in sys.stdin.readline().split()]
print('#'* int(C), end = '  \n')
for i in range(R-2):
    print('#'+'.'*int(C-2),end ='# \n')
print('#'* int(C), end = '  \n')
