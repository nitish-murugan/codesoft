#To-do List

while True:
    print("--------------------------")
    choice = int(input("1. Create a new task \n2.Update the existing task \n3.Track your process \n4.Exit \nEnter your choice ?! "))
    print("--------------------------")

    if choice==1:
        fileObj = open("task.txt",'a')
        task = input("Enter the task to be done: ")
        endTime = input("Enter the deadline of this task(DD/MM/YYYY) :")
        fileObj.write(task+" - "+endTime+'\n')
        print("Task added successfully")
        fileObj.close()
    
    elif choice==2:
        fileObj = open("task.txt",'r')
        print("Which task should be altered")
        data = fileObj.readlines()
        for index, txt in enumerate(data):
            print(f"{index+1}. {txt.strip()}")
        choice1 = int(input("Enter the task number to alter: "))
        choice2 = int(input("Do you want to extend the date (or) alter the task (or) Completed the task (1/2/3): "))
        if(choice2==3):
            del data[choice1-1]
            fileObj.close()
            fileObj = open("task.txt",'w')
            fileObj.writelines(data)
            fileObj.close()
        else:
            temp = data[choice1-1].split('-')
            if(choice2 == 1):
                dateNew = input("Enter the deadline of this task(DD/MM/YYYY) :")
                temp = temp[0]+"- "+dateNew
            elif(choice2 == 2):
                dataNew = input("Enter the task to be done: ")
                temp = dataNew+" -"+temp[1]
            data[choice1-1] = temp
            fileObj.close()
            fileObj = open("task.txt",'w')
            fileObj.writelines(data)
            fileObj.close()
        print("Task altered successfully")
        
    elif choice==3:
        print("Task in pending: ")
        fileObj = open("task.txt",'r')
        data = fileObj.readlines()
        for index, txt in enumerate(data):
            print(f"{index+1}. {txt.strip()}")

    elif choice==4:
        break
    
    else:
        print("Enter a valid choice")