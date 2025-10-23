import requests

# URL:en till API:et som vi vill hämta data ifrån
# Detta är länken till alla jordartsobjekt (items) i samlingen 'grundlager'
url = "https://api.sgu.se/oppnadata/jordarter25k-100k/ogc/features/v1/collections/grundlager/items"

# Namnet på filen vi vill spara datan i.
# Ändelsen .geojson är bra eftersom det är formatet datan levereras i.
filnamn = "jordartsdata.geojson"

print(f"Försöker hämta data från: {url}")

try:
    # Gör ett GET-anrop till URL:en.
    # timeout=30 betyder att vi väntar i max 30 sekunder på svar.
    response = requests.get(url, timeout=30)

    # Kontrollerar om anropet lyckades (statuskod 200 OK).
    # Om inte, kastas ett undantag (fel) och programmet hoppar till 'except'-blocket.
    response.raise_for_status()

    # Öppna filen 'jordartsdata.geojson' i skrivläge ('w').
    # 'encoding="utf-8"' är viktigt för att svenska tecken (å, ä, ö) ska sparas korrekt.
    # 'with open(...)' ser till att filen stängs automatiskt efteråt.
    with open(filnamn, 'w', encoding='utf-8') as fil:
        # Skriv hela svarets textinnehåll till filen.
        fil.write(response.text)

    print(f"Klart! Datan har sparats i filen '{filnamn}'")

except requests.exceptions.RequestException as e:
    # Detta block körs om något gick fel med webbanropet.
    print(f"Ett fel inträffade vid hämtning av datan: {e}")

except Exception as e:
    # Detta block körs om något annat oväntat fel inträffade.
    print(f"Ett oväntat fel inträffade: {e}")