def performOperations(N, op):
    list = [i for i in range(1,N+1)]
    for j in op:
        if j in list:
            x = list[0]
            list[0] = list[-1]
            list[-1] = x
            print(list)
        else: 
            list.pop(-1)
            list.append(j)
            print(list) 
        Sum = sum(list)
        print(Sum)
        

N,M = input().strip().split()
N,M = [int(N),int(M)]

op = []
for a0 in range(M):
    op_i = int(input().strip()) 
    op.append(op_i) 

performOperations(N, op) 


