import os
os.system('color 3f')
import win32com.client as wincl
speak =wincl.Dispatch("SAPI.spVoice")
score=0
print("hey buddy! i'm Echo")
speak.Speak("hey buddy! i'm Echo")
print("what's your name?")
speak.Speak("what's your name?")
name = input()
print("i'm delighted to meet you " +name)
speak.Speak("i'm delighted to meet you " +name)
print("by the way what's your age? ")
speak.Speak("by the way what's your age? ")
age= int(input())
print("okay,you will be " +str(int(age)+1) + " next year" )
speak.Speak("okay,you will be " +str(int(age)+1) + " next year")



if (age<=1000):
    print("Young people recognize the big challenges that are coming up")
    speak.Speak("Young people recognize the big challenges that are coming up")
    print("that sounds good right..!")
    speak.Speak("that sounds good right...!")
    speak.Speak("shall we play a game ?, for the correct answer 10 points will be awarded and for wrong ones -5 ")
    reply= input("shall we play a game ?, for the correct answer 10 points will be awarded and for wrong ones -5 ")
    
    
    
    
    
    if reply == "yes":
        
        
        speak.Speak("1. Some months have 31 days, others have 30 days, but how many have 28 days? ")
        reply = input("1. Some months have 31 days, others have 30 days, but how many have 28 days? ")
        
        if reply == "all":
            print("yes! you are correct")
            speak.Speak("yes! you are correct")
            score+=10
        else:
            print("no, you are mistaken!  the answer is all months will have 28 days")
            speak.Speak("no, you are mistaken!  the answer is all months will have 28 days")
            score-=5
            
        speak.Speak(" 2. Where is an ocean with no water ? ")
        reply = input(" 2. Where is an ocean with no water ? ")
        
        if reply == 'map':
            print("yes! you are correct")
            speak.Speak("yes! you are correct")
            score+=10
        else:
            print("no you were wrong the answer is MAP ")
            speak.Speak("no you were wrong the answer is MAP ")
            score-=5
            
        speak.Speak(" 3. which is correct PENGUINS FLIES OR PENGUIN FLIES ")    
        reply = input(" 3. which is correct PENGUINS FLIES OR PENGUIN FLIES ")
        if reply == "none":
            print("yes! you were correct")
            speak.Speak("yes! you were correct")
            score+=10
        else:
            print("the answer is NOTA.. don't you know penguins cannot fly..")
            speak.Speak("the answer is NOTA.. don't you know penguins cannot fly..")
            score-=5
            
        speak.Speak(" 4. A is the father of B but B is the not son of A  ")
        reply = input(" 4. A is the father of B but B is the not son of A  ")
        if reply == "daugther":
            print("you are good!")
            speak.Speak("you are good!")
            score+=10
        else:
            print("no it's not correct. the answer is daugther")
            speak.Speak("no it's not correct. the answer is daugther")
            score-=5
            
        speak.Speak(" 5. what has a head and a tail but no body ? ")
        reply = input(" 5. what has a head and a tail but no body ? ")
        if reply == "coin":
            print("you are great!")
            speak.Speak("you are great!")
            score+=10
        else:
            print("no the answer is a coin! beter luck next time  ")
            speak.Speak("no the answer is a coin! beter luck next time ")
            score-=5
        speak.Speak(" 6. which animal will contain another animal?")
        reply= input("6. which animal will contain another animal ?")
        if reply == "elephant":
            print("winning is an art")
            speak.Speak("winning is an art")
            score+=10
        else:
            print("you lose.. the answer is ELEPHANT ")
            speak.Speak(" you lose.. the answer is ELEPHANT ")
            score-=5
            
        speak.Speak(" 7. what is the first name of GOOGLE ? ")
        reply = input(" 7. what is the first name of GOOGLE ? ")
        if reply == "backrub":
            print("you are genius..i think you are techie")
            speak.Speak("you are genius..i think you are techie")
            score+=10
        else:
            print("simply GOOGLE it!..lol")
            speak.Speak("simply GOOGLE it!..lol")
            score-=5
            
        speak.Speak("8. what is the full form of virus ? ")
        reply = input("8. what is the full form of virus ? ")
        if reply == "vital information resource under seize":
            print("yes it is")
            speak.Speak("yes it is")
            score+=10
        else:
            print("here goes the answer.. vital information resource under seize")
            speak.Speak("here goes the answer.. vital information resource under seize")
            score-=5
            
        speak.Speak(" 9. a number which can produce same value by adding or multiplying itself ")
        reply =input(" 9. a number which can produce same value by adding or multiplying itself ")
        if reply == "two":
            print("yes, you are correct")
            speak.Speak("yes, you are correct")
            score+=10
        else:
            print("no, the answer is 2")
            speak.Speak("no, the answer is 2")
            score-=5
            
        speak.Speak(" 10. how many sides  does a circle have ? ")
        reply= input(" 10. how many sides  does a circle have ? ")
        if reply == "two":
            print("the answer is !true... two sides INSIDE AND OUTSIDE")
            speak.Speak("the answer is !true.. two sides INSIDE AND OUTSIDE")
            score+=10
        else:
            print("the answer is !false")
            speak.Speak("the answer is !false")
            score-=5
        
        
            
    else:
        print("okay, nice to meet you, bye.")
        speak.Speak("okay, nice to meet you ,bye.")
        
        
    
    
    
    
        

else:
    print("hai")

print("you have scored",+score,"points out of 100")

print("nice to meet you i litreally enjoyed talking with you and thank you for my developer ROSHAN PRASAD                                                                             ")
speak.Speak("nice to meet you i litreally enjoyed talking with you and thank you for my developer ROSHAN PRASAD                                                                        ")
