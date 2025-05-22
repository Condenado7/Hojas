import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Detector de Enfermedades en Plantas",
    page_icon="🌿",
    layout="centered"
)

st.title("Detector de Enfermedades en Plantas 🌿")
st.write("Sube una imagen de una hoja y el modelo predecirá si está sana o enferma, y qué tipo de enfermedad tiene.")

# Función para cargar el modelo
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('plant_disease_model_tf.h5')
    return model

# Función para preprocesar la imagen
def preprocess_image(image):
    image = image.convert("RGB")  # 🔄 Fuerza RGB
    img = image.resize((128, 128))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array / 255.0  # Normalización
    img_array = np.expand_dims(img_array, axis=0)  # Crear batch
    return img_array

# Función para hacer la predicción
def predict(image, model):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    return prediction

def es_sano_o_enfermo(clase_traducida):
    palabras_sanas = ["Sano", "Sana", "Healthy"]
    for palabra in palabras_sanas:
        if palabra.lower() in clase_traducida.lower():
            return True
    return False
# Diccionario de traducción EN ➜ ES
class_translation = {
    "Cassava - Bacterial Blight (CBB)": "Yuca - Tizón Bacteriano",
    "Cassava - Brown Streak Disease (CBSD)": "Yuca - Raya Marrón",
    "Cassava - Green Mottle (CGM)": "Yuca - Moteado Verde",
    "Cassava - Healthy": "Yuca - Sana",
    "Cassava - Mosaic Disease (CMD)": "Yuca - Enfermedad del Mosaico",
    "Rice - BrownSpot": "Arroz - Mancha Marrón",
    "Rice - Healthy": "Arroz - Sano",
    "Rice - Hispa": "Arroz - Hispa",
    "Rice - LeafBlast": "Arroz - Tizón Foliar",
    "apple - scab": "Manzana - Sarna",
    "apple - black rot": "Manzana - Podredumbre Negra",
    "apple - cedar apple rust": "Manzana - Óxido del Cedro",
    "apple - healthy": "Manzana - Sana",
    "cherry (including sour) - healthy": "Cereza - Sana",
    "cherry (including sour) - powdery mildew": "Cereza - Mildiú Polvoso",
    "corn (maize) - cercospora leaf spot gray leaf spot": "Maíz - Mancha de Cercospora",
    "corn (maize) - common rust": "Maíz - Royas Comunes",
    "corn (maize) - healthy": "Maíz - Sano",
    "corn (maize) - northern leaf blight": "Maíz - Tizón del Norte",
    "grape - black rot": "Uva - Podredumbre Negra",
    "grape - esca (black measles)": "Uva - Esca (Sarampión Negro)",
    "grape - healthy": "Uva - Sana",
    "grape - leaf blight": "Uva - Tizón de la Hoja",
    "orange - haunglongbing (citrus greening)": "Naranja - Huanglongbing (Enverdecimiento Cítrico)",
    "peach - bacterial spot": "Durazno - Mancha Bacteriana",
    "peach - healthy": "Durazno - Sano",
    "pepper, bell - bacterial spot": "Pimiento - Mancha Bacteriana",
    "pepper, bell - healthy": "Pimiento - Sano",
    "potato - early blight": "Papa - Tizón Temprano",
    "potato - healthy": "Papa - Sana",
    "potato - late blight": "Papa - Tizón Tardío",
    "squash - powdery mildew": "Calabaza - Mildiú Polvoso",
    "strawberry - healthy": "Fresa - Sana",
    "strawberry - leaf scorch": "Fresa - Mancha de la Hoja",
    "tomato - bacterial spot": "Tomate - Mancha Bacteriana",
    "tomato - early blight": "Tomate - Tizón Temprano",
    "tomato - healthy": "Tomate - Sano",
    "tomato - late blight": "Tomate - Tizón Tardío",
    "tomato - leaf mold": "Tomate - Moho",
    "tomato - septoria leaf spot": "Tomate - Mancha de Septoria",
    "tomato - spider mites two-spotted spider mite": "Tomate - Araña Roja",
    "tomato - target spot": "Tomate - Mancha Objetiva",
    "tomato - tomato mosaic virus": "Tomate - Virus del Mosaico",
    "tomato - tomato yellow leaf curl virus": "Tomate - Enrollamiento Amarillo"
}

# Cargar índices de clase guardados (class_indices.json)
try:
    with open('class_indices.json') as f:
        class_indices = json.load(f)

    # Reconstrucción segura y ordenada de class_names
    class_names = [clase for clase, _ in sorted(class_indices.items(), key=lambda item: item[1])]
except Exception as e:
    st.error(f"❌ Error al cargar class_indices.json: {e}")
    st.stop()

# Cargar modelo
try:
    model = load_model()
    st.success("✅ Modelo cargado exitosamente.")
    st.write(f"Este modelo tiene **{model.output_shape[-1]}** salidas (clases).")

    # Validar que el número de clases coincida
    if len(class_names) != model.output_shape[-1]:
        st.warning(f"⚠️ Número de clases en class_indices ({len(class_names)}) no coincide con las salidas del modelo ({model.output_shape[-1]}).")
except Exception as e:
    st.error(f"❌ Error al cargar el modelo: {e}")
    st.stop()
# Cargar índices de clase guardados (class_indices.json)
try:
    with open('class_indices.json') as f:
        class_indices = json.load(f)

    # Reconstrucción segura y ordenada de class_names
    class_names = [clase for clase, _ in sorted(class_indices.items(), key=lambda item: item[1])]
except Exception as e:
    st.error(f"❌ Error al cargar class_indices.json: {e}")
    st.stop()

# Cargar modelo
try:
    model = load_model()
    st.success("✅ Modelo cargado exitosamente.")
    st.write(f"Este modelo tiene **{model.output_shape[-1]}** salidas (clases).")

    # Validar que el número de clases coincida
    if len(class_names) != model.output_shape[-1]:
        st.warning(f"⚠️ Número de clases en class_indices ({len(class_names)}) no coincide con las salidas del modelo ({model.output_shape[-1]}).")
except Exception as e:
    st.error(f"❌ Error al cargar el modelo: {e}")
    st.stop()


# Interfaz para subir la imagen
uploaded_file = st.file_uploader("Elige una imagen de una hoja...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Mostrar la imagen
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada", use_column_width=True)
    
    # Botón para hacer predicción
    if st.button("Predecir"):
        with st.spinner("Analizando la imagen..."):
            prediction = predict(image, model)

            predicted_class_index = np.argmax(prediction)
            if predicted_class_index < len(class_names):
                predicted_class = class_names[predicted_class_index]
            else:
                predicted_class = f"Clase desconocida ({predicted_class_index})"

            confidence = float(prediction[0][predicted_class_index]) * 100

            st.subheader("Resultado:")
            translated_class = class_translation.get(predicted_class, predicted_class)

            if es_sano_o_enfermo(translated_class):
                st.success(f"📊 Predicción: **{translated_class}** (Planta sana) con {confidence:.2f}% de confianza")
            else:
                st.error(f"📊 Predicción: **{translated_class}** (Planta enferma) con {confidence:.2f}% de confianza")

            st.subheader("Probabilidades de todas las clases:")

            # Solo crear DataFrame si las longitudes coinciden
            if len(class_names) == len(prediction[0]):
                probs_df = {
                    "Clase": class_names,
                    "Probabilidad (%)": [float(p) * 100 for p in prediction[0]]
                }

                df = pd.DataFrame(probs_df)
                df_top = df.sort_values("Probabilidad (%)", ascending=False).head(5)
                st.table(df_top)

                df_low = df.sort_values("Probabilidad (%)", ascending=True).head(5)
                st.table(df_low)
            else:
                st.warning("⚠️ No se pueden mostrar las probabilidades porque las clases y las predicciones no coinciden en tamaño.")

