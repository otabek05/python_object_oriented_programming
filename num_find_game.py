import random


def find_number(x=10):
    tasodifiy_son=random.randint(1,x)
    print(f"I think a number from 1 to {x}. Can you find it?", end='')
    taxminlar=0
    while True:
        taxminlar+=1
        taxmin=int(input('>>>'))
        if taxmin>tasodifiy_son:
            print('please enter smaller amount')
        elif taxmin<tasodifiy_son:
            print('please enter greater amount')
        else:
            print('You won!!')
            break
    print(f'Congratulations!! you won with {taxminlar} guesses ')
    return taxminlar


def find_number_pc(x=10):
    input(f'think a number from 1 to 10 and press any keyword! I will try to find the number you will have thought')
    quyi=1
    yuqori=x
    taxminlar=0
    while True:
        taxminlar+=1
        if quyi!=yuqori:
            taxmin=random.randint(quyi,yuqori)
        else:
            taxmin=quyi
        javob=input(f'Your guess is {taxmin}! if it is true (t), if your guess is higher (+) otherwise(-)')
        if javob=='-':
            yuqori=taxmin-1
        elif javob=='+':
            quyi=taxmin+1
        else:
            break
    print(f'I have found the number with {taxminlar} try!!!')
    return taxminlar


def play(x=10):
    again=True
    while again:
        taxminlar_pc=find_number_pc(x)
        taxminlar_user=find_number(x)
        if taxminlar_user>taxminlar_pc:
            print(f'I won with {taxminlar_pc} try')
        elif taxminlar_user<taxminlar_pc:
            print(f'you won with {taxminlar_user} try')
        else:
            print('Durrang')
        yana=input('do you wanna countinue the game? yes(y) no(n)')
        if yana=='y':
            again=True
        else:
            break


play()