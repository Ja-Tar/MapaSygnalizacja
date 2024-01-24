import requests
import xml.etree.ElementTree as ET

# Lista linków do plików SVG
svg_links = [
    "https://upload.wikimedia.org/wikipedia/commons/9/9e/Bia%C5%82e_d%C3%B3%C5%82_ci%C4%85g%C5%82e.svg",
    "https://upload.wikimedia.org/wikipedia/commons/2/2f/Podstawa_semafor-C2.svg"
]

# Pusta lista do przechowywania treści plików SVG
svg_contents = []

# Pobieranie treści plików SVG
for link in svg_links:
    response = requests.get(link)
    if response.status_code == 200:
        svg_contents.append(response.content)
    else:
        print(f"Nie udało się pobrać pliku SVG z linku: {link}")

# Tworzenie głównego elementu SVG
root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg", attrib={"version": "1.1", "encoding": "UTF-8"})

# Iteracja przez treści pobranych plików SVG i dodanie ich do głównego SVG
for i, content in enumerate(svg_contents):
    try:
        # Parsowanie treści pliku SVG
        svg_tree = ET.fromstring(content)

        # Tworzenie grupy (g) dla każdego pliku SVG
        svg_group = ET.SubElement(root, "g", {"transform": f"translate(0, {i * 28})"})

        # Dodanie elementów z parsowanego pliku SVG do grupy
        svg_group.extend(svg_tree)
    except ET.ParseError:
        print(f"Nie udało się sparsować pliku SVG z linku: {svg_links[i]}")

# Ustawienie szerokości i wysokości obszaru SVG
root.set("width", "50")
root.set("height", str(len(svg_links) * 28))  # Ustawienie wysokości na całkowitą wysokość wszystkich obrazów

# Tworzenie drzewa XML
tree = ET.ElementTree(root)

# Zapisywanie do pliku SVG
tree.write("combined_svg.svg", encoding="utf-8", xml_declaration=True)
