import os
from PIL import Image


def main(main_images_folder, new_width=800):
    if not os.path.isdir(main_images_folder):  # se não for diretório da erro
        raise NotADirectoryError(f'{main_images_folder} não existe.')

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            # print(file)
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)

            converted_tag = '_CONVERTED'

            new_file = file_name + converted_tag + extension
            new_file_full_path = os.path.join(root, new_file)

            # remove as imagens convertidas
            # if converted_tag in file_full_path:
            #     os.remove(file_full_path)
            #
            # continue

            if os.path.isfile(new_file_full_path):
                print(f'Arquivo {new_file_full_path} já existe.')
                continue

            if converted_tag in file_full_path:
                print('Imagem já convertida.')
                continue

            img_pillow = Image.open(file_full_path)

            width, height = img_pillow.size
            new_height = round((new_width * height) / width)

            # print(width, height)

            new_image = img_pillow.resize(
                (new_width, new_height),
                Image.LANCZOS
            )

            new_image.save(
                new_file_full_path,
                optimize=True,
                quality=70,
                exif=img_pillow.info['exif']  # exif para não perder dados das imagens originais
            )

            print(f'{file_full_path} convertido com sucesso!')
            new_image.close()
            img_pillow.close()

            # os.remove(file_full_path)
            # remove as imagens originais: CUIDADO!


if __name__ == '__main__':
    main_images_folder = '/home/elton/teste'
    main(main_images_folder, new_width=1920)