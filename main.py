import pandas as pd
import random as r

df = pd.read_csv('languagelist.csv', index_col=0)

print('The romanized spelling of a japanese phrase will come up, Type out what the phrase says in english \nwith no punctuation: ')
numbers = []
while True:
    numb = r.randint(1,32)
    while numb in numbers:
        numb = r.randint(1,32)

    phrase = df['Phrases'][numb]
    translation = (df['Translation'][numb]).lower()
    print(phrase)
    userInp = input('Translate: ').lower()

    if translation == userInp:
        numbers.append(numb)
        print('-------!CORRECT!-------')
    else:
        print(f'-------!WRONG!-------\n---The Correct Answer is {translation}---')
        
