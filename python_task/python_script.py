import os
import time
from collections import Counter
import re
import fnmatch



### --- Path Chooser --- ###
## For Docker
root = os.environ.get('DIRECTORY_PATH', '.')


## My tests path
# pathh = input("\nPlease provide a FULL PATH of the directory you want to search in.\n(press enter to use current dir): ")
# if pathh == "":
#     root = os.path.join('.')                    
# else:
#     root = os.path.join(f'{pathh}')



# File types txt only
file_types = ["*.txt"]





### --- Word counter --- ###
def get_most_common_words(text, num_words=10):

    # Finding the words
    words = re.findall(r'\w+', text.lower())

    # Counting the words & getting the 10 most commom
    common_words = Counter(words).most_common(num_words)
    
    # Retunging the words
    return common_words





### --- Get Last Modification Time of Files --- ###

def get_file_modification_times(root, file_types):
   
    # Empty dictionary
    mod_times = {}

    # Getting each file from the provided path
    for directory, subdir_list, file_list in os.walk(root):
        for file_name in fnmatch.filter(file_list, file_types[0]):
            source_file_name = os.path.join(directory, file_name)

            # Getting the modification time in computer readable time
            mod_times[source_file_name] = os.path.getmtime(source_file_name)
            
    return mod_times





### --- Searching for .txt files and processing --- ###
def searching():
    
    # Counting all words from all files
    all_words = Counter()

    # Getting each file from the provided path
    for directory, subdir_list, file_list in os.walk(root):
        for file_name in fnmatch.filter(file_list, file_types[0]):
            source_file_name = os.path.join(directory, file_name)
            
            # Open each file
            with open(source_file_name, 'r', encoding="utf-8") as myfile:

                # Read file
                text = myfile.read()

                # Use get_most_common_words function above
                common_words = get_most_common_words(text)

                print(f"Most common words in {file_name}: {common_words}")

                # Add the words from the file to the all_words counter
                all_words.update(re.findall(r'\w+', text.lower()))

    return all_words.most_common(5)
    




### --- Main Execution --- ###
if __name__ == "__main__":

    # Setting last modification time
    last_mod_times = get_file_modification_times(root, file_types)


    while True:
        # Getting current modification times
        current_mod_times = get_file_modification_times(root, file_types)

        # Run main task (searching) if the state has changed since last change
        if current_mod_times != last_mod_times:
            most_common_words = searching()
            print(f"\nMost common words in all files: {most_common_words}")
            last_mod_times = current_mod_times.copy()

        # Just a print to make sure it works :)
        print("\nVerifying every 60 seconds..")
        time.sleep(10)  # Sleep 60 seconds between checks
