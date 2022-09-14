print('Assalom alaykum')

def ranged(min,max, path=1):
    numbers=[]
    while min<max:
        numbers.append(min)
        min+=path
    return numbers

x=ranged(0,20,2)
print(x)

print('karra jadval')

for num in range(1,11):
    for son in range(1,11):
        print(f'{num}x{son}={num*son}')
    print('here is next one!!!')

g
def changer():
    x=int(input('enter number to see in letter version'))
    if x==0:
        print('no/l')
    elif x==1:
        print('one')
    elif x==2:
        print('two')
    elif x==3:
        print('three')


changer()