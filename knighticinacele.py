# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:33:59 2022

@author: okmen
"""


from PIL import Image
from pytesseract import pytesseract
import pyautogui
import time
import keyboard
import random
import threading

#knighticin


#tamelsiyan
#G124578g*
#ahk = AHK(executable_path="D:\masaüstü\yazılımileilgilihersey\onluk\knight online\AHK\AutoHotkey.exe")
#path_to_tesseract = r"D:\masaüstü\yazılımileilgilihersey\tesseract\tesseract.exe"
path_to_tesseract = r"tesseract\tesseract.exe"
#win = ahk.find_window(title=b'Knight OnLine Client') # Find the opened window    
pytesseract.tesseract_cmd = path_to_tesseract
#win.activate()  
time.sleep(0.5)

#win.activate()  



global sundiriesetiklamavetic
def sundiriesetiklamavetic():
    
    while 1:
              
        canbari=pyautogui.locateOnScreen('knighticin/canbari.png',confidence=0.93 ,grayscale = False)
        canbari2=pyautogui.locateOnScreen('knighticin/canbari2.png',confidence=0.93 ,grayscale = False)
        if canbari !=None or canbari2 !=None:
            print("buldu")
            try:
                korx_refa, kory_refa = pyautogui.center(canbari)
            except:
                korx_refa, kory_refa = pyautogui.center(canbari2)
                        
            break
    
    
    pyautogui.click(x=korx_refa+50, y=kory_refa-20)
    pyautogui.mouseDown(button='right'); pyautogui.mouseUp(button='right')
    pyautogui.mouseDown(button='right'); pyautogui.mouseUp(button='right') 
    print("tiklama yaptı")    
    while 1:   
        ticaret=pyautogui.locateOnScreen('resimler/ticaretisteme.png',confidence=0.93 ,grayscale = True)
        ticaret2=pyautogui.locateOnScreen('resimler/ticaretisteme2.png',confidence=0.93 ,grayscale = True)
        ticaretisteme3=pyautogui.locateOnScreen('resimler/ticaretisteme3.png',confidence=0.93 ,grayscale = True)
        ticaretisteme4=pyautogui.locateOnScreen('resimler/ticaretisteme4.png',confidence=0.93 ,grayscale = True)
        ticaretisteme5=pyautogui.locateOnScreen('resimler/ticaretisteme5_carpi.png',confidence=0.93 ,grayscale = True)
        #durdur=pyautogui.locateOnScreen('resimler/durdur.png',confidence=0.93 ,grayscale = True)
        if ticaret !=None:
            print("buldu")
            korx, kory = pyautogui.center(ticaret)
            pyautogui.click(x=korx, y=kory)
            pyautogui.mouseDown(); pyautogui.mouseUp() 
            #pyautogui.mouseDown(); pyautogui.mouseUp() 
            break
        elif ticaret2 !=None:
            print("buldu")
            korx, kory = pyautogui.center(ticaret2)
            pyautogui.click(x=korx, y=kory)
            pyautogui.mouseDown(); pyautogui.mouseUp() 
            break
        elif ticaretisteme3 !=None:
            print("buldu")
            korx, kory = pyautogui.center(ticaretisteme3)
            pyautogui.click(x=korx, y=kory)
            pyautogui.mouseDown(); pyautogui.mouseUp() 
            break
        elif ticaretisteme4 !=None:
            print("buldu")
            korx, kory = pyautogui.center(ticaretisteme4)
            pyautogui.click(x=korx, y=kory)
            pyautogui.mouseDown(); pyautogui.mouseUp() 
            break
        elif ticaretisteme5 !=None:
            print("buldu")
            korx, kory = pyautogui.center(ticaretisteme5)
            #250 repair
            pyautogui.click(x=korx, y=kory+200)
            pyautogui.mouseDown(); pyautogui.mouseUp() 
            #pyautogui.mouseDown(); pyautogui.mouseUp() 
            break
        """
        elif durdur !=None:
            print("durdu")
            break
        """
        
        
sundiriesetiklamavetic()


global yhafiza_bas,yhafiza_bit
global hangisialar

try:
        hangisialar="4"
        hangisialar=hangisialar.split(",")
        
        if len(hangisialar)==1:
            
            yhafiza_bas=-1
            yhafiza_bit=1
            
        elif len(hangisialar)==2:
            
            yhafiza_bas=-1
            yhafiza_bit=2
            
        elif len(hangisialar)==3:
            
            yhafiza_bas=-1
            yhafiza_bit=3
            
        elif len(hangisialar)==4:
            
            yhafiza_bas=-1
            yhafiza_bit=4

except:pass




def inventoryislemleri():
    global yhafiza_bas,yhafiza_bit
    global hangisialar
    global korx_ref,kory_ref    
    DEVAM=True
    if DEVAM==True:
            
        def sellitemilkasama():
            global korx_ref,kory_ref    
            while 1:
              
                sell=pyautogui.locateOnScreen('resimler/sell item.png',confidence=0.93 ,grayscale = True)
                if sell !=None:
                    print("buldu")
                    pyautogui.click(x=pyautogui.center(sell)[0], y=pyautogui.center(sell)[1])
                    pyautogui.mouseDown(); pyautogui.mouseUp() 
                    break
               
            while 1:
              
                confirm=pyautogui.locateOnScreen('resimler/confirm.png',confidence=0.93 ,grayscale = True)
                if confirm !=None:
                    print("buldu")
                    pyautogui.click(x=pyautogui.center(confirm)[0], y=pyautogui.center(confirm)[1])
                    pyautogui.mouseDown(); pyautogui.mouseUp() 
                    break
            
            while 1:
              
                satmaicinref=pyautogui.locateOnScreen('resimler/satmaicinref.png',confidence=0.93 ,grayscale = True)
                if satmaicinref !=None:
                    print("buldu")
                    korx_ref, kory_ref = pyautogui.center(satmaicinref)
                    pyautogui.click(x=(korx_ref-(60*0)), y=(kory_ref+(60*2)))
                    pyautogui.mouseDown(); pyautogui.mouseUp()             
                    break
        
        
        time.sleep(2)
        sellitemilkasama()
        
        
        
        
        
        def nontradable():   
                nontradable=pyautogui.locateOnScreen('resimler/nontradable.png',confidence=0.93 ,grayscale = True)
                if nontradable !=None:
                    print("buldu")
                    pyautogui.click(x=pyautogui.center(nontradable)[0], y=pyautogui.center(nontradable)[1])
                    pyautogui.mouseDown(); pyautogui.mouseUp()          
                    
        
        
        def selltikla():
                selltikla=pyautogui.locateOnScreen('resimler/selltikla.png',confidence=0.93 ,grayscale = True)
                if selltikla !=None:
                    print("buldu")
                    pyautogui.click(x=pyautogui.center(selltikla)[0], y=pyautogui.center(selltikla)[1])
                    pyautogui.mouseDown(); pyautogui.mouseUp() 
        
        def onay2():
                onay2=pyautogui.locateOnScreen('resimler/onay2.png',confidence=0.93 ,grayscale = True)
                if onay2 !=None:
                    print("buldu")
                    pyautogui.click(x=pyautogui.center(onay2)[0], y=pyautogui.center(onay2)[1])
                    pyautogui.mouseDown(); pyautogui.mouseUp()   
               
        
        
        
        time.sleep(2)
        def siralaratikla():
            global korx_ref,kory_ref    
            global hangisialar
            for i in range(0,len(hangisialar)):
                print(i)
                
                try:
                        yicin=int(hangisialar[i])+1
                        for xicin in range(0,7):
                                
                            pyautogui.click(x=(korx_ref-(60*xicin)), y=(kory_ref+(60*yicin)))
                            time.sleep(0.2)
                            pyautogui.mouseDown(button='right'); pyautogui.mouseUp(button='right') 
                         
                        nontradable()
                        selltikla()
                        onay2()
                except Exception as e:
                    print(e)
            
            
            
        
        
        siralaratikla()
        
        def carpi():
            while 1:
              
                carpi=pyautogui.locateOnScreen('resimler/carpi.png',confidence=0.93 ,grayscale = True)
                if carpi !=None:
                    print("buldu")
                    korx, kory = pyautogui.center(carpi)
                    pyautogui.click(x=korx, y=kory)
                    pyautogui.mouseDown(); pyautogui.mouseUp()   
                    break
        
        carpi()
        
        time.sleep(0.2)
        keyboard.press("I")
        time.sleep(0.2)
        keyboard.release("I")
        def vipsandik():
            time.sleep(2)
            while 1:
                  
                    vipsandik=pyautogui.locateOnScreen('resimler/vipsandik.png',confidence=0.93 ,grayscale = True)
                    if vipsandik !=None:
                        print("buldu")
                        korx, kory = pyautogui.center(vipsandik)
                        pyautogui.click(x=korx, y=kory)
                        pyautogui.mouseDown(); pyautogui.mouseUp()   
                        break
        
        vipsandik()
        
        def depodanalhepsini():
            while 1:
                  
                    kilit=pyautogui.locateOnScreen('resimler/kilit.png',confidence=0.93 ,grayscale = True)
                    kilit2=pyautogui.locateOnScreen('resimler/kilit2.png',confidence=0.93 ,grayscale = True)
                    if kilit !=None:
                        print("buldu")
                        korx, kory = pyautogui.center(kilit)
                        break
                    elif kilit2 !=None:
                        print("buldu")
                        korx, kory = pyautogui.center(kilit2)
                        break
            
            time.sleep(2)
            while 1:
                for yicinal in range(-1,7):  
                    for xicinal in range(5,11):
                            
                        pyautogui.click(x=(korx-(60*xicinal)), y=(kory+(60*yicinal+20)))
                        time.sleep(0.2)
                        pyautogui.mouseDown(button='right'); pyautogui.mouseUp(button='right') 
                break
                
            
            while 1:
                  
                    carpi=pyautogui.locateOnScreen('resimler/carpi.png',confidence=0.93 ,grayscale = True)
                    if carpi !=None:
                        print("buldu")
                        korx, kory = pyautogui.center(carpi)
                        pyautogui.click(x=korx, y=kory)
                        pyautogui.mouseDown(); pyautogui.mouseUp()   
                        break
        
        #depodanalhepsini() eski yöntem
        
        def depodansiraylaal():
            global yhafiza_bas,yhafiza_bit
            while 1:
                  
                    kilit=pyautogui.locateOnScreen('resimler/kilit.png',confidence=0.93 ,grayscale = True)
                    kilit2=pyautogui.locateOnScreen('resimler/kilit2.png',confidence=0.93 ,grayscale = True)
                    if kilit !=None:
                        print("buldu")
                        korx, kory = pyautogui.center(kilit)
                        break
                    elif kilit2 !=None:
                        print("buldu")
                        korx, kory = pyautogui.center(kilit2)
                        break
            
            time.sleep(2)
            
                  
            while 1:
                    
                for yicinal in range(yhafiza_bas,yhafiza_bit):  
                    for xicinal in range(5,11):
                                
                        pyautogui.click(x=(korx-(60*xicinal)), y=(kory+(60*yicinal+20)))
                        time.sleep(0.2)
                        pyautogui.mouseDown(button='right'); pyautogui.mouseUp(button='right') 
                break
            
            
            if len(hangisialar)==1:
            
                yhafiza_bas=yhafiza_bit-1
                yhafiza_bit=yhafiza_bit+1
                
                if yhafiza_bit>7:
                    yhafiza_bit=7
                
            elif len(hangisialar)==2:
                
                yhafiza_bas=yhafiza_bit-1
                yhafiza_bit=yhafiza_bit+2
                if yhafiza_bit>7:
                    yhafiza_bit=7
                
            elif len(hangisialar)==3:
                
                yhafiza_bas=yhafiza_bit-1
                yhafiza_bit=yhafiza_bit+3
                if yhafiza_bit>7:
                    yhafiza_bit=7
                
            elif len(hangisialar)==4:
                
                yhafiza_bas=yhafiza_bit-1
                yhafiza_bit=yhafiza_bit+4
                if yhafiza_bit>7:
                    yhafiza_bit=7


            return yhafiza_bas
        sonuc=depodansiraylaal()
        while 1:
                  
            carpi=pyautogui.locateOnScreen('resimler/carpidepo.png',confidence=0.93 ,grayscale = True)
            if carpi !=None:
                print("buldu carpi")
                korx, kory = pyautogui.center(carpi)
                pyautogui.click(x=korx, y=kory)
                pyautogui.mouseDown(); pyautogui.mouseUp()   
                break
        if sonuc==6:
            return "bitir"
        else:
            return "devam"
        print("carpıya basması gerek")
        
       
while 1:        
    sonuc=inventoryislemleri()
    print("nerdekalmis:")
    print(sonuc)
    
    sundiriesetiklamavetic()
    #######################################
    
    #son satış
    if sonuc=="bitir":
            
        
        global korx_ref,kory_ref  
        def sellitemilkasama():
                global korx_ref,kory_ref    
                while 1:
                  
                    sell=pyautogui.locateOnScreen('resimler/sell item.png',confidence=0.93 ,grayscale = True)
                    if sell !=None:
                        print("buldu")
                        pyautogui.click(x=pyautogui.center(sell)[0], y=pyautogui.center(sell)[1])
                        pyautogui.mouseDown(); pyautogui.mouseUp() 
                        break
                   
                while 1:
                  
                    confirm=pyautogui.locateOnScreen('resimler/confirm.png',confidence=0.93 ,grayscale = True)
                    if confirm !=None:
                        print("buldu")
                        pyautogui.click(x=pyautogui.center(confirm)[0], y=pyautogui.center(confirm)[1])
                        pyautogui.mouseDown(); pyautogui.mouseUp() 
                        break
                
                while 1:
                  
                    satmaicinref=pyautogui.locateOnScreen('resimler/satmaicinref.png',confidence=0.93 ,grayscale = True)
                    if satmaicinref !=None:
                        print("buldu")
                        korx_ref, kory_ref = pyautogui.center(satmaicinref)
                        pyautogui.click(x=(korx_ref-(60*0)), y=(kory_ref+(60*2)))
                        pyautogui.mouseDown(); pyautogui.mouseUp()             
                        break
            
            
        time.sleep(2)
        sellitemilkasama()
            
            
            
            
            
        def nontradable():   
                    nontradable=pyautogui.locateOnScreen('resimler/nontradable.png',confidence=0.93 ,grayscale = True)
                    if nontradable !=None:
                        print("buldu")
                        pyautogui.click(x=pyautogui.center(nontradable)[0], y=pyautogui.center(nontradable)[1])
                        pyautogui.mouseDown(); pyautogui.mouseUp()          
                        
            
            
        def selltikla():
                    selltikla=pyautogui.locateOnScreen('resimler/selltikla.png',confidence=0.93 ,grayscale = True)
                    if selltikla !=None:
                        print("buldu")
                        pyautogui.click(x=pyautogui.center(selltikla)[0], y=pyautogui.center(selltikla)[1])
                        pyautogui.mouseDown(); pyautogui.mouseUp() 
            
        def onay2():
                    onay2=pyautogui.locateOnScreen('resimler/onay2.png',confidence=0.93 ,grayscale = True)
                    if onay2 !=None:
                        print("buldu")
                        pyautogui.click(x=pyautogui.center(onay2)[0], y=pyautogui.center(onay2)[1])
                        pyautogui.mouseDown(); pyautogui.mouseUp()   
                   
            
            
            
        time.sleep(2)
        def siralaratikla():
                global korx_ref,kory_ref    
                global hangisialar
                for i in range(0,len(hangisialar)):
                    print(i)
                    
                    try:
                            yicin=int(hangisialar[i])+1
                            for xicin in range(0,7):
                                    
                                pyautogui.click(x=(korx_ref-(60*xicin)), y=(kory_ref+(60*yicin)))
                                time.sleep(0.2)
                                pyautogui.mouseDown(button='right'); pyautogui.mouseUp(button='right') 
                             
                            nontradable()
                            selltikla()
                            onay2()
                    except Exception as e:
                        print(e)
                
                
                
            
            
        siralaratikla()
            
        def carpi():
                while 1:
                  
                    carpi=pyautogui.locateOnScreen('resimler/carpi.png',confidence=0.93 ,grayscale = True)
                    if carpi !=None:
                        print("buldu")
                        korx, kory = pyautogui.center(carpi)
                        pyautogui.click(x=korx, y=kory)
                        pyautogui.mouseDown(); pyautogui.mouseUp()   
                        break
            
        carpi()
        
        ######################################
        if sonuc=="bitir":
            break
###############################################################################
#repair kısmı repair_ref tamamdır.

def repairetmesundiries():
    
    while 1:
              
        canbari=pyautogui.locateOnScreen('knighticin/canbari.png',confidence=0.93 ,grayscale = False)
        canbari2=pyautogui.locateOnScreen('knighticin/canbari2.png',confidence=0.93 ,grayscale = False)
        if canbari !=None or canbari2 !=None:
            print("buldu")
            try:
                korx_refa, kory_refa = pyautogui.center(canbari)
            except:
                korx_refa, kory_refa = pyautogui.center(canbari2)
                        
            break
    
    
    pyautogui.click(x=korx_refa+50, y=kory_refa-20)
    pyautogui.mouseDown(button='right'); pyautogui.mouseUp(button='right')
    pyautogui.mouseDown(button='right'); pyautogui.mouseUp(button='right') 
        
    while 1:   
        repair1=pyautogui.locateOnScreen('resimler/repair1.png',confidence=0.93 ,grayscale = True)
        repair2=pyautogui.locateOnScreen('resimler/repair2.png',confidence=0.93 ,grayscale = True)
        repair3=pyautogui.locateOnScreen('resimler/repair3.png',confidence=0.93 ,grayscale = True)
        ticaretisteme5=pyautogui.locateOnScreen('resimler/ticaretisteme5_carpi.png',confidence=0.93 ,grayscale = True)
        #durdur=pyautogui.locateOnScreen('resimler/durdur.png',confidence=0.93 ,grayscale = True)
        if repair1 !=None:
            print("buldu")
            korx, kory = pyautogui.center(repair1)
            pyautogui.click(x=korx, y=kory)
            pyautogui.mouseDown(); pyautogui.mouseUp() 
            #pyautogui.mouseDown(); pyautogui.mouseUp() 
            break
        elif repair2 !=None:
            print("buldu")
            korx, kory = pyautogui.center(repair2)
            pyautogui.click(x=korx, y=kory)
            pyautogui.mouseDown(); pyautogui.mouseUp() 
            break
        elif repair3 !=None:
            print("buldu")
            korx, kory = pyautogui.center(repair3)
            pyautogui.click(x=korx, y=kory)
            pyautogui.mouseDown(); pyautogui.mouseUp() 
            break

        elif ticaretisteme5 !=None:
            print("buldu")
            korx, kory = pyautogui.center(ticaretisteme5)
            #250 repair
            pyautogui.click(x=korx, y=kory+250)
            pyautogui.mouseDown(); pyautogui.mouseUp() 
            #pyautogui.mouseDown(); pyautogui.mouseUp() 
            break
        """
        elif durdur !=None:
            print("durdu")
            break
        """

def carpi():
              
    carpi=pyautogui.locateOnScreen('resimler/carpi.png',confidence=0.93 ,grayscale = True)
    if carpi !=None:
        print("buldu")
        korx, kory = pyautogui.center(carpi)
        pyautogui.click(x=korx, y=kory)
        pyautogui.mouseDown(); pyautogui.mouseUp()   
                    
        
carpi()

time.sleep(2)
repairetmesundiries()



while 1:
    time.sleep(2)          
    repair_ref=pyautogui.locateOnScreen('resimler/repair_ref.png',confidence=0.93 ,grayscale = True)
    if repair_ref !=None:
        print("buldu")
        korx, kory = pyautogui.center(repair_ref)  
        break


for xicin in range(1,4):
    for yicin in range(0,5):
        pyautogui.click(x=(korx+(60*xicin)), y=(kory-(60*yicin)))
        pyautogui.mouseDown(); pyautogui.mouseUp() 





































