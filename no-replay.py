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
    print("\033[1;33mNo-Replay 0.1\033[0m\n\033[1mBy Fabiano Vasconcelos\033[0m | \033[36mwww.fabianovasconcelos.com\033[0m");
    print("Copyright Fabiano Vasconcelos © 2023 Todos os direitos reservados.\n");

# Verificar se o número de argumentos é suficiente
if len(sys.argv) < 2:
    os.system('clear');
    print("\n=> Erro: Você precisa especificar a pasta em que estão os arquivos que você quer analisar.")
    print("Uso: $ no-replay [pasta a ser analisada]\n");
    label();
    sys.exit(1)

def is_valid_path(path):
    if os.path.isdir(path) == False:
        print("\n=> Erro: Este não é um caminho ou pasta válida. Por favor aponte uma pasta válida.");
        print("Uso: $ no-replay [pasta a ser analisada]\n");
        sys.exit(1);

def listar_arquivos(pasta):
    for root, dirs, files in os.walk(pasta):
        for file in files:
            caminho_completo = os.path.join(root, file);
            retorno = calcular_md5(caminho_completo);
            print(retorno);
            print(caminho_completo+"\n");

def main():
    os.system('clear');
    label();
    is_valid_path(DIRETORIO_BASE);
    listar_arquivos(DIRETORIO_BASE);

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