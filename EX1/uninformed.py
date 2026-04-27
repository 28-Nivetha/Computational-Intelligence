from collections import deque
import heapq  # For priority queue implementation

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []
            print("Node added")
        else:
            print("Node already exists")

    def add_edge(self, u, v, cost=0):
        if u in self.graph and v in self.graph:
            if (v, cost) in self.graph[u]:
                print("Edge already exists")
            else:
                self.graph[u].append((v, cost))
                self.graph[v].append((u, cost))
                print("Edge added")
        else:
            print("Add nodes first")

    def delete_node(self, node):
        if node in self.graph:
            self.graph.pop(node)
            for n in self.graph:
                self.graph[n] = [(x, c) for x, c in self.graph[n] if x != node]
            print("Node deleted")
        else:
            print("Node not found")

    def delete_edge(self, u, v):
        if u in self.graph:
            initial_count = len(self.graph[u])
            self.graph[u] = [(x, c) for x, c in self.graph[u] if x != v]
            self.graph[v] = [(x, c) for x, c in self.graph[v] if x != u]
            if len(self.graph[u]) < initial_count:
                print("Edge deleted")
            else:
                print("Edge not found")
        else:
            print("Edge not found")

    def display(self):
        print("\nGraph:")
        for node in self.graph:
            print(node, "-", self.graph[node])

    def display_adj_list(self, node):
        if node in self.graph:
            print(node, "-", self.graph[node])
        else:
            print("Node not found")

    def _print_step(self, iteration, fringe, explored):
        fringe_str = str([item[0] for item in fringe])
        explored_str = str(sorted(list(explored)))
        print(f"{iteration:<10} | {fringe_str:<30} | {explored_str}")

    def bfs_lr(self, start, goal_node=None):
        if start == goal_node:
            print(f"Start node is the goal! Path: {start}")
            return

        explored = set()
        fringe = deque([(start, [start])])
        iteration = 1

        print(f"\n{'Iter':<10} | {'Fringe (Queue)':<30} | {'Explored Set'}")
        print("-" * 60)

        while fringe:
            self._print_step(iteration, fringe, explored)
            node, path = fringe.popleft()

            if node not in explored:
                explored.add(node)
                if node == goal_node:
                    print(f"\nGoal node '{goal_node}' reached! Optimal Path: {' -> '.join(path)}")
                    return

                for neigh, _ in self.graph[node]:
                    if neigh not in explored and neigh not in [item[0] for item in fringe]:  # Check if not in fringe
                        fringe.append((neigh, path + [neigh]))
            iteration += 1
        print(f"\nGoal node '{goal_node}' not found.")

    def bfs_rl(self, start, goal_node=None):
        if start == goal_node:
            print(f"Start node is the goal! Path: {start}")
            return

        explored = set()
        fringe = deque([(start, [start])])
        iteration = 1

        print(f"\n{'Iter':<10} | {'Fringe (Queue)':<30} | {'Explored Set'}")
        print("-" * 60)

        while fringe:
            self._print_step(iteration, fringe, explored)
            node, path = fringe.popleft()

            if node not in explored:
                explored.add(node)
                if node == goal_node:
                    print(f"\nGoal node '{goal_node}' reached! Optimal Path: {' -> '.join(path)}")
                    return

                for neigh, _ in reversed(self.graph[node]):
                    if neigh not in explored and neigh not in [item[0] for item in fringe]:  # Check if not in fringe
                        fringe.append((neigh, path + [neigh]))
            iteration += 1
        print(f"\nGoal node '{goal_node}' not found.")

    def dfs_lr(self, start, goal_node=None):
        if start == goal_node:
            print(f"Start node is the goal! Path: {start}")
            return

        explored = set()
        fringe = [(start, [start])]
        iteration = 1

        print(f"\n{'Iter':<10} | {'Fringe (Stack)':<30} | {'Explored Set'}")
        print("-" * 60)

        while fringe:
            self._print_step(iteration, fringe, explored)
            node, path = fringe.pop()

            if node not in explored:
                explored.add(node)
                if node == goal_node:
                    print(f"\nGoal node '{goal_node}' reached! Optimal Path: {' -> '.join(path)}")
                    return

                for neigh, _ in reversed(self.graph[node]):
                    if neigh not in explored and neigh not in [item[0] for item in fringe]:  # Check if not in fringe
                        fringe.append((neigh, path + [neigh]))
            iteration += 1
        print(f"\nGoal node '{goal_node}' not found.")

    def dfs_rl(self, start, goal_node=None):
        if start == goal_node:
            print(f"Start node is the goal! Path: {start}")
            return

        explored = set()
        fringe = [(start, [start])]
        iteration = 1

        print(f"\n{'Iter':<10} | {'Fringe (Stack)':<30} | {'Explored Set'}")
        print("-" * 60)

        while fringe:
            self._print_step(iteration, fringe, explored)
            node, path = fringe.pop()

            if node not in explored:
                explored.add(node)
                if node == goal_node:
                    print(f"\nGoal node '{goal_node}' reached! Optimal Path: {' -> '.join(path)}")
                    return

                for neigh, _ in self.graph[node]:
                    if neigh not in explored and neigh not in [item[0] for item in fringe]:  # Check if not in fringe
                        fringe.append((neigh, path + [neigh]))
            iteration += 1
        print(f"\nGoal node '{goal_node}' not found.")

    def ucs(self, start, goal_node=None):
        if start == goal_node:
            print(f"Start node is the goal! Path: {start}")
            return

        explored = set()
        # Priority queue for the frontier, initialized with the start node
        frontier = [(0, start, [start])]  # (path_cost, node, path)
        iteration = 1

        print(f"\n{'Iter':<10} | {'Frontier (Priority Queue)':<40} | {'Explored Set'}")
        print("-" * 60)

        while frontier:
            self._print_step(iteration, frontier, explored)
            path_cost, node, path = heapq.heappop(frontier)

            if node not in explored:
                explored.add(node)
                if node == goal_node:
                    print(f"\nGoal node '{goal_node}' reached! Optimal Path: {' -> '.join(path)} with cost {path_cost}")
                    return

                for neigh, cost in self.graph[node]:
                    if neigh not in explored:
                        new_cost = path_cost + cost
                        heapq.heappush(frontier, (new_cost, neigh, path + [neigh]))
            iteration += 1
        print(f"\nGoal node '{goal_node}' not found.")

# Menu options defined before the loop
menu_options = [
    "1 Add Node",
    "2 Add Edge",
    "3 Delete Node",
    "4 Delete Edge",
    "5 Display Graph",
    "6 Display Adjacency List",
    "7 BFS Left to Right",
    "8 BFS Right to Left",
    "9 DFS Left to Right",
    "10 DFS Right to Left",
    "11 UCS",
    "12 Exit"
]

g = Graph()
print("\n Menu")
for option in menu_options:
   print(option)

while True:
#    print("\nM E N U")
 #   for option in menu_options:
  #      print(option)

    try:
        ch = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if ch == 1:
        g.add_node(input("Node: "))
    elif ch == 2:
        u = input("From: ")
        v = input("To: ")
        cost = int(input("Cost (0 if none): "))
        g.add_edge(u, v, cost)
    elif ch == 3:
        g.delete_node(input("Node: "))
    elif ch == 4:
        u = input("From: ")
        v = input("To: ")
        g.delete_edge(u, v)
    elif ch == 5:
        g.display()
    elif ch == 6:
        g.display_adj_list(input("Node: "))
    elif ch == 7:
        s = input("Start node: ")
        gl = input("Enter goal node: ")
        g.bfs_lr(s, gl if gl else None)
    elif ch == 8:
        s = input("Start node: ")
        gl = input("Enter goal node: ")
        g.bfs_rl(s, gl if gl else None)
    elif ch == 9:
        s = input("Start node: ")
        gl = input("Enter goal node: ")
        g.dfs_lr(s, gl if gl else None)
    elif ch == 10:
        s = input("Start node: ")
        gl = input("Enter goal node: ")
        g.dfs_rl(s, gl if gl else None)
    elif ch == 11:
        s = input("Start node: ")
        gl = input("Enter goal node: ")
        g.ucs(s, gl if gl else None)
    elif ch == 12:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
