from queue import PriorityQueue
import copy


class State:

    def __init__(self, nums, parent, moves, h, g, n):
        self.nums = copy.deepcopy(nums)
        self.parent = parent
        self.moves = moves
        self.h = h
        self.g = g
        self.n = n

    def calculate_manhattan(self):
        current = []
        goal = []

        for i in range(self.n):
            for j in range(self.n):
                goal.append(self.nums[i][j])

        current = copy.deepcopy(goal.copy())
        goal.sort()
        goal.append(0)
        goal.pop(0)

        for i in range(1, len(goal)):
            distance = abs(current.index(i) - goal.index(i))
            self.h += distance / n + distance % n

    def copy(self):
        state = State(self.nums, self.moves, self.h, self.g, self.n)
        return state

    def generate_next_states(self):
        next_states = []
        child_nums = []
        for i in range(n):
            for j in range(n):

                if self.nums[i][j] == 0:
                    child_nums = copy.deepcopy(self.nums)
                    if i == 0 and j == 0:
                        child_nums[i][j], child_nums[i][j + 1] = child_nums[i][j + 1], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to left"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i + 1][j] = child_nums[i + 1][j], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to up"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)
                        break

                    if i == 0 and j == n - 1:
                        child_nums[i][j], child_nums[i][j - 1] = child_nums[i][j - 1], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to right"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i + 1][j] = child_nums[i + 1][j], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to up"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)
                        break

                    if i == n - 1 and j == 0:
                        child_nums[i][j], child_nums[i][j + 1] = child_nums[i][j + 1], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to left"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i - 1][j] = child_nums[i - 1][j], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to down"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)
                        break

                    if i == n - 1 and j == n - 1:
                        child_nums[i][j], child_nums[i][j - 1] = child_nums[i][j - 1], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to right"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i - 1][j] = child_nums[i - 1][j], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to down"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)
                        break

                    if i == 0:
                        child_nums[i][j], child_nums[i][j - 1] = child_nums[i][j - 1], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to right"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i][j + 1] = child_nums[i][j + 1], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to left"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i + 1][j] = child_nums[i + 1][j], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to up"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)
                        break

                    if i == n - 1:
                        child_nums[i][j], child_nums[i][j - 1] = child_nums[i][j - 1], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to right"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i][j + 1] = child_nums[i][j + 1], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to left"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i - 1][j] = child_nums[i - 1][j], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to down"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)
                        break

                    if j == 0:
                        child_nums[i][j], child_nums[i][j + 1] = child_nums[i][j + 1], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to left"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i + 1][j] = child_nums[i + 1][j], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to up"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i - 1][j] = child_nums[i - 1][j], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to down"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)
                        break

                    if j == n - 1:
                        child_nums[i][j], child_nums[i][j - 1] = child_nums[i][j - 1], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to right"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i - 1][j] = child_nums[i - 1][j], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to down"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i + 1][j] = child_nums[i + 1][j], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to up"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)
                        break

                    else:
                        child_nums[i][j], child_nums[i][j - 1] = child_nums[i][j - 1], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to right"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i][j + 1] = child_nums[i][j + 1], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to left"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i - 1][j] = child_nums[i - 1][j], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to down"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)

                        child_nums[i][j], child_nums[i + 1][j] = child_nums[i + 1][j], child_nums[i][j]
                        moves = str(child_nums[i][j]) + " to up"
                        next_states.append(
                            State(child_nums, self, moves, 0, self.g + 1, self.n)
                        )
                        child_nums = copy.deepcopy(self.nums)
                        break

        return next_states

    def solution(self):
        solution = [self.moves]
        path = self
        while path.parent is not None:
            path = path.parent
            solution.append(path.moves)
        solution = solution[:-1]
        solution.reverse()
        return solution


n = int(input("Enter n:\n"))
input_nums = []
for i in range(n):
    single_row = list(map(int, input().split()))
    input_nums.append(single_row)


given_state = State(input_nums, None, None, 0, 0, n)
given_state.calculate_manhattan()
explored = [input_nums]
next_states = []
queue = PriorityQueue()
queue.put((given_state.h, 0, given_state))
counter = 0

while not queue.empty():

    current_state = queue.get()
    current_state = current_state[2]
    explored.append(current_state.nums)

    if current_state.h == 0:
        solution = current_state.solution()
        c = 0
        for child in solution:
            print(child)
            c += 1
        print(c, " steps")
        break

    next_states = current_state.generate_next_states()

    for next_state in next_states:
        if next_state.nums not in explored:
            counter += 1
            next_state.calculate_manhattan()
            queue.put((next_state.h, counter, next_state))

    #while not heuristics.empty():  ## empty the queue
    #    try:
    #        heuristics.get(False)
    #    except heuristics.empty():
    #        continue
    #    heuristics.task_done()

    #for child in next_states:
    #   child.calculate_manhattan()
    #    if child.nums not in explored:
    #        heuristics.put(child.h)

    #m = heuristics.get()
    #heuristics.put(m)
    #for child in next_states:
    #    if child.h == m and child.nums not in explored:
    #        current_state.h = child.h
    #        current_state.g = child.g
    #        current_state.nums = copy.deepcopy(child.nums.copy())
    #        current_state.moves = child.moves
    #        current_state.n = child.n
    #       valid_states.append(child)
    #        break

#for valid_state in valid_states:
#    print(valid_state.moves)
