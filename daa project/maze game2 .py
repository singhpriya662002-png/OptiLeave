import pygame
import random
import sys
import os
import tkinter as tk
from tkinter import ttk
from heapq import heappush, heappop

# --- CONFIGURATION ---
CELL_SIZE = 25
MAZE_SIZE = 21 
WIDTH = MAZE_SIZE * CELL_SIZE
HEIGHT = MAZE_SIZE * CELL_SIZE

COLORS = {
    'bg': (20, 20, 25),
    'wall': (44, 62, 80),
    'path': (236, 240, 241),
    'current': (46, 204, 113),
    'player': (52, 152, 219),
    'exit': (231, 76, 60),
    'hint': (241, 196, 15),
    'scan': (155, 89, 182) # Purple for scanning
}

class DAAVizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DAA Algorithm Visualizer - Kruskal & Dijkstra")
        self.root.geometry(f"{WIDTH + 300}x{HEIGHT + 40}")
        self.root.configure(bg="#2c3e50")
        
        self.maze = [[1 for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]
        self.player_pos = [0, 0]
        self.goal = (MAZE_SIZE - 1, MAZE_SIZE - 1)
        self.hint_path = []
        self.current_algo_info = "Press a button to start"
        self.running = True

        self.setup_ui()
        self.setup_pygame()

    def setup_ui(self):
        """Professional Sidebar with Complexity Info"""
        self.sidebar = tk.Frame(self.root, width=280, bg="#34495e", height=HEIGHT)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        tk.Label(self.sidebar, text="DAA ANALYTICS", font=("Helvetica", 16, "bold"), 
                 bg="#34495e", fg="#1abc9c", pady=10).pack()

        # Action Buttons
        ttk.Button(self.sidebar, text="Run Kruskal (Gen)", command=self.visual_kruskal).pack(fill=tk.X, pady=5)
        ttk.Button(self.sidebar, text="Run Dijkstra (Solve)", command=self.visual_dijkstra).pack(fill=tk.X, pady=5)
        ttk.Button(self.sidebar, text="Reset", command=self.reset_system).pack(fill=tk.X, pady=5)

        # Complexity Display Box
        self.info_box = tk.Label(self.sidebar, text=self.current_algo_info, justify=tk.LEFT, 
                                 bg="#2c3e50", fg="#ecf0f1", font=("Consolas", 10), 
                                 padx=10, pady=10, wraplength=250, relief=tk.SUNKEN)
        self.info_box.pack(fill=tk.BOTH, expand=True, pady=10)

        # Legend
        legend = "● Player | ■ Target\n■ Scan | ■ Path"
        tk.Label(self.sidebar, text=legend, bg="#34495e", fg="#bdc3c7", font=("Helvetica", 9)).pack(pady=10)

        self.game_frame = tk.Frame(self.root, width=WIDTH, height=HEIGHT)
        self.game_frame.pack(side=tk.RIGHT, padx=10, pady=10)

    def setup_pygame(self):
        os.environ['SDL_WINDOWID'] = str(self.game_frame.winfo_id())
        if sys.platform == "win32": os.environ['SDL_VIDEODRIVER'] = 'windib'
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def update_info(self, text):
        self.info_box.config(text=text)
        self.root.update()

    def visual_kruskal(self):
        """Role: Randomly connects points to create a tree-based maze without cycles."""
        self.reset_system()
        info = (
            "ALGO: KRUSKAL'S\n"
            "ROLE: Minimum Spanning Tree\n"
            "---------------------------\n"
            "TIME: O(E log E) or O(E log V)\n"
            "SPACE: O(V + E)\n"
            "---------------------------\n"
            "STATUS: Removing edges randomly to create a maze with NO cycles."
        )
        self.update_info(info)
        
        parent = {(x, y): (x, y) for y in range(0, MAZE_SIZE, 2) for x in range(0, MAZE_SIZE, 2)}
        def find(i):
            if parent[i] == i: return i
            parent[i] = find(parent[i])
            return parent[i]

        edges = []
        for y in range(0, MAZE_SIZE, 2):
            for x in range(0, MAZE_SIZE, 2):
                self.maze[y][x] = 0
                if x + 2 < MAZE_SIZE: edges.append(((x, y), (x + 2, y)))
                if y + 2 < MAZE_SIZE: edges.append(((x, y), (x, y + 2)))
        
        random.shuffle(edges)
        for (u, v) in edges:
            root_u, root_v = find(u), find(v)
            if root_u != root_v:
                parent[root_u] = root_v
                self.maze[(u[1]+v[1])//2][(u[0]+v[0])//2] = 0
                self.draw_maze(current_node=v)
                pygame.time.delay(15)
                self.root.update()
        self.update_info(info + "\n\nDONE: Maze Generated!")

    def visual_dijkstra(self):
        """Role: Finds the guaranteed shortest path in a weighted/unweighted graph."""
        info = (
            "ALGO: DIJKSTRA'S\n"
            "ROLE: Shortest Path Finder\n"
            "---------------------------\n"
            "TIME: O((V + E) log V)\n"
            "SPACE: O(V)\n"
            "---------------------------\n"
            "STATUS: Exploring nodes layer by layer using Priority Queue."
        )
        self.update_info(info)
        
        self.hint_path = []
        start = tuple(self.player_pos)
        pq = [(0, start, [])]
        visited = set()
        
        while pq:
            cost, curr, path = heappop(pq)
            if curr == self.goal:
                self.hint_path = path + [curr]
                self.update_info(info + f"\n\nPATH FOUND!\nCost: {len(self.hint_path)}")
                return
            
            if curr in visited: continue
            visited.add(curr)
            
            pygame.draw.rect(self.screen, COLORS['scan'], (curr[0]*CELL_SIZE+6, curr[1]*CELL_SIZE+6, CELL_SIZE-12, CELL_SIZE-12))
            pygame.display.flip()
            pygame.time.delay(50) 
            self.root.update()

            for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
                nx, ny = curr[0]+dx, curr[1]+dy
                if 0 <= nx < MAZE_SIZE and 0 <= ny < MAZE_SIZE and self.maze[ny][nx] == 0:
                    heappush(pq, (cost + 1, (nx, ny), path + [curr]))

    def draw_maze(self, current_node=None):
        self.screen.fill(COLORS['bg'])
        for y in range(MAZE_SIZE):
            for x in range(MAZE_SIZE):
                color = COLORS['wall'] if self.maze[y][x] == 1 else COLORS['path']
                if current_node == (x, y): color = COLORS['current']
                pygame.draw.rect(self.screen, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))
        for (hx, hy) in self.hint_path:
            pygame.draw.rect(self.screen, COLORS['hint'], (hx*CELL_SIZE+8, hy*CELL_SIZE+8, CELL_SIZE-16, CELL_SIZE-16))
        pygame.draw.rect(self.screen, COLORS['exit'], (self.goal[0]*CELL_SIZE+5, self.goal[1]*CELL_SIZE+5, CELL_SIZE-10, CELL_SIZE-10))
        pygame.draw.circle(self.screen, COLORS['player'], (self.player_pos[0]*CELL_SIZE+12, self.player_pos[1]*CELL_SIZE+12), 10)
        pygame.display.flip()

    def reset_system(self):
        self.maze = [[1 for _ in range(MAZE_SIZE)] for _ in range(MAZE_SIZE)]
        self.player_pos = [0, 0]
        self.hint_path = []
        self.update_info("Maze Reset. Press 'Run Kruskal' to generate.")
        self.draw_maze()

    def main_loop(self):
        if self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.running = False
                if event.type == pygame.KEYDOWN:
                    dx, dy = 0, 0
                    if event.key == pygame.K_UP: dy = -1
                    elif event.key == pygame.K_DOWN: dy = 1
                    elif event.key == pygame.K_LEFT: dx = -1
                    elif event.key == pygame.K_RIGHT: dx = 1
                    nx, ny = self.player_pos[0]+dx, self.player_pos[1]+dy
                    if 0 <= nx < MAZE_SIZE and 0 <= ny < MAZE_SIZE and self.maze[ny][nx] == 0:
                        self.player_pos = [nx, ny]
                        self.hint_path = []
            self.draw_maze()
            self.root.after(10, self.main_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = DAAVizApp(root)
    app.main_loop()
    root.mainloop()
    pygame.quit() 