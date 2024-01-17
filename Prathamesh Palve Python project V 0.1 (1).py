#!/usr/bin/env python
# coding: utf-8

# 

# In[1]:


def class_welcome_bot():
    #Welcome to NetTech bot
    #welcome user
    print("Welcome to NetTech")
    #ask user to its name
    user_name=input("Enter you rname here: ")
    #greet user 
    print("Hello",user_name) 
    #ask user to its mobile number
    user_mob=input("Enter your mobile number here: ")
    #display users mobile number
    print("your mobile number is",user_mob)
    #ask user to email id
    user_email=input("Enter your email id here: ")
    #display user email id
    print("Your email id is:",user_email)
    #ask user to its preferred course
    course=input("Enter your preferred course here:")
    #display users preffered course
    print("Your preferred course is:",course)
    #ask user to its preferred location
    location=input("Enter your preferred location here:")
    #display users location
    print("your preferred location is:",location)
    


def recommendation_bot():
    #Mumbai's Recommedation chai bot
    #user welcome
    print("Welocme to the city of Garma chai | AAmchi Mumbai!")
    #ask user to its name
    name=input("Please Enter your name here: ")
    #greet user
    print("Hello",name)
    #ask user to budget for chai
    budget=int(input("Please Enter your budget here: "))
    #>500 --> go to taj hotel
    if budget>=500:
        print("Go to Taj Hotel")
    #100-500 --> go to starbucks
    elif budget>=100 and budget<500:
        print("Go to Starbucks")
    #50-100 --> go to udipi hetel
    elif budget>=50 and budget<100:
        print("Go to udipi hotel")
    #20-50 --> go to prathamesh's cafe
    elif budget>=20 and budget<50:
        print("Go to cafe")
    #5--20 --> go to tapri
    elif budget>=5 and budget<20:
        print("Go to Tapri better than 5 star hotel")
    else:
        print("Go back to simon!")
    



def shoes_recommendation_bot():  
    #Running Shoes Recommendation bot
    #WElcome user
    print("Welcome to the Shoes Recommendation bot!")
    #ask suer to its name
    name=input("Please Enter your Name here: ")
    #Greet user
    print("Hello",name)
    #Ask user to its budget
    budget=int(input("Please Enter your budget here: "))
    #display result according to users budget
    #>5000 buy Nike shoes
    if budget>=5000:
        print("Buy a Nike Running shoes")
    #3000-5000
    elif budget>=3000 and budget<5000:
        print("Buy an adidas shoes")
    #1000-3000
    elif budget>=1000 and budget<3000:
        print("buy a decathlon shoes | Better than others")
    #500-1000
    elif budget>=500 and budget<1000:
        print("buy a sega shoes ")
    #<500 
    else:
        print("No recommendation for this budget")


def GK_Quiz():
    #GK QUiZ
    #Welocme user
    print("WElcome to India GK Quiz")
    user_ans=input("What is the National Animal of India: ")
    #show correct answer
    if user_ans=="tiger":
        print("Your Answer is correct")
    else:
        print("Your Answer is Wrong")
    GK_Quiz()

def heads_and_tails():
    #Heads and Tails Game
    #Welcome user
    print("Welcome to the Heads and Tails Game!")
    #ask user tot heads or tails
    user_choice=input("Please choose heads or tails")
    #display user choice
    print("you choose:",user_choice)
    #coin toss
    import random
    if(random.choice('ht'))=='h':
        coin_toss='Heads'
    else:
        coin_toss='Tails'
    #display coin result
    print("coin Result:",coin_toss)
    #if user choice is equal to coin toss --> you win
    if user_choice.lower()==coin_toss.lower():
        print("You win!")
    #else --> you lose!
    else:
        print("you lose!")
    heads_and_tails()

def dice_game():
    #Dice Game!
    ##Welcome user
    print("WElcome to the Dice Game!")
    #ask user to its choice
    user_choice=int(input("Please Enter your choice here: "))
    if user_choice>=1 and user_choice<=6:
        print("You choose: ",user_choice)
        #after scrolling the roll
        import random
        dice_roll=int(random.choice('123456'))
        #display result
        print("display result: ",dice_roll)
        #if the user choice is equal to dice roll --> you win
        if user_choice==dice_roll:
            print("you win!")
        else:
            print("you lose!")
    else:
        print("Invalid Numbers",user_choice)



def two_dice_game():
    #Welcome to two dice game
    print("Welcoem to to Two Dice Game!")
    #Enter a input between (2-12)
    user_choice=int(input("Enter a number between 2 to 12: "))
    if user_choice>=2 and user_choice<=12:
        print("you choose",user_choice)

    #dice roll
        import random
        dice_roll=random.randrange(2,13)
    #display result
        print("Dispaly result",dice_roll)
    #if user choice and dice roll is equal--> you win
        if user_choice==dice_roll:
            print("you win!")
        else:
            print("you lose")
    else:
        print("invalid input",user_choice)

def mulitiplication_table():
    #Welcome to Multiplication table
    #Welcome user
    print("Welocme to multiplication table")
    #take 1 number from user
    num=int(input("Please Enter your number here:"))
    #display multiplication table
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

def cube():
    #Welcome to the cube table
    #Welcome user
    print("WElcome to Cube tables")
    #take 1 number from user
    num=int(input("Enter your number here: "))
    #display cube
    print ('cube of ',num, '=',num**3)


def factorial():
    #Welcome to finding factorial method
    #Welcome user
    print("Welcome to find factorial Website!")
    #ask user to take 1 number as input
    num=int(input("Enter your number here: "))
    n=1
    #display factorial 
    for i in range(1,num+1):
        n=n*i
    #Display factorial of the number
    print(n)


def fionacci_series():
    #Welcome to fibonacii series
    #WElocme user
    print("Welcome to the world of fibonacci Series")
    #ask user take 1 number as input
    # user_input=int(input("Enter your number here: "))
    a=0
    b=1

    for i in range(1,10):
        c=a+b
        print(c)
        a=b
        b=c

    

def password_generator():
    #Password gneerator
    #Welcome user
    print("Welcome to a strong  password generator platform!")
    #ask your to how many characters of password is want
    num=int(input("Plese Enter your number here: "))
    if num>=8:
        print("you choose:",num)
        import random
        import string
        password=''
        #display password
        for i in range(num):
            password=password+random.choice(string.ascii_letters+string.digits+string.punctuation)
        print(password)
    else:
        print("Sorry you should type at least 8 characters of password")

def countdown_timer():  
    from countdown import countdown 
    countdown(mins=1,secs=9)
    countdown(1)
    countdown(mins=0,secs=10)

def mind_game():
    #Mind game
    #WElcome user
    print("WElcome to the world of Mind Game!")
    #predicat a one number between 1-5000
    print("Predicate a one numbers between 1 -5000")
    import time
    time.sleep(3)
    #multiply that number with 2
    print("Mutlipy the predicated number by 2")
    time.sleep(3)
    #add 50 on that number
    print("Add 50 on mulitiply number")
    time.sleep(3)
    #divide that number by 2
    print("Divide that number by 2")
    time.sleep(3)
    #now minus guess number from current number
    print("Minus guess number from the current number")
    time.sleep(5)
    #now you will get 25 answer
    print("Now you will you get 25 Answer")


# In[ ]:





# In[ ]:





# In[ ]:





# 
# 

# In[ ]:


#importing tkinter library 
import tkinter as tk

#creating a main window
window=tk.Tk()

#chang title 
window.title('Prathamesh Palve')

#size
window.geometry('730x500')

#label
tk.Label(window,text='Python project',font=('Helvetica',21),bg='black',fg='red').place(x=270,y=30)
tk.Label(window,text='Made by: Prathamesh Palve',font=('Helvetica',16,'bold')).place(x=220,y=100)

#Button
tk.Button(window,text='Welcome Bot',command=class_welcome_bot,bg='orange',fg='black').place(x=50,y=150,width=200,height=25)
tk.Button(window,text='Recommendation Bot',command=recommendation_bot,bg='orange',fg='black').place(x=270,y=150,width=200,height=25)
tk.Button(window,text='Shoes Recommendation Bot',command=shoes_recommendation_bot,bg='orange',fg='black').place(x=490,y=150,width=200,height=25)
tk.Button(window,text='Gk Quiz',command=GK_Quiz,bg='orange',fg='black').place(x=50,y=200,width=200,height=25)
tk.Button(window,text='Heads and Tails Game',command=heads_and_tails,bg='orange',fg='black').place(x=270,y=200,width=200,height=25)
tk.Button(window,text='Dice Game',command=dice_game,bg='orange',fg='black').place(x=490,y=200,width=200,height=25)
tk.Button(window,text=' Two Dice Game ',command=two_dice_game,bg='orange',fg='black').place(x=50,y=250,width=200,height=25)
tk.Button(window,text='Multipliction Table  ',command=mulitiplication_table,bg='orange',fg='black').place(x=270,y=250,width=200,height=25)
tk.Button(window,text=' Cube',command=cube,bg='orange',fg='black').place(x=490,y=250,width=200,height=25)
tk.Button(window,text=' Factorial ',command=factorial,bg='orange',fg='black').place(x=50,y=300,width=200,height=25)
tk.Button(window,text=' Fibonacaii ',command=fionacci_series,bg='orange',fg='black').place(x=270,y=300,width=200,height=25)
tk.Button(window,text='password generator ',command=password_generator,bg='orange',fg='black').place(x=490,y=300,width=200,height=25)
tk.Button(window,text=' countdown generator',command=countdown_timer,bg='orange',fg='black').place(x=50,y=350,width=200,height=25)
tk.Button(window,text='password generator ',command=password_generator,bg='orange',fg='black').place(x=270,y=350,width=200,height=25)
tk.Button(window,text='Mind Game ',command=mind_game,bg='orange',fg='black').place(x=490,y=350,width=200,height=25)





#this is important to write

window.mainloop()



# In[2]:





# In[ ]:





# In[ ]:




