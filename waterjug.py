from fractions import gcd
from states import findStates
from bfs import do_bfs
from dfs import do_dfs

a = int(input('Enter capacity of first jug :').strip())
b = int(input('Enter capacity of second jug : ').strip())
c = int(input('Amount to be measured : '))
if (c > a and c > b) or a != b or c%gcd(a,b) !=0:
    print('bad input')
    exit()
rules=['fill first jug','fill second jug','empty first jug','empty second jug','pour from jug 1 to 2','pour from jug 2 to 1']
states = [[0,0]] 
states_mat=[]

#finding all possible states
res=findStates(states,states_mat,a,b)
states=res[0]
states_mat=res[1]
            
#bfs
print('\n Using BFS')
solution=do_bfs(states,states_mat,[0,0],c)
for i in range(len(solution)):
    rule='Initial state'
    if i != 0:
        prev=solution[i-1]
        idx=states.index(prev)
        row=states_mat[idx]
        current=solution[i]
        rule=rules[row.index(current)]
    print('{} {} {}'.format(solution[i][0],solution[i][1],rule))

#dfs
print('\n Using DFS')
solution=do_dfs(states,states_mat,[0,0],c)
for i in range(len(solution)):
    rule='Initial state'
    if i != 0:
        prev=solution[i-1]
        idx=states.index(prev)
        row=states_mat[idx]
        current=solution[i]
        rule=rules[row.index(current)]
    print('{} {} {}'.format(solution[i][0],solution[i][1],rule))
