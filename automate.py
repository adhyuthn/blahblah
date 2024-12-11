import requests
import pprint

API_KEY = 'AIzaSyBRlNH70z3tuBVz5BKlAMNMOo2gPnYZ-84'
spreadsheet_id = '1LKY0vyVjpCy0cozdtQnI56wOQFqSqlI18_5I-Wxe8GM'
range_to_read = 'A2:D'
url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_to_read}?key={API_KEY}'

response = requests.get(url)
last_entry = response.json()["values"][-1]
time_text    = last_entry[0]
heading_text = last_entry[1]
content_text = last_entry[2]

print("RESPONSE:\n", response.json())

with open("README.md", "a") as fd:
    fd.write(f"### {heading_text}\nTimestamp: {time_text}\n{content_text}\n\n")
