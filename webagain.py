import streamlit as st

# 1. Konfigurasi halaman agar bersih dan terpusat
st.set_page_config(page_title="Pencarian Web", layout="centered", initial_sidebar_state="collapsed")

# 2. Menggunakan CSS untuk menyembunyikan menu bawaan Streamlit dan mengatur gaya tampilan
st.markdown("""
    <style>
    /* Menyembunyikan komponen bawaan Streamlit agar bersih */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Mengatur jarak konten agar berada di tengah layar secara vertikal */
    .block-container {
        padding-top: 12rem;
        max-width: 45rem;
    }
    
    /* Mengatur gaya kotak jalan pintas */
    .shortcut-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background-color: #f0f2f6;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        text-decoration: none;
        color: #31333F;
        font-weight: bold;
        transition: transform 0.2s, background-color 0.2s;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
    }
    .shortcut-box:hover {
        transform: translateY(-5px);
        background-color: #e4e6eb;
        color: #0078ff;
    }
    .icon {
        font-size: 40px;
        margin-bottom: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Kolom Pencarian Google
query = st.text_input(
    label="Pencarian",
    placeholder="🔍 Cari lewat Google atau masukkan alamat...",
    label_visibility="collapsed"
)

# Jika user mengetik sesuatu lalu menekan Enter, arahkan langsung ke Google Search
if query:
    st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'https://google.com{query}\'" />', unsafe_allow_html=True)

st.write("") # Memberi jarak vertikal
st.write("")

# 4. Membuat Grid Kotak-Kotak Jalan Pintas Sesuai Permintaan
kolom1, kolom2, kolom3, kolom4 = st.columns(4)

# Kotak 1: YouTube
with kolom1:
    st.markdown("""
        <a href="https://youtube.com" target="_blank" class="shortcut-box">
            <div class="icon">▶️</div>
            <div>YouTube</div>
        </a>
    """, unsafe_allow_html=True)

# Kotak 2: Discord
with kolom2:
    st.markdown("""
        <a href="https://discord.com" target="_blank" class="shortcut-box">
            <div class="icon">💬</div>
            <div>Discord</div>
        </a>
    """, unsafe_allow_html=True)

# Kotak 3: WhatsApp
with kolom3:
    st.markdown("""
        <a href="https://whatsapp.com" target="_blank" class="shortcut-box">
            <div class="icon">🟢</div>
            <div>WhatsApp</div>
        </a>
    """, unsafe_allow_html=True)

# Kotak 4: TLauncher
with kolom4:
    st.markdown("""
        <a href="https://tlauncher.org" target="_blank" class="shortcut-box">
            <div class="icon">🎮</div>
            <div>TLauncher</div>
        </a>
    """, unsafe_allow_html=True)
