import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as mcolors

class GameOfLife:
    def __init__(self, size=(50, 50), random_init=True):
        self.size = size
        if random_init:
            # Increase the probability of live cells for better visibility
            self.grid = np.random.choice([0, 1], size=size, p=[0.7, 0.3])
        else:
            self.grid = np.zeros(size)
            
    def get_neighbors(self):
        """Count the number of live neighbors for each cell."""
        neighbors = np.zeros_like(self.grid)
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                neighbors += np.roll(np.roll(self.grid, i, axis=0), j, axis=1)
        return neighbors
    
    def step(self):
        """Evolve the grid one step according to Conway's Game of Life rules."""
        neighbors = self.get_neighbors()
        # Create a new grid based on the rules
        new_grid = np.zeros_like(self.grid)
        
        # Rule 1: Any live cell with 2 or 3 live neighbors survives
        survival = (self.grid == 1) & ((neighbors == 2) | (neighbors == 3))
        
        # Rule 2: Any dead cell with exactly 3 live neighbors becomes alive
        birth = (self.grid == 0) & (neighbors == 3)
        
        # Combine rules
        new_grid[survival | birth] = 1
        
        # Update grid
        self.grid = new_grid
        return self.grid

    def set_pattern(self, pattern, position):
        """Set a specific pattern at the given position."""
        x, y = position
        h, w = pattern.shape
        self.grid[x:x+h, y:y+w] = pattern

class GameOfLifeVisualizer:
    def __init__(self, game):
        plt.ion()  # Turn on interactive mode
        self.game = game
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.img = self.ax.imshow(game.grid, interpolation='nearest', 
                                 cmap='viridis', vmin=0, vmax=1)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_title("Conway's Game of Life")
        self.frame_count = 0
    
    def update(self, frame):
        """Update function for animation."""
        self.game.step()
        self.img.set_array(self.game.grid)
        self.frame_count += 1
        if self.frame_count % 10 == 0:  # Print every 10 frames
            print(f"Frame {self.frame_count}, Active cells: {np.sum(self.game.grid)}")
        return [self.img]
    
    def animate(self, frames=200, interval=100):
        """Animate the Game of Life evolution."""
        print("Starting animation...")
        print(f"Initial active cells: {np.sum(self.game.grid)}")
        
        self.anim = FuncAnimation(
            self.fig, self.update, frames=frames,
            interval=interval, blit=True
        )
        plt.show(block=True)  # Make sure to block until window is closed

def create_glider():
    """Create a glider pattern."""
    return np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ])

def create_blinker():
    """Create a blinker pattern."""
    return np.array([[1, 1, 1]])

def create_block():
    """Create a block pattern."""
    return np.array([
        [1, 1],
        [1, 1]
    ])

def main():
    # Initialize the game with a 50x50 grid
    print("Initializing Game of Life...")
    game = GameOfLife(size=(50, 50), random_init=False)
    
    # Add some interesting patterns
    glider = create_glider()
    blinker = create_blinker()
    block = create_block()
    
    # Place patterns at different locations
    game.set_pattern(glider, (5, 5))
    game.set_pattern(blinker, (20, 20))
    game.set_pattern(block, (30, 30))
    
    print("Setting up visualization...")
    vis = GameOfLifeVisualizer(game)
    print("Starting animation - close the window to exit")
    vis.animate(frames=500, interval=10)  # Reduced interval for smoother animation

if __name__ == "__main__":
    main() 