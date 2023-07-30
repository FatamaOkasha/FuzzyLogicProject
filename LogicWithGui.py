# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:08:16 2022

@author: Ramadan
"""
#global variablies 
NameDisciption = None
variables = [] # this need to be append
inputway = 'gui'
outlist = []
rules = []
result = []
crispnumbers=[]
dic_crisp={}
resulted_dic ={}
allMemberships=[]
import tkinter as tk
#from tkinter import __ttk 


def Add_variable(VarsText = None):
    # "Return list of vairables  include var name , type , range (press 1)"
    input_var_list=[]
    small_list=[]
    if(inputway == "console"):
        print("Enter the variable’s name, type (IN/OUT) and range ([lower, upper]): \n (press x to finish)")
        print("-----------------------------------------------------------")
        while(True):
            i = input()
            if i=="x":
                # main_menu()
                break
            small_list = list(i.split())
            if small_list[1] == 'OUT':
                outlist.append(small_list[0])
            small_list[2:]=[list(map(int,small_list[2:]))]
            input_var_list.append(small_list)
    elif(inputway == "gui"):
        for line in VarsText.split('\n'):
            i = line
            if i=="x":
                # main_menu()
                break
            small_list = list(i.split())
            if small_list[1] == 'OUT':
                outlist.append(small_list[0])
            small_list[2:]=[list(map(int,small_list[2:]))]
            input_var_list.append(small_list)
    elif(inputway == "file"):
        pass
    return input_var_list

#input_var_list=Add_variable()

def Add_fuzzy_sets(screen ,VarsText = None):
    input_fuzzy_list=[]
    outer_dic={}
    inner_dic={}
    var_name = input("Enter the variables,s name :")
    print("Enter the fuzzy set name, type (TRI/TRAP) and values : \n (press x to finish)")
    if (inputway == 'console'):
        while True :
            i = input()
            if i == "x":
                # main_menu()
                break
    
            small_fuzzy_list = list(i.split())
            if small_fuzzy_list[1] == "TRI":
                small_fuzzy_list[2:5] = list(map(int, small_fuzzy_list[2:5]))
            elif small_fuzzy_list[1] == "TRAP":
                small_fuzzy_list[2:6] = list(map(int, small_fuzzy_list[2:6]))
            input_fuzzy_list.append(small_fuzzy_list)
            for c in range(len(input_fuzzy_list)):
    
                inner_dic[input_fuzzy_list[c][0]]=list(input_fuzzy_list[c][2:])
                outer_dic[var_name]=inner_dic
    elif(inputway == "gui"):
        
        lineNumber =1
        for line in VarsText.split('\n'):
            if(lineNumber == 1):
                var_name = line
                continue
            lineNumber +=1
            i = line
            if i == "x":
                # main_menu()
                break
            small_fuzzy_list = list(i.split())
            if small_fuzzy_list[1] == "TRI":
                small_fuzzy_list[2:5] = list(map(int, small_fuzzy_list[2:5]))
            elif small_fuzzy_list[1] == "TRAP":
                small_fuzzy_list[2:6] = list(map(int, small_fuzzy_list[2:6]))
            input_fuzzy_list.append(small_fuzzy_list)
            for c in range(len(input_fuzzy_list)):
    
                inner_dic[input_fuzzy_list[c][0]]=list(input_fuzzy_list[c][2:])
                outer_dic[var_name]=inner_dic
    elif(inputway == "file"):
        pass
    result = [outer_dic]
    return  [outer_dic]

def addRule(rulesText = None):
    if(inputway == "console"):
        for i in range(3):
            print("Enter Your Rules : ")
            rule=input()
            if rule =='x':
                break
            rules.append(rule)
    elif(inputway == "gui"):
        for rule in rulesText.split('\n'):
            if rule =='x':
                break
            rules.append(rule)
    return rules

#result=Add_fuzzy_sets()
# i=1
# while(i!=len(input_var_list)):
#   result+=Add_fuzzy_sets()
#   i+=1
def setnumber(txxtt):
    number = txxtt.get(1.0, "end-1c")
    crispnumbers.append(number)

    
def set_crisp_values(screenn , input_var_list):
        #" This function set crisp values for input var only "
        print("Enter crisp values :")
        if(inputway == "console"):
            for i in range (len(input_var_list)):
                if input_var_list[i][1]=="IN":
                    number=int(input(input_var_list[i], ":"))
                    dic_crisp[input_var_list[i][0]]= number
        elif(inputway == "gui"):
            clear_frame(screenn)
            L = tk.Label(screenn, text="Enter crisp values \n ---------------------------------------", font=('Helvetica bold', 15))
            L.pack()
            number_num = 0
            for i in range (len(input_var_list)):
                if input_var_list[i][1]=="IN":
                    number_num +=1
                    L = tk.Label(screenn, text=str(input_var_list[i])+ ":", font=('Helvetica bold', 10))
                    L.pack()
            
                            
                    txt = tk.Text(screenn, height=2, width=5)
                    txt.pack()
                    submit_btn = tk.Button(screenn,  padx=2, pady=8, text="Submit", command= lambda : setnumber(txt))
                    submit_btn.pack()
                    quit_Btn_fn(screenn)
            number_num2 = 0   
            done_btn = tk.Button(screenn,   padx=40, pady=18, text="Done", command= lambda : calc_memebrship(dic_crisp))
            done_btn.pack()
            for i in range(len(input_var_list)):
                if input_var_list[i][1]=="IN":
                    number_num2 +=1
                    dic_crisp[input_var_list[i][0]]= crispnumbers[number_num2]  
            
            
#print("Crisp_dic", dic)
def calc_memebrship(dic):
    print("hello from clac_memebership")
    print("this result" , result)
    Trap = [0, 1, 1, 0]
    tri = [0, 1, 0]
    inner_dic = {}
    three_dic = {}

    for i in result:
        # {project}
        #
        crisp_value = None
        for key in dic.keys():
            if key == list(i.keys())[0]:
                crisp_value = dic.get(key)
                break

        for j in i:
            # print(i[j])
            for k in i[j]:
                # print(i[j][k])
                size = len(i[j][k])
                for s in range(size):
                    if crisp_value not in range(min(i[j][k]), max(i[j][k])):
                        membership_value = 0
                        break

                    if crisp_value > i[j][k][s]:

                        # print(crisp_value>i[j][k][s])
                        # membership_value=0
                        continue
                    else:
                        if size == 3:
                            FirstPoint = [i[j][k][s], tri[s]]
                            SecondPoint = [i[j][k][s - 1], tri[s - 1]]
                            m = (SecondPoint[1] - FirstPoint[1]) / (SecondPoint[0] - FirstPoint[0])
                            c = FirstPoint[1] - (m * FirstPoint[0])
                            membership_value = (m * crisp_value) + c
                            three_dic[k] = membership_value
                            resulted_dic[j] = three_dic
                            break

                        else:
                            FirstPoint = [i[j][k][s], Trap[s]]
                            SecondPoint = [i[j][k][s - 1], Trap[s - 1]]
                            m = (SecondPoint[1] - FirstPoint[1]) / (SecondPoint[0] - FirstPoint[0])
                            c = FirstPoint[1] - (m * FirstPoint[0])
                            membership_value = (m * crisp_value) + c
                            flag = 1
                            inner_dic[k] = membership_value
                            resulted_dic[j] = inner_dic
            
    return resulted_dic
#memberShips=calc_memebrship(dic_crisp)
# memberShips=calc_memebrship(dic_crisp)

def display_output(result):  #5555555555555555555555555555555555555555
    print("Hello from function Display Output ")
    for dic in result:
        if list (dic.keys())[0] in outlist:
         return  [dic]


#print("This is the Output sets and its Values : \n",out_var)
################################################### Rules ###############################################

def And(a,b):
    if a>b:
        return(b)
    else:
        return(a)
        
def Or(a,b):
    if a>b:
        return(a) 
    else:
        return(b)

def Not(a):
    return(1-a)


# def addRule():
    
#     for i in range(3):
#         print("Enter Your Rules : ")
#         rule=input()
#         if rule =='x':
#             break
#         rules.append(rule)
#     return rules

# rule=addRule()
#memberShips = resulted_dic
def Inference(memberShips,rule):
  global allMemberships
  mem={}
 
  for  r in range(len(rule)):  
     
      rulesIntoArray=rule[r].split(" ")
      for i in range(len(rulesIntoArray)):
       
            if rulesIntoArray[2]=='or' or rulesIntoArray[2]=='Or':
               
                   result=Or(memberShips[rulesIntoArray[0]][rulesIntoArray[1]],memberShips[rulesIntoArray[3]][rulesIntoArray[4]])
                   
                   if rulesIntoArray[0] in mem.keys():
                       
                       mem[rulesIntoArray[6]]={}
                       mem[rulesIntoArray[0]][rulesIntoArray[1]]=result
                       
                       
                   else:
                       
                       mem[rulesIntoArray[6]]={}                     
                       mem[rulesIntoArray[6]][rulesIntoArray[7]]=result
                   
                   
            if rulesIntoArray[2]=='and' or rulesIntoArray[2]=='And':
               
                   result=And(memberShips[rulesIntoArray[0]][rulesIntoArray[1]],memberShips[rulesIntoArray[3]][rulesIntoArray[4]])
                   
                   if rulesIntoArray[0] in mem.keys():
                     
                       mem[rulesIntoArray[6]]={}
                       mem[rulesIntoArray[0]][rulesIntoArray[1]]=result                       
                       
                   else:
                      
                       mem[rulesIntoArray[6]]={}
                       mem[rulesIntoArray[6]][rulesIntoArray[7]]=result
                   
               
     
      display_output(result)
      allMemberships += mem.values()     
  return allMemberships
  
#print("Calc The output at : \n",Inference(memberShips,rule))

############################################# DeFuzzification #################################
def DeFuzzification():
        out_var=display_output(result)
        deFuzzStep=Inference(allMemberships,rules)
        centroids =[]
        sumMembership=0
        predictedVal=0
        for i in out_var :
            for j in i.keys():
                for k in i[j]:
                    sumAll=0
                    for c in range(len(i[j][k])):
                        sumAll= sumAll + i[j][k][c]    
                    centroids.append(sumAll/len(i[j][k]))
                    
        #print(centroids)
        for i in range(len(deFuzzStep)):
            
            for j in deFuzzStep[i].values() :
                sumMembership=sumMembership+j
                
                centroids[i]=centroids[i]*j
        predictedVal=sum(centroids)
        predicted = predictedVal/sumMembership
        print("Aaaaaaaaaaaaaaaaaaaaay : Predicted Value is : ",predicted)
        memberShips=calc_memebrship(dic_crisp)
        Inference(memberShips,rules)
        return predicted
 # out_var=display_output(result)
# DeFuzzification(out_var,deFuzzStep)



def clear_frame(frame):
   for widgets in frame.winfo_children():
      widgets.destroy()

      
def text_scren(winw, txtTShow, WhichMinueItem):
    global VailidateGetText
    clear_frame(winw)
    L = tk.Label(winw, text=txtTShow, font=('Helvetica bold', 15))
    L.pack()
    
    MakeSapce(winw)
    txt = tk.Text(winw, height=5, width=80)
    txt.pack()
    
    
    submit_btn = tk.Button(winw,  padx=40, pady=18, text="Submit", command= (lambda : VailidateGetText(winw, txt, WhichMinueItem)))
    submit_btn.pack()
   
    
    quit_Btn_fn(winw)
    print("we are in text_scren")
    
    #shouled return the text here so it be used -------------------------------------------------
    
      
def MakeSapce(WinScr, xP=0, yP=0):
    space = tk.Label(WinScr, text="", padx=xP, pady= yP)
    space.pack()
    

#some action functions
def quit_Btn_fn(Screenx, XP= 740, YP= 650):
    Quit_btn = tk.Button(Screenx, text="Quit", bg="red", padx=10, pady=10, command=lambda: (Screenx.destroy()))
    Quit_btn.place(x= XP, y= YP)
    
    #------------------------------------------Makeking the screen
Hello_scr = tk.Tk()
Hello_scr.title("Fuzzy Logic Toolbox")
Hello_scr.geometry("800x700")
EnterName_Label = tk.Label(Hello_scr, text="Welcom to Fuzzy Logic Toolbox ", font=('Helvetica bold', 20))
EnterName_Label.pack()
MakeSapce(Hello_scr)


def sel():
    if(var.get() == 1) :
        inputway = 'gui'
    elif(var.get() == 2) :
        inputway = 'console'
    elif(var.get() == 3) :
        inputway = 'file'
    selection = "You selected the option " + inputway
    label.config(text = selection, font=('Helvetica bold', 10 ), fg="red")


var = tk.IntVar()

l = tk.Label(Hello_scr,  padx= 100, text="select the way you will Enter the input the defualt way is GUI", font=('Helvetica bold', 15))
l.pack(anchor = 'w')
R1 = tk.Radiobutton(Hello_scr, text="GUI", padx= 100, variable=var, value=1, font=('Helvetica bold', 20), command=sel)
R1.pack(anchor = 'w')

R2 = tk.Radiobutton(Hello_scr, text="Console", padx= 100, variable=var, value=2 , font=('Helvetica bold', 20), command=sel)
R2.pack(anchor = 'w' )

R3 = tk.Radiobutton(Hello_scr, text="File", padx= 100, variable=var, value=3 , font=('Helvetica bold', 20), command=sel)
R3.pack(anchor = 'w' )

label = tk.Label(Hello_scr)
label.pack()

MakeSapce(Hello_scr)


def MainMenu(screen):
    global VailidateGetText
    L = tk.Label(screen, text="Main Menu:",font=('Helvetica bold', 25))
    L.pack()
    
    L2 = tk.Label(screen, text="_________________________________", font=('Helvetica bold', 10))
    L2.pack()
    
    MakeSapce(screen)
    AddVariables_btn = tk.Button(Hello_scr, text="1- Add variables." ,width=30 , font=('Helvetica bold', 12), anchor="w", padx=40, pady=20, command=lambda: text_scren(Hello_scr, "Enter the variable’s name, type (IN/OUT) and range ([lower, upper]): (Press x to finish)", 1))
    AddVariables_btn.pack()
    
    AddFuzzySets_btn = tk.Button(Hello_scr, text="2- Add fuzzy sets to an existing variable" ,width=30 , font=('Helvetica bold', 12), padx=40, pady=20, command=lambda: text_scren(Hello_scr, "Enter the variable’s name in the first line \nEnter the fuzzy set name, type (TRI/TRAP) and values: (Press x to finish)", 2))
    AddFuzzySets_btn.pack()
    
    AddRules_btn = tk.Button(Hello_scr, text="3- Add rules", width=30 , font=('Helvetica bold', 12) ,anchor="w",  padx=40, pady=20, command=lambda: text_scren(Hello_scr, "Enter the rules in this format: (Press x to finish)\nIN_variable set operator IN_variable set => OUT_variable set", 3))
    AddRules_btn.pack()
    
    
    RunTheSimulation_btn = tk.Button(Hello_scr, text="4- Run the simulation on crisp values.",width=30 , font=('Helvetica bold', 12) , padx=40, pady=20, command=lambda: set_crisp_values(Hello_scr , variables))
    RunTheSimulation_btn.pack()
    
    quit_Btn_fn(screen)

def VailidateGetText(screen,textt, WhichMinueItem):
    Returned_txt = textt.get(1.0, "end-1c")
    if(Returned_txt !=""):
        #https://stackoverflow.com/questions/862412/is-it-possible-to-have-multiple-statements-in-a-python-lambda-expression
        if (WhichMinueItem == 1):
            global variables
            inputvar = Add_variable(Returned_txt)
            variables += inputvar
            texttoShow = "variables are added successfully "
        elif(WhichMinueItem == 2):
            texttoShow = "fuzzy sets are added to its variable ssuccessfully "
        elif(WhichMinueItem == 3):
            addRule(Returned_txt)
            texttoShow = "Rules are added successfully "
        elif(WhichMinueItem == 4):
            set_crisp_values(variables)
            texttoShow = "Running the simulation…"
        else :
            print("exiption")
        
        clear_frame(screen)
        MainMenu(screen)
        
    else:
        # #clear_frame(winw)
        # if (WhichMinueItem == 1):
        #     txtTShow = "Invalid Added variables"
        # elif(WhichMinueItem == 2):
        #     txtTShow =" "
        # elif(WhichMinueItem == 2):
        #     txtTShow =" "
        # elif(WhichMinueItem == 2):
        #     txtTShow =" "
        # else :
        texttoShow = "Invalied input"
        
    L = tk.Label(screen, text=texttoShow , font=('Helvetica bold', 10) ,  dg="red")
    L.pack()

def SubmitFuzzyName_de_btn(NameD_Text, screen):
    global NameDisciption
    
    tex = NameD_Text.get(1.0, "end-1c")
    # NameDisciption = VailidateGetText(screen, NameD_Text)
    if(tex !=""):
        print(tex)
        NameDisciption = tex
        clear_frame(screen)
        MainMenu(screen)
    else:
        L = tk.Label(screen, text="Enter Valied system’s Name and a brief description ",  bg="red", font=('Helvetica bold', 10))
        L.pack()
def inputWay_Scr(screen):
    
    pass
    
def CreateNewFuzzy(createFuzzy_scr) :
    clear_frame(createFuzzy_scr)
    createFuzzy_scr.title("create New Fuzzy")
    createFuzzy_scr.geometry("800x700")
    EnterName_Label = tk.Label(createFuzzy_scr, text="Enter the system’s name and a brief description: ", font=('Helvetica bold', 15))
    EnterName_Label.pack()
    SysNameBrief_Text = tk.Text(createFuzzy_scr, height=5, width=80)
    SysNameBrief_Text.pack()
    #print(SysNameBrief_Text.grab_current())
    # t = tk.Text(createFuzzy_scr, height=20, width=40)
    # t.pack()
    submit_btn = tk.Button(createFuzzy_scr,  padx=40, pady=18, text="Submit", command= lambda: SubmitFuzzyName_de_btn(SysNameBrief_Text, createFuzzy_scr))
    submit_btn.pack()
    quit_Btn_fn(createFuzzy_scr)
    
    #Entry.grid(row=0, column=0, columnspan=5)

    
def Quit_Action():
    print("should be closing")

CreateNewFuzzy_btn = tk.Button(Hello_scr, text="Create a New Fuzzy system ", padx=40, pady=20, command=lambda: CreateNewFuzzy(Hello_scr))
CreateNewFuzzy_btn.pack()
MakeSapce(Hello_scr)
Quit_btn = tk.Button(Hello_scr, text="Quit", bg="red", padx=40, pady=20, command=lambda: Hello_scr.destroy())
Quit_btn.pack()


#Quit_btn.bind('<ButtonPress>', Quit_Action)


#Entry = tk.Entry(Hello_scr, width=50, borderwidth=5)
#Entry.grid(row=0, column=0, columnspan=5)












Hello_scr.mainloop()