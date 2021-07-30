import json 
file_to_translate= input("Hi, please indicate the .txt file to translate: ")

# Lolspeak dictionary from selected file.
def clean_dic(file):
    """
    Creates a dictionery from a list.txt
    
    Input:
    file: file with the dictionary
    
    Output:
    data_clean_dictionary: clean dictionary
    
    """
    file = open(file,"r")
    data = file.read() 

    data_clean = data.replace("\n ","") 
    data_clean_dictionary =json.loads(data_clean)
        
    return data_clean_dictionary

#create the lol dictionary
loldic=clean_dic("loldictionary.txt") 

#Translate file
text = open(file_to_translate,"r") 
data = text.read() 

# To keep the linebreack, we change the separator
data_characters = data.replace("\n", " >>><<< ")

# Separate special characters from words
data_characters = data_characters.replace ("!", " !")
data_characters = data_characters.replace (")", " )")
data_characters = data_characters.replace ("?", " ?")
data_characters = data_characters.replace ("(", "( ")
data_characters = data_characters.replace (",", " ,")
data_characters = data_characters.replace (":", " :")

# List with each word and special characters
words= data_characters.split() 

#Translation
words_lol = [] 

# For each word of the text
for w in words: 
    
    # Do this word have a match in the dictionary?
    match = False 
    # Do this word have is in lowercase?
    lower = False 
    
    # Transform all words to lowercase
    w_l = w.lower() 
    
    # Check if the original word was in lowercase
    if w == w_l:
        lower = True    
    
    # Check if the lowercase world is in dictionary
    for d in loldic: 
        if w_l==d: 
            match = True
            
    # If there is a match, change the word for the lolspeak word        
    if match == True and lower == True:
        words_lol.append(loldic[w_l])
    elif match == True and lower == False:
        words_lol.append(loldic[w_l].capitalize())
    else:
        words_lol.append(w)

# Create a new string with the text of the translated list
data_lol_characters = ""
for w in words_lol:
    data_lol_characters = data_lol_characters + w + " "

# Convert special character as they were inicially
data_lol = data_lol_characters.replace(" >>><<< ","\n")
data_lol = data_lol.replace (" !", "!")
data_lol = data_lol.replace (" )", ")")
data_lol = data_lol.replace (" ?", "?")
data_lol = data_lol.replace ("( ", "(")
data_lol = data_lol.replace (" ,", ",")
data_lol = data_lol.replace (" :", ":")

# Save the file
lol_name = file_to_translate.replace(".txt","") + "_lolcat.txt"
file_lol = open(lol_name, "w")
file_lol.write(data_lol)
file_lol.close()