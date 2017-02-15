import os
def print_menu(): 
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. LineageOS"
    print "2. Stock Android"
    print "3. Kernel Builder"
    print "4. Device Information"
    print "5. Exit"
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
     
    if choice==1:     
        os.system("python LineageOS/Setup.py")
    elif choice==2:
        print "Not implemented yet"
    elif choice==3:
        print "Not implemented yet"
    elif choice==4:
        print "Not implemented yet"
    elif choice==5:
	exit()
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        raw_input("Wrong option selection. Enter any key to try again..")
