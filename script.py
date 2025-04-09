import os
import shutil


pasta_fotos = r'C:/Users/usuar/Documents/foto_cand2024_PE_div'
if os.path.exists(pasta_fotos):
    print("O caminho existe.")
else:
    print("O caminho não existe.")
pasta_destino = 'C:/Users/usuar/Documents/fotos_cand_prefeit_PE'
arquivo_ids_prefeitos = 'C:/Users/usuar/Documents/prefeitos_ids.txt'

with open(arquivo_ids_prefeitos, 'r') as f:
    ids_prefeitos = set(line.strip() for line in f)

for nome_arquivo in os.listdir(pasta_fotos):
    print(nome_arquivo)
    id_foto, extensao = os.path.splitext(nome_arquivo)

    if id_foto in ids_prefeitos:
        shutil.copy(os.path.join(pasta_fotos, nome_arquivo), os.path.join(pasta_destino, nome_arquivo))


print('Fotos copiadas')