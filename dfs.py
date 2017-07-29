def tracepath(path,start):
    solution=[start]
    while start != [0,0]:
        temp=path[str(start)]
        start=temp
        solution.append(temp)
    return list(reversed(solution))

def do_dfs(states,states_mat,root,goal):
    visited=[]
    stack=[root]
    path={}
    while len(stack) > 0:
        temp=stack.pop()
        if temp[0] == goal or temp[1]==goal:
            return tracepath(path,temp)
        if temp not in visited:
            visited.append(temp)
            idx=states.index(temp)
            row=states_mat[idx]
            row=list(reversed(row))
            for s in row:
                if len(s)>0 and s not in visited:
                    stack.append(s)
                    path[str(s)]=temp
    return 0