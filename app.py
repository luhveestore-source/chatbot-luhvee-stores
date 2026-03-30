
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Robô Luana - Central de Marketing", page_icon="🛍️")

st.title("🤖 Robô Luana: Sua Agência de Vendas")
st.markdown("---")

# Menu Lateral para Organização
with st.sidebar:
    st.header("Configurações")
    nicho = st.selectbox("Escolha o Nicho do Produto:", 
                        ["Cozinha e Casa", "Limpeza Prática", "Moda", "Beleza", "Achadinhos Shopee/ML", "Eletrônicos"])
    canal = st.multiselect("Gerar para quais redes?", 
                          ["Instagram", "WhatsApp/Telegram", "Facebook", "ManyChat (DM)"],
                          default=["Instagram", "ManyChat (DM)"])

# Entrada de Dados
st.subheader("📝 Detalhes do Produto")
nome_produto = st.text_input("Nome do Produto (ex: Mop de Limpeza):")
link_produto = st.text_input("Cole o Link do Produto aqui:")

if st.button("🚀 GERAR SCRIPTS DE VENDA"):
    if nome_produto and link_produto:
        st.markdown("---")
        
        # Lógica de Geração de Conteúdo (Exemplo para Instagram)
        if "Instagram" in canal:
            st.subheader("📸 Para Instagram (Reels/Feed)")
            legenda = f"""🤩 **ACHADINHO QUE VOCÊ PRECISA!**
            
Sério, esse(a) {nome_produto} mudou minha rotina! ✨ Ideal para quem busca praticidade e qualidade no dia a dia. 

🛍️ **QUER O LINK COM DESCONTO?**
Comente **INFO** que eu te mando agora mesmo no seu Direct! 🚀

#achadinhos #shopee #mercadolivre #luhveestore #{nicho.replace(' ', '')}"""
            st.text_area("Copie a Legenda:", legenda, height=200)

        # Lógica para WhatsApp
        if "WhatsApp/Telegram" in canal:
            st.subheader("📲 Para Grupos (WhatsApp/Telegram)")
            zap = f"🔥 *OFERTA IMPERDÍVEL!* \n\nAcabei de encontrar o {nome_produto} com o melhor preço do mercado! 😱\n\nConfira aqui antes que acabe: {link_produto}\n\n_Siga a LuVee para mais achados!_"
            st.text_area("Copie para o Zap:", zap, height=120)

        # Lógica para ManyChat
        if "ManyChat (DM)" in canal:
            st.subheader("🤖 Para o ManyChat (Automação)")
            dm = f"Olá! ✨ Fico feliz com seu interesse no(a) {nome_produto}! \n\nAqui está o seu link exclusivo para compra: {link_produto} \n\nQualquer dúvida é só me chamar! 😊"
            st.text_area("Copie para a DM do ManyChat:", dm, height=120)
            
    else:
        st.error("Por favor, preencha o nome e o link do produto!")

st.markdown("---")
st.info("Dica: Use sempre o link das suas Coleções se quiser centralizar, ou o link direto para vendas rápidas!")
