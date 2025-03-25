import json 

# Cargar el archivo GeoJSON
with open("colombia.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Filtrar las características donde "NOMBRE_DPT" sea "BOYACA"
boyaca_features = {
    "type": "FeatureCollection",
    "features": [
        feature for feature in data["features"]
        if feature["properties"].get("NOMBRE_DPT") == "BOYACA"
    ]
}

# Guardar el nuevo archivo GeoJSON
with open("boyaca_filtered.geojson", "w", encoding="utf-8") as file:
    json.dump(boyaca_features, file, ensure_ascii=False, indent=4)

print("Archivo filtrado guardado como boyaca_filtered.geojson")