"""
Config

- Creation of folder and file for statistics
    'game_history' to store result statistics
- Difficulty levels: easy 20, medium 12 and hard 5  
- Range of number to guess (1-1000)
"""

import os 
import openpyxl
from pathlib import Path


# Create folder and statistics file 
folder = "c:\\PythonExercises" if os.name == 'nt' else os.path.expanduser("~/PythonExercises")
statistics_file = os.path.join(folder, "statistics.xlsx") 
os.makedirs(folder, exist_ok=True)

# Create file
if not os.path.exists(statistics_file):
    excel_document = openpyxl.Workbook()
    sheet = excel_document.active
    sheet.title = "Statistics"
    sheet.append(["Date", "Name", "Mode", "Difficulty", "Attempts", "Result"])
    excel_document.save(statistics_file)

# Difficulty levels
difficulty = {
    '1': {'level': 'Easy', 'attempts': 20},
    '2': {'level': 'Medium', 'attempts': 12},    
    '3': {'level': 'Hard', 'attempts': 5}    
}

# Range for guessing
min_num = 1
max_num = 1000