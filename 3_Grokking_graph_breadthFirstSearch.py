from collections import deque

#make a graph using dictionary
graph = {}
graph['mangesh'] = ['raj','ramr','don']
graph['don'] = ['king','ramr','pranjal']
graph['raj'] = ['lucky']
graph['ramr'] = ['lucky']
graph['king'] = ['pranjal']
graph['pranjal'] = ['ramr']
graph['lucky'] = ['rubym']
graph['rubym'] = ['pranjal']

#define a function to find a mango seller
def isMangoSeller(name):
    return name[-1] == 'm'
    
#define search function
def search(graph,root):
    #make a queue and add root in the queue
    queue = deque()
    queue.append(root)
    #make a list for visited
    visited = []
    #run a loop till queue is not empty
    while(queue):
        #person = dequeu element
        person = queue.popleft()
        #check if person is visited or not
        if person not in visited:
            #if not then check if he/she is mango seller
            if isMangoSeller(person):
                return f'{person} is a mango seller.'
            #else add person to the visited list
            else:
                visited.append(person)
                #and add his neighbours to the queue
                queue.extend(graph[person])
    return False
    
print(search(graph,'mangesh'))
