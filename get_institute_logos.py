import os
import requests
import wikipediaapi
from bs4 import BeautifulSoup

universities = [
    "Athens School of Fine Arts",
    "Aristotle University of Thessaloniki",
    "School of Pedagogical and Technological Education (ASPETE)",
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
    "Harokopio University of Athens",
]

os.makedirs("logos", exist_ok=True)

# ✅ Add a proper User-Agent string
USER_AGENT = "UniversityLogoFetcher/1.0 (https://github.com/floriandima; contact: florian@example.com)"

wiki = wikipediaapi.Wikipedia(user_agent=USER_AGENT, language="en")


def get_logo_url(page_title):
    page = wiki.page(page_title)
    if not page.exists():
        return None
    response = requests.get(page.fullurl, headers={"User-Agent": USER_AGENT})
    soup = BeautifulSoup(response.text, "html.parser")
    infobox = soup.find("table", {"class": "infobox"})
    if not infobox:
        return None
    img = infobox.find("img")
    if img and "src" in img.attrs:
        return "https:" + img["src"]
    return None


def download_logo(uni):
    print(f"Searching logo for: {uni}")
    logo_url = get_logo_url(uni)
    if logo_url:
        filename = os.path.join("logos", uni.replace(" ", "_") + ".png")
        response = requests.get(logo_url, headers={"User-Agent": USER_AGENT})
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"No logo found for {uni}")


for u in universities:
    download_logo(u)
