import os

def find_all_files(type = ".txt", path = os.getcwd()):
    '''Вывод списка файлов с требуемым расширениям из указанной директории '''
    list_of_files = [file for file in os.listdir(path) if file.endswith(type)]    
    return list_of_files

def sort_files(list_of_files):
    ''' Сортировка по размеру файла'''
    sorted_list_of_files = sorted(list_of_files, key = os.path.getsize)    
    return sorted_list_of_files

def combine_text(list_of_files, path = os.getcwd()):
    combine_text_str = ""    
    for i, file in enumerate(list_of_files):
        path_to_file = os.path.join(path, file)
        with open(path_to_file, 'rt', encoding='utf-8') as text:
            for count in range(i+1):
                str_a = text.readline()
                combine_text_str += f'{file}\n{i+1}\n{str_a}' if count == 0 else f'{str_a}'      
    return combine_text_str

def merge_files(combine_text_str, file_name = 'result.txt', path = os.getcwd()):
    with open(file_name, 'w') as text:
        return text.write(combine_text_str)
     


print(find_all_files())
print(sort_files(find_all_files()))
print(combine_text(sort_files(find_all_files())))
print(merge_files(combine_text(sort_files(find_all_files()))))
