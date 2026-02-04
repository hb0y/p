import streamlit as st
import requests

st.set_page_config(page_title="PS3 Avatar Store", page_icon="🎮", layout="wide")

# --- قاعدة بيانات الافتارات (تقدر تزيد عليها بنفس الترتيب) ---
AVATAR_LIBRARY = [
    {"name": "Monreve Avatar II", "id": "EP4491-CUSA05486_00-AVATAR0000000011", "price": "1.49$", "region": "SA/EU"},
    {"name": "God of War: Kratos", "id": "UP9000-NPUA80491_00-AVATAR0000000001", "price": "0.49$", "region": "US"},
    {"name": "Uncharted: Nathan Drake", "id": "UP0001-NPUA80033_00-AVATAR0000000001", "price": "0.49$", "region": "US"},
    {"name": "The Last of Us: Joel", "id": "UP9000-NPUA80960_00-AVATAR0000000002", "price": "0.49$", "region": "US"},
    {"name": "Sly Cooper", "id": "EP9000-NPEA00338_00-AVATAR00000
