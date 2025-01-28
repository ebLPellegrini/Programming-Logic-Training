firstChoice = input()
secondChoice = input()
thirdChoice = input()

if firstChoice == 'vertebrado':
    if secondChoice == 'ave':
        if thirdChoice == 'carnivoro':
            print('aguia')
        elif thirdChoice == 'onivoro':
            print('pomba')
        else:
            print('Input nao aceito')
    elif secondChoice == 'mamifero':
        if thirdChoice == 'onivoro':
            print('homem')
        elif thirdChoice == 'herbivoro':
            print('vaca')
        else:
            print('Input nao aceito')
    else:
        print('Input nao aceito')
elif firstChoice == 'invertebrado':
    if secondChoice == 'inseto':
        if thirdChoice == 'hematofago':
            print('pulga')
        elif thirdChoice == 'herbivoro':
            print('lagarta')
        else:
            print('Input nao aceito')
    elif secondChoice == 'anelideo':
        if thirdChoice == 'hematofago':
            print('sanguessuga')
        elif thirdChoice == 'onivoro':
            print('minhoca')
        else:
            print('Input nao aceito')
    else:
        print('Input nao aceitot')
else:
    print('Input nao aceito')