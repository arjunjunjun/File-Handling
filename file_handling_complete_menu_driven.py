import os
import pickle
import csv
import string

print("******************************************WELCOME******************************************")

print('\n')
print("           The following is a menu to manage records in different file modes")
print('\n')
print("If you wish to return back to a file menu when adding records, simply input 'undo' in name                                            field")
print('\n')

print("*******************************************START*******************************************")

"""TEXT FILE"""

if not os.path.isfile("records.txt"):
    file=open("records.txt",'w')
    file.close()


def clear_text():
    file=open("records.txt",'r')
    x=file.read()
    if len(x)==0:
        print("File is already empty!")
    else:
        a=input("Are you sure you wish to delete all records?(Y/N) ")
        if a in['y','Y']:
            file=open("records.txt",'w')
            print("all records deleted!")
            file.close()
    

def add_text():
    file=open("records.txt", 'a')
    lst=[]
    
    while True:
        a=input("enter your name: ")
        if a=="undo":
            return
        words=a.split()
        new="_".join(words)

        while True:
            try:
                b=int(input("enter your class: "))
                if b>12 or b<=0:
                    print("invalid input!!!")
                else:
                    break
            except:
                print("invalid input!!!")
            
            
        while True:
            sec = input("enter your section: ")
            if len(sec)==1 and sec in string.ascii_letters:
                b=str(b)+'-'+sec
                break
            else:
                print("invalid input!!!")

        while True:
            try:
                c = float(input("enter your percentage: "))
                if c=="undo":
                    return
                if c>100 or c<0:
                    print("invalid input!!!")
                else:
                    break
            except:
                print("invalid input!!!")

        d=input("do you wish to enter more records? (Y/N): ")
        lst.append(f"{new} {b} {c} ")
        lst.append('\n')
        if d in ['n', 'N']:
            break

    file.writelines(lst)
    print('\n')
    print("records added successfully!")
    file.close()


def read_text():
    file = open("records.txt", 'r')
    f1 = file.read()
    print(f1)

def count_text():
    file = open("records.txt", 'r')
    f1 = file.readlines()
    count=len(f1)
    print("number of records are: ",count)

def search_text():
    cnt = 0
    with open('records.txt','r') as f:
        lst = f.read().splitlines()
    if len(lst)==0:
        print("No records exist!")
    else:
        word = input('Enter word:  ')
        for rec in lst:
            if word in rec:
                cnt += 1
        print("number of times the word appears is:",cnt)

def count2_text():
    file=open("records.txt",'r')
    f1=file.read().splitlines()
    count1=0
    count2=0
    for i in f1:
        for x in i:
            if x.isdigit():
                count1=count1+1
            elif x.isalpha():
                count2=count2
            elif x.isspace():
                count2=count2
            else:
                count2=count2+1
    print("number of digits is",count1)
    print("number of special characters is",count2)


def arrange_text():
    with open('records.txt','r') as f:
        x = f.read().splitlines()
        if len(x)==0:
            print("No records exist!")
        else:   
            for i in x:
                q=sorted(x)
            
            with open('records.txt','w') as f1:
                for i in q:
                    f1.writelines(i)
                    f1.write('\n')
                print("Records arranged successfully!")

        


def modify_text():
    with open('records.txt','r') as f:
        lst = f.read().splitlines()
        new = []
        if len(lst)==0:
            print("No records exist!")
        else: 
            for rec in lst:
                l=rec.split()
                if float(l[-1])!=0.0:
                    l[-1]=float(l[-1])-1
                new_rec = ""
                for i in l:
                    new_rec += str(i) + ' '
                new_rec = new_rec[:-1] + '\n'
                new.append(new_rec)
                    
                    
            with open('records.txt','w') as f:
                f.writelines(new)
                print('\n')
                print('Records updated succesfully!')


def delete_text():
    with open('records.txt','r') as f:
        lst = f.read().splitlines()
        new = []
        if len(lst)==0:
            print("No records exist!")
        else:   
            for rec in lst:
                l=rec.strip().split(' ')
                if float(l[-1]) > 33:
                    new.append(rec + '\n')
            with open('records.txt','w') as f:
                f.writelines(new)
                print('Records updated succesfully!')


def delete_text2():
    with open('records.txt','r') as f:
        a=input("enter name: ")
        print('\n')
        lst = f.read().splitlines()
        new=[]
        new1=[]
        new2=[]
        double=[]    
                
        for rec in lst:
            l=rec.strip().split(' ')
            if l[0]==a:
                print(l)
                    

            if not l[0]==a:
                new.append(rec+'\n')
            if l[0]==a:
                new1.append(rec+'\n')

        if len(new1)==0:
            print("student not found!")
            return

        
        print('\n')
        if len(new1)>1:
            ch=input("are you sure you wish to delete any of the above records? (Y/N) ")
        else:
            ch=input("are you sure you wish to delete the above record? (Y/N) ")

        if ch in ['y','Y']:
            pass
        else:
            print('\n')
            print("no records deleted!")
            return

                


        if len(new1)>1:
            print('\n')
            z=input("Two or more students have the same name! \nEnter class of the student whoose records you wish to delete: ")

            classes=[]
            chosenclass=[]
            try:
                for rec in lst:
                    l=rec.strip().split(' ')
                    if l[0]==a:
                        chosenclass.append(l[1])
                    classes.append(l[1])

            except:
                print('')
                
            if z in classes and z not in chosenclass:
                print('\n')
                print("No matches of given class and name found!")
                return

        
            if z not in classes:
                print('\n')
                print("class does not exist!")
                return
            
        if len(new1)>1:
            try:      
                for i in lst:
                    l=i.strip().split(' ')

                    if not (l[1])==z:
                        new2.append(i+'\n')

                    if l[0]!=a:
                        if l not in new2:
                            new2.append(i+'\n')
                        
            except:
                print('')


            for i in new2:
                if i not in double:
                    double.append(i)

            if len(new2)>0:
                with open('records.txt','w') as f:
                    f.writelines(double)
                    print('\n')
                    print("Record deleted succesfully!")
                
    try:
        if len(new1)==1:
            if not len(new2)>0:
                with open('records.txt','w') as f:
                    f.writelines(new)
                    print('Record deleted succesfully!')
    except:
        print('')            

    
def text_menu():
        while True:
                ch=input("\nenter your choice: \n1:add records \n2:display all records \n3:count number of records \n4:find any word \n5:arrange records in ascending order \n6:count special characters/digits \n7:deduct 1% from all records \n8:delete records below 33% \n9:delete any record \n10:clear all records \n11:break \n \n")
                if ch == '1':
                    add_text()
                elif ch == '2':
                    read_text()
                elif ch == '3':
                    count_text()
                elif ch == '4':
                    search_text()
                elif ch=='5':
                    arrange_text()
                elif ch == '6':
                    count2_text()
                elif ch == '7':
                    modify_text()
                elif ch == '8':
                    delete_text()
                elif ch == '9':
                    delete_text2()
                elif ch == '10':
                    clear_text()
                elif ch=='11':
                    print("Thank you :)")
                    break
                    
                else:
                    print("invalid input!!!")

        


"""BINARY FILE"""


if not os.path.isfile("binary_.dat"):
    file=open("binary_.dat",'wb')
    file.close()

def clear_binary():
    flag=0
    file=open("binary_.dat",'rb')
    try:
        x=pickle.load(file)
    except:
        flag=1
        print("file is already empty!")

    if flag==0:
        a=input("Are you sure you wish to delete all records?(Y/N) ")
        if a in['y','Y']:
            file=open("binary_.dat",'wb')
            print("all records deleted!")
            file.close()

def add_binary():
    flag=0
    z=[]
    empty=0
    lst=[]
    with open ("binary_.dat",'rb') as file:
        try:
            while True:
                records=pickle.load(file)
                for i in records:
                    z.append(i)
        except:
            print('')

    ids=[]
    ids2=[]
    for i in z:
        ids.append(i[1])
    

    with open ("binary_.dat",'ab') as file:
        try:
            while True:

                a=input("enter employee name: ")
                if a=="undo":
                    return
                words=a.split()
                new="_".join(words)

                while True:
                    b=int(input("enter employee id: "))
                    b=abs(b)

                    for i in lst:
                        ids2.extend(i)
                        
                    if b not in ids and b not in ids2:
                        break
                    else:
                        print("employee id already exists!")

                while True:
                    c=int(input("enter employee salary: "))
                    if c<0:
                        print("invalid input!!!")
                    else:
                        break
                
                d=input("do you wish to add more records? (Y/N): ")
                lst.append([new,b,c])
                if d in ['n', 'N']:
                    break

            
            pickle.dump(lst,file)
            print("records added successfully!")
        except:
            print("invalid input!!!")

def display_binary():
    with open ("binary_.dat",'rb') as file:
        try:
            while True:
                x=pickle.load(file)
                for i in x:
                    print(i)
        except EOFError:
            print(' ')


def arrange_binary():
    var=0
    a='binary_.dat'
    for a in os.listdir():
        file_size = os.stat('binary_.dat').st_size
        if file_size == 0:
            var=var

        else:
            var=1
            

    if var==0:
        print("file is empty!")

    elif var==1:
        with open('binary_.dat','rb') as f:
            lst=[]
            try:
                while True:
                    x=pickle.load(f)
                    for i in x:
                        lst.append(i)
            except EOFError:
                print('')

                
            if x is not None:
                q=sorted(lst)

                with open('binary_.dat','wb') as f1:
                    pickle.dump(q,f1)
                    print("Records arranged successfully!")

            
def display2_binary():
    var=0
    a='binary_.dat'
    for a in os.listdir():
        file_size = os.stat('binary_.dat').st_size
        if file_size == 0:
            var=var

        else:
            var=1
        
    if var==0:
        print("file is empty!")
    elif var==1:
        with open ("binary_.dat",'rb') as file:
            try:
                a=int(input("enter salary: "))
                try:
                    while True:
                        x=pickle.load(file)
                        for i in x:
                            if i[2]>a:
                                print(i)

                except EOFError:
                    print(' ')
            except:
                print("invalid input!!!")
            
def modify_binary_1():
    with open ("binary_.dat",'rb') as file:
        global variable
        variable=0
        a='binary_.dat'
        for a in os.listdir():
            file_size = os.stat('binary_.dat').st_size
            if file_size == 0:
                variable=variable

            else:
                variable=1
                

        if variable==0:
            print("file is empty!")

        elif variable==1:
            global a11
            a11=input("enter employee name: ")
            new=[]

            try:
                while True:
                    x=pickle.load(file)
                    for i in x:
                        if i[0]==a11:
                            new.append(i)

            except EOFError:
                print(' ')

            if len(new)>0:
                print(new)

            if len(new)>1:
                print("more than two employees have the same name! \nSalary bonus will be given to each employee respective to order of their records!")
                print('\n')

def modify_binary():
    with open ("binary_.dat",'rb') as file:
        newlst=[]
        l=[]
        new=[]

        try:
            while True:
                x=pickle.load(file)
                for i in x:
                    try:
                        if i[0]==a11:
                            b=int(input("enter salary bonus: "))
                            if b<0:
                                print('\n')
                                print("negative bonus cannot be given. Absolute value of input added!")
                            b=abs(b)
                            i[2]=i[2]+b
                            l.append(i)
                        newlst.append(i)

                    except:
                            print("invalid input!!!")
                            return
                
        except EOFError:
            print(' ')

        if len(l)==0 and variable==1:
            print("employee not found!")
                    
        if len(l)>0:
            with open ("binary_.dat",'wb') as file:
                pickle.dump(newlst,file)
                print("record updated successfully!")

def delete_binary():
    with open ("binary_.dat",'rb') as file:
        lst1=[]
        x=[]
        new=[]
        new1=[]
        flag=0
        final=[]
        chosenid=[]
        everyid=[]
        try:
            a=input("enter employee name: ")
            print('\n')
            try:
                while True:
                    data=pickle.load(file)
                    x.extend(data)
            
            except EOFError:
                print(' ')
        

            for i in x:
                everyid.append(i[1])
                if i[0]==a:
                    print(i)
                    new.append(i)
                    chosenid.append(i[1])
                    
                if not i[0]==a:
                    lst1.append(i)

            if len(new)==0:
                print("employee not found!")
                return

            print('\n')

            if len(new)>1:
                b=input("are you sure you wish to delete any of the above records? (Y/N) ")
            else:
                b=input("are you sure you wish to delete the above record? (Y/N) ")                

            if b in ['y','Y']:
                var=1
            else:
                print("no records deleted!")
                return

            if len(new)>1:
                print('\n')
                z=int(input("Two or more employee's have the same name! \nEnter id of the employee whoose records you wish to delete: "))

                if z in everyid and z not in chosenid:
                    print('\n')
                    print("No matches of given employee id and name found!")
                    return

                for i in x:
                    if not i[1]==z:
                        new1.append(i)
                    if i[0]!=a:
                        new1.append(i)

                for i in new1:
                    if i not in final:
                        final.append(i)

            if len(final)==len(x):
                print('\n')
                print("id does not exist!")
                flag=1
                return

                    
            if len(new1)>1 and flag==0:
                with open ("binary_.dat",'wb') as file:
                        pickle.dump(final,file)
                        print("record deleted successfully!")
                        return
                
            try:
                if var==1 and flag==0:
                    with open ("binary_.dat",'wb') as file:
                        pickle.dump(lst1,file)
                        print("record deleted successfully!")
            except:
                print('')
        except:
            print("invalid input!")           
                
                
def binary_menu():
        while True:
            a=input("\nenter your choice: \n1:add records \n2:display all records \n3:arrange records in ascending order \n4:display records above entered salary \n5:give salary bonus to any employee \n6:delete any record \n7:clear all records  \n8:break \n \n")
            if a=='1':
                add_binary()
            elif a=='2':
                display_binary()
            elif a=='3':
                arrange_binary()
            elif a=='4':
                display2_binary()
            elif a=='5':
                modify_binary_1()
                modify_binary()
            elif a=='6':
                delete_binary()
            elif a=='7':
                clear_binary()
            elif a=='8':
                print("thank you :)")
                break
            else:
                print("invalid input!!!")
                    

            

"""CSV FILE"""            

if not os.path.isfile("student.csv"):
    file=open("student.csv",'w')
    file.close()

def clear_csv():
    file=open("records.txt",'r')
    x=csv.reader(file)
    lst=[]
    for i in x:
        lst.append(i)
    if len(lst)==0:
        print("File is already empty!")
    else:
        a=input("Are you sure you wish to delete all records?(Y/N) ")
        if a in['y','Y']:
            file=open("student.csv",'w',newline='')
            print("all records deleted!")
            file.close()

def add_csv():
    with open("student.csv",'r') as f:
        l=[]
        ids2=[]
        z=csv.reader(f)
        for i in z:
            l.append(i[1])
    file=open("student.csv",'a',newline='')
    y=csv.writer(file)
    lst=[]

    try:
        while True:
            a=input("enter student name: ")
            if a=="undo":
                    return
            words=a.split()
            new="_".join(words)

            while True:
                b=int(input("enter student admission number: "))
                b=abs(b)
                for i in lst:
                    ids2.extend(i)

                if str(b) not in l and int(b) not in ids2:
                    break
                else:
                    print("admission number already exists!")

                
                    
                
            while True:
                c = float(input("enter your percentage: "))
                if c>100 or c<0:
                    print("invalid input!!!")
                else:
                    break

            d=input("do you wish to add more records? (Y/N): ")
            q=[new,b,c]
            lst.append(q)
            if d in ['n', 'N']:
                break
        y.writerows(lst)
        print("records added successfully!")
        file.close()

    except:
        print("invalid input!!!")
    

def display_csv():
    file1=open("student.csv",'r')
    x=csv.reader(file1)
    for i in x:
        print(i)
    file1.close()

def display2_csv():
    file2=open("student.csv",'r')
    x=csv.reader(file2)
    try:
        a=float(input("enter percentage: "))
        for i in x:
            if float(i[2])>a:
                print(i)
    except:
         print("invalid input!!!")

    file2.close()


def arrange_csv():
    with open('student.csv', 'r') as f:
        x=csv.reader(f)
        q=sorted(x)
        
        with open("student.csv",'w',newline='') as file:
                    y=csv.writer(file)
                    y.writerows(q)
                    print("records arranged succesfully!")



def modify_csv():
    global lst
    lst=[]
    file3=open("student.csv",'r')
    x=csv.reader(file3)
    for i in x:
        if '95'>=i[2]>'90':
        lst.append(i)
    print("records updated successfully!")
    file3.close()

def modify2_csv():
    file4=open("student.csv",'w',newline='')
    x=csv.writer(file4)
    x.writerows(lst)
    file4.close()

def modify_ini():
    try:
        global exitt
        exitt=0
        with open("student.csv",'r') as f1:
            global flag_var
            flag_var=0

            x=csv.reader(f1)
            global a111
            a111=input("enter student name: ")            
            new1=[]
            
            global admns
            admns=[]

            global chosenadmn2
            chosenadmn2=[]
            for i in x:
                admns.append(i[1])
                if i[0]==a111:
                    new1.append(i)
                    chosenadmn2.append(i[1])
            
            if len(new1)==0:
                print("student not found!")
                exitt=1
                return

            if len(new1)>1:
                print('\n')
                flag_var=1
                global admn_csv
                admn_csv=int(input("more than two students have the same name! \nEnter current admission number of the student whose record you wish to update: "))
                print('\n')
    except:
        print("invalid input!!!")
        exitt=1
        return
            

def modify4_csv():
    if exitt==1:
        return

    try:
        if str(admn_csv) not in admns:
            print("amdn no. does not exist!")
            return

        if str(admn_csv) not in chosenadmn2:
            print("match not found!")
            return
    except:
        pass

    l=[]
    new=[]
    new1=[]
    flag=0
    file6=open("student.csv",'r')
    x=csv.reader(file6)            
    try:
        for i in x:
            if flag_var==1:
                ch=1
                if int(i[1])==admn_csv:
                    print("match found!")
                    print(i)
                    
                    while True:
                        b=int(input("enter new admission number: "))
                        if str(b) not in admns:
                            break
                        else:
                            print("admission number already exists!")
                    b=abs(b)
                    i[1]=b
                    flag=1
                
            if i[0]==a111 and flag_var==0 :
                ch=1
                while True:
                    b=int(input("enter new admission number: "))
                    if str(b) not in admns:
                        break
                    else:
                        print("admission number already exists!")
                b=abs(b)
                i[1]=b
            l.append(i)
    

        try:
            if ch==1:
                print("record updated successfully!")
        except:
            print("student not found!")

        file7=open("student.csv",'w',newline='')
        x=csv.writer(file7)
        x.writerows(l)
        file7.close()

    except:
        print("invalid input!!!")

    

def delete_csv():
    ch=0
    flag=0
    lst=[]
    new=[]
    new1=[]
    new2=[]
    new3=[]
    newlst=[]
    final=[]
    everyadmn=[]
    chosenadmn=[]
    
    a=input("enter student name: ")
    print('\n')
    with open("student.csv",'r') as file8:
        x=csv.reader(file8)
        for i in x:
            everyadmn.append(i[1])
            lst.append(i)
            if i[0]==a:
                chosenadmn.append(i[1])
                ch=1
                print(i)
        if ch==0:
            print("student not found!")
            return
                
        print('\n')                    
        try:
             with open("student.csv",'r') as f:
                o=csv.reader(f)
                for i in o:
                    if not i[0]==a:
                         new.append(i)

                    if i[0]==a:
                         new1.append(i)

                    if not i[0]==a:
                        new3.append(i)
        except:
            print('')

        if len(new1)>1:
            inp=input("are you sure you wish to delete any of the above records? (Y/N)")
        else:
            inp=input("are you sure you wish to delete the above record? (Y/N)")

        if inp in ['y','Y']:
            b=1
        else:
            print("no records deleted!")
            return
            


        if len(new1)>1:
            print('\n')
            z=input("Two or more students have the same name! \nEnter admn no. of the student whoose records you wish to delete: ")
            car=1
            if z in everyadmn and z not in chosenadmn:
                    print('\n')
                    print("No matches of given admn no. and name found!")
                    return

        with open("student.csv",'r') as file9:
            if len(new1)>1:
                k=csv.reader(file9)
                for i in k:
                    newlst.append(i)
                    if not i[1]==z:
                        new2.append(i)
                    if not i[0]==a:
                        new2.append(i)

                for i in new2:
                    if i not in final:
                        final.append(i)

                if len(final)==len(lst):
                    print("admn no. not found!")
                    return

                try:
                    if len(new1)>1 and flag==0:
                        with open("student.csv",'w',newline='') as file10:
                            y=csv.writer(file10)
                            y.writerows(final)
                            print("record deleted successfully!")
                except:
                    print('')        
    
    try:
        if ch==1:
            if len(new1)==1 and flag==0:
                with open("student.csv",'w',newline='') as file:
                    y=csv.writer(file)
                    y.writerows(new)
                    print("record deleted successfully!")
    except:
        print('')

    
    
    
def csv_menu():
        while True:
                inp=input("\nenter your choice: \n1:add   \n2:display all \n3:display records above percentage \n4:arrange records in ascending order \n5:add 5% to all records above 90 \n6:modify admission number \n7:delete any record \n8:clear all records  \n9:break \n \n")
                if inp=='1':
                    add_csv()
                elif inp=='2':
                    display_csv()
                elif inp=='3':
                    display2_csv()
                elif inp=='4':
                    arrange_csv()
                elif inp=='5':
                    modify_csv()
                    modify2_csv()
                elif inp=='6':
                    modify_ini()
                    modify4_csv()
                elif inp=='7':
                    delete_csv()
                elif inp=='8':
                    clear_csv()
                elif inp=='9':
                    print("Thank you :)")
                    break
                else:
                    print("invalid input!!!")
   
        

            
"""MENU"""

def main():
    while True:
        a=input("\nenter your choice: \n1: TEXT FILE \n2: BINARY FILE \n3: CSV FILE \n4: BREAK \n")

        if a=='1':
              text_menu()
        elif a=='2':
            binary_menu()
        elif a=='3':
            csv_menu()
        elif a=='4':
            print("Thank you for your time :]")
            break
        else:
            print("invalid input!!!")

main()



