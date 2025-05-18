# Calculator - Aplicativo de Calculadora com Histórico

Este é um projeto de **calculadora com interface gráfica (GUI)** desenvolvido em **Python** utilizando a biblioteca `customtkinter`. O aplicativo permite realizar operações matemáticas básicas, visualizar o histórico de cálculos e manter um design moderno e responsivo. Este projeto foi criado com foco em praticar conceitos de **GUI**, organização de código, manipulação de arquivos e boas práticas de desenvolvimento em **Python**.

---

## Funcionalidades

- Operações básicas: adição, subtração, multiplicação, divisão e módulo (`%`)
- Interface gráfica customizada com `customtkinter`
- Histórico de cálculos persistente em arquivo `.csv`
- Reutilização de operações passadas com um clique
- Limpeza do histórico com botão dedicado
- Layout adaptado e amigável ao usuário

---

## Estrutura do Projeto

```
Calculator/
│
├── history/
│ └── history.csv     # Armazena o histórico de operações
│
├── images/           # Ícones e imagens usados na GUI
│
├── constants.py      # Constantes visuais e de layout
├── gui.py            # Interface gráfica principal
├── history.py        # Lógica de manipulação do histórico (salvar, exibir, limpar)
├── logic.py          # Lógica das operações matemáticas
├── main.py           # Arquivo de entrada da aplicação

```


---

## Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/emilyfas/calculator.git
cd calculator
```

### 2. Instale as dependências
Este projeto requer as seguintes bibliotecas:

- CustomTkinter
- Pillow
- Sympy

Você pode instalar todas com:

```
pip install -r requirements.txt
```

### 3. Execute a aplicação

```
python main.py
```

---

## Detalhes Técnicos
`gui.py`

Responsável por iniciar e organizar todos os elementos gráficos, como:

- Campo de entrada/display
- Botões numéricos e operadores
- Janela de histórico com scroll
- Ícones personalizados
- Eventos de clique e teclado

`logic.py`
Controla toda a lógica matemática e tratamento de entrada, incluindo:

- Validação de operadores
- Construção da expressão
- Simplificação e cálculo usando sympy
- Formatação e normalização de resultados com Decimal
- Restauração de entradas a partir do histórico

`history.py`
Gerencia o histórico das operações realizadas:

- Salva cada operação no history.csv
- Lê e exibe as operações anteriores
- Limpa o histórico
- Permite restaurar uma operação clicando nela

`constants.py`
Centraliza valores fixos usados no projeto como:

- Cores da interface
- Dimensões dos botões e janela
- Caminhos para os arquivos de imagem
- Operadores permitidos

---

## Interface da Aplicação

A calculadora possui um tema escuro e botões estilizados para melhor visualização.   
Os ícones utilizados estão na pasta `images/`.

### Imagens de Referência:
TODO: Adicionar capturas de tela 


<img src="https://github.com/user-attachments/assets/8deb1b2c-2c71-4f4b-97a0-4f1429b27773" width="260"/>

<img src="https://github.com/user-attachments/assets/7f2ccd54-7638-482e-8e17-1d139b02b57f" width="220"/>

<img src="https://github.com/user-attachments/assets/160d9208-298f-4b08-9511-8f4401e764fc" width="260"/>

<img src="https://github.com/user-attachments/assets/234a5f9b-f717-47cf-acd4-7858664f1aa5" width="220"/>

---

## Tecnologias Utilizadas
- **Python 3.12**

- [CustomTkinter](https://customtkinter.tomschimansky.com/) — para interface gráfica moderna

- **Pillow** — para exibir ícones na GUI

- **Sympy** — para manipulação segura de expressões matemáticas

- **CSV** — para salvar e recuperar histórico de operações

---

## Exemplo de Operação

**1.** Digite uma expressão (ex: `5 + 7`)     

**2.** Clique em `=`    

**3.** O resultado aparecerá no display    

**4.** A operação será salva automaticamente no histórico   

**5.** Clique em `History` para visualizar ou restaurar   

---

## Histórico
O histórico é armazenado no arquivo `calculator/history/history.csv` com o seguinte formato:

```
Operação,Resultado
5+7,12
3*4,12
```
Ele é automaticamente limpo ao fechar o app ou manualmente clicando no botão de lixeira dentro da janela de histórico.

---

## Autora  
**Emilly Fernandes**   
Estudante de Ciência da Computação   
Projeto desenvolvido para portfólio pessoal.   
[LinkedIn](https://www.linkedin.com/in/emilly-fernandes) | [Portfólio](https://emilyfas.github.io/meu-portfolio/)

## Dê uma estrela!
Se você gostou deste projeto, deixe uma ⭐ no repositório para ajudar na visibilidade!
