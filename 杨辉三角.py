def triangles(n):
    line = [1]
    i = 0
    while i < n:
        i = i + 1 
        yield line
        line = [1] + [line[x] + line[x + 1] for x in range(len(line) - 1)] + [1]

a = triangles(5)
print(next(a))
print(next(a))
print(next(a))

'''
  1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
'''