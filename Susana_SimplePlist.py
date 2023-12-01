"""
=========================================================
   https://github.com/entediado97/Susana_SimplePlist
=========================================================
"""
import os
import shutil
import subprocess
from tqdm import tqdm  # Importa a biblioteca tqdm

# Função para imprimir texto em amarelo
def print_yellow(text):
    print(f"\033[93m{text}\033[0m")

# Exibir o novo banner da ferramenta
banner = """
  #####                                     
 #     # #    #  ####    ##   #    #   ##   
 #       #    # #       #  #  ##   #  #  #  
  #####  #    #  ####  #    # # #  # #    # 
       # #    #      # ###### #  # # ###### 
 #     # #    # #    # #    # #   ## #    # 
  #####   ####   ####  #    # #    # #    # 
         
          Simple Plist - beniwh                                             
"""
print_yellow(banner)

def find_copy_and_convert_plist_files(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Obter todos os arquivos plist do diretório de origem
    plist_files = [os.path.join(root, file) for root, dirs, files in os.walk(src_dir) for file in files if file.endswith(".plist")]

    file_counter = 1
    for src_file_path in tqdm(plist_files, desc="Copiando e convertendo arquivos", unit="file"):  # Barra de progresso
        dest_file_name = f"Info_{file_counter}.xml"
        dest_file_path = os.path.join(dest_dir, dest_file_name)

        # Copia o arquivo plist
        shutil.copy2(src_file_path, dest_file_path)

        # Converte o arquivo plist para xml
        convert_command = f"plistutil -i {dest_file_path} -o {dest_file_path}"
        subprocess.run(convert_command, shell=True)

        file_counter += 1

# Solicita ao usuário o diretório de origem
source_directory = input("Digite o caminho do diretório de origem: ")

# Define o diretório de destino com base na entrada do usuário
destination_directory = os.path.join(input("Digite o caminho base para o diretório de destino: "), "Info-plist")

# Chama a função
find_copy_and_convert_plist_files(source_directory, destination_directory)

# Mensagem final
#print("\n")  # Salta uma linha
print_yellow("Ex de uso: >grep -rin PESQUISA CAMINHO/Info-plist")
