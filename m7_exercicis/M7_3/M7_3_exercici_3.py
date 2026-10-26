#L’usuari/ària ha d’introduir una frase i el programa ha de dir si la frase és un palíndrom.

sentence: str = input('Write a sentence: ').lower().replace(" ","")

invertedSentence: str = ""

for caracter in sentence:
    invertedSentence = caracter + invertedSentence

if sentence == invertedSentence:
    print('The sentence IS a palindrome')
else:
    print('The sentence IS NOT a palindrome')