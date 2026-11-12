import streamlit as st
import os

# Configuración inicial de la página
st.set_page_config(page_title="Mental AI Insights", page_icon="🧠", layout="wide")

# --- ESTILOS CSS PERSONALIZADOS (Dashboard Moderno) ---
st.markdown("""
<style>
    /* Fondo principal suave */
    .stApp {
        background-color: #F4F7F6;
    }
    /* Estilo de la barra lateral */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #EAEAEA;
        padding-top: 2rem;
    }
    /* Títulos limpios */
    h1, h2, h3, h4 {
        color: #2C3E50;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
    }
    /* Botón moderno */
    .stButton>button {
        background-color: #5D5FEF;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #4A4CBF;
        color: white;
        box-shadow: 0 4px 12px rgba(93, 95, 239, 0.3);
    }
    /* Estilo de los expanders para simular tarjetas */
    .streamlit-expanderHeader {
        background-color: #FFFFFF;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (SIDEBAR) ---
img_path = "/content/Logo_de_la_Univesidad_de_la_Salle_(Bogotá).svg"
if os.path.exists(img_path):
    st.sidebar.image(img_path, use_container_width=True)

st.sidebar.markdown("### ⚙️ Configuración")

api_key_default = os.environ.get("OPENAI_API_KEY", "")
api_key = st.sidebar.text_input("🔑 OpenAI API Key", value=api_key_default, type="password")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

st.sidebar.markdown("---")
st.sidebar.markdown("### 📄 Documentos")
archivo_pdf = st.sidebar.file_uploader("Cargar Artículo (PDF)", type=["pdf"])
if archivo_pdf:
    st.sidebar.success("✅ Documento cargado y procesado")

# --- ÁREA PRINCIPAL ---
st.markdown("<h1>🧠 Mental AI Insights</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.2rem; color: #7F8C8D; margin-bottom: 2rem;'>Análisis crítico de literatura científica sobre IA y Salud Mental</p>", unsafe_allow_html=True)

# Contenedores simulando tarjetas
col1, col2 = st.columns([2, 1.2], gap="large")

with col1:
    st.markdown("### 💬 Chat Clínico")
    st.markdown("Interactúa con el asistente para extraer evidencia estructurada del documento.")
    
    # Contenedor de chat
    with st.container():
        pregunta = st.text_input("", placeholder="Ej: ¿Cuáles son los riesgos de sesgo algorítmico en diagnósticos?")
        if st.button("🚀 Consultar Evidencia"):
            if not api_key:
                st.warning("⚠️ Ingresa tu API Key en la barra lateral.")
            else:
                with st.spinner("🧠 Analizando base vectorial..."):
                    st.info("💡 **Respuesta (Simulada):** El uso de IA presenta oportunidades como el acceso 24/7, pero el documento destaca riesgos críticos asociados a la pérdida del vínculo terapéutico y sesgos en el entrenamiento de los algoritmos (Página 4).")

with col2:
    st.markdown("### 📊 Dimensiones de Análisis")
    st.markdown("<p style='color: #7F8C8D; font-size: 0.9rem;'>Áreas de enfoque clínico</p>", unsafe_allow_html=True)
    
    with st.expander("🌿 Bienestar Psicológico", expanded=True):
        st.write("Evaluación del impacto general en la salud mental de los usuarios.")
    with st.expander("😟 Ansiedad y Depresión", expanded=False):
        st.write("Efectividad y riesgos de herramientas de triaje y acompañamiento.")
    with st.expander("🤖 Dependencia Tecnológica", expanded=False):
        st.write("Riesgos de sustitución del vínculo humano por chatbots.")
    with st.expander("⚖️ Ética y Privacidad", expanded=False):
        st.write("Manejo de datos sensibles y sesgos algorítmicos.")
