from playwright.sync_api import sync_playwright
import csv
import os
import time
import json

CSV_FILE = "boletos.csv"
URL = "https://devtools.com.br/gerador-boleto/"
PDF_DIR = "boletos_pdf"
JSON_DIR = "boletos_json"

os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(JSON_DIR, exist_ok=True)

def gerar_boleto(page, linha):
    page.wait_for_selector("iframe", timeout=10000)
    target_iframe = None
    for frame in page.frames:
        try:
            if frame.locator("#sacado").count() > 0:
                target_iframe = frame
                break
        except:
            continue

    if not target_iframe:
        raise Exception("Iframe do formulário não encontrado.")

    target_iframe.locator("#sacado").fill(linha[0])
    target_iframe.locator("#cpf_cnpj").fill(linha[1])
    target_iframe.locator("#data_venc").fill(linha[2])
    valor = linha[3].replace(",", ".") if linha[3] else "0.0"
    target_iframe.locator("#valor_cobrado").fill(str(float(valor)))
    target_iframe.locator("#numero_documento").fill(linha[4])

    with page.context.expect_page() as new_page_info:
        target_iframe.locator("#btn_enviar, #btn_submit, .btn-info").click()
    
    boleto_page = new_page_info.value
    
    boleto_page.wait_for_load_state("networkidle")
    time.sleep(2) 

    pdf_file = os.path.join(PDF_DIR, f"{linha[1]}-{linha[4]}.pdf")
    
    boleto_page.emulate_media(media="screen")
    
    boleto_page.pdf(
        path=pdf_file, 
        format="A4",
        print_background=True,
        margin={"top": "1cm", "bottom": "1cm", "left": "1cm", "right": "1cm"}
    )
    
    print(f"PDF salvo: {pdf_file}")

    boleto_page.close()

    return pdf_file

def salvar_json(linha):

    dados = {
        "Nome / Razão Social": linha[0],
        "Documento Federal (CPF/CNPJ)": linha[1],
        "Data Vencimento": linha[2],
        "Valor (R$)": float(linha[3].replace(",", ".")) if linha[3] else 0.0,
        "Número Documento": linha[4]
    }

    json_file = os.path.join(JSON_DIR, f"{linha[1]}-{linha[4]}.json")
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print(f"JSON gerado: {json_file}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) 
    context = browser.new_context()
    page = context.new_page()

    print("Acessando a página...")
    page.goto(URL)

    if not os.path.exists(CSV_FILE):
        print(f" Arquivo {CSV_FILE} não encontrado!")
    else:
        with open(CSV_FILE, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader) 

            for idx, linha in enumerate(reader, start=1):
                linha = [campo.strip() if campo.strip() != "" else "" for campo in linha]
                print(f"\nProcessando linha {idx}: {linha}")

                try:
                    gerar_boleto(page, linha)
                    salvar_json(linha)
                except Exception as e:
                    print(f" Erro na linha {idx}: {e}")
                    page.goto(URL)

    print("\nProcesso concluído")
    browser.close()