import customtkinter as ctk

# Configuração global do tema visual
ctk.set_appearance_mode("dark")

class SaborExpressGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("Sabor Express - Cadastros de Restaurantes")
        self.geometry("950x550")
        self.resizable(False, False)

        #lista de restaurantes
        self.restaurantes = []

        # Paleta de cores para os botões e detalhes visuais
        self.cor_destaque = "#DA390D"
        self.cor_botao_hover = "#822D09"

        # --- ESTRUTURA DE LAYOUT (Duas Colunas) ---
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Coluna Esquerda: Formulários de Cadastro e Status
        self.frame_esquerda = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_esquerda.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Título do Programa
        self.label_titulo = ctk.CTkLabel(
            self.frame_esquerda, 
            text="Sabor Express", 
            font=("Helvetica", 28, "bold"),
            text_color=self.cor_destaque
        )
        self.label_titulo.pack(pady=(10, 20))

        # --- SEÇÃO 1: CADASTRAR RESTAURANTE ---
        self.label_cadastro = ctk.CTkLabel(self.frame_esquerda, text="Cadastrar Novo Restaurante", font=("Helvetica", 14, "bold"))
        self.label_cadastro.pack(anchor="w", padx=15, pady=(5, 2))

        self.input_nome = ctk.CTkEntry(self.frame_esquerda, placeholder_text="Nome do Restaurante", width=260)
        self.input_nome.pack(pady=5)

        self.input_categoria = ctk.CTkEntry(self.frame_esquerda, placeholder_text="Categoria", width=260)
        self.input_categoria.pack(pady=5)

        self.btn_cadastrar = ctk.CTkButton(
            self.frame_esquerda, 
            text="Cadastrar", 
            fg_color=self.cor_destaque,
            hover_color=self.cor_botao_hover,
            text_color="#000000",
            font=("Helvetica", 12, "bold"),
            command=self.cadastrar_novo_restaurante
        )
        self.btn_cadastrar.pack(pady=(5, 20))

        # --- SEÇÃO 2: ALTERNAR STATUS ---
        self.label_status = ctk.CTkLabel(self.frame_esquerda, text="Alternar Status (Ativar/Desativar)", font=("Helvetica", 14, "bold"))
        self.label_status.pack(anchor="w", padx=15, pady=(5, 2))

        self.input_status_nome = ctk.CTkEntry(self.frame_esquerda, placeholder_text="Digite o nome exato do restaurante", width=260)
        self.input_status_nome.pack(pady=5)

        self.btn_status = ctk.CTkButton(
            self.frame_esquerda, 
            text="Alternar Estado", 
            fg_color=self.cor_destaque,
            hover_color=self.cor_botao_hover,
            text_color="#000000",
            font=("Helvetica", 12, "bold"),
            command=self.status_restaurante
        )
        self.btn_status.pack(pady=5)

        # Label para exibir mensagens de sucesso ou erro (Tratamento de Erros Visual)
        self.label_feedback = ctk.CTkLabel(self.frame_esquerda, text="", font=("Helvetica", 12, "italic"))
        self.label_feedback.pack(pady=15)

        # Coluna Direita: Painel de Exibição da Lista
        self.frame_direita = ctk.CTkFrame(self)
        self.frame_direita.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.label_lista_titulo = ctk.CTkLabel(self.frame_direita, text="Restaurantes Cadastrados", font=("Helvetica", 16, "bold"))
        self.label_lista_titulo.pack(pady=10)

        # Caixa de texto onde as informações serão "printadas" na tela
        self.caixa_lista = ctk.CTkTextbox(self.frame_direita, width=450, height=380, font=("Courier New", 14))
        self.caixa_lista.pack(padx=15, pady=10, fill="both", expand=True)

        # Executa a listagem inicial assim que o programa abre
        self.listar_restaurantes()


    def cadastrar_novo_restaurante(self):
        # Captura o texto digitado nos campos
        nome = self.input_nome.get().strip()
        categoria = self.input_categoria.get().strip()

        # TRATAMENTO DE ERRO: Verifica se os campos estão vazios
        if not nome or not categoria:
            self.exibir_feedback("Erro: Preencha todos os campos!", "red")
            return

        dados_restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
        self.restaurantes.append(dados_restaurante)

        # Limpa as caixas de entrada de texto
        self.input_nome.delete(0, 'end')
        self.input_categoria.delete(0, 'end')

        # Atualiza a tela
        self.exibir_feedback(f"'{nome}' cadastrado com sucesso!", "green")
        self.listar_restaurantes()

    def listar_restaurantes(self):
        # Limpa a caixa de texto para não duplicar os dados antigos
        self.caixa_lista.delete("0.0", "end")

        cabecalho = f"{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(18)} | {'Status'}\n"
        linha_divisoria = "-" * 57 + "\n"
        
        self.caixa_lista.insert("end", cabecalho)
        self.caixa_lista.insert("end", linha_divisoria)

        # Varre a lista de dicionários exatamente como você fez
        for restaurante in self.restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            
            # Insere a linha formatada dentro do componente visual
            linha = f"- {nome_restaurante.ljust(18)} | {categoria.ljust(18)} | {ativo}\n"
            self.caixa_lista.insert("end", linha)

    def status_restaurante(self):
        nome_busca = self.input_status_nome.get().strip()
        restaurante_encontrado = False

        # TRATAMENTO DE ERRO: Se o usuário clicar sem digitar nada
        if not nome_busca:
            self.exibir_feedback("Erro: Digite o nome de um restaurante!", "red")
            return

        for restaurante in self.restaurantes:
            # .lower() adicionado para que encontre mesmo se digitar maiúscula/minúscula diferente
            if nome_busca.lower() == restaurante['nome'].lower():
                restaurante_encontrado = True
                
                # Inverte o booleano (mesma lógica sua)
                restaurante['ativo'] = not restaurante['ativo']
                
                status_atual = "ativado" if restaurante['ativo'] else "desativado"
                self.exibir_feedback(f"O restaurante '{restaurante['nome']}' foi {status_atual}!", self.cor_destaque)
                break

        # TRATAMENTO DE ERRO: Se rodar o loop inteiro e não achar o nome
        if not restaurante_encontrado:
            self.exibir_feedback("O restaurante não foi encontrado!", "red")

        # Limpa o campo de busca e atualiza a listagem ao lado
        self.input_status_nome.delete(0, 'end')
        self.listar_restaurantes()

    def exibir_feedback(self, mensagem, cor):
        """Função auxiliar para mostrar mensagens rápidas na tela"""
        self.label_feedback.configure(text=mensagem, text_color=cor)


if __name__ == '__main__':
    # Inicializa e roda o loop contínuo da interface gráfica
    app = SaborExpressGUI()
    app.mainloop()