# Text to HTML converter

This app is used to convert formatted text to raw HTML

All you need is to paste your formatted text to text editor and click the button. Raw HTML will appear in HTML editor field.

## Installation

1. Copy a repository on your computer.
2. Create a virtual environment with `python -m venv venv`.
3. Activate it using `./venv/Scripts/activate`.
4. Install requirements with `pip install -r requirements.txt`.
5. Change your directory to `text_to_html` using `cd text_to_html`.
6. Apply all migrations using `python manage.py makemugrations` & `python manage.py migrate`
7. Launch application with `python manage.py runserver` and follow the link `http://127.0.0.1:8000`.