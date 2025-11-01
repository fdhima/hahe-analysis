import requests
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv
import os
import re


load_dotenv()
DATA_SOURCE = os.getenv("DATA_SOURCE")

payload = {
    "filter[collectionyear]": "2025",   # 2023-2024
    "filter[instituteid]": "",  # All institutes
    "list[limit]": 0,   # All records

}
response = requests.post(DATA_SOURCE, data=payload)
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")

data = []
soup_data = soup.find_all('div', class_='stats-item')
for item in soup_data:
    institution = item  .find('div', class_='stats-item-title').text.strip()
    institution = re.search("^ΙΔΡΥΜΑ ::", institution)
    
    established = item.find('span', class_='stats-item-date').text.strip()
    established = re.search("Ημ/νία Ίδρυσης: ", established)
    
    variables = item.find_all('div', class_='stats-item-variable-title')
    print(f"variables: {variables}")
    for var in variables:
        print(var)
        variable = var.text.strip()
        if variable == "Απόφοιτοι ΠΠΣ Ιδρύματος":
            graduates = var.find_next_sibling('div', class_='stats-item-variable-value').text.strip()
        elif variable == "Εγγεγραμμένοι φοιτητές ΠΠΣ Ιδρύματος":
            registed_students = var.find_next_sibling('div', class_='stats-item-variable-value').text.strip()
        elif variable == "Εισαχθέντες φοιτητές ΠΠΣ Ιδρύματος":
            freshmen = var.find_next_sibling('div', class_='stats-item-variable-value').text.strip()
        elif variable == "Ενεργοί φοιτητές ΠΠΣ Ιδρύματος":
            active_students = var.find_next_sibling('div', class_='stats-item-variable-value').text.strip()

    data.append({
        'institution': institution.string[institution.end():],
        'established': established.string[established.end():],
        "gradutes": graduates,
        "registed_students": registed_students,
        "freshmen": freshmen,
        "active_students": active_students,
    })

df = pd.DataFrame(data)
df.to_csv('hahe.csv', index=False)


