import xml.etree.ElementTree as ET

# Lista linków do plików SVG
svg_links = [
    "https://upload.wikimedia.org/wikipedia/commons/9/9e/Bia%C5%82e_d%C3%B3%C5%82_ci%C4%85g%C5%82e.svg",
    "https://upload.wikimedia.org/wikipedia/commons/2/2f/Podstawa_semafor-C2.svg"
]

# Tworzenie głównego elementu SVG
root = ET.Element("svg", xmlns="http://www.w3.org/2000/svg")

# Iteracja przez listę linków i dodanie każdego pliku SVG pod poprzednim
for i, link in enumerate(svg_links):
    # Tworzenie elementu <image> dla każdego pliku SVG
    image_element = ET.SubElement(root, "image", {"href": link, "y": str(i * 28)})  # Ustawienie y dla każdego obrazu

# Ustawienie szerokości i wysokości obszaru SVG
root.set("width", "50")
root.set("height", str(len(svg_links) * 28))  # Ustawienie wysokości na całkowitą wysokość wszystkich obrazów

# Tworzenie drzewa XML
tree = ET.ElementTree(root)

# Zapisywanie do pliku SVG
tree.write("combined_svg.svg")