import PySimpleGUI as sg
import math
import per
import copy
sg.theme('SandyBeach')
A=('______________________________________')
H =['.','.','.','.','.']


lay = [[sg.Text('Welcome to Permutetry made my DDKS,By Clicking OK, You agree to the Terms And Conditions !')],
                [sg.Button('OK')],[sg.Button('Don\'t Agree')]]
window = sg.Window('Permutetry',lay)
input_result= [[sg.Text('Enter the Object of which you want to make Permutations/Arrangements')],
       [sg.Text('Enter Here : '),sg.InputText()],
       [sg.Button('Submit')],[sg.Button('Exit')],[sg.Text()],[sg.Button('Arrangments')],[sg.Button('Sort',key='SORT')],[sg.Button('Search')]]
arrangments = [[sg.Text('Result')],[sg.Text('........................................................')],[sg.Text(A,key ='ddks')],[sg.Listbox(H,size=(20,22),key='JAI')]]
               

layout = [
    [sg.Column(input_result),
     sg.VSeperator(),
     sg.Column(arrangments)
     ]
    ]
window1 = sg.Window('Permutetry',layout,grab_anywhere=True)


while True:
    event,values = window.read()
    if event == ('Don\'t Agree') or event == sg.WIN_CLOSED:
        window.close
        window1.close()
        break
    if event == 'OK':
        window.close()
        window1.read()
        break
window.close()

while True:
    event,values = window1.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        window1.close()
        break
    if event =='Submit':
        B = per.per(values[0])
        window1['ddks'].update(B)
    if event == 'Arrangments':
        AR,K =per.arrang(values[0])
        window1['JAI'].update(AR)
    if event == 'SORT':
        try:
            BR = copy.copy(AR)
            BR.sort()
        except:
            KR,L=per.arrang(values[0])
            BR = copy.copy(KR)
            BR.sort()
        window1['JAI'].update(BR)
    if event == 'Search':
        try:
            BR= copy.copy(AR)
            BR.sort()
        except:
            KR,L=per.arrang(values[0])
            BR = copy.copy(KR)
            BR.sort()
        lay1=[[sg.Text('Enter the object which you want to Search !')],[sg.InputText()],[sg.Button('Search')],[sg.Text('_______________________________',key ='SEAR')]]
        Search =  sg.Window('Search Manager',lay1)
        while True:
            event,values = Search.read()
            if event=='Search':
                try:
                    HR = BR.index(values[0])
                    TR = HR + 1
                    OP = values[0],'is at',TR,'in the list !'
                    Search['SEAR'].update(OP)
                except:
                    Search['SEAR'].update('Object doesn\'t found')
            if event ==sg.WIN_CLOSED:
                break
        Search.close()
                
                
            
        
        
        
        

        
        
        
        
         
        
         
         
                                            
       





        
        
        



