from time import time
import queue

from Astar_N_puzzle import State




goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

n = int(input("Enter n:\n"))
input_nums = []
for i in range(n):
    single_row = list(map(int, input().split()))
    input_nums.append(single_row)

if State.solvable(input_nums, n):
    t = time()
    given_state = State(input_nums, None, None, 0, 0, n)
    fringe = queue.Queue()
    fringe.put(given_state)
    current_state = fringe.get()

    while current_state.nums != goal:
        for child in current_state.generate_next_states():
            fringe.put(child)
        current_state = fringe.get()
    print(time() - t)
    solution = current_state.solution()
    c = 0
    for child in solution:
        print(child)
        c += 1
    print(c, " steps")
else:
    print("This puzzle isn't solvable")
