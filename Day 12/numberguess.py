import random
actual=random.randint(1,100)
flag=True
count=0
while flag is True:
        count+=1
        guess=int(input("Guess a Number between 1-100 :- "))
        if(guess>actual):
            print("Guessed Number High, Try Low")
        elif(guess==actual):
            print("You guessed "+str(actual)+" it is Correct..")
            flag=False
        else:
            print("Guessed Number Low,Try High")
        print("You Have "+str(10-count)+" Chances Left")
        if(count==10):
            print("Game Over")
            flag=False
        
    
