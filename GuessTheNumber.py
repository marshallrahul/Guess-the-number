import random

def guess_the_number(): 

    playing = True
    
    while playing:
        i = random.randint(1, 20) 
        # print(i)
        a = 7
        while True:
            try:
                while True:
                    val = int(input("\nEnter a number between (1-20): ")) 
                    if val > 20 or val < 0:
                        print("Invalid number!!!\n")
                        break
                    else:
	                    break
                
                a -= 1
                print("\nAttempt remaining: {}".format(a))    # number of attempt
                # check lose
                if a == -1:    
                    print("\nThe number is : {}".format(i))
                    print("\nLOSE")
                    break
                
                # check win
                if val == i:    
                    print("\nYOU HAVE WON")
                    break

                # range of close numbers
                rang1 = [num for num in range(i, i+2)]
                rang2 = [num for num in reversed(range(i-2, i))]
                
                # check the number 
                if val in rang1:    
                    print("little too high")
                elif val in rang2:
                    print("little too low")
                elif val not in rang1 and (val > i):
                    print("too high")
                elif val not in rang2 and (val < i):
                    print("too low")
            
            except ValueError:
                print("An error ocured!")

        d = str(input("\nDo you want to play again (y/n): "))
        if d.lower() == 'y':
            playing = True
        else:
            print("\nThanks for playing!")
            playing = False
	        
guess_the_number()
