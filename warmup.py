import math

def helloworld():
    print("Hello, world!")
helloworld()    

def board():
    pion = '|'.join(['  ']*3)
    poziom = '\n{}\n'.format('-'*8)
    print(pion,pion,pion,sep=poziom)
board()    
def tictactoe():
    pion = 'H'.join(['  |  |  ']*3) + '\n'
    poziom ='H'.join(['--+--+--']*3) + '\n'
    blok = pion.join([poziom]*3)
    separator = '+'.join(['='*8]*3) + '\n'
    print(blok,blok,blok,sep=separator)
tictactoe()
def multiples():
    for i in range (0,1002):
        if i%5==0:
            print(i,end=' ')
        elif i%3==0:
            print(i,end=' ')
        i=i+1
multiples()
def collatz(number):
    if number%2==0:
        print(number, "->", end=' '),
        number=number/2        
        collatz(number)
    elif number%2==1:
        if number==1:
            print(number)
        else:
            print(number, "->", end=' '),
            number=3*number+1            
            collatz(number)
collatz(55)
def converter():
    while True:
        try:
            fahr = float(input("Temperature F? "))
        except KeyboardInterrupt:
            print("\nExiting converter...")
            break
        except ValueError as exc:
            print(exc)
        else:
            cels = (fahr - 32) * 5 / 9
          
            print("It is {} degrees Celsius".format(cels))
converter()            


