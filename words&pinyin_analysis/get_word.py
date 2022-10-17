import pkg_resources
from symspellpy.symspellpy import SymSpell
import csv

sym_spell = SymSpell(max_dictionary_edit_distance=0, prefix_length=7)
dictionary_path = pkg_resources.resource_filename("symspellpy", "frequency_dictionary_en_82_765.txt")
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

def clear_words(password):
    clear_password = ''
    for p in password:
        if p.isalpha() == True:
            clear_password += p
    return clear_password
# print(clear_words('sss11ss'))
def find_words(password):
    try:
        result = sym_spell.word_segmentation(password)
    except IndexError:
        return None
    else:
        passwords = result.corrected_string.split(" ")
        if result.distance_sum == len(passwords) - 1:
            return passwords
        else:
            return None
# xx = find_words('dictionary')
# print(xx)
total_words = []
with open('yahoo.csv') as file:   #读入文件

    lines = csv.reader(file)
    print(lines)
    for line in lines:   #逐行读入
        password = ''.join(line)
        password = clear_words(password)
        # print(password)
        words = find_words(password)
        if words !=None:
            for word in words:
                total_words.append(word)
                print(word)
print(total_words)
# total_words = ['i','love','you','hello','love']
words_count = {}
for single_word in total_words:
    # if(len(single_word) == 1) and (single_word != 'i' or single_word != 'I' or single_word != 'a' or single_word != 'A' or single_word != 'u' or single_word != 'U'):
    #     continue
    if single_word not in words_count:
        words_count[single_word] = 1
    else:
        words_count[single_word] += 1
print(words_count)
re = sorted(words_count.items(), key=lambda item:item[1], reverse=True)
print(re)
