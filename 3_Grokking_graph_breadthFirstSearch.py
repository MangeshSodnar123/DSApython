from collections import deque

def isMangoSeller(name):
    return name[-1] == 'm'

graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj','peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom','jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

def breadthFirstSearch(graph,root):
    queue = deque()
    queue += graph[root]
    visited = []
    while(queue):
        person = queue.popleft()
        if person not in visited:
            if isMangoSeller(person):
                return f'{person} is Mango Seller.'
            else:
                queue += graph[person]
                visited.append(person)
    return False

root = 'you'
print(breadthFirstSearch(graph,root))
