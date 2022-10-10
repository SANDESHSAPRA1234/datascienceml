import collections
class graph:
   def __init__(self,dict=None):
      if dict is None:
         dict = {}
      self.dict = dict
def bfs(graph, startnode):

   seen, queue = set([startnode]), collections.deque([startnode])
   while queue:
      vertex = queue.popleft()
      marked(vertex)
      for node in graph[vertex]:
         if node not in seen:
            seen.add(node)
            queue.append(node)

def marked(n):
   print(n)


dict = { 
   "a" : set(["b","e","f"]),
   "b" : set(["a", "e","c"]),
   "c" : set(["b", "d"]),
   "d" : set(["c","e"]),
   "e" : set(["a","b","d"]),
   "f" : set([])
}
bfs(dict, "a")
