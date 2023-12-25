import numpy as np

def StringEncoder(array):

    newArray = np.array([])

    for i in range(0, len(array)):

        newStr = np.str_('')

        s = np.str_(array[i])
        newS = ''

        for y in range(0, len(s)):
            if(s[y].isalpha()):
                newS += s[y]
        print(newS)

        for x in range(0, len(newS)):

            if(newS[x].isalpha() and x % 2 == 1):
                alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                            'n','o','p','q','r','s','t','u','v','w','x','y','z']
                for j in range(0, len(alphabet)):
                    
                    if newS[x].lower() == alphabet[j]:
                        print((alphabet.index(newS[x].lower()) + 1) + 
                              (alphabet.index(newS[x - 1].lower()) + 1))
                        newStr += np.str_((alphabet.index(newS[x].lower()) + 1) + 
                                          (alphabet.index(newS[x - 1].lower()) + 1))
        print(newStr)
        newInt = int(newStr)
        newArray = np.append(newArray, newInt)
    
    return newArray


array = np.array(['Snyder, Mrs. John Pillsbury (Nelle Stevenson)'])

print(StringEncoder(array))