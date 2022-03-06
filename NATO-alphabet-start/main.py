import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())

#Create a dictionary
#{new_key:new_value for (index,row) in df.iterrows()}
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#print(phonetic_dict)


#Create a list of the phonetic code words from a word that the user inputs
import sys
try:
    word = input("Enter a word: ").upper()
except:
    print("Please enter characters!")
    sys.exit()
#new_list = [new_item for item in list if test]
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
