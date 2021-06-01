# Simple 'recgame info' using Flask
[![Python](https://img.shields.io/badge/Python-3.9.5-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0.1-red.svg)](https://pypi.org/project/mgz/)
[![Pillow](https://img.shields.io/badge/Pillow-8.0.0-yellow.svg)](https://pypi.org/project/Pillow/)
[![Mgz](https://img.shields.io/badge/Mgz-1.5.0-green.svg)](https://pypi.org/project/mgz/)

[![Screenshot](./screenshots/screenshot_001.png)]()
## Description
Website to analyze AoE2 recgames.

## Usage
- Install Python3 [python.org](https://www.python.org/)
- Install Flask `pip install flask`
- Install mgz `pip install mgz`
- Install Pillow `pip install pillow`

- Clone this repo, open the folder, run a console.
- Run flask `flask run` **or** `python app.py`
- upload AoE2 recgames:
  - .mgl
  - .mgx
  - .mgz
- You will get a **minimap**, and the info in **JSON** format.

## Using the API
You could get all the info scanned going to this url [localhost:5500/get_data](localhost:5500/get_data).

## Screenshots

**Go to 'search file'**

[![Screenshot](./screenshots/step1.png)]()

---
**Upload a file and press 'SUBIR'**

[![Screenshot](./screenshots/step2.png)]()

---
**HERE YOU HAVE!**

[![Screenshot](./screenshots/step3.png)]()

## Special thanks.
- GoFullPage (Chrome extension)
- Screely - [screely.com](https://www.screely.com/)