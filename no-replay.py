"""
No-Replay
Script para Linux que varre uma unidade de HDD ou SSD, detecta arquivos duplicados com a segurança do rash md5, elimina as cópias desnecessárias ou coloca-as em quarentena
Autor: FabianoVasconcelos.com
Data: 10/07/2023
"""

import os;
import hashlib;
import sys;

DIRETORIO_BASE = sys.argv[1];

def label():
    print("\n\033[1;33mNo-Replay 0.1\033[0m\n\033[1mBy Fabiano Vasconcelos\033[0m | \033[36mwww.fabianovasconcelos.com\033[0m");
    print("Copyright Fabiano Vasconcelos © 2023 Todos os direitos reservados.");

# Verificar se o número de argumentos é suficiente
if len(sys.argv) < 2:
    os.system('clear');
    print("\n=> Erro: Você precisa especificar a pasta em que estão os arquivos que você quer analisar.")
    print("Uso: $ no-replay [pasta a ser analisada]\n");
    sys.exit(1)

def is_valid_path(path):
    if os.path.isdir(path) == False:
        print("\n=> Erro: Este não é um caminho ou pasta válida. Por favor aponte uma pasta válida.");
        print("Uso: $ no-replay [pasta a ser analisada]\n");
        sys.exit(1);

def listar_arquivos(pasta):
    lista_arquivos = [];
    for root, dirs, files in os.walk(pasta):

        # Ignorar diretórios começados com ponto
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            if not file.startswith('.'):
                caminho_completo = os.path.join(root, file);
                lista_arquivos.append(caminho_completo);
    return lista_arquivos;

def detectar_arquivos_duplicados(lista_arquivos):
    hash_arquivos = {};
    duplicatas = {};
    contador = 0;
    for arquivo in lista_arquivos:
        hash = calcular_md5(arquivo);
        if hash in hash_arquivos:
            contador += 1;
            if hash in duplicatas:
                duplicatas[hash].append(arquivo);
            else:
                duplicatas[hash] = [hash_arquivos[hash], arquivo];
        else:
            hash_arquivos[hash] = arquivo;
    
    return contador, duplicatas;

# Exibir os arquivos duplicados e seus caminhos
    print("\nArquivos duplicados:\n")
    for hash, caminhos in duplicatas.items():
        print(f"Arquivo {caminhos[0]} também aparece como:")
        for caminho in caminhos[1:]:
            print(f"=> {caminho}")
        print()

def main():
    os.system('clear');
    is_valid_path(DIRETORIO_BASE);
    lista_arquivos = listar_arquivos(DIRETORIO_BASE);
    contador, duplicatas = detectar_arquivos_duplicados(lista_arquivos);
    print("\nArquivos duplicados:\n");
    for hash, caminhos in duplicatas.items():
        print(f"Arquivo {caminhos[0]} também aparece como:");
        for caminho in caminhos[1:]:
            print(f"=> {caminho}");
        print();
    print("Total de arquivos repetidos encontrados: ", contador);
    label();

def calcular_md5(arquivo):
    hash_md5 = hashlib.md5()
    with open(arquivo, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Verificar se o script está sendo executado diretamente (não importado como um módulo)
if __name__ == "__main__":
    main()
    print("\n\n");