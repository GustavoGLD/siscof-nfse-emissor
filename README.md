# SISCOF NFSe Emissor

## 🧾 Visão Geral

O **SISCOF NFSe Emissor** é uma solução em Python para geração automática e auditável de **Notas Fiscais de Serviço Eletrônicas (NFSe)** e **arquivos de apuração tributária**, com foco em ISS, PIS, COFINS e IR. 

Projetado para instituições financeiras, adquirentes e empresas de pagamento, o sistema processa transações de cartão e transforma essas informações em documentos fiscais conforme as exigências municipais, com exportação estruturada e logs de auditoria.

---

## 🚀 Funcionalidades Principais

- 📥 Coleta de transações financeiras (via tabela `tbl_dirf`).
- 📊 Cálculo automático de tributos a partir de percentuais parametrizáveis.
- 🧾 Geração de NFS-e por CNPJ tomador, com persistência em banco (`notas_fiscais`) e detalhamento em arquivo `.txt`.
- 🗂 Geração de arquivos ISS por município/UF, consolidados por competência.
- 📑 Exportação de log de execução (sucesso/falha) em CSV (`log_nf.csv`) para auditoria.
- ♻️ Suporte a reprocessamento e rastreabilidade de dados em caso de falha.

---

## 🧮 Tributos Calculados

Os seguintes tributos são calculados automaticamente, com base em valores parametrizados no banco (`param_decred`) ou `config.py`:

- **ISS** (Imposto Sobre Serviços)
- **PIS** (Programa de Integração Social)
- **COFINS** (Contribuição para o Financiamento da Seguridade Social)
- **IR** (Imposto de Renda)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.9+**
- **SQLAlchemy** (ORM com `DeclarativeBase`)
- **Pandas** (para exportação de logs)
- **Loguru** (logging estruturado e decoradores de rastreamento)
- **Dataclasses** (estruturação e serialização de dados)
- **PostgreSQL** (banco principal, adaptável via SQLAlchemy)

---


## 📁 Estrutura de Diretórios

```

siscof-nfse-emissor/
├── gerador\_nf.py                 # Script principal (entrypoint)
├── config.py                     # Configurações (caminhos, percentuais, db\_url)
└── src/
├── infra/
│   ├── core/
│   │   ├── base.py           # Base ORM
│   │   └── connection.py     # Conexão com o banco
│   ├── entities/             # Mapeamentos ORM
│   └── functions/            # Regras de negócio
│       └── structures/       # Helpers de formatação de saída
└── utils/                    # Utilitários transversais (logging, conversões, agrupamento)

```

---


## ⚙️ Fluxo de Execução

1. **Geração das NFSe** (`gerar_nf`)
   - Extrai e agrupa transações de cartão (`tbl_dirf`)
   - Calcula impostos e monta objetos `NotaFiscal`
   - Persiste registros e logs (`log_nf`)

2. **Geração de Arquivo Texto NFSe** (`gerar_nf_txt`)
   - Formata as linhas de saída (RPS) e trailer
   - Salva em `tabela_nf` e escreve `.txt`

3. **Geração de Arquivos ISS** (`gera_iss_txt`)
   - Agrega valores por município/UF
   - Salva em `tbl_iss` e exporta `.txt`

4. **Exportação de Logs** (`gerar_log_nf`)
   - Lê `log_nf` e exporta `log_nf.csv`

---

## 📁 Saída Esperada

* Arquivo `.txt` com todas as NFS-e emitidas por mês:

  ```
  NFSE_12345678000199_052024_A.txt
  ```
* Arquivos de ISS por município:

  ```
  ISS_SP_SÃO_PAULO_202405.TXT
  ```
* Log completo das tentativas de emissão:

  ```
  log_nf.csv
  ```

---

## 🚀 Como Executar

1. **Clone o projeto e instale as dependências**

```bash
git clone https://github.com/seuusuario/siscof-nfse-emissor.git
cd siscof-nfse-emissor
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````

2. Configure o `config.py`:

```python
db_url = "postgresql+psycopg2://user:senha@host:5432/nome_do_banco"
OutputFolders = {
    "log_nf": "./log_nf/",
    "iss_txt": "./iss_txt/"
}
Impostos = {
    "pct_iss": 0.02,
    "pct_pis": 0.0065,
    "pct_cofins": 0.03,
    "pct_ir": 0.015
}
```

3. **Execute o orquestrador**

```bash
python gerador_nf.py
```

---

## 🧪 Funcionalidades Avançadas

* ✅ **Logging por NF**: cada geração é registrada com mensagem e stack trace (se necessário).
* 🔁 **Reprocessamento seguro**: ideal para fluxos em lote mensais.
* 📚 **Separação de camadas**: Entities, Functions, Utils bem definidos.
* 🧱 **Flexível**: fácil adaptação para novos layouts ou municípios com requisitos específicos.

---

## 🔄 Extensibilidade

* ✅ Suporte futuro à exportação em **XML ou JSON**
* ✅ Suporte a múltiplos `pacquirer_id` com facilidade
* ✅ Parametrização por `relativedelta` em vez de mês fixo
* ✅ Suporte a novas obrigações fiscais (RPS eletrônico, integração via WebService)

---

## 👨‍💻 Autor

**Gustavo Lídio Damaceno** • [LinkedIn](https://www.linkedin.com/in/gustavo-lidio-damaceno/)

