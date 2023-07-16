import streamlit as st
from streamlit_option_menu import option_menu

#navigasi
with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Prediksi Rating'])
    selected

if (selected == 'Home'):
    st.title("Koefisien Pajak Web Application")
    st.write("By : PSTB - BRIN team")

if (selected == 'Prediksi Rating'):
    # horizontal Menu
    selected2 = option_menu(None, ["Diesel", "Gasoline"],  
    orientation="horizontal")
    
    if (selected2 == "Diesel"):
        opasitas = st.text_input("Opasitas kendaraan (angka 0 - 100):", 0)
        tahun = st.text_input("Tahun Pembuatan kendaraan (s/d 2023):", 0)
        
        hitungD = st.button("HITUNG RATING")
    if (selected2 == "Gasoline"):
        tahun = st.text_input("Tahun Pembuatan kendaraan (s/d 2023):", 0)
        co = st.text_input("Nilai CO kendaraan (0 - 10):", 0)
        hc = st.text_input("Nilai HC kendaraan (0 - 10000):", 0)
        hitungG = st.button("HITUNG RATING")