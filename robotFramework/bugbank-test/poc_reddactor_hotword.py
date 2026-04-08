import json
import re
import os

# --- NOVA CONFIGURAÇÃO: STRICT vs WEAK ---
INFOTYPES_CONFIG = {
    "CPF": {
        # Regex Padrão: Exige pontos e traço
        "strict": r"\d{3}\.\d{3}\.\d{3}-\d{2}",
        # Regex Flexível: Aceita se tiver Hotword (simula erro de digitação/OCR)
        # Lê-se: Números, talvez ponto, números, talvez traço...
        "weak": r"\d{3}\.?\d{3}\.?\d{3}-?\d{2}", 
        "hotwords": ["CPF", "CIC"]
    },
    "RG": {
        "strict": r"\d{1,2}\.\d{3}\.\d{3}",
        "weak": r"\d{1,9}", # Aceita qualquer sequencia de números se tiver escrito RG
        "hotwords": ["RG", "IDENTIDADE"]
    },
    # Tipos simples mantêm apenas uma regex
    "EMAIL": {"strict": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"},
    "MATRICULA": {"strict": r"\d{4}\d{5}"},
    "NIT": {"strict": r"\d{3}\.\d{5}\.\d{2}-\d{1}"},
    "NOME": {"strict": r"[A-ZÀ-Ÿ][a-zà-ÿ]+"},
    "ENDERECO": {"strict": r".+"}
}

def carregar_gabarito(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"ERRO: Arquivo {caminho_arquivo} não encontrado.")
        return []
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except: return []

    documentos = []
    for task in dados:
        itens_gabarito = []
        dados_temporarios = {}
        
        for annotation in task.get('annotations', []):
            for result in annotation.get('result', []):
                res_id = result.get('id')
                if not res_id: continue
                
                if res_id not in dados_temporarios:
                    dados_temporarios[res_id] = {'label': None, 'valor': None}
                
                if 'rectanglelabels' in result.get('value', {}):
                    dados_temporarios[res_id]['label'] = result['value']['rectanglelabels'][0]
                if 'text' in result.get('value', {}):
                    dados_temporarios[res_id]['valor'] = result['value']['text'][0]

        for dados in dados_temporarios.values():
            if dados['label'] and dados['valor']:
                itens_gabarito.append(dados)
        
        if itens_gabarito: documentos.append(itens_gabarito)
    return documentos

def validar_regras(gabarito):
    print(f"\n{'INFOTYPE':<10} | {'VALOR (GABARITO)':<30} | {'STATUS':<15} | {'DETALHE'}")
    print("-" * 85)

    acertos = 0
    total = 0

    for doc in gabarito:
        for item in doc:
            total += 1
            tipo = item['label']
            valor = item['valor']
            
            config = INFOTYPES_CONFIG.get(tipo)
            
            if config:
                # 1. Tenta Regex ESTRITA (Cenário Ideal)
                if re.search(config['strict'], valor):
                    print(f"{tipo:<10} | {valor:<30} | ✅ PASS          | Regex Padrão")
                    acertos += 1
                
                # 2. Se falhar, tenta Regex FRACA + Simulação de Hotword
                elif 'weak' in config and re.search(config['weak'], valor):
                    print(f"{tipo:<10} | {valor:<30} | ⚠️  HOTWORD SAVE | Salvo pelo contexto '{config['hotwords'][0]}'")
                    acertos += 1 # Consideramos acerto porque o Reddactor pegaria
                
                else:
                    print(f"{tipo:<10} | {valor:<30} | ❌ FAIL          | Nem o contexto salvou")
            else:
                print(f"{tipo:<10} | {valor:<30} | ℹ️  SKIP          | Sem config")

    if total > 0:
        score = (acertos / total) * 100
        print("-" * 85)
        print(f"TAXA DE SUCESSO FINAL: {score:.1f}%")

if __name__ == "__main__":
    validar_regras(carregar_gabarito('gabarito.json'))