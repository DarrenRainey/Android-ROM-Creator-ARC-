import os
def print_menu(): 
    print 30 * "-" , "Select Branch" , 30 * "-"
    print "1. CM-14 (Android 7.1)"
    print "5. Exit"
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
     
    if choice==1:     
        os.system("cd ~/android/system && repo init -u https://github.com/LineageOS/android.git -b cm-14.1")
        os.system("cd ~/android/system && repo sync")
        print("Sync Complete You Can Now Go Back And Build Some ROMS")
    elif choice==5:
	exit()
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        raw_input("Wrong option selection. Enter any key to try again..")
