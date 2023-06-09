my_dict = {
    1: 'AEIOULNSTRАВЕИНОРСТ',
    2: 'DGДКЛМПУ',
    3: 'BCMPБГЁЬЯ',
    4: 'FHVWYЙЫ',
    5: 'KЖЗХЦЧ',
    8: 'JXШЭЮ',
    10: 'QZФЩЪ'
}

my_word = (input('Введите слово на английском или русском: ')).upper()
points = 0

for i in range(len(my_word)):
    for key in my_dict:
        if (my_word[i] in my_dict[key]):
            points += key

print(my_word)
print(points) 