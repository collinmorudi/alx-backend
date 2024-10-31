Project Overview
This project focuses on implementing various caching systems using Python. The goal is to understand and implement different caching algorithms such as FIFO, LIFO, LRU, MRU, and LFU. The project is part of the #100DaysOfALXSE challenge and is designed to enhance skills in backend development, particularly in data handling and caching mechanisms.
Learning Objectives
Explain what a caching system is.
Define FIFO, LIFO, LRU, MRU, and LFU caching algorithms.
Understand the purpose and limitations of a caching system.
Requirements
All Python scripts must be executable and interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
The first line of each file should be #!/usr/bin/env python3.
All files must end with a new line.
The code must adhere to the pycodestyle style (version 2.5).
A README.md file is mandatory at the root of the project folder.
All modules, classes, and functions must have proper documentation.
Project Structure
base_caching.py: The parent class BaseCaching that defines the basic structure of the caching system.
0-basic_cache.py: The BasicCache class that inherits from BaseCaching and implements a basic caching system without limits.
1-fifo_cache.py: The FIFOCache class that implements the FIFO caching algorithm.
2-lifo_cache.py: The LIFOCache class that implements the LIFO caching algorithm.
0-main.py, 1-main.py, 2-main.py: Test scripts for each caching implementation.
Tasks
0. Basic Dictionary
Create a BasicCache class that inherits from BaseCaching and implements a basic caching system without any limits.
