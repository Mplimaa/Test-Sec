import platform
import sys

def main():
    os_info = platform.system()

    if os_info == 'Windows':
        print("Rodando em um ambiente Windows.")
        # Código específico para Windows
    elif os_info == 'Darwin':
        print("Rodando em um ambiente macOS.")
        # Código específico para macOS
    elif os_info == 'Linux':
        print("Rodando em um ambiente Linux.")
        # Código específico para Linux
    else:
        print("Sistema Operacional não identificado.")
        sys.exit(1)

    # Código geral que é compatível com todos os SOs
    print("Executando operações comuns.")

if __name__ == "__main__":
    main()
