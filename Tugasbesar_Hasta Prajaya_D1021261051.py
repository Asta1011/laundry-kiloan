import streamlit as st

st.set_page_config(page_title="LaundryKu | Kalkulator Laundry", page_icon="🧺", layout="centered", initial_sidebar_state="collapsed")

st.markdown('''<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');
html,body,[class*="css"],[data-testid="stApp"]{font-family:'Nunito',sans-serif!important}
[data-testid="stAppViewContainer"]{background:linear-gradient(180deg,#0076c8 0%,#008fd4 30%,#04b8db 65%,#48d5d6 100%);min-height:100vh}
[data-testid="stAppViewContainer"]:before{content:"";position:fixed;inset:0;pointer-events:none;background:radial-gradient(ellipse at 22% 0%,#baf8ff50,transparent 50%),repeating-linear-gradient(110deg,transparent 0 100px,#ffffff09 110px 130px,transparent 145px 220px);z-index:0}
.block-container{position:relative;z-index:2;max-width:680px;padding:1.15rem 1rem 3rem}
#MainMenu,footer,header{visibility:hidden}
/* Decorative underwater bubbles float upward independently of Streamlit reruns. */
.bubble-field{position:fixed;inset:0;overflow:hidden;pointer-events:none;z-index:1}
.bubble{position:absolute;bottom:-90px;width:var(--size);height:var(--size);left:var(--left);border:2px solid #e7ffff80;border-radius:50%;background:radial-gradient(circle at 32% 25%,#ffffffad 0 8%,#a4f8ff3b 17%,#8cddff12 58%,#ffffff35 100%);box-shadow:inset -3px -4px 8px #d6ffff36,0 0 12px #e5ffff2e;animation:rise var(--duration) linear infinite;animation-delay:var(--delay)}
@keyframes rise{0%{transform:translate3d(0,0,0) scale(.7);opacity:0}10%{opacity:.75}80%{opacity:.7}100%{transform:translate3d(var(--drift),-115vh,0) scale(1.2);opacity:0}}
.hero{position:relative;overflow:hidden;background:linear-gradient(125deg,#063b92e8,#006ac1d9);padding:25px 20px;border-radius:26px;color:white;border:1px solid #d6faff75;box-shadow:0 16px 30px #003f7945;margin-bottom:19px}
.hero:before{content:"";position:absolute;width:170px;height:170px;border-radius:50%;background:#d5ffff14;right:-50px;top:-60px}
.hero .eyebrow{font-size:11px;letter-spacing:1.6px;font-weight:900;color:#aef8ff}
.hero h1{color:white;font-size:clamp(29px,7vw,41px);line-height:1.1;margin:12px 0;font-weight:900}
.hero p{color:#dffaff;font-size:14px;margin:0;max-width:390px}
.ocean-scene{height:118px;position:relative;margin-top:10px;border-bottom:4px dotted #baf6e6aa}
.sponge{position:absolute;right:18%;bottom:4px;width:76px;height:86px;border-radius:14px 16px 12px 12px;background:#ffdf3d;border:3px solid #b88e00;box-shadow:inset -8px -5px #f5b824;transform:rotate(-5deg);animation:bob 3.2s ease-in-out infinite}
.sponge:before{content:"";position:absolute;left:13px;top:20px;width:13px;height:17px;background:white;border:3px solid #173f65;border-radius:50%;box-shadow:24px 0 0 -1px white,24px 0 0 2px #173f65}
.sponge:after{content:"◡";position:absolute;left:26px;top:36px;font-size:30px;color:#744523;font-weight:900}
.sponge .holes{position:absolute;left:7px;top:8px;color:#c49b08;font-size:10px;letter-spacing:19px}
.sponge .shirt{position:absolute;bottom:0;left:0;right:0;height:19px;background:linear-gradient(#fff 0 55%,#a86d44 55%);border-radius:0 0 8px 8px}
.sponge .tie{position:absolute;bottom:6px;left:34px;width:7px;height:14px;background:#e84c48;clip-path:polygon(50% 0,100% 35%,75% 100%,25% 100%,0 35%)}
@keyframes bob{0%,100%{transform:translateY(0) rotate(-5deg)}50%{transform:translateY(-9px) rotate(2deg)}}
.jelly{position:absolute;left:12%;bottom:22px;font-size:47px;animation:swim 5s ease-in-out infinite}
@keyframes swim{50%{transform:translate(25px,-18px) rotate(12deg)}}
.seaweed{position:absolute;bottom:0;left:4%;font-size:38px}
.section-heading{font-weight:900;color:#fff;font-size:19px;margin:12px 0 5px;text-shadow:0 2px 5px #005d88}
.small-note{font-size:13px;color:#e7ffff;margin:0 0 12px}
[data-testid="stForm"]{border:1px solid #ffffffb0;background:#f4fffff2;border-radius:22px;padding:18px 18px 13px;box-shadow:0 10px 26px #004d8750}
label{font-weight:800!important;color:#114771!important}
.stButton button,[data-testid="stFormSubmitButton"] button{border-radius:13px!important;min-height:47px;font-weight:900!important}
[data-testid="stFormSubmitButton"] button{background:linear-gradient(100deg,#007cc7,#00b8c5)!important;color:white!important;border:0!important}
.result{background:#f5fffff5;border:1px solid #d2ffff;border-radius:23px;padding:22px;margin-top:18px;box-shadow:0 8px 24px #004d8740;animation:appear .4s ease-out}
@keyframes appear{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.result h3{margin:0 0 4px;color:#064d78;font-size:20px}
.result .muted{color:#527e94;font-size:12px;margin-bottom:17px}
.receipt-row{display:flex;justify-content:space-between;gap:12px;padding:10px 0;border-bottom:1px dashed #b4e2ea;color:#3d687e;font-size:14px}
.receipt-row b{color:#07496b;text-align:right}
.total{background:linear-gradient(110deg,#c9fff2,#b7f3da);border-radius:16px;padding:17px;margin-top:16px;display:flex;justify-content:space-between;align-items:center;color:#09634c;font-weight:900;gap:8px}
.total strong{font-size:clamp(20px,6vw,28px)}
.footnote{text-align:center;color:white;font-size:12px;margin-top:23px;text-shadow:0 1px 3px #005a83}
@media(max-width:480px){.block-container{padding:.8rem .8rem 2rem}.hero{padding:22px 17px;border-radius:20px}[data-testid="stForm"]{padding:13px}.result{padding:17px}.receipt-row{font-size:13px}}
@media(prefers-reduced-motion:reduce){.bubble,.sponge,.jelly{animation:none!important}}
</style>''', unsafe_allow_html=True)

# Background and decorations stay behind the Streamlit inputs, so controls remain clickable.
import random
random.seed(42)
bubbles = ''.join(
    f'<span class="bubble" style="--left:{random.randint(2,97)}%;--size:{random.randint(13,55)}px;--duration:{random.randint(9,19)}s;--delay:-{random.randint(0,20)}s;--drift:{random.randint(-75,75)}px"></span>'
    for _ in range(25)
)
st.markdown(f'<div class="bubble-field" aria-hidden="true">{bubbles}</div>', unsafe_allow_html=True)

def rupiah(n):
    return 'Rp ' + f'{n:,}'.replace(',', '.')

if 'hasil' not in st.session_state:
    st.session_state.hasil = None
if 'nim_input' not in st.session_state:
    st.session_state.nim_input = ''
if 'berat_input' not in st.session_state:
    st.session_state.berat_input = ''

st.markdown('''<div class="hero"><div class="eyebrow">🫧 LAUNDRYKU • UNDERWATER EDITION</div><h1>🌊 Laundry di<br>dasar laut!</h1><p>Hitung biaya cucian sambil ditemani gelembung laut dan si spons kuning ceria 🧽</p><div class="ocean-scene" aria-hidden="true"><span class="seaweed">🌿</span><span class="jelly">🪼</span><div class="sponge"><span class="holes">● ●</span><span class="shirt"></span><span class="tie"></span></div></div></div>''', unsafe_allow_html=True)
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
