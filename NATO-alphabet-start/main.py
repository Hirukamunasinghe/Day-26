import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data.to_dict())

#Create a dictionary
#{new_key:new_value for (index,row) in df.iterrows()}
phonetic_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(phonetic_dict)
#print(phonetic_dict)


#Create a list of the phonetic code words from a word that the user inputs



#new_list = [new_item for item in list if test]
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
