'''
Created on Nov 30, 2020

@author: Salzaidy
'''

def queue_time(customers, n):

    tills = [0]*n
    print(tills)
    
    for i in customers:
        tills[0] += i
        tills.sort()
    return max(tills)

queue_time([], 1)
queue_time([5,4,6], 2)
queue_time([2], 5)
queue_time([1,2,3,4,5], 1)
queue_time([1,2,3,4,5], 100)
