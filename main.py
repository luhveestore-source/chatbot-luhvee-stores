# --- ASSISTENTE LUHVEE STORES ---

# 1. Definimos o que o bot faz
def iniciar_chatbot_luhvee():
    link_oficial = "https://luhveestore-unbgvh5h.manus.space"
    
    print("\n" + "="*45)
    print("      🛍️  BEM-VINDO À LUHVEE STORES  🛍️      ")
    print("="*45)
    
    nome = input("\nOlá! Como posso te chamar? ")
    
    print(f"\n[LuhVee]: Prazer em te atender, {nome}!")
    print(f"👉 ACESSE NOSSA VITRINE AQUI: {link_oficial}")
    
    print("\nDigite 1 para ver o link de novo ou 2 para sair.")

    while True:
        escolha = input("\nOpção: ")
        if escolha == "1":
            print(f"\nLink: {link_oficial}")
        elif escolha == "2":
            print(f"\nAté logo, {nome}!")
            break
        else:
            print("Escolha 1 ou 2.")

# 2. MANDAMOS O BOT RODAR DIRETAMENTE (Sem códigos complexos)
iniciar_chatbot_luhvee()
