# Internationalization in Flask (i18n)

This project focuses on implementing internationalization (i18n) in a Flask web application. It demonstrates how to make a web app accessible to users from various language backgrounds by supporting localization of text and timestamps.

## Learning Objectives

The main goals of this project are:
1. **Template Parameterization**: Use Flask templates to display content in multiple languages.
2. **Locale Inference**: Determine the user's preferred language based on URL parameters, user settings, or request headers.
3. **Timestamp Localization**: Format timestamps to match the user's locale.

## Requirements

- Python version: **3.7**
- Operating System: **Ubuntu 18.04 LTS**
- Style Guidelines: **pycodestyle** version 2.5
- All code files should:
  - End with a new line.
  - Start with `#!/usr/bin/env python3`.
  - Be executable.
- Documentation:
  - All modules, classes, and functions must have detailed documentation.
  - Functions and methods must be type-annotated.

## Project Structure

- `0-app.py`: The main Flask application file, containing a simple route.
- `templates/0-index.html`: HTML template displaying a basic page.

## Tasks

### Task 0: Basic Flask App

- **Goal**: Set up a basic Flask app.
- **Details**: Create a single route `/` and an HTML template that displays:
  - **Title**: "Welcome to Holberton"
  - **Header**: "Hello world"

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/alx-backend.git
   cd alx-backend/0x02-i18n
Run the Flask app:

bash
Copy code
python3 0-app.py
Access the app at http://127.0.0.1:5000/.
