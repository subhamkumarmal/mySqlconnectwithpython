from tasks.tasks import task1,task2,task3,task4,task5
conditions ='Y'

while conditions=='Y':
    taskSelect =int(input(" 1.CREATE \n 2.READ \n 3.INSERT \n 4.DELETE \n 5.DROP TABLE\n"))

    if taskSelect==1:
        task1()
    elif taskSelect==2:
        task2()
    elif taskSelect==3:
        task3()
    elif taskSelect==4:
        task4()
    elif taskSelect==5:
        task5()
    else:
        print("Kindly enter the correct input for the task : ")

    conditions=input("do you want to continute the task Y/N").upper()




