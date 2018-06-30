string = input("che cavolo vuoi? ")

def palindromo(word):
    if string[::-1] == string:
        return True
    else:
        return False 
    

def palindromo2(word):
    word = word.replace(" ","")
    for i in range(len(word) // 2):
        if word[i] != word[len(word)-1-i]:
            return False

    return True

if palindromo2(string):
    print("Che bello hai trovato un Palindromo!")
else:
    print('Spiacente. Non e\' palindroma.')
    