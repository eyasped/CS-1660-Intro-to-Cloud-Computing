import os

def Hadoop():    
    print("1. Appache Hadoop")
    
def Spark():
    print("2. Appache Spark")
    
def JupyterNotebook():
    print("3. Jupyter Notebook")
    command_str = 'python -m webbrowser -t "http://localhost:8888/tree" '
    os.system(command_str)
    
def  Sonar():
    print("4. SonarQube and SonarScanner \n")
    
# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Ask for the user's choice.
    choice = input("\n------Welcome to Big Data Processing Application----- \n "+
            "Please type the number that corresponds to which application you would like to run: \n" +
            "1. Appache Hadoop \n" +
            "2. Appache Spark \n" +
            "3. Jupyter Notebook \n" +
            "4. SonarQube and SonarScanner \n" +
            "Enter q to quit. \n"+
            "Enter your input: ")
    
    # Respond to the user's choice.
    if choice == '1':
        Hadoop()
    elif choice == '2':
        Spark()
    elif choice == '3':
        JupyterNotebook()  
    elif choice == '4':      
        Sonar()
    elif choice == 'q':
        print("\nThanks for using this app. See you later.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")
        