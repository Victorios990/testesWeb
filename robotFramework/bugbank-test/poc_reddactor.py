import json
import re
import os

# --- CONFIGURAÇÃO DOS INFOTYPES ---
INFOTYPES_CONFIG = {
    "CPF": r"\d{3}\.\d{3}\.\d{3}-\d{2}",  
    "EMAIL": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "RG": r"\d{1,2}\.\d{3}\.\d{3}",        
    "MATRICULA": r"\d{4}\d{5}",
    "NIT": r"\d{3}\.\d{5}\.\d{2}-\d{1}",
    "NOME": r"[A-ZÀ-Ÿ][a-zà-ÿ]+", # Regex simples para testar nomes
    "ENDERECO": r".+" # Aceita qualquer coisa para teste
}

def carregar_gabarito(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"ERRO CRÍTICO: Não achei o arquivo '{caminho_arquivo}' na pasta atual.")
        return []

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except json.JSONDecodeError:
        print("Erro: O arquivo gabarito.json não é um JSON válido.")
        return []
    
    documentos = []
    
    # Loop por cada documento (Task)
    for task in dados:
        itens_gabarito = []
        
        # Dicionário temporário para juntar Retângulo + Texto pelo ID
        dados_temporarios = {}

        annotations = task.get('annotations', [])
        for annotation in annotations:
            for result in annotation.get('result', []):
                res_id = result.get('id')
                if not res_id: continue

                if res_id not in dados_temporarios:
                    dados_temporarios[res_id] = {'label': None, 'valor': None}

                # Tenta pegar a Etiqueta (Label)
                if 'rectanglelabels' in result.get('value', {}):
                    dados_temporarios[res_id]['label'] = result['value']['rectanglelabels'][0]

                # Tenta pegar o Texto (Transcription)
                if 'text' in result.get('value', {}):
                    dados_temporarios[res_id]['valor'] = result['value']['text'][0]

        # Agora consolida o que achou
        for res_id, dados in dados_temporarios.items():
            if dados['label'] and dados['valor']:
                itens_gabarito.append({
                    "label": dados['label'],
                    "valor": dados['valor']
                })
        
        if itens_gabarito:
            documentos.append(itens_gabarito)
            
    return documentos

def validar_regras(gabarito):
    if not gabarito:
        print("Nenhum dado encontrado. Verifique se você marcou as caixas E digitou o texto no Label Studio.")
        return

    print(f"\n{'DOC ID':<5} | {'INFOTYPE':<10} | {'VALOR NO GABARITO':<30} | {'STATUS':<10}")
    print("-" * 75)

    total_testes = 0
    acertos = 0

    for i, doc in enumerate(gabarito):
        for item in doc:
            total_testes += 1
            tipo = item['label']
            valor_humano = item['valor']
            
            if tipo in INFOTYPES_CONFIG:
                regex = INFOTYPES_CONFIG[tipo]
                match = re.search(regex, valor_humano)
                
                if match:
                    print(f"{i+1:<5} | {tipo:<10} | {valor_humano:<30} | ✅ PASS")
                    acertos += 1
                else:
                    print(f"{i+1:<5} | {tipo:<10} | {valor_humano:<30} | ❌ FAIL (Regex rejeitou)")
            else:
                print(f"{i+1:<5} | {tipo:<10} | {valor_humano:<30} | ⚠️ SKIP (Sem Regex)")

    if total_testes > 0:
        score = (acertos / total_testes) * 100
        print("-" * 75)
        print(f"TAXA DE SUCESSO: {score:.1f}%")
        if score < 95:
             print("Resultado: 🔴 O sistema encontrou falhas de validação.")
        else:
             print("Resultado: 🟢 Tudo validado com sucesso.")
    else:
        print("Aviso: O JSON existe mas não consegui extrair pares de Label/Texto dele.")

if __name__ == "__main__":
    validar_regras(carregar_gabarito('gabarito.json'))