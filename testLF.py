import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Počasí ve městě", layout="centered")
st.title("🌤️ Aplikace pro zobrazení počasí pomocí wttr.in")

city = st.text_input("Zadej název města (např. Praha, Brno, Ostrava):", value="Praha")

if city:
    st.markdown(f"### Počasí pro: **{city.title()}**")
    # Sestavení URL pro získání obrázku s předpovědí z wttr.in
    url = f"https://wttr.in/{city}.png"
    try:
        response = requests.get(url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content))
        st.image(image, caption=f"Počasí v {city.title()}", use_column_width=True)
    except requests.exceptions.RequestException as e:
        st.error(f"Nepodařilo se získat počasí: {e}")

st.markdown("---")
st.markdown(
    "Zdroj dat: [wttr.in](https://wttr.in/)"
)
