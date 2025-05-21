import json

class_names = [
    "Cassava - Bacterial Blight (CBB)",
    "Cassava - Brown Streak Disease (CBSD)",
    "Cassava - Green Mottle (CGM)",
    "Cassava - Healthy",
    "Cassava - Mosaic Disease (CMD)",
    "Rice - BrownSpot",
    "Rice - Healthy",
    "Rice - Hispa",
    "Rice - LeafBlast",
    "apple - scab",
    "apple - black rot",
    "apple - cedar apple rust",
    "apple - healthy",
    "cherry (including sour) - healthy",
    "cherry (including sour) - powdery mildew",
    "corn (maize) - cercospora leaf spot gray leaf spot",
    "corn (maize) - common rust",
    "corn (maize) - healthy",
    "corn (maize) - northern leaf blight",
    "grape - black rot",
    "grape - esca (black measles)",
    "grape - healthy",
    "grape - leaf blight",
    "orange - haunglongbing (citrus greening)",
    "peach - bacterial spot",
    "peach - healthy",
    "pepper, bell - bacterial spot",
    "pepper, bell - healthy",
    "potato - early blight",
    "potato - healthy",
    "potato - late blight",
    "squash - powdery mildew",
    "strawberry - healthy",
    "strawberry - leaf scorch",
    "tomato - bacterial spot",
    "tomato - early blight",
    "tomato - healthy",
    "tomato - late blight",
    "tomato - leaf mold",
    "tomato - septoria leaf spot",
    "tomato - spider mites two-spotted spider mite",
    "tomato - target spot",
    "tomato - tomato mosaic virus",
    "tomato - tomato yellow leaf curl virus"
]

# Crear diccionario índice → clase
class_indices = {class_name: idx for idx, class_name in enumerate(class_names)}

# Guardar en archivo JSON
with open('class_indices.json', 'w') as f:
    json.dump(class_indices, f, indent=4)

print("Archivo 'class_indices.json' generado correctamente.")
