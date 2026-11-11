import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="Estrelas da Casa", page_icon="⭐", layout="wide")

# Inicialização do Placar com 25 estrelas fixas para cada jogador
if "jogadores" not in st.session_state:
    st.session_state.jogadores = {
        "TAILAN": {"estrelas": 25, "escudos": 0, "fantasmas": 0, "chefes": 0, "coringas": 0},
        "CAROL": {"estrelas": 25, "escudos": 0, "fantasmas": 0, "chefes": 0, "coringas": 0},
        "KARINE": {"estrelas": 25, "escudos": 0, "fantasmas": 0, "chefes": 0, "coringas": 0},
        "CAIO": {"estrelas": 25, "escudos": 0, "fantasmas": 0, "chefes": 0, "coringas": 0}
    }

# Controle de tarefas concluídas no dia atual para não pontuar duas vezes
if "tarefas_concluidas_hoje" not in st.session_state:
    st.session_state.tarefas_concluidas_hoje = []

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

# --- BLOCO DE REGRAS FIXO NO TOPO DO APP ---
with st.expander("📜 CLIQUE AQUI PARA VER AS REGRAS OFICIAIS DO JOGO", expanded=True):
    st.markdown("""
    * **Cartões:** 1 card = 1 tarefa só.
    * **Funcionamento:** Dado é todo dia. Após concluir a tarefa, marque na escala para atualizar o Ranking Geral.
    * **Sequência de Turnos:** TAILAN ➔ CAROL ➔ KARINE ➔ CAIO.
    * **Prêmio Final:** No fim de ano, quem tiver mais estrelas ganha **R$ 150,00**.
    
    ### 🎲 Efeitos do Dado Diário
    * **Dado 1:** Perde 1 estrela. | **Dado 2:** Nada acontece. | **Dado 3:** Ganha +1 estrela.
    * **Dado 4:** Ganha **🛡️ ESCUDO** (Não perde estrela por 1 tarefa não feita).
    * **Dado 5:** Ganha **👻 FANTASMA** (Faz 1 tarefa sumir).
    * **Dado 6:** Ganha **👑 CHEFE** (Manda outra pessoa fazer 1 tarefa sua).
    * **🃏 CORINGA:** Vira Fantasma, Escudo ou Chefe (Não vira Sorte).
    
    ### 🔓 Desbloqueio por Metas de Estrelas
    * **35 estrelas:** 👻 FANTASMA | **45 estrelas:** 🛡️ ESCUDO | **55 estrelas:** 👑 CHEFE | **65 estrelas:** 🃏 CORINGA
    """)

st.write("---")

# Identificação rápida do participante
st.sidebar.header("👤 Quem está mexendo?")
jogador_atual = st.sidebar.selectbox("Escolha seu nome:", ["Selecione...", "TAILAN", "CAROL", "KARINE", "CAIO"])

# Abas principais
aba_escala, aba_ranking, aba_dados = st.tabs([
    "📅 Marcar Tarefas", "🏆 Ranking Geral", "🎲 Dado Diário"
])

# --- ABA 1: MARCAR TAREFAS ---
with aba_escala:
    st.header("📅 Escala de Tarefas do Dia")
    
    col1, col2 = st.columns(2)
    with col1:
        semana_sel = st.radio("Selecione a Semana:", ["Semana 1", "Semana 2"], horizontal=True)
    with col2:
        dia_sel = st.selectbox("Selecione o Dia:", ["QUA", "QUI", "SEX", "SÁB", "DOM", "SEG", "TER"])
        
    escala_ativa = escala_semana1 if semana_sel == "Semana 1" else escala_semana2
    
    st.subheader("📋 Suas Obrigações do Dia")
    if jogador_atual == "Selecione...":
        st.warning("👉 Por favor, selecione seu nome na barra lateral esquerda para conseguir pontuar!")
    else:
        st.write(f"Olá **{jogador_atual}**, abaixo estão as suas tarefas escaladas para hoje:")
        
        alguma_tarefa = False
        for tarefa, dias in escala_ativa.items():
            responsavel = dias[dia_sel]
            
            if responsavel == jogador_atual:
                alguma_tarefa = True
                chave_tarefa = f"{semana_sel}_{dia_sel}_{tarefa}_{jogador_atual}"
                
                col_txt, col_btn = st.columns([3, 1])
                with col_txt:
                    st.markdown(f"### ✨ {tarefa}")
                with col_btn:
                    if chave_tarefa in st.session_state.tarefas_concluidas_hoje:
                        st.success("✅ Concluída! (+1 ⭐)")
                    else:
                        if st.button("Concluí! ⭐", key=chave_tarefa):
                            st.session_state.jogadores[jogador_atual]["estrelas"] += 1
                            st.session_state.tarefas_concluidas_hoje.append(chave_tarefa)
                            st.toast(f"Parabéns! +1 estrela adicionada para {jogador_atual}!", icon="⭐")
                            st.rerun()
                            
        if not alguma_tarefa:
            st.info("Você não tem nenhuma tarefa escalada para esse dia!")

    st.write("---")
    st.subheader("👀 Olhar Escala Completa")
    lista_completa = [{"Tarefa": t, "Responsável": d[dia_sel]} for t, d in escala_ativa.items()]
    st.table(pd.DataFrame(lista_completa))

# --- ABA 2: RANKING GERAL ---
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
            "Jogador": jog, 
            "Estrelas ⭐": infos["estrelas"],
            "Poderes Liberados 🔓": ", ".join(poderes) if poderes else "Nenhum",
            "🛡️ Escudos": infos["escudos"], 
            "👻 Fantasmas": infos["fantasmas"], 
            "👑 Chefes": infos["chefes"]
        })
    st.table(pd.DataFrame(dados_tabela).sort_values(by="Estrelas ⭐", ascending=False))

# --- ABA 3: DADO DIÁRIO ---
with aba_dados:
    st.header("🎲 Rodar o Dado Diário")
    if jogador_atual == "Selecione...":
        st.warning("👉 Selecione seu nome na barra lateral para poder rodar o dado.")
    else:
        st.write(f"Rolando dado para o usuário ativo: **{jogador_atual}**")
        if st.button("🎲 Lançar Meu Dado"):
            num = random.randint(1, 6)
            st.subheader(f"Resultado do Dado: {num}")
            if num == 1: 
                st.session_state.jogadores[jogador_atual]["estrelas"] -= 1
                st.error("Perdeu 1 estrela!")
            elif num == 3: 
                st.session_state.jogadores[jogador_atual]["estrelas"] += 1
                st.success("Ganhou +1 estrela!")
            elif num == 4: st.session_state.jogadores[jogador_atual]["escudos"] += 1
            elif num == 5: st.session_state.jogadores[jogador_atual]["fantasmas"] += 1
            elif num == 6: st.session_state.jogadores[job_atual]["chefes"] += 1
            st.rerun()
