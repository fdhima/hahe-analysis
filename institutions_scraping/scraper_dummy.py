import requests
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv
import os
import re


def save_to_csv(data: list[dict], filename: str):
    """Save the list of dictionaries to a CSV file.
    
    Args:
        data (list): List of dictionaries containing the scraped data.
        filename (str): The name of the CSV file to save the data.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


def map_programme(id: str) -> str:
    """Map programme names to standardized names."""
    programmes_map = {
        # '0': '- Select programme -',
        '1': 'Athens School of Fine Arts',
        '2': 'Aristotle University of Thessaloniki',
        '3': 'School of Pedagogical and Technological Education',
        '4': 'Agricultural University of Athens',
        '5': 'Democritus University of Thrace',
        '6': 'International Hellenic University',
        '7': 'National and Kapodistrian University of Athens',
        '8': 'National Technical University of Athens',
        '9': 'Hellenic Open University',
        '10': 'Hellenic Mediterranean University',
        '11': 'Ionian University',
        '12': 'Athens University of Economics and Business',
        '13': 'University of the Aegean',
        '14': 'University of West Attica',
        '15': 'University of Western Macedonia',
        '16': 'University of Thessaly',
        '17': 'University of Ioannina',
        '18': 'University of Crete',
        '19': 'University of Macedonia',
        '20': 'University of Patras',
        '21': 'University of Piraeus',
        '22': 'University of Peloponnese',
        '23': 'Panteion University of Social and Political Sciences',
        '24': 'Technical University of Crete',
        '25': 'Hellenic Army Academy',
        '26': 'Hellenic Air Force Academy',
        '27': 'Hellenic Naval Academy',
        '28': 'Harokopio University'
    }
    return programmes_map.get(id, "Unknown programme")


def scrape_data(soup: BeautifulSoup):
    """Scrape data from the BeautifulSoup object and return a list of dictionaries.
    
    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing the HTML content.
    """
    soup_data = soup.find_all('div', class_='stats-item')
    print(f"soup_data: {soup_data}")
    for item in soup_data:
        print(f"item: {item}")
        institution = item.find('div', class_='page-header').text.strip()
        institution = re.search("^ ΙΔΡΥΜΑ ::", institution)

        programme = item.find('div', class_='stats-item-title').text.strip()
        programme = re.search("^ ΠΠΣ ::", programme)
        
        established = item.find('span', class_='stats-item-date').text.strip()
        established = re.search("^Ημ/νία Ίδρυσης: ", established)
        
        variables = item.find_all('div', class_='stats-item-variable-title')
        print(f"variables: {variables}")
        for var in variables:
            print(var)
            variable = var.text.strip()
            if variable == "Απόφοιτοι ΠΠΣ":
                graduate = var.find_next_sibling('div', class_='stats-item-variable-value').text.strip()
            elif variable == "Εγγεγραμμένοι φοιτητές ΠΠΣ":
                registered = var.find_next_sibling('div', class_='stats-item-variable-value').text.strip()
            elif variable == "Εισαχθέντες φοιτητές ΠΠΣ":
                enrolled = var.find_next_sibling('div', class_='stats-item-variable-value').text.strip()
            elif variable == "Ενεργοί φοιτητές ΠΠΣ":
                active = var.find_next_sibling('div', class_='stats-item-variable-value').text.strip()

        return {
            # 'institution': institution.string[institution.end():].strip(),
            "institution": map_programme(payload.get("filter[instituteid]")),
            'collection_year': payload.get("filter[collectionyear]"),
            'programme': programme.string[programme.end():].strip(),
            'established': established.string[established.end():],
            "graduate": int(graduate.replace('.', '')),
            "registered": int(registered.replace('.', '')),
            "enrolled": int(enrolled.replace('.', '')),
            "active": int(active.replace('.', '')),
        }


load_dotenv()
DATA_SOURCE = os.getenv("DATA_SOURCE")

payload = {
    "filter[collectionyear]": "2025",   # 2023-2024
    "filter[instituteid]": "",  # All institutes
    "list[limit]": 0,   # All records
}

data = []
for year in range(2020, 2026):
    for inst_id in range(1, 29):
        payload["filter[instituteid]"] = str(inst_id)
        payload["filter[collectionyear]"] = str(year)
        print(f"payload: {payload}")
        response = requests.post(DATA_SOURCE, data=payload, headers={"User-Agent": "Mozilla/5.0"})
        print(response.content.decode(response.encoding or 'utf-8'))
        response.raise_for_status()
        soup = BeautifulSoup(response.content.decode(response.encoding or 'utf-8'), "html.parser")


        data.append(scrape_data(soup))
        save_to_csv(data, f"hahe_{payload.get('filter[instituteid]')}_{payload.get('filter[collectionyear]')}.csv")
        
