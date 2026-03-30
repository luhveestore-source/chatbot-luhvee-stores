import streamlit as st

# Configuração da página
st.set_page_config(page_title="Robô Luana - Central de Marketing", page_icon="🛍️", layout="wide")

st.title("🤖 Robô Luana: Sua Agência de Vendas (Versão Pro)")
st.markdown("---")

# Menu Lateral para Organização
with st.sidebar:
    st.header("⚙️ Configurações")
    nicho = st.selectbox("Escolha o Nicho:", 
                        ["Cozinha e Casa", "Limpeza Prática", "Moda", "Beleza", "Achadinhos Shopee/ML", "Eletrônicos"])
    canal = st.multiselect("Gerar para quais redes?", 
                          ["Instagram", "WhatsApp/Telegram", "Facebook", "ManyChat (DM)"],
                          default=["Instagram", "ManyChat (DM)"])
    
    st.markdown("---")
    st.subheader("🖼️ Mídia do Produto")
    foto_upload = st.file_uploader("Carregar foto do produto (Opcional):", type=["jpg", "png", "jpeg"])

# Entrada de Dados
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Detalhes do Produto")
    nome_produto = st.text_input("Nome do Produto (ex: Mop de Limpeza):")
    link_produto = st.text_input("Cole o Link de Afiliado aqui:")
    
    botao_gerar = st.button("🚀 GERAR PACOTE DE VENDAS")

with col2:
    if foto_upload is not None:
        st.subheader("👀 Prévia do Produto")
        st.image(foto_upload, use_container_width=True, caption=nome_produto)
    else:
        st.info("💡 Carregue uma foto na barra lateral para ver a prévia aqui!")

# Geração de Conteúdo
if botao_gerar:
    if nome_produto and link_produto:
        st.success("Scripts gerados com sucesso! Copie abaixo:")
        
        # --- INSTAGRAM ---
        if "Instagram" in canal:
            with st.expander("📸 LEGENDA PARA INSTAGRAM", expanded=True):
                legenda = f"🤩 **ACHADINHO QUE VOCÊ PRECISA!**\n\nSério, esse(a) {nome_produto} mudou minha rotina! ✨ Ideal para quem busca praticidade e qualidade no dia a dia. \n\n🛍️ **QUER O LINK COM DESCONTO?**\nComente **INFO** que eu te mando agora mesmo no seu Direct! 🚀\n\n#achadinhos #shopee #mercadolivre #luhveestore #{nicho.replace(' ', '')}"
                st.code(legenda, language=None)
                st.caption("Dica: Use um vídeo de demonstração para aumentar as vendas.")

        # --- WHATSAPP ---
        if "WhatsApp/Telegram" in canal:
            with st.expander("📲 SCRIPT PARA WHATSAPP/TELEGRAM"):
                zap = f"🔥 *OFERTA IMPERDÍVEL!* \n\nAcabei de encontrar o {nome_produto} com o melhor preço do mercado! 😱\n\nConfira aqui antes que acabe: {link_produto}\n\n_Siga a LuVee para mais achados!_"
                st.code(zap, language=None)

        # --- MANYCHAT ---
        if "ManyChat (DM)" in canal:
            with st.expander("🤖 MENSAGEM PARA O MANYCHAT (DM)", expanded=True):
                dm = f"Olá! ✨ Fico feliz com seu interesse no(a) {nome_produto}! \n\nAqui está o seu link exclusivo para compra: {link_produto} \n\nQualquer dúvida é só me chamar! 😊"
                st.code(dm, language=None)
                st.info("Cole esse texto na sua automação de 'Palavra-Chave' do ManyChat.")
                
    else:
        st.error("⚠️ Por favor, preencha o Nome e o Link do produto para continuar!")

st.markdown("---")
