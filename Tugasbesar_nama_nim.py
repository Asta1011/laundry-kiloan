import streamlit as st

st.set_page_config(page_title="LaundryKu | Kalkulator Laundry", page_icon="🧺", layout="centered", initial_sidebar_state="collapsed")

st.markdown('''<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"], [data-testid="stApp"] {font-family:'Plus Jakarta Sans',sans-serif;}
[data-testid="stAppViewContainer"] {background:linear-gradient(160deg,#e9f7ff 0%,#f5f8ff 48%,#f5edff 100%);}
.block-container {max-width:680px;padding:1.2rem 1rem 3rem;}
#MainMenu,footer,header {visibility:hidden;}
.hero {background:linear-gradient(125deg,#0956ba,#5576e8 65%,#8e69de);padding:27px 23px;border-radius:25px;color:white;box-shadow:0 12px 30px #2459bd30;margin-bottom:22px;}
.hero .eyebrow {font-size:12px;letter-spacing:2px;font-weight:800;opacity:.85;}
.hero h1 {color:white;font-size:clamp(28px,7vw,39px);line-height:1.16;margin:12px 0 9px;font-weight:800;}
.hero p {color:#e8f2ff;font-size:14px;margin:0;}
.section-heading {font-weight:800;color:#172c58;font-size:18px;margin:12px 0 5px;}
.small-note {font-size:12px;color:#62728c;margin:0 0 12px;}
[data-testid="stForm"] {border:1px solid #dce7fa;background:#ffffff;border-radius:22px;padding:18px 18px 13px;box-shadow:0 8px 24px #2e4c8c12;}
label {font-weight:700!important;color:#26365a!important;}
.stButton button, [data-testid="stFormSubmitButton"] button {border-radius:13px!important;min-height:47px;font-weight:800!important;}
[data-testid="stFormSubmitButton"] button {background:linear-gradient(100deg,#1169d9,#6555d9)!important;color:white!important;border:0!important;}
.result {background:white;border:1px solid #dce7fa;border-radius:23px;padding:22px;margin-top:18px;box-shadow:0 8px 24px #2e4c8c12;}
.result h3 {margin:0 0 4px;color:#152b56;font-size:20px;}
.result .muted {color:#71809c;font-size:12px;margin-bottom:17px;}
.receipt-row {display:flex;justify-content:space-between;gap:12px;padding:10px 0;border-bottom:1px dashed #dbe3f2;color:#4a5c7b;font-size:14px;}
.receipt-row b {color:#152b56;text-align:right;}
.total {background:linear-gradient(110deg,#dcfce7,#e1f9ed);border-radius:16px;padding:17px;margin-top:16px;display:flex;justify-content:space-between;align-items:center;color:#13643c;font-weight:800;}
.total strong {font-size:clamp(21px,6vw,28px);}
.footnote {text-align:center;color:#8190a7;font-size:12px;margin-top:23px;}
@media(max-width:480px){.block-container{padding:0.8rem .8rem 2rem}.hero{padding:24px 19px;border-radius:20px}[data-testid="stForm"]{padding:13px}.result{padding:17px}.receipt-row{font-size:13px}}
</style>''', unsafe_allow_html=True)

def rupiah(n):
    return 'Rp ' + f'{n:,}'.replace(',', '.')

if 'hasil' not in st.session_state:
    st.session_state.hasil = None
if 'nim_input' not in st.session_state:
    st.session_state.nim_input = ''
if 'berat_input' not in st.session_state:
    st.session_state.berat_input = ''

st.markdown('''<div class="hero"><div class="eyebrow">🫧 LAUNDRYKU • SMART CALCULATOR</div><h1>🧺 Laundry bersih,<br>hitung makin mudah.</h1><p>Masukkan NIM dan berat cucian untuk melihat total biaya serta diskon spesialmu ✨</p></div>''', unsafe_allow_html=True)
st.markdown('<div class="section-heading">🧮 Hitung biaya laundry</div><p class="small-note">Isi kedua kolom berikut, lalu tekan tombol Hitung.</p>', unsafe_allow_html=True)

with st.form('form_laundry'):
    nim = st.text_input('🎓 NIM (10 digit)', key='nim_input', placeholder='Contoh: 2411001347', max_chars=20)
    berat_teks = st.text_input('⚖️ Berat cucian (kg)', key='berat_input', placeholder='Contoh: 4')
    col1, col2 = st.columns(2)
    with col1:
        hitung = st.form_submit_button('🧮 Hitung', use_container_width=True)
    with col2:
        reset = st.form_submit_button('↺ Reset', use_container_width=True)

if reset:
    st.session_state.hasil = None
    st.session_state.nim_input = ''
    st.session_state.berat_input = ''
    st.rerun()

if hitung:
    st.session_state.hasil = None
    if len(nim) != 10 or not nim.isdigit() or not nim.isascii():
        st.error('NIM tidak valid! Masukkan tepat 10 digit angka (0–9).')
    elif not berat_teks.isascii() or not berat_teks.isdigit() or int(berat_teks) <= 0:
        st.error('Berat tidak valid! Masukkan bilangan bulat positif lebih dari 0.')
    else:
        berat = int(berat_teks)
        digit_terakhir = int(nim[-1])
        jumlah_genap = sum(int(d) % 2 == 0 for d in nim)
        tarif = 5000 + digit_terakhir * 500
        persen = jumlah_genap
        normal = berat * tarif
        potongan = normal * persen // 100
        total = normal - potongan
        st.session_state.hasil = (nim, berat, tarif, jumlah_genap, persen, normal, potongan, total)

if st.session_state.hasil:
    nim, berat, tarif, genap, persen, normal, potongan, total = st.session_state.hasil
    st.markdown(f'''<div class="result"><h3>🧾 Rincian pembayaran</h3><div class="muted">Perhitungan berhasil • LaundryKu</div>
    <div class="receipt-row"><span>NIM pelanggan</span><b>{nim}</b></div>
    <div class="receipt-row"><span>Berat cucian</span><b>{berat} kg</b></div>
    <div class="receipt-row"><span>Tarif per kg</span><b>{rupiah(tarif)}</b></div>
    <div class="receipt-row"><span>Jumlah digit genap</span><b>{genap} digit</b></div>
    <div class="receipt-row"><span>Diskon</span><b>{persen}%</b></div>
    <div class="receipt-row"><span>Biaya normal</span><b>{rupiah(normal)}</b></div>
    <div class="receipt-row"><span>Potongan</span><b>− {rupiah(potongan)}</b></div>
    <div class="total"><span>💚 Total bayar</span><strong>{rupiah(total)}</strong></div></div>''', unsafe_allow_html=True)

st.markdown('<div class="footnote">✨ LaundryKu · Praktis, cepat, dan hemat ✨</div>', unsafe_allow_html=True)
