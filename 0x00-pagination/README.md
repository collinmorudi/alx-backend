# Dataset Pagination Project

## Overview
This project explores pagination techniques in Python, aiming to efficiently handle large datasets. You'll work on three key types of pagination:
1. Basic pagination using page and page_size parameters.
2. Hypermedia pagination with metadata.
3. Deletion-resilient pagination.

The project dataset is `Popular_Baby_Names.csv`, which you'll use to test and demonstrate pagination functionalities.

## Learning Objectives
By the end of this project, you should be able to:
- Implement dataset pagination using page and page_size parameters.
- Implement hypermedia-based pagination for better navigation and metadata control.
- Implement pagination that remains stable even when entries are deleted.

## Project Requirements
Ensure your work meets the following requirements:
- **Environment**: Python 3.7, Ubuntu 18.04 LTS
- **Code Standards**: Adhere to pycodestyle (version 2.5.*)
- **Documentation**: All modules and functions must be fully documented:
  - Include a docstring explaining the purpose of each module, class, and method.
  - Ensure the documentation is meaningful and accurately describes functionality.
- **Type Annotations**: All functions and coroutines must be type-annotated.
- **File Specifications**:
  - All files should end with a new line.
  - The first line of every Python file must be `#!/usr/bin/env python3`.
  - Code length will be tested using the `wc` command.

## Dataset Setup
Download `Popular_Baby_Names.csv` and ensure it’s in the root of the project directory. This file will serve as your primary data source for implementing pagination.

## Exercises
As part of the project, complete these exercises:

### Exercise 1: Simple Pagination
Implement pagination with `page` and `page_size` parameters. This method should allow retrieval of any specific page of data in the dataset.

### Exercise 2: Hypermedia Pagination
Add metadata (e.g., total pages, current page) to support hypermedia pagination, enabling more navigable and structured access to data pages.

### Exercise 3: Deletion-Resilient Pagination
Develop a pagination method that remains stable and unaffected by deletions, ensuring page integrity as data is removed from the dataset.

---

## Running the Project
1. Clone the repository.
2. Ensure `Popular_Baby_Names.csv` is in the root directory.
3. Run the pagination scripts using Python 3.7.

---
