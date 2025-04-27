import streamlit as st

from datetime import datetime
from services import search_books

st.set_page_config(page_title="Meu App", layout="wide")

sidebar = st.sidebar

sidebar.markdown("## 📚 Navegação")
menus = sidebar.radio(
    "Escolha uma opção:",
    ["🏠 Início", "🔍 Buscar", "⚙️ Configurações"],
    index=0
)

if menus.startswith("🏠"):
    st.title("Bem-vindo ao Início!")
elif menus.startswith("🔍"):
    st.title("Busca Avançada")
elif menus.startswith("⚙️"):
    st.title("Configurações do Sistema")


st.title("🏫 Biblioteca Nacional ")
st.divider()

st.markdown(" ### 📚 Pesquise por livro ou conteudo ")
search = st.text_input(label="Pesquisar", placeholder="Digite seu texto aqui")

if search:
    time_start = datetime.now()
    resultados = search_books(search)
    time_end = datetime.now()
    tempo_execucao = time_end - time_start

    st.markdown('</div>', unsafe_allow_html=True)
    st.warning(body=f"Tempo total: {tempo_execucao.total_seconds()} segundos", icon='⌛')
    st.write(f"🔎 Resultados para **'{search}'**:")

    for resultado in resultados:
      st.markdown(f"""
      <div style="border: 1px solid #DDD; border-radius: 8px; padding: 15px; margin-bottom: 10px; box-shadow: 1px 1px 5px rgba(0,0,0,0.05);">
          <span style="font-size: 18px;">{resultado}</span>
      </div>
      """, unsafe_allow_html=True)

else:
    st.markdown('</div>', unsafe_allow_html=True)