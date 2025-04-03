import os
import shutil

# Detecta se python3 está disponível, senão usa python
python_cmd = shutil.which("python3") or shutil.which("python")

comandos = {
    "1": f"{python_cmd} src/main.py",
    "2": f"{python_cmd} -m unittest discover tests",
}

print("1 - Iniciar o jogo")
print("2 - Rodar os testes")
opcao = input("Escolha uma opção: ")

if opcao in comandos:
    os.system(comandos[opcao])
else:
    print("Opção inválid1a.")
