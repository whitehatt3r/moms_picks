# 🎰 Lottery Number Picker

A simple Python + Tkinter app that generates **Mega Millions–style** lottery numbers using historical draw data.  
The program reads a CSV of past winning numbers, builds a frequency table, and then selects 5 numbers (1–70) weighted by frequency, plus a bonus ball (1–25).

⚠️ **Disclaimer:** This is for fun only. It does not improve your odds of winning.

---

## ✨ Features
- Reads past winning numbers from CSV
- Uses **pandas** + **numpy** to weight number selection
- Flashing **Tkinter GUI** with a "Generate Numbers" button
- Outputs a new set of lottery numbers + bonus ball

---

## 📂 Project Structure
moms_picks/
├─ src/
│ └─ winner_winner.py
├─ data/
│ └─ Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv
├─ requirements.txt
└─ README.md

---

## ⚙️ Requirements
- Python 3.10 or higher
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)  
Tkinter comes bundled with most Python installs. On Linux you may need to install it manually:
```bash

sudo apt install python3-tk
pip install -r requirements.txt
pandas
numpy

#Run the app
# Activate virtual environment first
# Windows PowerShell
.\.venv\Scripts\activate
python .\src\winner_winner.py

# macOS / Linux
source .venv/bin/activate
python ./src/winner_winner.py

#CSV Format
The CSV must contain a column called Winning Numbers, where each row has 5 numbers separated by spaces. Example:
3 15 27 44 65
10 24 36 54 68

📝 Notes

The variable is called power_ball in code, but it represents the Mega Ball (1–25).

The CSV should be stored in the data/ folder.

Works on Windows, macOS, and Linux.
