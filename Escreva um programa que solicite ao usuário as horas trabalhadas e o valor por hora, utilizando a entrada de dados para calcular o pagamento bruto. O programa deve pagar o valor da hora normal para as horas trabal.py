score1 = input("Enter Score: ")
try:
    score=float(score1)
    score < 0 
    score > 1
except:
    print( 'wrong' )
    quit()
    
if score < 0.6: 
    print ("F")
elif score == 0.6 or score < 0.7:   
    print ("D") 
elif score == 0.7 or score < 0.8:    
    print ("C")
elif score == 0.8 or score < 0.9:   
    print ("B")
elif score == 0.9:   
    print ("A")
     
     
     