import sys

from stats import get_num_words
from stats import count_words
from stats import count_characters
from stats import make_report

def main():

  if(len(sys.argv) < 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  path = sys.argv[1]
  book_text = get_num_words(path)

  # Count all words of the text
  num_words = count_words(book_text)
  # print(f'{num_words} words found in the document')

  # Count all characters of the text
  dictionaryChars = count_characters(book_text)
  # print(dictionaryChars)

  # Make a report
  reportList = make_report(num_words, dictionaryChars, path)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for item in reportList:
    if item['char'].isalpha():
      print(f"{item['char']}: {item['num']}")
  print("============= END ===============")

main()