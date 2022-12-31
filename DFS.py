graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : ['4'],
  '4' : ['8'],
  '8' : []
}
# //again this is a random graph in the form of python dictionaries 
# //Depth first search begins 
visited=set()#taking visisted as a set object 
def dfs(visited,graph,node):
    if node not in visited:
        print(node,end='')#if it is not visited then traverse i.e. print it 
        visited.add(node)
        for neighbour in graph[node] :
            dfs(visited,graph,neighbour)
print('DFS traversal')
dfs(visited,graph,'5')#calling the function 