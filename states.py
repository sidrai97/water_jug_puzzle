def findStates(states,states_mat,a,b):
    for i in states:
        x,y=i[0],i[1]
        temp=[]
        
        #rule1
        temp2=[]
        if x<a:
            temp2.append(a)
            temp2.append(y)
        temp.append(temp2)

        #rule2
        temp2=[]
        if y<b:
            temp2.append(x)
            temp2.append(b)
        temp.append(temp2)

        #rule3
        temp2=[]
        if x>0:
            temp2.append(0)   
            temp2.append(y)
        temp.append(temp2)

        #rule4
        temp2=[]
        if y>0:
            temp2.append(x)
            temp2.append(0)
        temp.append(temp2)

        #rule5
        temp2=[]
        if x>0 and max(0,x+y-b) != x and min(x+y,b) != y:
            temp2.append(max(0,x+y-b))
            temp2.append(min(x+y,b))
        temp.append(temp2)

        #rule6
        temp2=[]
        if y>0 and min(x+y,a) != x and max(0,x+y-a) != y:
            temp2.append(min(x+y,a))
            temp2.append(max(0,x+y-a))
        temp.append(temp2)

        states_mat.append(temp)
        for state in temp:
            if len(state)>0 and state not in states:
                states.append(state)

    return [states,states_mat]