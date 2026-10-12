import random

import streamlit as st

from preguntas import PREGUNTAS, TEMAS

st.set_page_config(page_title="Test · Entornos de Desarrollo", page_icon="🧪", layout="centered")

st.title("🧪 Test de Entornos de Desarrollo")
st.caption("DAW 1.º · 3 alternativas por pregunta · basado en el material de clase")

# ---------- Configuración ----------
with st.sidebar:
    st.header("Configuración")
    temas = st.multiselect("Temas", TEMAS, default=TEMAS)
    pool = [p for p in PREGUNTAS if p["tema"] in temas]
    if not pool:
        st.warning("Elige al menos un tema.")
        st.stop()
    n = st.number_input("Número de preguntas", min_value=1, max_value=len(pool), value=min(20, len(pool)), step=1)
    barajar = st.checkbox("Barajar las preguntas", value=True)
    st.caption(f"Banco disponible: {len(pool)} preguntas")


def nuevo_test():
    seleccion = random.sample(pool, int(n)) if barajar else pool[: int(n)]
    test = []
    for p in seleccion:
        opciones = p["opciones"][:]
        random.shuffle(opciones)
        test.append({**p, "opciones": opciones})
    st.session_state.test = test
    st.session_state.corregido = False
    st.session_state.respuestas = []
    st.session_state.version = st.session_state.get("version", 0) + 1


with st.sidebar:
    st.button("🔄 Nuevo test", on_click=nuevo_test, use_container_width=True)

if "test" not in st.session_state:
    nuevo_test()

test = st.session_state.test
ver = st.session_state.version

# ---------- Test ----------
if not st.session_state.corregido:
    with st.form("form_test"):
        for i, p in enumerate(test):
            st.markdown(f"**{i + 1}. {p['pregunta']}**")
            st.caption(p["tema"])
            st.radio("Respuesta", p["opciones"], index=None, key=f"q{ver}_{i}", label_visibility="collapsed")
            st.divider()
        enviado = st.form_submit_button("✅ Corregir", use_container_width=True)
    if enviado:
        st.session_state.respuestas = [st.session_state.get(f"q{ver}_{i}") for i in range(len(test))]
        st.session_state.corregido = True
        st.rerun()

# ---------- Resultados ----------
else:
    respuestas = st.session_state.respuestas
    aciertos = sum(1 for p, r in zip(test, respuestas) if r == p["correcta"])
    sin_responder = sum(1 for r in respuestas if r is None)
    total = len(test)
    nota = round(aciertos / total * 10, 2)

    c1, c2, c3 = st.columns(3)
    c1.metric("Aciertos", f"{aciertos}/{total}")
    c2.metric("Nota", f"{nota}/10")
    c3.metric("Sin responder", sin_responder)
    if aciertos == total:
        st.balloons()
    st.button("🔄 Hacer otro test", on_click=nuevo_test, use_container_width=True)
    st.subheader("Revisión")

    for i, (p, r) in enumerate(zip(test, respuestas)):
        ok = r == p["correcta"]
        with st.expander(f"{'✅' if ok else '❌'} {i + 1}. {p['pregunta']}", expanded=not ok):
            st.markdown(f"**Tu respuesta:** {r if r else '_Sin responder_'}")
            if not ok:
                st.markdown(f"**Respuesta correcta:** {p['correcta']}")
            if p["explicacion"]:
                st.info(p["explicacion"])
