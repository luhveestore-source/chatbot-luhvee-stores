
import streamlit as st

# Configuração visual do Painel
st.set_page_config(page_title="LuhVee Store Admin", page_icon="💰")

st.title("🤖 Painel de Controle: Robô Luana")
st.markdown("---")

# --- BANCO DE DADOS REAL ---
links_vendas = {
    "prodentim_en": {
        "nome": "ProDentim (USA/International) 🦷",
        "url": "http://exclusive-dental-deal.netlify.app",
        "copy": "Hi! Here is your exclusive access to ProDentim: http://exclusive-dental-deal.netlify.app"
    },
    "shopee_br": {
        "nome": "Minha Loja Shopee (Coleções) 🛍️",
        "url": "https://collshp.com/luhveestores?view=storefront",
        "copy": "Oi! Veja todos os meus achadinhos da Shopee aqui: https://collshp.com/luhveestores?view=storefront"
    },
    "mercadolivre_br": {
        "nome": "Mercado Livre (Ofertas) 📦",
        "url": "https://www.mercadolivre.com.br/social/axwelloliveira",
        "copy": "Confira as ofertas que separei no Mercado Livre: https://www.mercadolivre.com.br/social/axwelloliveira"
    },
    "hotmart_br": {
        "nome": "Hotmart (Produto VIP) ✨",
        "url": "https://go.hotmart.com/B104903884Q",
        "copy": "Aqui está o acesso ao conteúdo da Hotmart: https://go.hotmart.com/B104903884Q"
    }
}

# --- ORGANIZAÇÃO EM ABAS ---
tab_post, tab_links = st.tabs(["📲 Gerar Mensagem p/ Direct", "🔗 Gerenciar Links"])

with tab_post:
    st.subheader("Selecione o Produto para o Robô:")
    opcao = st.selectbox("Qual link deseja enviar?", list(links_vendas.keys()), format_func=lambda x: links_vendas[x]['nome'])
    
    st.write("Copia a mensagem abaixo e cola na automação do seu Instagram/WhatsApp:")
    st.code(links_vendas[opcao]['copy'])

with tab_links:
    st.subheader("Links Oficiais de Afiliada")
    for chave, info in links_vendas.items():
        with st.expander(info['nome']):
            st.write(f"**URL de Destino:** {info['url']}")
            st.button(f"Testar Link {chave}", on_click=lambda url=info['url']: st.write(f"Abrindo... {url}"))

st.sidebar.success("O Robô está ativo e sincronizado!")
