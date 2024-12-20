import requests
import pprint
import os

API_KEY = os.environ["API_KEY_SHEETS2"]
SPREADSHEET_ID = os.environ["SPREADSHEET_ID_SHEETS2"]
range_to_read = 'A2:C'
url = f'https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{range_to_read}?key={API_KEY}'

response = requests.get(url)
last_entry = response.json()["values"][-1]
time_text    = last_entry[0]
heading_text = last_entry[1]
content_text = last_entry[2]

print("RESPONSE:\n", response.json())

with open("README.md", "a") as fd:
    fd.write(f"### {heading_text}\nTimestamp: {time_text} \n\n{content_text}\n\n---\n\n")
