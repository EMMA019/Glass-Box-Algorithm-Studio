🧊 Glass-Box Algorithm Studio v2.0

"See logic in motion."

A next-generation algorithm visualization platform that places black-box algorithms into a "Glass-Box," making their thought processes and behaviors transparent.

📖 Overview

Glass-Box Algorithm Studio is a browser-based, interactive environment for learning and experimenting with algorithms.

Unlike traditional visualization tools, it combines a cyberpunk UI with an immersive 3D space (VR compatible) to allow you to intuitively "experience" algorithmic behaviors. It leverages the Vue.js 3 reactivity system to deliver real-time, smooth simulations.

✨ Features

1. Dual View Mode

2D Dashboard: A tactical view for grasping the big picture. Displays heatmaps and detailed graphs.

3D VR Immersive: An immersive view using A-Frame. Step inside the algorithm's world to spatially observe the movements of agents and data.

2. Algorithm Modules

🤖 Q-Learning (Reinforcement Learning)

Visualizes the learning process of a maze-exploring agent.

Features: Q-value heatmaps, visualization of the exploration vs. exploitation balance (ε-greedy).

Perspective: Observe the "trial and error" process as the agent learns to avoid walls, dodge pits, and find the goal.

🕸️ Graph Search (Dijkstra)

Visualizes the shortest path search between nodes.

Features: Color-coded display of visited nodes, frontiers (search candidates), and the determined path.

Perspective: Watch how the search wave expands and converges on the optimal solution.

🏎️ Sorting Race

Displays the speed and behavioral differences between algorithms in a race format.

Matchup: Quick Sort vs. Bubble Sort.

Features: Real-time tracking of comparisons and swaps. Active operation zones are highlighted.

🎯 Monte Carlo Simulation

Visualizes the process of estimating Pi (π) using random numbers.

Features: Real-time convergence graph. Dynamically renders the estimate approaching "3.14159..." as the number of trials increases.

3. Advanced Controls

Speed Control: Adjustable simulation speed via slider (from 1x to 20x).

Safety Guardrails: Robust state management that preserves Vue 3 reactivity.

🛠️ Tech Stack

Designed for portability, this project operates as a build-free, single-file configuration (CDN-based).

Core Framework: Vue.js 3 (Composition API)

Styling: Tailwind CSS

3D Engine: A-Frame

Font: JetBrains Mono (Google Fonts)

Design System: Glassmorphism + Cyberpunk Neon UI

🚀 Getting Started

Requirements

Modern Browser (Chrome, Firefox, Edge, Safari)

Internet Connection (Required to load libraries via CDN)

How to Run

No special installation steps (like npm install) are required.

Clone this repository.

git clone [https://github.com/EMMA019/Glass-Box-Algorithm-Studio.git](https://github.com/EMMA019/Glass-Box-Algorithm-Studio.git)


Open GlassBox_Algorithm_Studio_v2.html in your browser.

# Just open the file
# Mac
open GlassBox_Algorithm_Studio_v2.html

# Windows
start GlassBox_Algorithm_Studio_v2.html


🎮 Controls

Action

Description

INITIATE

Starts the simulation.

HALT

Pauses the simulation.

SYSTEM RESET

Initializes the state and generates new data (mazes, arrays, etc.).

SPEED SLIDER

Adjusts execution speed. Left for slow (observation), Right for fast (convergence).

2D/VR Toggle

Switches between 2D Dashboard and 3D VR views using the toggle at the top.

WASD / Mouse

Used for camera movement and perspective control in 3D mode.

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

