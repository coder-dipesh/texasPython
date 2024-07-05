

def countUpperLower(paragraph):
    # Create a dictionary 'count' to store the count of upper and lower case characters
    count = {
      "UPPER_CASE": 0,
      "LOWER_CASE": 0
            }
    # Loop through the string 
    for character in paragraph:
        if character.isupper():
            count["UPPER_CASE"] += 1
        elif character.islower():
            count["LOWER_CASE"] += 1
        else:
            pass
    
    print("Original String: ", paragraph)
    print("No. of Upper case characters: ", count["UPPER_CASE"])
    print("No. of Lower case Characters: ", count["LOWER_CASE"])


# Call the 'string_test' function with the input string 'The quick Brown Fox'
countUpperLower('The quick Brown Fox') 
