#1
pets={}
print("введите имя питомца:")
pitomets = input()
slPit ={}
print("введите вид питомца:")
slPit["Вид питомца"] = input()
print("введите возраст питомца:")
slPit["Возраст питомца"] = int(input())
print("введите имя владельца:")
slPit["Имя владельца"] = input()

pets[pitomets] = slPit

keysPit = list(slPit.keys())

ValuesPit = list(slPit.values())

GG = "года"

if ValuesPit[1]%10 == 0 or ValuesPit[1]%10 >5 or (ValuesPit[1] > 5 and ValuesPit[1] < 21): 
    GG = "лет"
elif ValuesPit[1]%10 == 1:
    GG = "год"

print("Это " + ValuesPit[0] + " по кличке " + pitomets + ". " + str(keysPit[1]) + ": " + str(ValuesPit[1]) + " " + GG + ". " +  str(keysPit[2]) + ": "+ str(ValuesPit[2]))

#print(pets)

#2
print("введите число от:")
numOt = int(input())

print("введите число до:")
numDo = int(input())

my_dict = {}

while numOt <= numDo: 
    my_dict[numOt] = numOt**numOt
    numOt+=1
    
print(my_dict)

