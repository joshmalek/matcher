import numpy as np
import time


class User:
    def __init__(self,name):
        self.interests = np.random.randint(0,11,10).tolist()
        self.matches = []
        self.name = "u"+str(name+1)

def compare(u1, u2):
    sum_diff = 0
    #print("comparing u"+ str(i+1) + " and u"+ str(j+1))
    for x in range(0,len(u1.interests)):
        sum_diff += abs(u1.interests[x]-u2.interests[x])

    likeness = 100-sum_diff
    print(u1.interests)
    print("and")
    print(u2.interests)
    print("are " + str(likeness) + "% alike")
    print()
    return likeness

start_time = time.time()
users = [User(i) for i in range(0,500)]
print(len(users))
for i in range(0,len(users)):
    for j in range(i,len(users)):
        if(i != j):
            likeness = compare(users[i],users[j])
            if(likeness > 70):
                users[i].matches.append((likeness,users[j].interests))
                users[j].matches.append((likeness,users[i].interests))
            #print(users[i].interests)
            #print("and")
            #print(users[j].interests)
            #print("are " + str(likeness) + "% alike")
            #print()
for i in range(0, len(users)):
    print(users[i].name +  " matches:",users[i].interests)
    sortd = sorted(users[i].matches)[::-1]
    for x in range(0,len(sortd)):
        print(sortd[x][0],sortd[x][1])
    print()
print("--- %s seconds ---" % (time.time() - start_time))
