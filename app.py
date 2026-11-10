import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Estrelas da Casa", page_icon="⭐", layout="wide")

if "jogadores" not in st.session_state:
    st.session_state.jogadores = {
        "TAILAN": {"estrelas": 0, "escudos": 0, "fantasmas": 0, "chefes": 0, "coringas": 0},
        "CAROL": {"estrelas": 0, "escudos": 0, "fantasmas": 0, "chefes": 0, "coringas": 0},
        "KARINE": {"estrelas": 0, "escudos": 0, "fantasmas": 0, "chefes": 0, "coringas": 0},
        "CAIO": {"estrelas": 0, "escudos": 0, "fantasmas": 0, "chefes": 0, "coringas": 0}
    }

escala_semana1 = {
    "Café manhã": {"QUA": "KARINE", "QUI": "CAIO", "SEX": "TAILAN", "SÁB": "CAROL", "DOM": "KARINE", "SEG": "CAIO", "TER": "TAILAN"},
    "Café tarde": {"QUA": "CAIO", "QUI": "CAROL", "SEX": "KARINE", "SÁB": "CAIO", "DOM": "TAILAN", "SEG": "CAROL", "TER": "KARINE"},
    "Varrer manhã": {"QUA": "KARINE", "QUI": "CAROL", "SEX": "KARINE", "SÁB": "CAIO", "DOM": "TAILAN", "SEG": "CAROL", "TER": "KARINE"},
    "Varrer tarde": {"QUA": "CAROL", "QUI": "CAIO", "SEX": "TAILAN", "SÁB": "CAROL", "DOM": "KARINE", "SEG": "CAIO", "TER": "TAILAN"},
    "Almoço": {"QUA": "CAROL", "QUI": "KARINE", "SEX": "CAROL", "SÁB": "KARINE", "DOM": "CAIO", "SEG": "CAROL", "TER": "KARINE"},
    "Janta": {"QUA": "TAILAN", "QUI": "CAROL", "SEX": "KARINE", "SÁB": "CAIO", "DOM": "TAILAN", "SEG": "CAROL", "TER": "KARINE"},
    "Fogão almoço": {"QUA": "CAROL", "QUI": "KARINE", "SEX": "CAIO", "SÁB": "TAILAN", "DOM": "CAROL", "SEG": "KARINE", "TER": "CAIO"},
    "Fogão janta": {"QUA": "KARINE", "QUI": "CAIO", "SEX": "TAILAN", "SÁB": "CAROL", "DOM": "KARINE", "SEG": "CAIO", "TER": "TAILAN"},
    "Banheiro": {"QUA": "KARINE", "QUI": "CAIO", "SEX": "TAILAN", "SÁB": "CAROL", "DOM": "KARINE", "SEG": "CAIO", "TER": "TAILAN"},
    "Garrafas": {"QUA": "CAIO", "QUI": "TAILAN", "SEX": "CAROL", "SÁB": "KARINE", "DOM": "CAIO", "SEG": "TAILAN", "TER": "CAROL"},
    "Roupa": {"QUA": "TAILAN", "QUI": "CAROL", "SEX": "KARINE", "SÁB": "CAIO", "DOM": "TAILAN", "SEG": "CAROL", "TER": "KARINE"},
    "Organizar": {"QUA": "CAROL", "QUI": "KARINE", "SEX": "CAIO", "SÁB": "TAILAN", "DOM": "CAROL", "SEG": "KARINE", "TER": "CAIO"},
    "Passar pano": {"QUA": "CAROL", "QUI": "-", "SEX": "KARINE", "SÁB": "-", "DOM": "CAIO", "SEG": "-", "TER": "TAILAN"}
}

escala_semana2 = {
    "Café manhã": {"QUA": "CAROL", "QUI": "KARINE", "SEX": "CAIO", "SÁB": "TAILAN", "DOM": "CAROL", "SEG": "KARINE", "TER": "CAIO"},
    "Café tarde": {"QUA": "CAIO", "QUI": "CAROL", "SEX": "KARINE", "SÁB": "CAIO", "DOM": "TAILAN", "SEG": "CAROL", "TER": "KARINE"},
    "Varrer manhã": {"QUA": "CAROL", "QUI": "KARINE", "SEX": "CAROL", "SÁB": "KARINE", "DOM": "CAIO", "SEG": "CAROL", "TER": "KARINE"},
    "Varrer tarde": {"QUA": "CAROL", "QUI": "CAIO", "SEX": "TAILAN", "SÁB": "CAROL", "DOM": "KARINE", "SEG": "CAIO", "TER": "TAILAN"},
    "Almoço": {"QUA": "CAROL", "QUI": "KARINE", "SEX": "CAROL", "SÁB": "KARINE", "DOM": "CAIO", "SEG": "CAROL", "TER": "KARINE"},
    "Janta": {"QUA": "CAIO", "QUI": "TAILAN", "SEX": "CAROL", "SÁB": "KARINE", "DOM": "CAIO", "SEG": "TAILAN", "TER": "CAROL"},
    "Fogão almoço": {"QUA": "CAROL", "QUI": "KARINE", "SEX": "CAIO", "SÁB": "TAILAN", "DOM": "CAROL", "SEG": "KARINE", "TER": "CAIO"},
    "Fogão janta": {"QUA": "CAROL", "QUI": "KARINE", "SEX": "CAIO", "SÁB": "TAILAN", "DOM": "CAROL", "SEG": "KARINE", "TER": "CAIO"},
    "Banheiro": {"QUA": "CAROL", "QUI": "KARINE", "SEX": "CAIO", "SÁB": "TAILAN", "DOM": "CAROL", "SEG": "KARINE", "TER": "CAIO"},
    "Garrafas": {"QUA": "KARINE", "QUI": "CAIO", "SEX": "TAILAN", "SÁB": "CAROL", "DOM": "KARINE", "SEG": "CAIO", "TER": "TAILAN"},
    "Roupa": {"QUA": "CAIO", "QUI": "TAILAN", "SEX": "CAROL", "SÁB": "KARINE", "DOM": "CAIO", "SEG": "TAILAN", "TER": "CAROL"},
    "Organizar": {"QUA": "TAILAN", "QUI": "CAROL", "SEX": "KARINE", "SÁB": "CAIO", "DOM": "TAILAN", "SEG": "CAROL", "TER": "CAIO"},
    "Passar pano": {"QUA": "-", "QUI": "CAROL", "SEX": "-", "SÁB": "KARINE", "DOM": "-", "SEG": "CAIO", "TER": "-"}
}

st.title("⭐ ESTRELAS DA CASA - CADA UM POR SI ⭐")
st.write("---")

aba_ranking, aba_escala, aba_dados, aba_regras = st.tabs([
    "🏆 Ranking Geral", "📅 Escala de Tarefas", "🎲 Dado Diário", "📜 Regras do Jogo"
])

with aba_ranking:
    st.header("🏆 Placar das Estrelas")
    dados_tabela = []
    for jog, infos in st.session_state.jogadores.items():
        poderes = []
        if infos["estrelas"] >= 35: poderes.append("👻 FANTASMA")
        if infos["estrelas"] >= 45: poderes.append("🛡️ ESCUDO")
        if infos["estrelas"] >= 55: poderes.append("👑 CHEFE")
        if infos["estrelas"] >= 65: poderes.append("🃏 CORINGA")
        
        dados_tabela.append({
            "Jogador": jog, "Estrelas ⭐": infos["estrelas"],
            "Poderes Liberados": ", ".join(poderes) if poderes else "Nenhum",
            "🛡️ Escudos": infos["escudos"], "👻 Fantasmas": infos["fantasmas"], "👑 Chefes": infos["chefes"]
        })
    st.table(pd.DataFrame(dados_tabela).sort_values(by="Estrelas ⭐", ascending=False))
    
    st.subheader("⚙️ Atualizar Estrelas")
    j_escolhido = st.selectbox("Jogador:", list(st.session_state.jogadores.keys()))
    qtd_estrelas = st.number_input("Quantidade:", value=1, step=1)
    if st.button("Confirmar"):
        st.session_state.jogadores[j_escolhido]["estrelas"] += qtd_estrelas
        st.success("Atualizado!")
        st.rerun()

with aba_escala:
    semana_sel = st.radio("Semana:", ["Semana 1", "Semana 2"], horizontal=True)
    dia_sel = st.selectbox("Dia:", ["QUA", "QUI", "SEX", "SÁB", "DOM", "SEG", "TER"])
    escala_ativa = escala_semana1 if semana_sel == "Semana 1" else escala_semana2
    lista_tarefas_dia = [{"Tarefa": t, "Responsável": d[dia_sel]} for t, d in escala_ativa.items()]
    st.table(pd.DataFrame(lista_tarefas_dia))

with aba_dados:
    j_dado = st.selectbox("Quem joga o dado?", list(st.session_state.jogadores.keys()))
    if st.button("🎲 Lançar Dado"):
        num = random.randint(1, 6)
        st.subheader(f"Resultado: {num}")
        if num == 1: st.session_state.jogadores[j_dado]["estrelas"] -= 1
        elif num == 3: st.session_state.jogadores[j_dado]["estrelas"] += 1
        elif num == 4: st.session_state.jogadores[j_dado]["escudos"] += 1
        elif num == 5: st.session_state.jogadores[j_dado]["fantasmas"] += 1
        elif num == 6: st.session_state.jogadores[j_dado]["chefes"] += 1
        st.rerun()
