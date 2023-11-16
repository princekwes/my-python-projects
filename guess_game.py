print("Welcome  To my computer Game")

score = 0
answer = input(" Do   you  want  to play? ")
if answer.lower() != "yes":
    quit()
    
answer = input( " What Is The Meaning of RAM?: ")
if answer.lower() == "random access memory":
    print( "Corect!")
    score += 1
else:
    print(" You Got  It Wrong! ")


answer = input( " What Is The Meaning of CPU?: ")
if answer.lower() == "central processing unit":
    print( "Corect!")
    score += 1
else:
    print(" You Got  It Wrong! ")
    
    
answer = input( " What Is The Meaning of PSU ?: ")
if answer.lower() == "power supply unit":
    print( "Corect!")
    score += 1
else:
    print(" You Got  It Wrong! ")
    
    
answer = input( " What Is The Meaning of GPU?: ")
if answer.lower() == "graphical processing  unit":
    print( "Corect!")
    score += 1
else:
    print(" You Got  It Wrong! ")

print("You Got "  + str(score) + "qustions correct! ")
print(" You Got " + str((score / 4) * 100)  + "%.")