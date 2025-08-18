# Manipulação de Arquivos (CLI)

Projeto simples em Python para gravar e ler textos em arquivos `.txt` por meio de um menu interativo no terminal.

> Este repositório foi extraído do diretório `manipulaçãoDeArquivos/` e contém scripts organizados em `menu/` e `services/`, além da pasta `arquivos_log/` para os arquivos gerados.

---

## ✨ Funcionalidades

- **Gravar arquivos**: solicita um texto no terminal e salva em `arquivos_log/log_cadastro_<n>.txt`.
- **Ler arquivos**: solicita o número do arquivo e exibe o conteúdo formatado no terminal.
- **Menu interativo**: interface simples via terminal com opções de **gravar**, **ler** e **sair**.

---

## 🧭 Estrutura do projeto

```
manipulaçãoDeArquivos/
├── main.py
├── arquivos_log/
│   ├── log_cadastro_1.txt
│   └── log_cadastro_2.txt
├── menu/
│   ├── __init__.py
│   └── menu_funcoes.py
└── services/
    ├── __init__.py
    ├── gravar_arquivo.py
    └── ler_arquivo.py
```

---

## 🧱 Pré-requisitos

- **Python 3.10+** (testado com CPython 3.13, mas o código é compatível com versões mais novas do Python 3).
- Sistema operacional Windows, macOS ou Linux (ver nota sobre caminhos abaixo).

> Não há dependências externas (nenhum `requirements.txt`).

---

## ▶️ Como executar

1. **Clone** o repositório ou extraia a pasta `manipulaçãoDeArquivos`.
2. (Opcional) **Crie e ative um ambiente virtual**:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/macOS
   source .venv/bin/activate
   ```
3. **Execute o programa**:
   ```bash
   python main.py
   ```

---

## ⚙️ Configuração de caminhos (IMPORTANTE)

No arquivo `services/gravar_arquivo.py`, o caminho usado para gravar os logs está **absoluto** e aponta para uma pasta específica do Windows:

```python
with open(
    f"C:\Users\João Pedro Sousa\Desktop\python\manipulaçãoDeArquivos\arquivos_log\log_cadastro_{cont}.txt",
    "w",
    encoding="utf-8",
) as arquivo_log:
    ...
```

Para executar em outra máquina ou em Linux/macOS, **ajuste esse caminho** ou substitua por um caminho **relativo** à pasta do projeto. Exemplo (mais portátil), usando `pathlib`:

```python
from pathlib import Path

base_dir = Path(__file__).resolve().parents[1]  # raiz do projeto
log_dir = base_dir / "arquivos_log"
log_dir.mkdir(exist_ok=True)

with open(log_dir / f"log_cadastro_{cont}.txt", "w", encoding="utf-8") as arquivo_log:
    ...
```

> Faça ajuste equivalente em `services/ler_arquivo.py` se necessário, para ler a partir do mesmo diretório `arquivos_log/`.

---

## 🖥️ Fluxo do menu

- **[1] Gravar arquivo** → solicita texto e pergunta se deseja continuar (`S/N`). Cada gravação cria `log_cadastro_<n>.txt`.
- **[2] Ler arquivo** → solicita o **número do arquivo** (ex.: `1` para `log_cadastro_1.txt`) e imprime o conteúdo com quebras a cada 40 caracteres.
- **[0] Sair** → encerra o programa.

---

## 🧪 Exemplo de uso

**Gravar**:
```
[Arquivo N° 1]
Escreva algo: Olá, mundo!
Deseja continuar? [S] para SIM, [N] para NÃO: S
[Arquivo N° 2]
Escreva algo: Outro texto...
Deseja continuar? [S] para SIM, [N] para NÃO: N
Programa encerrado...
```

**Ler**:
```
Informe o N° do arquivo: 1
----------------------------------------
         LEITURA DO ARQUIVO N° 1        
----------------------------------------
Olá, mundo!
```

---


