# Define the keypad mapping at the top of your file
keys = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

def return_all_words(input):
    if input == '':
        return ['']

    ans = []

    smallInput = input[1:]
    smallInputWords = return_all_words(smallInput)

    keyLetter = keys[input[0]]

    for myChar in keyLetter:
        for word in smallInputWords:
            ans.append(myChar + word)

    return ans

# Call the function and print the output
output = return_all_words("23")
print(output) 

result =return_all_words('23')
print (result)