"""
No-Replay
Varre uma unidade de HDD ou SSD, detecta arquivos duplicados no linux com o aval do rash md5, elimina as cópias desnecessárias ou coloca-as em quarentena
Autor: FabianoVasconcelos.com
Data: 10/07/2023
"""

import os;
import hashlib;

def main():
    os.system('clear');
    print("\033[1;33mNo-Replay 0.1\033[0m\n\033[1mBy Fabiano Vasconcelos\033[0m | \033[36mwww.fabianovasconcelos.com\033[0m");
    print("Copyright Fabiano Vasconcelos © 2023 Todos os direitos reservados.");


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