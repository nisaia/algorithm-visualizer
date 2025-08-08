import tkinter as tk

# Codice DFS da mostrare
code_lines = [
    "def dfs(node):",
    "    if node in visited:",
    "        return",
    "    visited.add(node)",
    "    for neighbor in graph[node]:",
    "        dfs(neighbor)"
]

# Grafo semplice
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Posizioni dei nodi per disegno
positions = {
    'A': (150, 50),
    'B': (80, 120),
    'C': (220, 120),
    'D': (50, 190),
    'E': (110, 190),
    'F': (220, 190)
}

# Passi da visualizzare
steps = []
visited = set()

def dfs_steps(node):
    if node in visited:
        steps.append((1, node))  # riga 1
        steps.append((2, node))  # riga 2
        return
    steps.append((3, node))  # riga 3
    visited.add(node)
    steps.append((4, node))  # riga 4
    for neighbor in graph[node]:
        steps.append((5, node, neighbor))  # riga 5
        dfs_steps(neighbor)

dfs_steps('A')

# GUI
root = tk.Tk()
root.title("DFS Visualizer")

# Codice
code_box = tk.Text(root, height=10, width=40, font=("Courier", 12))
code_box.pack(side=tk.LEFT, padx=10, pady=10)

for line in code_lines:
    code_box.insert(tk.END, line + "\n")

code_box.tag_config("highlight", background="yellow")

# Canvas per grafo
canvas = tk.Canvas(root, width=300, height=250, bg="white")
canvas.pack(side=tk.RIGHT, padx=10, pady=10)

visited_nodes = set()

def draw_graph(current=None, next_node=None):
    canvas.delete("all")
    # Archi
    for node, neighbors in graph.items():
        x1, y1 = positions[node]
        for neighbor in neighbors:
            x2, y2 = positions[neighbor]
            canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
    # Nodi
    for node, (x, y) in positions.items():
        color = "gray"
        if node in visited_nodes:
            color = "blue"
        if node == current:
            color = "orange"
        if node == next_node:
            color = "red"
        canvas.create_oval(x-20, y-20, x+20, y+20, fill=color)
        canvas.create_text(x, y, text=node, font=("Arial", 12, "bold"))

# Avanzamento
step_index = 0

def next_step():
    global step_index
    if step_index < len(steps):
        step = steps[step_index]
        code_box.tag_remove("highlight", "1.0", tk.END)
        line = step[0]
        code_box.tag_add("highlight", f"{line + 1}.0", f"{line + 1}.end")

        if line == 1 or line == 2:
            draw_graph(current=step[1])
        elif line == 3 or line == 4:
            visited_nodes.add(step[1])
            draw_graph(current=step[1])
        elif line == 5:
            draw_graph(current=step[1], next_node=step[2])

        step_index += 1
        root.after(1000, next_step)

next_step()
root.mainloop()
