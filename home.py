import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


def home():
    # st.sidebar.title(f"Hello {nama}")
    with st.sidebar:
        selected = option_menu(None, ["Home", 'Prediksi', "Optimasi Hyperparameter"],
        icons=['house', 'graph-up', 'gear-fill'], menu_icon="cast", default_index=0)

    if (selected == 'Home'):
        st.image("logo.png", None, use_column_width=True)
        st.markdown("<h1 style='font-size:40px;font-family: 'Courier New';'>SELAMAT DATANG,</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style=''>Web Aplikasi Prediksi Koefisien Pajak dan Pemodelan untuk Data Engineering</h2>", unsafe_allow_html=True)
        st.markdown("<h6 style=''>By : PSTB - BRIN team</h6>", unsafe_allow_html=True)

    if (selected == 'Prediksi'):
        with st.container():
            st.markdown("<h5 style='text-align : center;'>Prediksi Koefisien Pajak Bahan Bakar Diesel/Gasoline</h5>", unsafe_allow_html=True)
            ## horizontal Menu
            selected2 = option_menu(None, ["Diesel", "Gasoline"], 
            icons=['fuel-pump-diesel', 'fuel-pump'], 
            menu_icon="cast", default_index=0, orientation="horizontal")
                
            if (selected2 == "Diesel"):
                opasitas = st.number_input("Opasitas kendaraan (angka 0 - 100):", 0)
                tahun = st.number_input("Tahun Pembuatan kendaraan (s/d 2023):", 0)
                hasilD = tahun+opasitas
                hitungD = st.button("PREDIKSI", hasilD)
                if hitungD:
                    st.write("Hasil prediksi nilai rating bahan bakar diesel : ", hasilD)
                
            if (selected2 == "Gasoline"):
                tahun = st.number_input("Tahun Pembuatan kendaraan (s/d 2023):", 0)
                co = st.number_input("Nilai CO kendaraan (0 - 10):", 0)
                hc = st.number_input("Nilai HC kendaraan (0 - 10000):", 0)
                hasilG = tahun+co+hc
                hitungG = st.button("PREDIKSI", hasilG)
                if hitungG:
                    st.write("Hasil prediksi nilai rating bahan bakar gasoline : ", hasilG)
    
    if (selected == 'Optimasi Hyperparameter'):
        with st.container():
            st.markdown("<h5 style='text-align : center;'>Optimasi Hyperparameter dengan Multilayer Perceptron (MLP) dan Gaussian Process Regression (GPR)</h5>", unsafe_allow_html=True)
            ## horizontal Menu
            selected2 = option_menu(None, ["MLP", "GPR"], 
            icons=['1-circle-fill', '2-circle-fill'], 
            menu_icon="cast", default_index=0, orientation="horizontal")
                
            if (selected2 == "Diesel"):
                st.title("MLP")
            if (selected2 == "Gasoline"):
                st.title("GPR")
                
                 
def login():
    names = ["Audrina Angela", "Arlo Amstrong"]
    usernames = ["user1", "user2"]
    passwords = ["user1", "user2"]

    # print([names[0]])

    st.title('Login Page')
    # Add a login form

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if username in usernames and password in passwords:
            user_index = usernames.index(username)
            if passwords[user_index] == password:
                st.session_state.is_logged_in = True
            else:
                st.error('Invalid password')
        else:
            st.error('Invalid username')

def main():
    # Initialize the 'is_logged_in' session state variable
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False

    if not st.session_state.is_logged_in:
        login()
    else:
        home()

if __name__ == '__main__':
    main()
