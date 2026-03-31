import pandas as pn


data = {
    "Names":["Иван Петров", "Мария Смирнова", "Алексей Иванов", "Елена Голубева"],
    "Ages": [34, 28, 45, 52],
     "Caute":[1,34,12,56],
     "Class": [1, 2, 1, 2],
         "Dead": [True, False, True, False]
}
df = pn.DataFrame(data)
def deads(classes):
    dead = []
    dead_people = df[df["Dead"] == True]
    sl = dead_people[dead_people["Class"]==classes]
    mas = sl["Class"]
    for i in mas:
        dead.append(i)
    return len(dead)
def death():
    deaths = []
    for x in df["Class"]:
        deaths.append(x)
    deaths_count = len(deaths)
    first = deads(1)/deaths_count * 100
    second = deads(2)/deaths_count * 100
    third = deads(3)/deaths_count * 100
    danger = [first,second,third]
    dnds = {"Class":[1,2,3],"Danger":danger}
    dndf = pn.DataFrame(dnds)
    print(dndf)
    final_death_class = dndf[dndf["Danger"] == max(dndf["Danger"])]
    for z in final_death_class["Class"]:
        if z == 1:
            print(f"The first class the most danger.Death rate = {round(first)}%.People died:{deads(1)}")
        elif z == 2:
            print(f"The second class the most danger.Death rate = {round(second)}%.People died:{deads(2)}")
        elif z == 3:
            print(f"The third class the most danger.Death rate = {round(third)}%.People died:{deads(3)}")
def passengrtsearch(passenger:str):
        for m in df["Names"]:
             if m == passenger:
                 print(df[df["Names"] == m])
                 break
def addPerson(fullname,cauta,ages,classes,deads):
    df.loc[len(df)] = [fullname,ages,cauta,classes,deads]
def addmanyperson(fullnames:list[str],ages2:list[int],cautes:list[int],classes2:list[int],deads2:list[bool]):
    n = [len(df)]
    l = len(df)
    data2 = {"Names":fullnames,
           "Ages":ages2,
           "Caute":cautes,
           "Class":classes2,
           "Dead":deads2
           }
    for m in fullnames[1:]:
        l = l +1
        n.append(l)
    df2 = pn.DataFrame(data2,index=n)
    return pn.concat([df,df2],axis=0)
while True:
    inp = input()
    if inp == "stop":
        break
    if inp == "show me data" or inp == "show data":
        print(df)
    if inp == "find passenger":
        inppas = str(input("What passenge you want to find?"))
        passengrtsearch(inppas)
    if inp == "i want to add person" or inp == "Add person":
        fulln = str(input("Write name:"))
        cautn = int(input("Write caute:"))
        agen = int(input("Write age:"))
        classn = int(input("Write class:"))
        deadn = bool(input("Did he died?(True/False):"))
        addPerson(fulln,agen,cautn,classn,deadn)
    if inp == "i want to add many persons" or inp == "Add persons":
        fullns = input("Write names:")
        fullns2 = [name.strip() for name in fullns.split(",")]
        print(f"Max limit - {len(fullns2)}")
        cautn = input("Write cautes:")
        cautn2 =  [int(cau.strip()) for cau in cautn.split(",")]
        agens = input("Write ages:")
        agens2 =  [int(ag.strip()) for ag in agens.split(",")]
        classn = input("Write classes:")
        classn2 =  [int(cl.strip()) for cl in classn.split(",")]
        deadn = input("Did they died?(True/False):")
        deadn2 =  [bool(d.strip()) for d in deadn.split(",")]
        if len(fullns2) != len(cautn2) != len(agens2) != len(classn2) != len(deadn2):
            print("Incorrent data , try later")
        else:
            df = addmanyperson(fullns2,agens2,cautn2,classn2,deadn2)
    if inp == "show deaths rate":
        death()

#НАПИСАТЬ ФУНКЦИЮ ДОБАВЛЕНЯ СВОИХ СТРОК В ДАТАФРЕЙМ А АТКЖЕ ФУНКЦИЮ ДОБАВЛЕНИЯ МНОЖЕСТВА ДАННЫХ

