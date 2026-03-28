# --- DOCUMENTAÇÃO DO SEGMENTO ---
# Projeto: Chatbot LuhVee Stores
# Versão: 2.0
# Objetivo: Assistente de vendas para afiliados.

def exibir_menu():
    print("\n" + "="*30)
    print("      LUHVEE STORES      ")
    print("="*30)
    print("1. Promoções Mercado Livre")
    print("2. Ofertas Relâmpago Shopee")
    print("3. Produtos Digitais (Digistore24)")
    print("4. Falar com Atendimento Humano")
    print("5. Sair")
    print("="*30)

def chatbot():
    nome_cliente = input("Olá! Bem-vindo à LuhVee Stores. Como posso te chamar? ")
    print(f"\nPrazer em te conhecer, {nome_cliente}! Eu sou o seu assistente virtual.")
    
    while True:
        exibir_menu()
        opcao = input(f"{nome_cliente}, digite o número da opção desejada: ")

        if opcao == "1":
            print("\n[LuhVee]: Aqui estão os achadinhos do Mercado Livre: [LINK AQUI]")
        elif opcao == "2":
            print("\n[LuhVee]: Aproveite os cupons da Shopee: [LINK AQUI]")
        elif opcao == "3":
            print("\n[LuhVee]: Confira nossos treinamentos na Digistore24: [LINK AQUI]")
        elif opcao == "4":
            print("\n[LuhVee]: Um momento! Vou te passar o contato do nosso WhatsApp.")
        elif opcao == "5":
            print(f"\nAté logo, {nome_cliente}! A LuhVee Stores agradece a preferência.")
            break
        else:
            print("\n[Erro]: Ops! Essa opção não existe. Tente de 1 a 5.")

if _name_ == "_main_":
    chatbot()
