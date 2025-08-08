import tkinter as tk
import time

# Algoritmo da visualizzare
code_lines = [
    "for i in range(len(arr)):",
    "    min_idx = i",
    "    for j in range(i+1, len(arr)):",
    "        if arr[j] < arr[min_idx]:",
    "            min_idx = j",
    "    arr[i], arr[min_idx] = arr[min_idx], arr[i]"
]

arr = [5, 3, 8, 6, 2]
steps = []  # Salva i passi per visualizzazione

# Prepara i passi dell'algoritmo
def selection_sort_steps(array):
    a = array[:]
    for i in range(len(a)):
        steps.append((0, a[:], i, -1))  # riga 0
        min_idx = i
        steps.append((1, a[:], i, min_idx))  # riga 1
        for j in range(i+1, len(a)):
            steps.append((2, a[:], i, j))  # riga 2
            if a[j] < a[min_idx]:
                min_idx = j
                steps.append((4, a[:], i, min_idx))  # riga 4
        a[i], a[min_idx] = a[min_idx], a[i]
        steps.append((5, a[:], i, min_idx))  # riga 5

selection_sort_steps(arr)

# GUI
root = tk.Tk()
root.title("Selection Sort Visualizer")

# Codice
code_box = tk.Text(root, height=10, width=50, font=("Courier", 12))
code_box.pack(side=tk.LEFT, padx=10, pady=10)

for line in code_lines:
    code_box.insert(tk.END, line + "\n")

code_box.tag_config("highlight", background="yellow")

# Canvas per array
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(side=tk.RIGHT, padx=10, pady=10)

bar_width = 40
bar_spacing = 10

def draw_array(array, i, j):
    canvas.delete("all")
    for idx, val in enumerate(array):
        x0 = idx * (bar_width + bar_spacing)
        y0 = 200 - val * 20
        x1 = x0 + bar_width
        y1 = 200
        color = "gray"
        if idx == i:
            color = "blue"
        elif idx == j:
            color = "red"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        canvas.create_text(x0 + bar_width // 2, y0 - 10, text=str(val))

# Avanzamento
step_index = 0

def next_step():
    global step_index
    if step_index < len(steps):
        line, array, i, j = steps[step_index]
        code_box.tag_remove("highlight", "1.0", tk.END)
        code_box.tag_add("highlight", f"{line + 1}.0", f"{line + 1}.end")
        draw_array(array, i, j)
        step_index += 1
        root.after(1000, next_step)

next_step()
root.mainloop()
