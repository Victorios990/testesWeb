import json
import re
import os

# --- CONFIGURAÇÃO V3: REGEX + HOTWORDS + EXCLUSÕES ---
INFOTYPES_CONFIG = {
    "CPF": {
        "strict": r"\d{3}\.\d{3}\.\d{3}-\d{2}",
        "weak": r"\d{3}\.?\d{3}\.?\d{3}-?\d{2}",
        "hotwords": ["CPF", "CIC"],
        # Exemplo: Excluir CPFs de teste ou sequências inválidas conhecidas
        "exclusions": [r"000\.000\.000-00", r"111\.111\.111-11"] 
    },
    "NIT": {
        "strict": r"\d{3}\.\d{5}\.\d{2}-\d{1}",
        # Exemplo Prático: Imagine que existe um código de contrato interno 
        # que parece NIT, mas começa com "321.789". Vamos excluí-lo para testar.
        "exclusions": [r"^321\.789.*"] 
    },
    "NOME": {
        "strict": r"[A-Z][a-z]+ [A-Z][a-z]+",
        # Dicionário de Termos: Ignora nomes de cidades, empresas ou cargos comuns
        "dictionary": ["Master", "Logística", "Transportes", "São Paulo", "Goiânia", "Gerente"]
    },
    # Mantendo os outros simples
    "EMAIL": {"strict": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"},
    "RG": {"strict": r"\d{1,2}\.\d{3}\.\d{3}"},
    "MATRICULA": {"strict": r"\d{4}\d{5}"},
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
    print(f"\n{'INFOTYPE':<10} | {'VALOR (GABARITO)':<30} | {'STATUS':<18} | {'DETALHE'}")
    print("-" * 90)

    acertos = 0
    total = 0

    for doc in gabarito:
        for item in doc:
            total += 1
            tipo = item['label']
            valor = item['valor']
            
            config = INFOTYPES_CONFIG.get(tipo)
            
            if config:
                capturado = False
                motivo_captura = ""

                # 1. Tenta Regex ESTRITA
                if re.search(config['strict'], valor):
                    capturado = True
                    motivo_captura = "Regex Strict"
                # 2. Tenta Regex FRACA + Hotword
                elif 'weak' in config and re.search(config['weak'], valor):
                    capturado = True
                    motivo_captura = "Hotword/Weak"

                # 3. Se capturou, aplica REGRAS DE EXCLUSÃO (O Filtro Final)
                if capturado:
                    excluido = False
                    motivo_exclusao = ""

                    # 3.1 Exclusão por Regex
                    if 'exclusions' in config:
                        for ex_regex in config['exclusions']:
                            if re.search(ex_regex, valor):
                                excluido = True
                                motivo_exclusao = f"Regex Exclusão: {ex_regex}"
                                break
                    
                    # 3.2 Exclusão por Dicionário
                    if not excluido and 'dictionary' in config:
                        # Verifica se alguma palavra do dicionário está contida no valor
                        for termo in config['dictionary']:
                            if termo.lower() in valor.lower():
                                excluido = True
                                motivo_exclusao = f"Dicionário: '{termo}'"
                                break

                    # RESULTADO FINAL
                    if excluido:
                        # Se estava no Gabarito (era sensível) e foi excluído -> É um ERRO DE CONFIGURAÇÃO (Vazamento)
                        # Se o Gabarito marcasse "Falso Positivo", seria um Acerto. Como marcamos dados reais:
                        print(f"{tipo:<10} | {valor:<30} | ⛔ EXCLUÍDO (ERRO)  | {motivo_exclusao}")
                        # Nota: Consideramos erro aqui porque assumimos que tudo no gabarito DEVE ser pego.
                        # Se você quiser testar se a exclusão funciona, esse status confirma que ela agiu.
                    else:
                        print(f"{tipo:<10} | {valor:<30} | ✅ PASS            | {motivo_captura}")
                        acertos += 1

                else:
                    print(f"{tipo:<10} | {valor:<30} | ❌ FAIL            | Nenhuma Regex pegou")
            else:
                print(f"{tipo:<10} | {valor:<30} | ℹ️  SKIP            | Sem config")

    if total > 0:
        score = (acertos / total) * 100
        print("-" * 90)
        print(f"TAXA DE SUCESSO: {score:.1f}%")

if __name__ == "__main__":
    validar_regras(carregar_gabarito('gabarito.json'))