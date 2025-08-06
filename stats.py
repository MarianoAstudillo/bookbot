def get_num_words(filepath):
  with open(filepath) as f: 
    file_contents = f.read()
  return file_contents

def count_words(text): 
  num_words = text.split()
  return len(num_words)

def count_characters(text):
  dictionary = {}
  for char in text:
    char = char.lower()
    if char not in dictionary: 
      dictionary[char] = 1
    else:
      dictionary[char] += 1
  
  return dictionary

def sort_on(items):
  return items["num"]

def make_report(num_words, dictionaryChars, path):
  list_chars = []
  for letter in dictionaryChars:
    list_chars.append({'char': letter, 'num': dictionaryChars[letter]})
  
  list_chars.sort(reverse=True, key=sort_on)
  return list_chars