# Rocket Agenda

Agenda de contatos em linha de comando, desenvolvida como desafio do **Módulo 1** do curso de Python (Rocketseat). Permite cadastrar, listar, marcar favoritos, editar e remover contatos com uma interface interativa no terminal.

## O que o projeto faz

- **Listar contatos** — exibe todos os contatos com nome, telefone, e-mail e indicação de favorito.
- **Listar favoritos** — mostra apenas contatos marcados como favoritos.
- **Adicionar contato** — inclui nome, telefone, e-mail e opção de favorito.
- **Editar contato** — altera dados existentes (campos em branco mantêm o valor anterior); também serve para marcar/desmarcar favorito.
- **Apagar contato** — remove um contato após confirmação.
- **Sair** — encerra o programa.

Os dados ficam apenas **em memória** durante a execução; ao fechar o programa, a lista de contatos é perdida.

## Requisitos

- [Python](https://www.python.org/downloads/) **3.8+** (recomendado 3.10 ou superior).
- Não há dependências externas: o projeto usa apenas a biblioteca padrão (`utils.py` usa `math`).

## Como rodar

1. Entre na pasta do projeto:

   ```bash
   cd rocketseat-python-desafio1
   ```

2. Execute o programa:

   ```bash
   python3 agenda.py
   ```

   No Windows, se `python3` não existir, tente:

   ```bash
   python agenda.py
   ```

3. No menu, digite o **número da opção** (1 a 6) e pressione **Enter**.

## Estrutura dos arquivos

| Arquivo    | Descrição                                              |
| ---------- | ------------------------------------------------------ |
| `agenda.py` | Menu principal, lógica da agenda e fluxo interativo. |
| `utils.py`  | Função auxiliar `drawBox` para caixas no terminal.   |

## Autor

Dian Carlos — [dian.cabral@gmail.com](mailto:dian.cabral@gmail.com)
