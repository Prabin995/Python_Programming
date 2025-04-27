def camel_back(s):
    # Condition for removing _ from given string
    parts = s.split('_')
    # Condition for Capitalize letter after _ except first letter
    camel_case = parts[0] + ''.join(word.capitalize() for word in parts[1:] if word)
    return camel_case

#Testing some cases
print(camel_back('uusi_muuttuja'))      
print(camel_back('temp__muuttuja'))     
print(camel_back('kolmion_pinta_ala'))  