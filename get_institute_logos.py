import os
import requests
from googlesearch import search

# List of Greek universities
universities = [
    "Athens School of Fine Arts",
    "Aristotle University of Thessaloniki",
    "School of Pedagogical and Technological Education Greece",
    "Agricultural University of Athens",
    "Democritus University of Thrace",
    "International Hellenic University",
    "National and Kapodistrian University of Athens",
    "National Technical University of Athens",
    "Hellenic Open University",
    "Hellenic Mediterranean University",
    "Ionian University",
    "Athens University of Economics and Business",
    "University of the Aegean",
    "University of West Attica",
    "University of Western Macedonia",
    "University of Thessaly",
    "University of Ioannina",
    "University of Crete",
    "University of Macedonia",
    "University of Patras",
    "University of Piraeus",
    "University of the Peloponnese",
    "Panteion University of Social and Political Sciences",
    "Technical University of Crete",
    "Hellenic Army Academy",
    "Hellenic Air Force Academy",
    "Hellenic Naval Academy",
    "Harokopio University of Athens"
]

# Folder to save logos
os.makedirs("logos", exist_ok=True)

def download_image(url, filename):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

for uni in universities:
    query = f"{uni} logo site:.gr"
    try:
        # Get the first Google search result (usually an image)
        for result in search(query, num_results=5):
            if result.lower().endswith(('.png', '.jpg', '.jpeg', '.svg')):
                filename = os.path.join("logos", f"{uni.replace(' ', '_')}{os.path.splitext(result)[1]}")
                download_image(result, filename)
                break
    except Exception as e:
        print(f"Error searching for {uni}: {e}")

