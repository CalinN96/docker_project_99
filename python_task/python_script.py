import os
from collections import Counter
import re
import fnmatch

### --- Path Chooser --- ###
pathh = input("\nPlease provide a FULL PATH of the directory you want to search in.\n(press enter to use current dir): ")
if pathh == "":
    root = os.path.join('.')                    
else:
    root = os.path.join(f'{pathh}')


# File types set to txt only
file_types = ["*.txt"]

### --- Word counter --- ###
def get_most_common_words(text, num_words=10):
    words = re.findall(r'\w+', text.lower())
    common_words = Counter(words).most_common(num_words)
    return common_words

### --- Searching for .txt files and processing --- ###
def searching():
    files_containing_my_word = []
    
    for directory, subdir_list, file_list in os.walk(root):
        for file_name in fnmatch.filter(file_list, file_types[0]):
            source_file_name = os.path.join(directory, file_name)
            
            with open(source_file_name, 'r', encoding="utf-8") as myfile:
                text = myfile.read()
                common_words = get_most_common_words(text)
                print(f"Most common words in {file_name}: {common_words}")
                files_containing_my_word.append((file_name, common_words))

    return files_containing_my_word

### --- Main Execution --- ###
if __name__ == "__main__":
    searching()
