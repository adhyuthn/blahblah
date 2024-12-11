import requests
import pprint

API_KEY = 'AIzaSyBRlNH70z3tuBVz5BKlAMNMOo2gPnYZ-84'
spreadsheet_id = '1LKY0vyVjpCy0cozdtQnI56wOQFqSqlI18_5I-Wxe8GM'
range_to_read = 'A1:D5'
url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_to_read}?key={API_KEY}'

response = requests.get(url)
last_entry = response.json()["values"][-1]
heading_text = last_entry[1]
content_text = last_entry[2]

with open("README.md", "a") as fd:
    fd.write(f"### {heading_text}\n{content_text}\n\n")
