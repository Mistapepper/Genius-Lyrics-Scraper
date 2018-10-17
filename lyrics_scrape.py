from bs4 import BeautifulSoup
import requests
import re 
import openpyxl
import os

urlList = ["https://genius.com/Bruno-mars-and-david-guetta-versace-on-the-floor-bruno-mars-vs-david-guetta-lyrics"]

wb = openpyxl.load_workbook(os.path.expanduser("~/MyPythonScripts/lyric_counts.xlsx"))
sheet = wb.get_sheet_by_name('Sheet1')
lyricCol = sheet['D']
targetRow = 1
    
for link in urlList:
    response = requests.get(link)
    text = response.text
    soup = BeautifulSoup(text, "html.parser")

    lyricBlock = soup.find('div', attrs ={'class':"lyrics"})

    rawLyrics = lyricBlock.text
    lyrics = rawLyrics.replace("—", " ").split()
    print(len(lyrics))

    for cell in lyricCol:
        if targetRow == 1:
            targetRow += 1
            continue

        if cell.row == targetRow:
            cell.value = len(lyrics)
            print(cell.value)
            wb.save('lyric_counts.xlsx')
    targetRow += 1


