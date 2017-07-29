def tracepath(path,start):
    solution=[start]
    while start != [0,0]:
        temp=path[str(start)]
        start=temp
        solution.append(temp)
    return list(reversed(solution))

def do_bfs(states,states_mat,root,goal):
    visited=[root]
    queue=[root]
    path={}
    while len(queue) > 0:
        temp=queue[0]
        del(queue[0])
        if temp[0] == goal or temp[1]==goal:
            return tracepath(path,temp)
        idx=states.index(temp)
        row=states_mat[idx]
        for s in row:
            if len(s)>0 and s not in visited:
                queue.append(s)
                visited.append(s)
                path[str(s)]=temp