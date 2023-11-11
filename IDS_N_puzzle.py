import queue
from time import time
from Astar_N_puzzle import State

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
n = int(input("Enter n:\n"))
input_nums = []
for i in range(n):
    single_row = list(map(int, input().split()))
    input_nums.append(single_row)


def dfs(l, root):
    fringe = queue.LifoQueue()
    fringe.put(root)
    current_state = fringe.get()

    while current_state.nums != goal:
        if current_state.g < l:
            for next_state in current_state.generate_next_states():
                fringe.put(next_state)

        if fringe.qsize() > 0:
            current_state = fringe.get()
        else:
            return None

    return current_state


if State.solvable(input_nums, n):
    t = time()
    given_state = State(input_nums, None, None, 0, 0, n)
    last_state = None
    l = 1
    while last_state is None:
        last_state = dfs(l, given_state)
        l += 1

    print(time() - t)

    solution = last_state.solution()
    c = 0
    for child in solution:
        print(child)
        c += 1
    print(c, " steps")
else:
    print("This puzzle isn't solvable")
