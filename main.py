# --- DOCUMENTAÇÃO DO PROJETO ---
# Projeto: Assistente Digital LuhVee Stores
# Objetivo: Direcionar clientes para a vitrine de afiliados.

def iniciar_chatbot_luhvee():
    # Esta variável guarda o seu link oficial
    link_oficial = "https://luhveestore-unbgvh5h.manus.space"
    
    print("\n" + "="*45)
    print("      🛍️  BEM-VINDO À LUHVEE STORES  🛍️      ")
    print("="*45)
    
    nome = input("\nOlá! Como posso te chamar? ")
    
    print(f"\n[LuhVee]: Prazer em te atender, {nome}!")
    print(f"[LuhVee]: Preparamos uma seleção incrível de produtos do")
    print("         Mercado Livre, Shopee e Digistore24 para você.")
    
    print("\n" + "-"*45)
    print(f"👉 ACESSE NOSSA VITRINE AQUI:")
    print(f"🔗 {link_oficial}")
    print("-" * 45)
    
    print(f"\n{nome}, basta clicar no link azul acima para ver as ofertas!")
    print("\nDeseja algo mais?")
    print("1. Ver o link novamente")
    print("2. Encerrar atendimento")

    while True:
        escolha = input("\nDigite o número da sua opção: ")
        
        if escolha == "1":
            print(f"\n[LuhVee]: Aqui está o seu acesso exclusivo: {link_oficial}")
        elif escolha == "2":
            print(f"\n[LuhVee]: Boas compras, {nome}! A LuhVee Stores agradece.")
            break
        else:
            print("[Aviso]: Por favor, escolha a opção 1 ou 2.")

if _name_ == "_main_":
    iniciar_chatbot_luhvee()
