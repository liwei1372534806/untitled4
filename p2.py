"""
打印99乘法表
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i * j), end=' ')
    print()

print("-------------------------------------------------------------------")
i=1
while i<10:
    j=1
    while j<=i:
        # print('{}x{}={}\t'.format(j, i, i * j), end=' ')
        print('%dx%d=%-2d'%(j,i,i * j),end='  ')
        j+=1
    print()
    i += 1


