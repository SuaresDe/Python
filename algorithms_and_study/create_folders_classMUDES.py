import os

def create_folders_classes(base_folder, name_folder_base, start_index=1):

    name_folder_base = f"{name_folder_base} {start_index:03d}"  
    path_folder = os.path.join(base_folder, name_folder_base)
    

    while os.path.exists(path_folder):
        start_index += 1
        name_folder_base = f"{nome_base} {start_index:03d}"
        path_folder = os.path.join(base_folder, name_folder_base)

    os.makedirs(path_folder)
    print(f"Pasta '{path_folder}' criada com sucesso.")
    return path_folder

if __name__ == "__main__":
    base_folder = 'Semanal_MUDES'
    nome_base = 'Aula'
    start_index = 1

    for create_folders in range(1):  
        create_folders_classes(base_folder, nome_base, start_index)
        start_index += 1
