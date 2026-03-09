🤖 Gerador Automático de Boletos com Playwright

Este projeto é um script de automação em Python que gera boletos automaticamente a partir de um arquivo CSV, utilizando automação de navegador com Playwright.

O script acessa um gerador online de boletos, preenche o formulário automaticamente, gera o boleto, salva o PDF e também cria um arquivo JSON com os dados utilizados.

É uma solução útil para automatizar geração de boletos em lote, evitando preenchimento manual repetitivo.

🚀 Tecnologias utilizadas

🐍 Python

🎭 Playwright (automação de navegador)

📄 CSV para entrada de dados

📑 PDF para exportação do boleto

🗂 JSON para registro estruturado das informações

⚙️ Como funciona

O fluxo do script é o seguinte:

1️⃣ O programa lê um arquivo CSV contendo os dados dos boletos.

2️⃣ Para cada linha do CSV, o script:

Acessa o site
👉 https://devtools.com.br/gerador-boleto/

Encontra o iframe do formulário

Preenche automaticamente os campos:

👤 Nome / Razão Social

🪪 CPF ou CNPJ

📅 Data de vencimento

💰 Valor do boleto

🧾 Número do documento

3️⃣ Após enviar o formulário:

Uma nova página com o boleto é aberta

O script gera o PDF do boleto automaticamente

4️⃣ O sistema também gera um arquivo JSON com os dados utilizados no boleto.

📂 Estrutura do projeto
📁 projeto
 ├── boletos.csv
 ├── script.py
 │
 ├── 📁 boletos_pdf
 │     └── boletos gerados em PDF
 │
 └── 📁 boletos_json
       └── dados dos boletos em JSON
📄 Formato do arquivo CSV

O arquivo boletos.csv deve conter os seguintes campos:

Nome,CPF_CNPJ,Data_Vencimento,Valor,Numero_Documento
João Silva,12345678900,10/04/2026,150.00,001
Empresa XPTO,12345678000100,15/04/2026,2500.00,002

Campos:

Campo	Descrição
Nome	Nome da pessoa ou empresa
CPF_CNPJ	Documento federal
Data_Vencimento	Data de vencimento do boleto
Valor	Valor do boleto
Numero_Documento	Identificador do boleto
📑 Saídas geradas

Para cada boleto processado serão criados:

📄 PDF

Boleto gerado automaticamente

boletos_pdf/CPF-NumeroDocumento.pdf

Exemplo:

boletos_pdf/12345678900-001.pdf
🗂 JSON

Registro estruturado dos dados do boleto

boletos_json/CPF-NumeroDocumento.json

Exemplo:

{
  "Nome / Razão Social": "João Silva",
  "Documento Federal (CPF/CNPJ)": "12345678900",
  "Data Vencimento": "10/04/2026",
  "Valor (R$)": 150.0,
  "Número Documento": "001"
}
▶️ Como executar
1️⃣ Instalar dependências
pip install playwright

Depois instalar os navegadores:

playwright install
2️⃣ Criar o arquivo CSV

Crie um arquivo chamado:

boletos.csv

Com os dados dos boletos.

3️⃣ Executar o script
python script.py

O navegador será aberto automaticamente e os boletos serão gerados.

🧠 Funcionalidades implementadas

✔ Leitura de dados via CSV
✔ Automação web com Playwright
✔ Preenchimento automático de formulário
✔ Detecção de iframe
✔ Geração automática de PDF
✔ Exportação de dados em JSON
✔ Tratamento básico de erros
✔ Organização automática em pastas

💡 Possíveis melhorias futuras

🔹 Interface gráfica (GUI)

🔹 Execução em modo headless

🔹 Integração com APIs bancárias

🔹 Geração de relatório consolidado

🔹 Logs estruturados

👨‍💻 Autor

Projeto desenvolvido por Eduardo G.

📌 Focado em automação de tarefas repetitivas com Python.
