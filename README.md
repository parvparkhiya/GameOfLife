# RL based Game of Life generator

*In pixels black and white they dance,*  
*Cells alive in cosmic chance.*  
*Birth and death in rules divine,*  
*Conway's game, a grand design.*  
*Through generations they evolve,*  
*Life's mysteries we try to solve.*

## About
This project implements Conway's Game of Life, a cellular automaton that demonstrates how complex patterns can emerge from simple rules. The implementation includes a visual simulator and supports various initial patterns like gliders, blinkers, and blocks.

## Features
- Clean visualization using matplotlib
- Multiple pre-defined patterns (glider, blinker, block)
- Support for random initialization
- Configurable grid size and simulation speed
- Frame-by-frame evolution tracking

## Installation

1. Create and activate a conda environment:
```bash
conda create -n gol python=3.9
conda activate gol
```

2. Install required packages using requirements.txt:
```bash
pip install -r requirements.txt
```

## Usage

Run the simulation:
```bash
python src/run_gol.py
```

### Available Patterns
- **Glider**: A pattern that moves diagonally across the grid
- **Blinker**: An oscillating pattern that alternates between horizontal and vertical states
- **Block**: A stable 2x2 pattern that remains unchanged

## Controls
- Close the visualization window to end the simulation
- The simulation runs for 500 frames by default
- Each frame represents one generation of cell evolution

## Rules of the Game
1. Any live cell with 2 or 3 live neighbors survives
2. Any dead cell with exactly 3 live neighbors becomes alive
3. All other cells die or stay dead

## Project Structure
```
.
├── README.md
├── requirements.txt
└── src/
    └── run_gol.py
```

## License
This project is open source and available under the MIT License.

## Acknowledgments
Inspired by John Conway's Game of Life (1970)
Created with help from Cursor AI
