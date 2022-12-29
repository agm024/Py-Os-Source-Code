
password='a'

theme='blue'
apps=["Terminal","TicTacToe","Python","Firefox","Wikipedia","Settings","MyFiles"]
rapps=["Terminal","Tictactoe","Python","Firefox","Wikipedia","Settings","Myfiles"]
gameboard={"A1":"- ","A2":"- ","A3":"- ","B1":"- ","B2":"- ","B3":"- ","C1":"- ","C2":"- ","C3":"- "} #For TicTacToe
from termcolor import cprint
cprint("Loading proccess started",theme,attrs=['bold','underline'])
cprint("Please wait for loading to complete for the best results in Py OS",theme)
from replit import db as DB
from os import *
from random import randint as random
from time import sleep
import wikipedia
from tkinter import *
from tkinter import filedialog
import tkinter
import webbot
system('pip install webbot')
colors=['Red', 'Yellow', 'Green', 'Cyan', 'Blue', 'Magenta', 'White']

#list1.sort()

system("clear")
cprint("Loading proccess complete!",theme,attrs=['bold','underline'])
cprint("Now ready to run Py OS",theme)
sleep(1)
system("clear")

def openfile():
  name= filedialog.askopenfilename()
  print("Click the directory to open : "+name)
  Label(main, text="File selected : ", font = ("Arial","10")).pack()
  Label(main, text=name, font = ("Arial","15")).pack()
  Label(main, text="\nUse the console to open the file", font = ("Arial","10")).pack()
  error_msg="Error!"
def Myfiles():
  main = Tk()
  main.geometry("300x250")
  main.configure(bg='white')
  main.title("MyFiles")
  Label(main, text="Click the following to select a file - after you will be able to open it with the console :", font = ("Arial","10"), pady="5", padx="5").pack()
  Button(main,text="Select file", pady="4", padx="6", command=openfile,bg="darkblue",font=("Verdana", 15),  fg="white").pack()
  Label(main, text="\n", font = ("Arial","10")).pack()
  main.mainloop()
def print(t):
  cprint(t,theme,attrs=['bold'])
def Wikipedia():
  while 1==1:
    system('clear')
    global res
    cprint("Search Wikipedia",theme,attrs=['bold'],end=" ")
    cprint("(type 'Back' to leave)",theme,end=" ")
    cprint(":",theme,attrs=['bold'])
    res = input(" ")
    print("")
    if res.upper()=="BACK":
      system('clear')
      break
    try:
      summary = wikipedia.summary(res, sentences=4)
      cprint(summary,theme)
      print("")
      input("Press enter to do another search ")
    except:
      cprint("No results found.",'red',attrs=['bold'])
      sleep(2)
      system('clear')
def Terminal():
  system('clear')
  cprint("Terminal interpreter/compiler",theme,attrs=['bold'])
  print("")
  cprint('Type "Back" to leave',theme)
  print("")
  list=[]
  while 1==1:
    x=input("$ ")
    if x.lower()=="back":
      system('clear')
      break
    if x=="clear":
      list.clear()
    system("clear")
    y="$ "+x
    list.append(y)
    for i in list:
      cprint(i,theme)
    system(x)
def Python():
  system('clear')
  system('python3')
  system('clear')
def Chrome():
  system('clear')
  try:
    web = webbot.Browser()
    web.go_to("https://google.com")
  except:
    system('clear')
    cprint("Uh Oh! An error took place. Unable to open Chrome",'red',attrs=['bold'])
    sleep(2)
def Firefox():
  system("clear")
  try:
    cprint("Press Ctrl+C in the Console to exit Firefox",theme,attrs=['bold'])
    print("")
    system("firefox")
  except:
    system('clear')
    cprint("Uh Oh! An error took place. Unable to open Firefox",'red',attrs=['bold'])
def Tictactoe():
  while 1==1:
    displayBoard()
    print("Player 1's turn :")
    p1=input(" ")
    p1=p1.upper()
    check=0
    for var in gameboard.keys():
      if var==p1:
        check=1
    if (not(check==1)):
      print("Please enter a valid area :")
      p1=input(" ")
      check=0
      for var in gameboard.keys():
        if var==p1:
          check=1
      if (not(check==1)):
        print("Player 1's turn skipped")
    else:
      if gameboard[p1]=="- ":
        gameboard[p1]="X "
      else:
        print("Place taken (Player 1's turn was skipped)")
      if lefttoright("X ")==1:
        break
    
    displayBoard()
    print("Player 2's turn :")
    p2=input(" ")
    p2=p2.upper()
    check=0
    for var in gameboard.keys():
      if var==p2:
        check=1
    if (not(check==1)):
      print("Please enter a valid area :")
      p2=input(" ")
      check=0
      for var in gameboard.keys():
        if var==p2:
          check=1
      if (not(check==1)):
        print("Player 2's turn skipped")
    else:
      if gameboard[p2]=="- ":
        gameboard[p2]="O "
      else:
        print("Place taken (Player 2's turn was skipped)")
      if lefttoright("O ")==1:
        break
def displayBoard(): #For TicTacToe
  system('clear')
  print("  1 2 3")
  print("A "+gameboard["A1"]+gameboard["A2"]+gameboard["A3"])
  print("B "+gameboard["B1"]+gameboard["B2"]+gameboard["B3"])
  print("C "+gameboard["C1"]+gameboard["C2"]+gameboard["C3"])
  print("")
def lefttoright(player): #For TicTacToe
  co=1
  lefttoright=0
  for var in gameboard.values():
    if ((gameboard["A1"]==player)and((gameboard["A2"]==player)and(gameboard["A3"]==player))):
      print("Player "+player+" has won")
      return(1)
      break
    elif ((gameboard["B1"]==player)and((gameboard["B2"]==player)and(gameboard["B3"]==player))):
      print("Player "+player+" has won")
      return(1)
      break
    elif ((gameboard["C1"]==player)and((gameboard["C2"]==player)and(gameboard["C3"]==player))):
      print("Player "+player+" has won")
      return(1)
      break
    elif ((gameboard["A1"]==player)and((gameboard["B1"]==player)and(gameboard["C1"]==player))):
      print("Player "+player+" has won")
      return(1)
      break
    elif ((gameboard["A2"]==player)and((gameboard["B2"]==player)and(gameboard["C2"]==player))):
      print("Player "+player+" has won")
      return(1)
      break
    elif ((gameboard["A3"]==player)and((gameboard["B3"]==player)and(gameboard["C3"]==player))):
      print("Player "+player+" has won")
      return(1)
      break
    elif ((gameboard["A1"]==player)and((gameboard["B2"]==player)and(gameboard["C3"]==player))):
      print("Player "+player+" has won")
      return(1)
      break
    elif ((gameboard["A3"]==player)and((gameboard["B2"]==player)and(gameboard["C1"]==player))):
      print("Player "+player+" has won")
      return(1)
      break
  return("0")
def Login():
  system('clear')
  cprint("Password",theme,attrs=['bold'],end=" ")
  cprint("(default is 'a')",theme,end=" ")
  cprint(":",theme,attrs=['bold'])
  if input(" ")=='a':
    system('clear')
    cprint("Correct Password Entered",theme,attrs=['bold'])
    sleep(1)
    Load()
    Load()
    cprint("Loading Complete!",theme,attrs=['bold'])
    sleep(2)
  else:
    print("")
    cprint("Incorrect Password Entered",'red',attrs=['bold'])
    sleep(2)
    LoginT()
def Login2():
  system('clear')
  cprint("Password",theme,attrs=['bold'],end=" ")
  cprint("(default is 'a')",theme,end=" ")
  cprint(":",theme,attrs=['bold'])
  if input(" ")=='a':
    system('clear')
    cprint("Correct Password Entered",theme,attrs=['bold'])
    sleep(1)
    Load()
    Load()
    cprint("Loading Complete!",theme,attrs=['bold'])
    sleep(2)
  else:
    print("")
    cprint("Incorrect Password Entered",'red',attrs=['bold'])
    sleep(2)
    Login()
def Load():
  system('clear')
  cprint("Loading.",theme,attrs=['bold'])
  sleep(0.3)
  system('clear')
  cprint("Loading..",theme,attrs=['bold'])
  sleep(0.3)
  system('clear')
  cprint("Loading...",theme,attrs=['bold'])
  sleep(0.3)
  system('clear')
def Settings(password):
  actions=["Change the password","Change password","Password", "Change the theme","Change theme","Theme"]
  p=["Change the password","Change password","Password"]
  t=["Change the theme","Change theme","Theme"]
  system('clear')
  cprint("Hello, Welcome to Settings",theme,attrs=['underline','bold'])
  cprint("Settings is where you can customise Py OS - Make it your own.",theme)
  print("")
  cprint("What next?",theme,attrs=['underline','bold'])
  cprint("Enter anything from the list below to edit it",theme)
  print("")
  cprint("- Change the password\n",theme,attrs=['bold'])
  cprint("- Change theme\n",theme,attrs=['bold'])
  cprint("What would you like to do?",theme,attrs=['bold'])
  i=input(" ")
  i=i.capitalize()
  if i in actions:
    if i in p:
      system('clear')
      cprint("Let's first verify that it's you",theme,attrs=['bold'])
      cprint("Please enter your password to continue :",theme)
      i=input(" ")
      if i==password:
        system('clear')
        cprint("What would you like to change your password to?",theme,attrs=['bold'])
        i=input(" ")
        return(i)
        system('clear')
        cprint("Password set",theme,attrs=['bold'])
        sleep(2)
        system('clear')
        cprint("The new password is '"+i+"'",theme,attrs=['bold'])
    if i in t:
      system('clear')
      for i in colors:
        cprint(i,i.lower(),attrs=['bold'])
      print("")
      cprint("What color would you like to change the theme to?",theme,attrs=['bold'])
      i=input(" ")
      i=i.capitalize()
      if i in colors:
        return(i)
        system('clear')
        cprint("Theme set.",theme,attrs=['bold'])


def firsttime(i):
  if ((i.lower()=="yes")or(i.lower()=="yes.")):
    system('clear')
    cprint("Welcome to PyOS\n",theme,attrs=['bold','underline'])
    cprint("PyOS is well - an OS. PyOS was created 100% by Aarush.\n\n",theme)
    cprint("|",theme,end=" ", attrs=["bold"])
    cprint("Note! :",attrs=['bold'],end=" ")
    cprint("I Know You are New,")
    input("\n\nPress enter to continue")
    system('clear')
    cprint("Advantages\n",theme,attrs=['bold','underline'])
    cprint("PyOS is offline, fast and customisable. It has games, interpreters, search engines and more!\n",theme)
    input("Press enter to continue")
    system('clear')
    cprint("Disadvantages\n",theme,attrs=['bold','underline'])
    cprint("To think about it, No bugs or errors have been found in PyOS, so that doesn't really leave any disadvantage\n",theme)
    input("Press enter to continue")
    system('clear')
    cprint("Your turn\n",theme,attrs=['bold','underline'])
    cprint("It's time for you to try PyOS and see how all the things mentioned previously are true\n",theme)
    cprint("Press enter to run PyOS",theme,attrs=['bold'],end="")
    input("")
  elif ((i.lower()=="no")or(i.lower()=="no.")):
    Login()
  else:
    cprint("'"+i+"' is invalid. Please enter 'Yes','Yes.', 'No' or 'No.' to continue.",'red',attrs=['bold'])
    sleep(4)
    system('clear')
    cprint("Is this your first time on Py OS?",theme,attrs=['bold','underline'])
    cprint("If your new, you can see to help you use Py OS",theme)
    i=input(" ")
    firsttime(i)

system('clear')
cprint("Is this your first time on Py OS?",theme,attrs=['bold','underline'])
cprint("If your new, you can see a quick intro to Py OS ",theme)
i=input(" ")
firsttime(i)
while 1==1:
  system('clear')
  co=1
  for AppName in apps:
    cpr=AppName
    cprint(cpr,theme)
    co+=1
  print("")
  cprint("|",theme,end=" ", attrs=["bold"])
  cprint("Tip! :",attrs=['bold'],end=" ")
  cprint("This isn't case sensitive - even if you type 'PyThOn' it will open Python\n")
  cprint("Which app would you like to open?",theme,attrs=['bold'])
  i=input(" ")
  i=i.capitalize()
  if (not(i in rapps)):
    print("")
    cprint("Unknown app entered. Please enter one of the apps listed above",'red',attrs=['bold'])
    sleep(2)
  else:
    if (not(i=="Settings")):
      exec(i+"()")
    else:
      i=Settings(password)
      a=i.capitalize()
      if ((a==i) and (i in colors)):
        theme=i.lower()
      else:
        password=i