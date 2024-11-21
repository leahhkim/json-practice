import json
import csv
with open('data/schacon.repos.json', 'r') as file:
        data = json.load(file)
with open('chacon.csv', 'w', newline='') as csv_file:
        csvwrite = csv.writer(csv_file)
        for entry in data[0:5]:
                name = entry.get('name')
                html_url = entry.get('html_url')
                updated_at = entry.get('updated_at')
                visibility = entry.get('visibility')
                csvwrite.writerow([name, html_url, updated_at, visibility])
file.close()

