import os, sys, math, random
def creategui(arglist,clear=False,backbone=False):
    if clear == True:
        for i in range(100):
            print("")
    
    masterlaenge = 0
    for i in range(len(arglist)):
                   roflkopter = "|[" + str(i) + "] - " + arglist[i]
                   rofllaenge = len(roflkopter)
                   if rofllaenge > masterlaenge:
                       masterlaenge = rofllaenge
    print(str(masterlaenge))
    rouven = ""               
    #print("+---------------------+")
    print("+" + "-"*(masterlaenge - 1) + "+")
    for i in range(len(arglist)):
        # Jedem das an länge geben, was ihm zum längsten fehlt
        whattoprinta = "|[" + str(i+1) + "] - " + arglist[i]
        howmuchrouven = masterlaenge - len(whattoprinta)
        whattoprintb = whattoprinta + " "*howmuchrouven + "|"
        print(whattoprintb)
    if backbone == True:
        whattoprinta = "|[0] - << Back <<" 
        howmuchrouven = masterlaenge - len(whattoprinta)
        whattoprintb = whattoprinta + " "*howmuchrouven + "|"
        print(whattoprintb)
    print("+" + "-"*(masterlaenge - 1) + "+")

    lool = 99999999
    while lool > len(arglist):
        lool = int(input("[?]>"))
        if lool > len(arglist):
            print("FEHLER: Ungültie eingabe. Erneut versuchen")
    return lool
    
        
