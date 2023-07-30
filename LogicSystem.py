rules=[]
outlist = []
import matplotlib.pyplot as plt
def Add_variable():
    "Return list of vairables  include var name , type , range (press 1)"
    input_var_list=[]
    small_list=[]
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
    return input_var_list


input_var_list=Add_variable()

########################################################Take fuzzy  sets############################################
r=[{'proj_funding': {'low': [10, 30, 40, 60], 'medium': [40, 60, 70, 90], 'high': [70, 90, 100, 100]}}, {'exp_level': {'beginner': [0, 15, 30], 'intermediate': [15, 30, 45], 'expert': [30, 60, 60]}}]

def Add_fuzzy_sets():
    input_fuzzy_list=[]
    outer_dic={}
    inner_dic={}
    var_name = input("Enter the variables,s name :")
    print("Enter the fuzzy set name, type (TRI/TRAP) and values : \n (press x to finish)")

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
    return  [outer_dic]
result=Add_fuzzy_sets()
i=1
while(i!=len(input_var_list)):

  result+=Add_fuzzy_sets()
  i+=1

#print("result", result )


##########################################Take crisp values ########################################################
def set_crisp_values(input_var_list):
        " This function set crisp values for input var only "
        print("Enter crisp values :")
        
        dic_crisp={}
        for i in range (len(input_var_list)):
            if input_var_list[i][1]=="IN":
                number=int(input())
                dic_crisp[input_var_list[i][0]]= number
        return  dic_crisp
dic=set_crisp_values(input_var_list)
#print("Crisp_dic", dic)

############################################Membership######################################################
def calc_memebrship(dic):
    #print("hello from clac_memebership")
    #print("this result" , result)
    Trap = [0, 1, 1, 0]
    tri = [0, 1, 0]
    resulted_dic = {}
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
           
            for k in i[j]:
                
                size = len(i[j][k])
                for s in range(size):
                    if crisp_value not in range(min(i[j][k]), max(i[j][k])):
                        membership_value = 0
                        break

                    if crisp_value > i[j][k][s]:

                       
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

memberShips=calc_memebrship(dic)

#print('out:',memberShips)

def display_output(result):
    #print("Hello from function Display Output ")
    for dic in result:
        if list (dic.keys())[0] in outlist:
         return  [dic]
out_var=display_output(result)
print("This is the Output sets and its Values : \n",out_var)
################################################### Plot ################################################
indexlist=[]
def extract_index_list(r):
    print("Hello from Function  Extract list of Sets Range ")
    for outer_key in  r :
        # print(outer_key)
        for  inner_key in outer_key:
            # print(outer_key[inner_key])
            for rangeval in  outer_key[inner_key]:
                # print(outer_key[inner_key][rangeval])
                indexlist.append(outer_key[inner_key][rangeval])
    return indexlist
result_index_list=extract_index_list(r)



def draw_plot(result_index_list):
    ytrap=[0,1,1,0]
    ytri=[0,1,0]
    # count=1
    plt.subplots(figsize=(10, 8))
    for i in range(len(result_index_list)):
         if len(result_index_list[i])==4:
             #figure, axis = plt.subplots(2, 2)
             plt.subplot(3, 2, 1)
             plt.plot(result_index_list[i],ytrap)
             # count+=1
         elif len(result_index_list[i])==3:
             plt.subplot(3, 2, 2)
             plt.plot(result_index_list[i], ytri)
    plt.show()
    plt.legend()

draw_plot(result_index_list)
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


def addRule():
    
    for i in range(3):
        print("Enter Your Rules : ")
        rule=input()
        if rule =='x':
            break
        rules.append(rule)
    return rules

rule=addRule()

def Inference(memberShips,rule):
  
  
  allMemberships=[]
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
                   
               
     
      
      allMemberships+=mem.values()     
      
  return allMemberships
  
print("Calc The output at : \n",Inference(memberShips,rule))
deFuzzStep=Inference(memberShips,rule)
############################################# DeFuzzification #################################


def DeFuzzification(out_var,deFuzzStep):
    
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
        return predicted
DeFuzzification(out_var,deFuzzStep)

