#%%
import os
import shutil
from PIL import Image
from PIL import UnidentifiedImageError  # Importa a exceção UnidentifiedImageError


def optimize_image(input_path, output_path):
    # Verifica se o diretório de saída existe, caso contrário, cria-o
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Percorre todos os arquivos e subdiretórios no diretório de entrada
    for root, dirs, files in os.walk(input_path):
        # Percorre todos os arquivos no diretório atual
        for file in files:
            # Verifica se o arquivo é uma imagem (pode adicionar mais extensões, se necessário)
            if file.endswith((".jpg", ".jpeg", ".png", ".gif")):
                # Cria o caminho de entrada e saída dos arquivos
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_path, os.path.relpath(input_file_path, input_path))

                # Cria o diretório de saída para o arquivo, caso ainda não exista
                output_file_dir = os.path.dirname(output_file_path)
                if not os.path.exists(output_file_dir):
                    os.makedirs(output_file_dir)

                # # Abre a imagem usando a biblioteca Pillow
                # image = Image.open(input_file_path)

                # # Otimiza a imagem
                # image.save(output_file_path, optimize=True)

                # # Fecha a imagem
                # image.close()

                # print(f"Imagem otimizada: {input_file_path} -> {output_file_path}")

                try:
                    # Abre a imagem usando a biblioteca Pillow
                    image = Image.open(input_file_path)

                    # Otimiza a imagem
                    image.save(output_file_path, optimize=True)

                    # Fecha a imagem
                    image.close()

                    print(f"Imagem otimizada: {input_file_path} -> {output_file_path}")
                except UnidentifiedImageError:
                    # Copia e cola o arquivo para a pasta de saída
                    shutil.copy2(input_file_path, output_file_path)
                    print(f"Imagem não identificada: {input_file_path} -> {output_file_path}")



# Define os diretórios de entrada e saída
input_directory = 'C:\\Users\\marco\\Desktop\\Projeto\\compressor\\uploads'
output_directory = 'C:\\Users\\marco\\Desktop\\Projeto\\compressor\\uploads2'

# Chama a função para otimizar as imagens
optimize_image(input_directory, output_directory)
# %%
