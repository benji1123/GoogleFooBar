'''
Level 2
The two solutions below
give equivalent output with equivalent
complexity, but only Solution 2 passes
'''

'''
Solution 1
'''
import queue
def solution(src, dest):
	# map to [X, Y] (matrix coord sys)
	start = (src - src//8*8, src//8)
	target = (dest - dest//8*8, dest//8)
	# BFS: compute min steps to make deltas = 0
	visited = {start:0} # val = num-moves
	q = queue.Queue()
	q.put(start)
	# possible moves (pairs of x,y deltas)
	dx = [-2, -2, -1, -1, 1, 1, 2, 2]
	dy = [-1, 1, -2, 2, -2, 2, -1, 1]
	while q:
		t = q.get()
		if t == target:
			return visited[t]
		for i in range(8):
			result_sq = (t[0]+dx[i], t[1]+dy[i])
			# ensure board-bounds are not exceeded
			if (result_sq not in visited and
				result_sq[0] <= 7 and result_sq[1] <= 7):
					q.put(result_sq)
					visited[result_sq] = visited[t]+1
	return 0


'''
Solution 2
'''
from collections import deque
def solution2(src, dest):
	# map to [X, Y] (matrix indexing sys)
	start = (src - src//8*8, src//8)
	target = (dest - dest//8*8, dest//8)
	q = deque([])
	q.append(start)
	
	# BFS
	visited = {start:0} # val = num-moves
	dx = [-2, -2, -1, -1, 1, 1, 2, 2] # possible moves (x,y pairs)
	dy = [-1, 1, -2, 2, -2, 2, -1, 1]
	while q:
		t = q.popleft()
		if t == target:
			return visited[t] # HT stores num moves
		# 8 potential moves @ each square
		for i in range(8):
			result_sq = (t[0]+dx[i], t[1]+dy[i])
			# ensure board-bounds are not exceeded
			if (result_sq not in visited and
				result_sq[0] <= 7 and result_sq[1] <= 7):
					q.append(result_sq)
					visited[result_sq] = visited[t]+1 # num-moves increments
	return 0

'''
Demo
'''
src = 10
dest = 39
print(solution(src, dest))
print(solution2(src, dest))
