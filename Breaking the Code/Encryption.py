# Input text to code
text_original = input("Enter the code to cipher: ")

# This encrryption only consider lower case text
text_original = text_original.lower()

text_original_list = list(text_original)
dictionary = {"a":1, "b":2, "c":3, "d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,
              "l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,
              "u":21,"v":22,"w":23,"x":24,"y":25,"z":26, " ":27, ",":28, "!":29, "?":30,".":31}

# Creating an RSA key pair
p = 13 
q = 17  

#Public key n and e
n =p*q
phi_n = (p-1)*(q-1)
e = 5


#Private key d
i = 2
d = int((i*phi_n+1)/e)

# leters to numbers
text_original_number_list = []

for letter in text_original_list:
    text_original_number_list.append(dictionary[letter])

# Numbers to Code
text_coded_number_list = []

for number in text_original_number_list:
    c = (number**e)%n # % = mod = resto una divición // ** = ^
    text_coded_number_list.append(c)

# Coded text
text_coded = ""
for number in text_coded_number_list:
    text_coded = text_coded + str(number) + ","
    
print(text_coded)