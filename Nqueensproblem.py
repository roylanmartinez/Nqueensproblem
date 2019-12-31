''' dimension stands for the board dimension, it has to be an integer bigger than 3'''

dimension=10

# ---------------
def printer(vec):
    for j in range(len(vec)):
        for i in range(len(vec)):
            if i==vec[j][1]:
                print('♕',end='  ')

            else:
                print('.',end='  ')
        print('')
    print('\n')
def checker(v, ii):
    k=0
    for n in v:
        if ii == n[1] or abs(len(v) - n[0]) == abs(ii - n[1]):
            break
        else:
            k += 1
            if k == len(v):
                return True
vec,sol,tt,bk,inter=[[0,0]],0,0,False,[[0,[[0,0]],0,1]]
def tester(v, i=0, s=1):
    global sol, dimension, tt, inter, bk
    tt+=1
    inter.append([tt,v,i,s])
    if tt%599==0:
        return
    elif v == []:
        bk=True
        return False
    else:
        if s==0:
            if v[-1][-1]==dimension-1:
                v.pop()
                return tester(v, s=0)
            else:
                v[-1][-1]+=1
                return tester(v)
        elif len(v)!=1 and checker(v[0:len(v) - 1], v[-1][-1])==None:
            if v[-1][-1]==dimension-1:
                v.pop()
                return tester(v, s=0)
            else:
                v[-1][-1]+=1
                return tester(v)
        elif checker(v, i)==True:
            if len(v)==dimension-1:
                v.append([len(v),i])
                sol+=1
                print('SOLUTION {0} in a {1}x{1} board:'.format(sol, dimension))
                printer(v)
                v.pop()
                return tester(v, i + 1,s=0)
            v.append([len(v),i])
            return tester(v)
        else:
            if i>=dimension-1:
                if v[-1][-1]==dimension-1:
                    v.pop()
                    return tester(v, s=0)
                else:
                    v[-1][-1]+=1
                    return tester(v)

            else:
                return tester(v, i + 1)
while True:
    final=inter[-1]
    tester(final[1], final[2], final[3])
    del inter[0:len(inter)-1]
    if bk==True:
        break
print('The {} queens problem has in total {} solutions.\n\n---\n'.format(dimension, sol))
print('N-Queen solution by Roylan Martinez.')