# Copyright (c) 2021, Dashiell Ratcliffe
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 

# Thanks for viewing DASHOS Source Code! Leave any suggested improvments as I would love looking through them! Have a nice day :)

# Known errors:
# Cannot run gaminghub or any external python file twice

#TODO:
#Fix 'cd .' bug when in root dir

try:
  # For games (random number generation)
  import random
  # Invisible input
  import getpass
  # time.sleep()
  import time
  # To hash inputs
  import hashlib
  # For removing, deleting, copying etc. files
  import shutil
  # More file related and os related things
  import os
  # Find paths for files and folders
  from os import path
  # Colored text
  from termcolor import colored
  from termcolor import cprint
except Exception:
  print("There are missing modules on this device that are required for <DASHOS> functionality")
  print("Make sure you have python3 installed and are using it to run <DASHOS>\n\n")
  print("All modules used in <DASHOS>:\nrandom, getpass, time, hashlib, shutil, os, (from os) path, (from termcolor) colored, (from termcolor) cprint\n")
  print("Python3 comes with the above modules pre-installed except termcolor")
  print("To install Termcolor for Windows run in cmd: 'pip install termcolor'")
  print("To install Termcolor for Linux run in terminal: 'sudo apt-get install -y python-termcolor'\n")
  print("If you are still missing modules, reinstall python3 and install the missing modules seperately")
  exit()

os.system('cls' if os.name == 'nt' else 'clear')

# Get login details, loginsuccess set false
def Loginput(logincount):
  global loginsuccess
  loginsuccess = False
  # Keep asking for uname and pword unless they have been entered correctly (loginsuccess = True)
  if loginsuccess == False:
    loginuname = getpass.getpass(colored("-> Username: ", promptcolour))
    loginpword = getpass.getpass(colored("-> Password: ", promptcolour))

    # Search all accounts for matching username and password
    Login(loginuname, loginpword, logincount)

# Count how many times the user has tried to login, 3 max
def Count(logincount):
  # Check if user has attempted to login more than 3 times
  if logincount == 3:
    cprint("\nToo many incorrect attempts", "red")
    time.sleep(1)
    Shutdown()
  # If not then ask for uname and pword again as last time was unsuccessful
  else:
    Loginput(logincount)

# When successful login, this is called and clears screen ready for CLI
def Loginsuccessor():
  # You are now logged in and can perform operations
  cprint("Successful Login!", "green")
  # Reset currentlyadmin in case previous user was admin
  global currentlyadmin
  currentlyadmin = False
  # Load config file
  global numtocol
  numtocol = {
    "1": "grey",
    "2": "red",
    "3": "green",
    "4": "yellow",
    "5": "blue",
    "6": "magenta",
    "7": "cyan",
    "8": "white",
  }
  # Check existence
  try:
    path = f"DASHOS/Accounts/Account{logincurrentuser}/config"
    f = open(path, "r")
    global promptcolour
    global clicolour
    global dircolour
    global filecolour
    global pycolour
    promptcolour = f.readline(1)
    clicolour = f.readline(1)
    dircolour = f.readline(1)
    filecolour = f.readline(1)
    pycolour = f.readline(1)
    promptcolour = numtocol[promptcolour]
    clicolour = numtocol[clicolour]
    dircolour = numtocol[dircolour]
    filecolour = numtocol[filecolour]
    pycolour = numtocol[pycolour]
    f.close()
  except IOError:
    time.sleep(1)
    cprint("No config file found so loading defaults")
    path = f"DASHOS/Accounts/Account{logincurrentuser}/config"
    f = open(path, "w")
    f.write("78784")
    f.close()
  time.sleep(1.5)
  os.system('cls' if os.name == 'nt' else 'clear')
  # Go to command line as the user that Loginput() decided they were
  Cmdline(logincurrentuser, f"DASHOS/Accounts/Account{logincurrentuser}")



# Called when an error has been detected, will be dealt with depending on the protocol
def Error(protocol):
  print(" \n  \n  ")
  cprint("""
   __  ____    _    ____  _   _  __  
  / / |  _ \  / \  / ___|| | | | \ \ 
 / /  | | | |/ _ \ \___ \| |_| |  \ \\
 \ \  | |_| / ___ \ ___) |  _  |  / /
  \_\ |____/_/   \_\____/|_| |_| /_/ 
                                     
  _____ _  _____  _    _       _____ ____  ____    ___  ____  
 |  ___/ \|_   _|/ \  | |     | ____|  _ \|  _ \  / _ \|  _ \ 
 | |_ / _ \ | | / _ \ | |     |  _| | |_) | |_) || | | | |_) |
 |  _/ ___ \| |/ ___ \| |___  | |___|  _ <|  _ <|| |_| |  _ < 
 |_|/_/   \_\_/_/   \_\_____| |_____|_| \_\_| \_\ \___/|_| \_\\
  """, "red")
  time.sleep(1)
  # Tell user error code
  cprint("Error Code: " + protocol, "red")
  # If they are an admin (know the uname and pwor) they can still log in as a special user and try to fix problems manually.
  # This is not advised as logging in when there is an error could make things worse
  cprint("\nIf you are an admin, you may login anyway to try and fix errors and/or troubleshoot them manually", "red")
  wanttologin = input(colored("WARNING: This is not advised\n(Y/N)", "red", attrs=["bold"]))
  # If they do want to log in to fix errors manually then confirm they acctually are an admin
  if wanttologin.upper() == "Y":
    os.system('cls' if os.name == 'nt' else 'clear')
    global logincurrentuser
    logincurrentuser = 0
    # Currentuser 10 is admin - only accessible through fatal error and makes it safer to navigate
    Confirmadmin(10, "DASHOS")
  else:
    # If not admin or don't want to log in, fix error automatically based on protocol
    if protocol == "NUMUSERS_NOT_FOUND" or protocol == "NUMUSERS_CONFIGURED_INCORRECTLY":
      cprint("Please wait while <DASHOS> configures 'numusers'", "red")
      time.sleep(1)
      tempnumusers = 0
      # Check how many users exist based on account folder, write that number to numusers
      for i in range(0, 10):
        path = f"DASHOS/Accounts/Account{i}"
        if os.path.exists(path):
          tempnumusers += 1
        else:
          break
      path = "DASHOS/numusers"
      f = open(path, "w")
      f.write(str(tempnumusers))
      f.close()
      cprint("<DASHOS> will now shut down to save changes.", "red")
      cprint("After turning back on you should be able to login", "red")
      Shutdown()
    # No default or admin account was found so create one
    elif protocol == "NO_ACCOUNT_FOUND" or protocol == "NO_ADMIN_ACCOUNT_FOUND":
      cs = input(colored("To continue with setup and create an account press 'Y' or any other key for no ", "red"))
      if cs.upper() == "Y":
        print("\n")
        Createaccount(protocol)
      else:
        Shutdown()
    # Gaminghub.py was not found
    elif protocol == "GAMINGHUB_NOT_FOUND":
      cprint("\n'Gaminghub.py' which comes pre-installed with <DASHOS> has been either moved or deleted\nUnless you know where it has been moved to, a re-install of <DASHOS> is advised\n", "red")
      exit()
    elif protocol == "CHANGELOG_NOT_FOUND":
      cprint("\nNo changelog has been found.\nA changelog has been created to prevent errors but it is inaccurate.\nIn order to get the newest changelog, you must reinstall <DASHOS>", "red")
      path = "changelog"
      f = open(path, "w")
      f.write("v0.0\nCHANGELOG WAS NOT FOUND, REINSTALL <DASHOS> TO GET THE CHANGELOG AND CORRECT VERSION")
      exit()

# Exit program
def Shutdown():
  print("\nShutting Down", end="")
  time.sleep(0.5)
  # 'end="", flush = True' makes it so they print on the same line in the next available space
  cprint(".", attrs=["dark"], end="", flush = True)
  time.sleep(0.5)
  cprint(".", attrs=["dark"], end="", flush = True)
  time.sleep(0.5)
  cprint(".", attrs=["dark"])
  time.sleep(0.5)
  exit()

# Create a new account from the Error protocol, done as part of setup or when defaults were not found such as adminaccount
def Createaccount(protocol):
  accnumber = 0
  # If no default account was found, create a new default
  if protocol == "NO_ACCOUNT_FOUND":
    path = "DASHOS/Accounts/Account0/account0"
    f = open(path, "w")
    tempuname = input(colored("Please enter a username: ", promptcolour, attrs=["bold"]))
    temppword = input(colored("Please enter a password: ", promptcolour, attrs=["bold"]))
    # Encrypt data
    hasheduname = Hash(tempuname)
    hashedpword = Hash(temppword)
    f.write("\n")
    f.write(hasheduname)
    f.write("\n")
    f.write(hashedpword)
    f.close()
    time.sleep(1)
    cprint("Account Created\n ", "green")
    # Make numusers set to 1
    path = "DASHOS/numusers"
    f = open(path, "w")
    f.write("1")
    f.close()
    # Create default config file
    path = "DASHOS/Accounts/Account0/config"
    f = open(path, "w")
    f.write("78784")
    f.close()
    time.sleep(1)
  if protocol == "NO_ADMIN_ACCOUNT_FOUND":
    path = "DASHOS/Accounts/adminaccount"
    f = open(path, "w")
    adminuname = input(colored("Please enter an admin username: ", promptcolour, attrs=["bold"]))
    adminpword = input(colored("Please enter an admin password: ", promptcolour, attrs=["bold"]))
    hashedadminuname = Hash(adminuname)
    hashedadminpword = Hash(adminpword)
    f.write("\n")
    f.write(hashedadminuname)
    f.write("\n")
    f.write(hashedadminpword)
    f.close()
    time.sleep(1)
    cprint("Admin Account Created\n ", "green")
    time.sleep(1)
  cprint("<DASHOS> will now shut down to save changes.", "red")
  cprint("After turning back on you should be able to login", "red")
  Shutdown()

# Called once uname and pword have been entered by user - hashes both and checks with the real uname and pword every time for each account file and returns correct or incorrect
def Login(uname,pword,logincount):
  global logincurrentuser
  # Check if you want to reset DASHOS to defaults. Requires admin
  if uname.upper() == "$RESET" and pword.upper() == "$RESET":
    print("If you are an admin, you may now login.")
    confirm = input(colored("WARNING: This is not advised unless all login details have been lost\n(Y/N)", "red"))
    # Check if they are acctually an admin
    if confirm.upper() == "Y":
      logincurrentuser = 11
      Confirmadmin(11, "DASHOS")
    else:
      Shutdown()
  # Otherwise try to log them in
  else:
    path = "DASHOS/numusers"
    a = open(path, "r")
    # Read numusers so we know how many times to loop in order to check every accounts credentials file
    numusers1 = a.read()
    numusers = int(numusers1)
    # Now loop once for every existing account
    for i in range(0, numusers):
      # Reset uname and pword success from last time log in was attempted
      unamesuccess = False
      pwordsuccess = False
      # Open the account file asscociated with account (0 then 1 then 2 etc.)
      path1 = f"DASHOS/Accounts/Account{i}/account{i}"
      f = open(path1, "r")
      # For each line in account credentials file
      for i, line in enumerate(f):
        # If line 1 (username stored here)
        if i == 0:
          # Read the real username store in realuname
          realuname = f.readline()
          # Return hashed uname from Hash() function
          hasheduname = Hash(uname)
          lhasheduname = list(hasheduname)
          lhasheduname.append("\n")
          # Convert hashed uname list to string
          hasheduname = "".join(lhasheduname)
          # If hashed inputted uname is equal to real uname, uname was correct (unamesuccess = True)
          if realuname == hasheduname:
            unamesuccess = True
        # IMPORTANT: was tried with if i == 1 (if it is line 2, where password is stored) but that didn't work and for some reason this does :/
        if i == 0:
          #Same as uname
          realpword = f.readline()
          hashedpword = Hash(pword)
          if realpword == hashedpword:
            pwordsuccess = True
      # If both the password and username are correct for specific account file login was successful!
      if unamesuccess == True and pwordsuccess == True:
        loginsuccess = True
        logincurrentuser = int(f.name[-1])
        f.close()
        Loginsuccessor()
    # If they were not correct, increase login count and after checking Count(), restart the loop by checking the next account's credentials file.
    cprint("Incorrect username or password", "red")
    logincount += 1
    loginsuccess = False
    f.close()
    Count(logincount)

# Called when running sudo cmd, references hashed uname and pword to real ones and saves admin for entire session unless logout
def Confirmadmin(currentuser, currentdir):
  cprint("\nConfirm you are an admin", attrs=["bold"])
  # Reset adminloginsuccess from previous times
  global adminloginsuccess
  adminloginsuccess = False
  # Logincount works the same as before, 3 times max
  global adminlogincount
  adminlogincount = 0
  # Keep asking user for admin uname and pword until correct or too many tries
  while adminloginsuccess == False:
    adminloginuname = getpass.getpass(colored("\n-> Username: ", promptcolour))
    adminloginpword = getpass.getpass(colored("-> Password: ", promptcolour))
    adminunamesuccess = False
    adminpwordsuccess = False
    # Once entered, open admin account credentials file
    path = "DASHOS/Accounts/adminaccount"
    f = open(path, "r")
    # For each line in admin account file
    for i, line in enumerate(f):
      # If line 1 (username stored here)
      if i == 0:
        # Read the real username store in realuname
        adminrealuname = f.readline()
        # Return hashed uname from Hash() function
        adminhasheduname = Hash(adminloginuname)
        ladminhasheduname = list(adminhasheduname)
        ladminhasheduname.append("\n")
        adminhasheduname = "".join(ladminhasheduname)
        # If hashed inputted uname is equal to real uname, uname was correct (unamesuccess = True)
        if adminrealuname == adminhasheduname:
          adminunamesuccess = True
      # IMPORTANT: was tried with if i == 1 (if it is line 2, where password is stored) but that didn't work and for some reason this does :/
      if i == 0:
        # Same as uname
        adminrealpword = f.readline()
        adminhashedpword = Hash(adminloginpword)
        if adminrealpword == adminhashedpword:
          adminpwordsuccess = True
    f.close()
    # If both the password and username are correct for admin account file login was successful!
    if adminunamesuccess == True and adminpwordsuccess == True:
      # Set currentlyadmin so user has elevaated privileges for rest of session
      global currentlyadmin
      currentlyadmin = True
      # If user is 11 (came from error) log in as correct user and set path to DASHOS
      if currentuser == 11:
        os.system('cls' if os.name == 'nt' else 'clear')
        Cmdline(11, "DASHOS")
      # Otherwise go back to command line that user was before
      else:
        Cmdline(currentuser, currentdir)
    # If incorrect, increase count
    else:
      cprint("Incorrect username or password", "red")
      adminlogincount += 1
      adminloginsuccess = False
    # If too many attempts
    if adminlogincount == 3:
      cprint("Too many attempts", "red")
      # Check if in setup mode, in which case they never logged in so shouldn't go back to a command line like a normal user(would be a security flaw)
      if currentuser == 10 or currentuser == 11:
        Shutdown()
      Cmdline(logincurrentuser, currentdir)


# Called whenever a string needs to be hashed
def Hash(text):
  # Encode text so it can be hashed
  x = text.encode()
  # Call hashlib which hashes the encoded string input
  str = hashlib.sha256(x)
  hashtext = str.hexdigest()
  # Return the hashed string
  return(hashtext)

# Updates the numusers file correctly depending on the protocol
def Updatenumusers(protocol):
  # If just adding a new user
  if protocol == "ADD_USER":
    # Open numusers to read how many current users
    path = "DASHOS/numusers"
    f = open(path, "r")
    oldnumusers = int(f.read())
    f.close()
    # newnumusers is same as old +1 (as adding new user)
    newnumusers = oldnumusers + 1
    snewnumusers = str(newnumusers)
    # Open numusers again for writing and overwrite all data with newnumusers
    f = open(path, "w")
    f.write(snewnumusers)
    f.close()
    newdir = "DASHOS/Accounts"
    Cmdline(logincurrentuser, newdir)

#-------------------------------------------------
#-------------------------------------------------
# The CLI, core of the program, all commands are described in the 'Help' function
#-------------------------------------------------
#-------------------------------------------------
def Cmdline(currentuser, currentdir):
  currentcmd = input(colored(f"\n{currentdir}: ", clicolour))

  if currentcmd.lower() == "":
    print("Please enter a command")
    Cmdline(currentuser, currentdir)

  if currentcmd.lower() == "sudo":
    if currentlyadmin == False:
      Confirmadmin(currentuser, currentdir)
    else:
      print("You are already an admin")
      Cmdline(currentuser, currentdir)

  if currentcmd[0].lower() == "o" and currentcmd[1].lower() == "s":
    Oslibcmd(currentuser, currentdir, currentcmd)

  if currentcmd.lower() == "clear":
    os.system('cls' if os.name == 'nt' else 'clear')
    Cmdline(currentuser, currentdir)

  if currentcmd.lower() == "version":
    path = "changelog"
    f = open(path, "r")
    version = f.readline()
    f.close()
    print(version)
    Cmdline(currentuser, currentdir)
  
  if currentcmd.lower() == "changelog":
    os.system('cls' if os.name == 'nt' else 'clear')
    path = "changelog"
    f = open(path, "r")
    changelog = f.read()
    f.close
    print(changelog)
    while True:
      done = input(colored("\nWhen you are finished here enter 'Y' ", promptcolour))
      if done.lower() == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        Cmdline(currentuser, currentdir)

  if currentcmd[0].lower() == "c" and currentcmd[1].lower() == "d" and currentcmd[2].lower() == " ":
    Changedirectory(currentcmd, currentuser, currentdir)

  elif currentcmd[0].lower() == "m" and currentcmd[1].lower() == "v" and currentcmd[2].lower() == " ":
    Movefile(currentcmd, currentdir)

  elif currentcmd[0].lower() == "c" and currentcmd[1].lower() == "p" and currentcmd[2].lower() == " ":
    Copyfile(currentcmd, currentdir)

  elif currentcmd.lower() == "gaminghub":
    __import__("gaminghub.py")

  elif currentcmd.lower() == "whoami":
    if currentlyadmin == True:
      print(f"sudo account{currentuser}\n")
    else:
      print(f"account{currentuser}\n")
    Cmdline(currentuser, currentdir)

  elif currentcmd[0].lower() == "c" and currentcmd[1].lower() == "a" and currentcmd[2].lower() == "t" and currentcmd[3].lower() == " ":
    Cat(currentcmd, currentdir)

  elif currentcmd.lower() == "logout":
    print("\n")
    Loginput(0)

  elif currentcmd.lower() == "customise":
    Customiseconfig(currentuser, currentdir)

  elif currentcmd.lower() == "users":
    Users(currentuser, currentdir)

  elif currentcmd.lower() == "python":
    Pythonfile(currentuser, currentdir)

  elif currentcmd.lower() == "sysreset":
    if currentlyadmin == True:
      cprint("\nAre you sure you would like to reset <DASHOS> and reinstall accounts etc?\nWARNING: THIS WILL DELETE ALL DATA, FILES AND FOLDERS", "red")
      confirm = input("(Y/N)")
      if confirm.upper() == "Y":
        Sysreset()
      else:
        print("Sysreset cancelled")
        Cmdline(currentuser, currentdir)
    else:
      cprint("Permission denied", "red")
      Cmdline(currentuser, currentdir)
  
  elif currentcmd[0].lower() == "m" and currentcmd[1].lower() == "a" and currentcmd[2].lower() == "t" and currentcmd[3].lower() == "h":
    Math(currentcmd, currentdir)

  elif currentcmd[0].lower() == "r" and currentcmd[1].lower() == "m" and currentcmd[2].lower()== " ":
    Removefile(currentcmd, currentuser, currentdir)
  
  elif currentcmd[0].lower() == "l" and currentcmd[1].lower() == "s":
    if len(currentcmd) > 3:
      Listotherdirectory(currentuser, currentdir, currentcmd)
    else:
      Listdirectory(currentuser, currentdir)

  elif currentcmd.lower() == "shutdown":
    Shutdown()

  elif currentcmd.lower() == "help":
    Help(currentuser, currentdir)

  elif currentcmd[0].lower() == "m" and currentcmd[1].lower() == "k" and currentcmd[2].lower() == "d" and currentcmd[3].lower() == "i" and currentcmd[4].lower() == "r" and currentcmd[5].lower() == " ":
    Createdir(currentcmd, currentdir)
  
  elif currentcmd[0].lower() == "c" and currentcmd[1].lower() == "r" and currentcmd[2].lower() == "e" and currentcmd[3].lower() == "a" and currentcmd[4].lower() == "t" and currentcmd[5].lower() == "e" and currentcmd[6].lower() == " ":
    Createfile(currentcmd, currentdir)

  else:
    cprint("Command does not exist\nUse 'help' to get a list of commands and what they do", "white")
    Cmdline(logincurrentuser, currentdir)


#-------------------------------------------------
#-------------------------------------------------
# Commands
#-------------------------------------------------
#-------------------------------------------------

def Oslibcmd(currentuser, currentdir, currentcmd):
  currentcmd = currentcmd[3:]
  if currentlyadmin == True:
    confirm = input(colored("Running an 'os' command bypasses <DASHOS> security features - potentially making it unusable.\nMake sure you know what you are doing!(Y/N) ", "red"))
    if confirm.lower() == "y":
      os.system(currentcmd)
    else:
      cprint("Cancelled", "red", attrs=["bold"])
  else:
    cprint("Permission denied", "red")
  Cmdline(currentuser, currentdir)

# Customise colours of <DASHOS>
def Customiseconfig(currentuser, currentdir):
  # Tell user what possible colours and to input them as numbers
  print("\nCustomise <DASHOS> colours")
  print("Colour options:", colored("grey(1)", "grey"), colored("red(2)", "red"), colored("green(3)", "green"), colored("yellow(4)", "yellow"), colored("blue(5)", "blue"), colored("magenta(6)", "magenta"), colored("cyan(7)", "cyan"), colored("white(8)", "white"),)
  cprint("Input colours as numbers\n", attrs=["bold"])
  time.sleep(1)
  promptcol = input(colored("Prompt colour: ", "cyan"))
  clicol = input(colored("CLI prompt colour: ", "cyan"))
  dircol = input(colored("'ls' shows directories as this colour: ", "cyan"))
  filecol = input(colored("'ls' shows files as this colour: ", "cyan"))
  pycol = input(colored("Python command colour: ", "cyan"))
  # Open user's config file
  path = f"DASHOS/Accounts/Account{currentuser}/config"
  f = open(path, "w")
  # Set numlist to the combination of the numbers (total string)
  numlist = promptcol + clicol + dircol + filecol + pycol
  # Write options to config file
  f.write(numlist)
  f.close()
  f = open(path, "r")
  global promptcolour
  global clicolour
  global dircolour
  global filecolour
  global pycolour
  promptcolour = f.readline(1)
  clicolour = f.readline(1)
  dircolour = f.readline(1)
  filecolour = f.readline(1)
  pycolour = f.readline(1)
  promptcolour = numtocol[promptcolour]
  clicolour = numtocol[clicolour]
  dircolour = numtocol[dircolour]
  filecolour = numtocol[filecolour]
  pycolour = numtocol[pycolour]
  f.close()
  Cmdline(currentuser, currentdir)

# The CLI Calculator
def Math(currentcmd, currentdir):
  # Remove 'math ' from the cmd
  n = 5
  lcmd = list(currentcmd)
  lcurrentcmd = lcmd[n:]
  currentcmd = "".join(map(str, lcurrentcmd))
  sepcmd = currentcmd.split(" ")
  # Try to seperate 3 parts of equation, if not successful user has not used correct syntax
  try:
    num1 = int(sepcmd[0])
    num2 = int(sepcmd[2])
    operation = sepcmd[1]
  except Exception:
    cprint("Math Error", "red")
    Cmdline(logincurrentuser, currentdir)
  # Calculate result and print
  if operation == "*":
    answer = num1 * num2
  elif operation == "/":
    answer = num1 / num2
  elif operation == "+":
    answer = num1 + num2
  elif operation == "-":
    answer = num1 - num2
  print(answer)
  Cmdline(logincurrentuser, currentdir)


# Called when executing a python script
def Pythonfile(currentuser, currentdir):
  # Ask user what they want to do
  cprint("Please input a number based on what you are trying to do", pycolour)
  cprint("1. Execute python script\n2. Delete python script\n3. View python scripts", pycolour)
  cmd = int(input())
  # If execute
  if cmd == 1:
    # Make sure admins as only they are allowed to execute
    if currentlyadmin == True:
      # If admin warn them only to run python files from trusted source before asking for the filename
      cprint("Only run programs from a trusted source", "red")
      tempfname = input(colored("File name: ", pycolour))
      # If they try to run the main program file, deny request
      if tempfname == "main.py" or tempfname == "DASHOS.py":
        cprint("Permission denied", "red")
      # If the python file exists and it is not main.py, execute it
      elif os.path.exists(tempfname):
        listfname = list(tempfname)
        lfname = listfname[:-3]
        fname = "".join(map(str,lfname))
        try:
          __import__(fname)
        except:
          cprint("\n<DASHOS> encountered an error when executing external script", "red")
          print(Exception)
      # If file not found
      else:
        cprint("File not found", "red")
    # If not admin, deny request
    else:
      cprint("Permission Denied - only admins can execute scripts for security", "red")
  # If delete script
  elif cmd == 2:
    # Ask for script to delete
    fname = input(colored("File name: ", pycolour))
    # If trying to delete main program file, gaminghub or changelog file deny request
    if fname == "main.py" or fname == "gaminghub.py" or fname == "changelog":
      cprint("Permission denied", "red")
    # If not main.py, gaminghub.py or changelog and path exists, delete file
    elif os.path.exists(fname):
      os.remove(fname)
    # If path does not exist
    else:
      cprint("File not found", "red")
  # If view python files
  elif cmd == 3:
    # List root directory and remove the first 5 options (main.py, DASHOS etc.) so it only prints user made python files
    files = os.listdir()
    lfiles = files[5:]
    lfiles.remove("main.py")
    files = "  ".join(map(str, lfiles))
    cprint("\n" + files, "blue", attrs=["bold"])
  # If not 1,2 or 3 then not a valid option
  else:
    cprint("Please select a valid option", "red")
  # Return to CLI
  Cmdline(currentuser, currentdir)

# Delete a user, you can always delete yourself, never account0, and only others if admin
def Removeaccount(currentuser, currentdir):
  # Ask for user to delete
  user = int(input(colored("User to remove (0-9): ", "green", attrs=["dark"])))
  # Cannot delete default user
  if user == 0:
    cprint("You cannot remove the default user", "red")
    Cmdline(currentuser, currentdir)
  # Check if user exists
  path = f"DASHOS/Accounts/Account{user}"
  if os.path.exists(path):
    # If deleting self, delete directory Account{self} recursively
    if user == currentuser:
      # Remove directory recursively
      shutil.rmtree(path)
      path1 = "DASHOS/numusers"
      # Read current numusers and minus 1
      f = open(path1, "r")
      tempnumusers = int(f.readline())
      f.close()
      # Overwrite numusers with the new numusers
      f = open(path1, "w")
      newnumusers = tempnumusers - 1
      f.write(str(newnumusers))
      f.close()
      print("<DASHOS> will now shut down to save changes")
      Shutdown()
    # If admin, don't worry about deleting other accounts as they are allowed, same as above
    elif currentlyadmin == True:
      shutil.rmtree(path)
      path1 = "DASHOS/numusers"
      f = open(path1, "r")
      tempnumusers = int(f.readline())
      f.close()
      f = open(path1, "w")
      newnumusers = tempnumusers - 1
      f.write(str(newnumusers))
      f.close()
      print("<DASHOS> will now shut down to save changes")
      Shutdown()
    # If not deleting own account and not admin, deny request
    else:
      cprint("Permission denied", "red")
      Cmdline(currentuser, currentdir)
  # If user not found, user does not exist (unless misconfigured numusers)
  else:
    cprint("User does not exist", "red")
    Cmdline(currentuser, currentdir)

# Called for all account-based activity
def Users(currentuser, currentdir):
  #Ask user how to modify accounts
  cprint("Please input a number based on what you are trying to do:", "green", attrs=["dark"])
  cprint("1. Change current user login details\n2. Add a new user\n3. Remove a user", attrs=["dark", "bold"])
  usercmd = input()
  # If change credentials
  if usercmd == "1":
    Loginid(currentuser, currentdir)
  # If add new user
  elif usercmd == "2":
    # Only admins can add a new user
    if currentlyadmin == False:
      cprint("Permission denied", "red")
      Cmdline(currentuser, currentdir)
    # If admin, create new account
    else:
      Addaccount()
  # If remove account
  elif usercmd == "3":
    Removeaccount(currentuser, currentdir)
  # If not 1,2 or 3 then not a valid option
  else:
    cprint("Please select a valid option", "red")
    Cmdline(currentuser, currentdir)

# Copy a file from one place to the next
def Copyfile(currentcmd, currentdir):
  # Remove 'rm ' from the cmd
  n = 3
  currentcmdlist = list(currentcmd)
  cmdl = currentcmdlist[n:]
  # Convert into list and get full filename and destination path
  cmd = "".join(map(str, cmdl))
  cmdlist = cmd.split(" ")
  filename = cmdlist[0]
  path = cmdlist[1]
  # Convert path to full path
  pathandfname = path + "/" + filename
  filenamepath = f"{currentdir}/{filename}"
  # If copying account file, config file or gaminghub deny request
  if filenamepath == f"DASHOS/Accounts/Account{logincurrentuser}/account{logincurrentuser}":
    cprint("Permission denied", "red")
    Cmdline(logincurrentuser, currentdir)
  if filenamepath == f"DASHOS/Accounts/Account{logincurrentuser}/config":
    cprint("Permission denied", "red")
    Cmdline(logincurrentuser, currentdir)
  # If file does not already exist (attempted overwrite) and destination does exist allow the copy
  if not os.path.exists(pathandfname) and os.path.exists(path):
    # If copying outside account folder, must be admin
    if f"DASHOS/Accounts/Account{logincurrentuser}" not in path:
      if currentlyadmin == False:
        cprint("Permission denied", "red")
        Cmdline(logincurrentuser, currentdir)
    # If copying inside own folder, try to copy it as a file
    try:
      shutil.copy(filenamepath, path)
    # If that fails, try to copy as a directory
    except IOError:
      try:
        shutil.copytree(filenamepath, pathandfname)
      # If both fail, source and/or destination was not found
      except IOError:
        cprint("Source file or directory not found", "red")
    Cmdline(logincurrentuser, currentdir)
  else:
    cprint("Destination file or directory not found or directory already exists", "red")
    Cmdline(logincurrentuser, currentdir)

# Move a file from one place to the next
def Movefile(currentcmd, currentdir):
  #Remove 'mv ' from the cmd
  n = 3
  currentcmdlist = list(currentcmd)
  cmdl = currentcmdlist[n:]
  cmd = "".join(map(str, cmdl))
  # Get the filename and destination path
  cmdlist = cmd.split(" ")
  filename = cmdlist[0]
  path = cmdlist[1]
  filenamepath = f"{currentdir}/{filename}"
  # If file is account file, deny request
  if filenamepath == f"DASHOS/Accounts/Account{logincurrentuser}/account{logincurrentuser}":
    cprint("Permission denied", "red")
    Cmdline(logincurrentuser, currentdir)
  if filenamepath == f"DASHOS/Accounts/Account{logincurrentuser}/config":
    cprint("Permission denied", "red")
    Cmdline(logincurrentuser, currentdir)
  # If trying to move file not in user folder, must be admin
  if f"DASHOS/Accounts/Account{logincurrentuser}" not in path:
    if currentlyadmin == False:
      cprint("Permission denied", "red")
      Cmdline(logincurrentuser, currentdir)
  # If destination exists, try to move file
  if os.path.exists(path):
    try:
      shutil.move(filenamepath, path)
    # If it fails, source was not found
    except IOError:
      cprint("Source file or directory not found or file already exists", "red")
    Cmdline(logincurrentuser, currentdir)
  # If path does not exist, destination was not found
  else:
    cprint("Destination file or directory not found", "red")
    Cmdline(logincurrentuser, currentdir)

# Read contents of text file
def Cat(currentcmd, currentdir):
  # Remove 'cat ' from cmd
  n = 4
  tempcmdlist = list(currentcmd)
  cmdlist = tempcmdlist[n:]
  filename = "".join(map(str, cmdlist))
  # Try to open the specified file for reading
  try:
    # Merge specified path to current dir
    path = f"{currentdir}/{filename}"
    f = open(path, "r")
  # If file not found
  except IOError:
    cprint("File not found", "red")
    Cmdline(logincurrentuser, currentdir)
  # If file found, count = number of lines in file
  count = len(open(path).readlines())
  # For each line, text = line of file, print text
  for i, line in enumerate(f):
    text = f.read()
    print(text)
  f.close()
  Cmdline(logincurrentuser, currentdir)

# Change/write account details
def Loginid(currentuser, currentdir):
  # Path to file that needs to be changed
  path = f"DASHOS/Accounts/Account{currentuser}/account{currentuser}"
  f = open(path, "w")
  # Prompt for new uname and pword
  tempuname = input(colored("\nPlease enter your new username: ", promptcolour, attrs=["bold"]))
  temppword = input(colored("Please enter your new password: ", promptcolour, attrs=["bold"]))
  # Hash entered uname and pword
  hasheduname = Hash(tempuname)
  hashedpword  = Hash(temppword)
  # Write the hashed values to the file
  f.write("\n")
  f.write(hasheduname)
  f.write("\n")
  f.write(hashedpword)
  f.close()
  cprint("Account details has been successfully updated", "green")
  Cmdline(currentuser, currentdir)

# Add a new account
def Addaccount():
  # Get current numusers
  path = "DASHOS/numusers"
  f = open(path, "r")
  tempnumusers = f.readline()
  f.close()
  # If max users
  if tempnumusers == "10":
    cprint("Maximum number of users (10) has been reached.\nTo create a new account, delete a previous one", "red")
    (logincurrentuser, f"DASHOS/Accounts/Account{logincurrentuser}")
  # If not max users
  else:
    # Make directory for the new account
    os.mkdir(f"DASHOS/Accounts/Account{int(tempnumusers)}")
    # Get uname and pword for this new account
    tempuname = input(colored("Please enter a username for the new account: ", promptcolour, attrs=["bold"]))
    temppword = input(colored("Please enter a password for the new account: ", promptcolour, attrs=["bold"]))
    # Create account file and hash entered uname and pword
    path = f"DASHOS/Accounts/Account{tempnumusers}/account{tempnumusers}"
    f = open(path, "w")
    hasheduname = Hash(tempuname)
    hashedpword = Hash(temppword)
    # Write hashed uname and pword to account file
    f.write("\n")
    f.write(hasheduname)
    f.write("\n")
    f.write(hashedpword)
    f.close()
    path = f"DASHOS/Accounts/Account{tempnumusers}/config"
    f = open(path, "w")
    f.write("78784")
    f.close()
    cprint("Account successfully created", "green")
    # Update the numusers file
    Updatenumusers("ADD_USER")

# Reset the entire system, deleting all non-core files
def Sysreset():
  # Warn user not to exit, or very weird things could happen
  cprint("Sysreset in progess. Do not exit the program", "red")
  # Get current number of users
  path = "DASHOS/numusers"
  f = open(path, "r")
  tempnumusers = int(f.read())
  # For each user, recursively delete their account folder with all data in
  for i in range(0, tempnumusers):
    userpath = f"DASHOS/Accounts/Account{i}"
    shutil.rmtree(userpath)
    # For default user, once deleted create the Account0 folder
    if i == 0:
      path = "DASHOS/Accounts/Account0"
      os.makedirs(path)
  f.close()
  # Remove all other core files
  path = "DASHOS/numusers"
  os.remove(path)
  path = "DASHOS/Accounts/adminaccount"
  os.remove(path)
  time.sleep(0.5)
  cprint("<DASHOS> has been successfully wiped", "red", attrs=["bold"])
  Shutdown()

# Remove a single file or directory
def Removefile(currentcmd, currentuser, currentdir):
  # Remove 'rm ' from cmd
  lcurrentcmd = list(currentcmd)
  for i in range(0,3):
    lcurrentcmd.pop(0)
  # Get path to file
  filename = "".join(map(str, lcurrentcmd))
  path = f"{currentdir}/{filename}"
  boolean = os.path.exists(path)
  # If path exists
  if boolean == True:
    # If trying to delete account file or config file, deny request
    if filename == f"account{currentuser}":
      cprint("Permission denied", "red")
      Cmdline(currentuser, currentdir)
    if filename == "config" or filename == "Accounts" or filename == "Account0":
      cprint("Permission denied", "red")
      Cmdline(logincurrentuser, currentdir)
    # Try to open the file for writing
    else:
      try:
        f = open(path, "w")
        f.close()
      # If cannot open file
      except IOError:
        # If directory does not have contents
        if not os.listdir(path):
          os.rmdir(path)
          Cmdline(currentuser, currentdir)
        # If directory has contents, warn user
        else:
          print("This directory is not empty")
          confirm = input(colored("Are you sure you would like to remove it and all its contents? (Y/N)", "red"))
          # If user is sure, remove directory recursively
          if confirm.upper() == "Y":
            shutil.rmtree(path)
            Cmdline(currentuser, currentdir)
          else:
            cprint("\nCancelled", "red")
            Cmdline(currentuser, currentdir)
  # If file does not exist
  else:
    cprint("File or directory not found", "red")
    Cmdline(currentuser, currentdir)
  os.remove(path)
  Cmdline(currentuser, currentdir)

# List the files and directories in the current directory or a specified directory
def Listdirectory(currentuser, currentdir):
  print("\n")
  # Get directories and files and store in variables
  dirs = next(os.walk(currentdir))[1]
  files = next(os.walk(currentdir))[2]
  dirs = "  ".join(map(str, dirs))
  files = "  ".join(map(str, files))
  # Print them out as config colours
  print(colored(dirs, dircolour), "", colored(files, filecolour))
  print("\n")
  Cmdline(currentuser, currentdir)

def Listotherdirectory(currentuser, currentdir, currentcmd):
  print("\n")
  # Remove 'ls ' from the command
  directory = currentcmd[3:]
  # If listing directory is in current directory
  if directory[0] == "?":
    directory = directory[1:]
    # Get full path by combining current directory with target directory
    fullpath = currentdir + "/" + directory
    # If directory exists
    if os.path.exists(fullpath):
      # Get directories and files in target directory and store in variables
      dirs = next(os.walk(fullpath))[1]
      files = next(os.walk(fullpath))[2]
      dirs = "  ".join(map(str, dirs))
      files = "  ".join(map(str, files))
      # Print them out as config colours
      print(colored(dirs, dircolour), "", colored(files, filecolour))
      print("\n")
    # If directory doesn't exist
    else:
      cprint("Directory does not exist", "red")
  # Otherwise listing directory with use of full path
  else:
    if os.path.exists(directory):
      # If target directory outside of current user directory
      if f"DASHOS/Accounts/Account{logincurrentuser}" not in directory:
        # If not admin
        if currentlyadmin == False:
          cprint("Permission denied", "red")
          Cmdline(logincurrentuser, currentdir)
      # Get directories and files in target directory and store in variables
      dirs = next(os.walk(directory))[1]
      files = next(os.walk(directory))[2]
      dirs = "  ".join(map(str, dirs))
      files = "  ".join(map(str, files))
      print(colored(dirs, dircolour), "", colored(files, filecolour))
      print("\n")
    else:
      cprint("Directory does not exist", "red")
  Cmdline(currentuser, currentdir)

# Displays how to use all the commands
def Help(currentuser, currentdir):
  os.system('cls' if os.name == 'nt' else 'clear')
  print("""
  HELP:
    COMMANDS:
        customise: Allows you to customise colours of certain things to your liking

        sudo: Will prompt to confirm you are an admin
              If you login as an admin successfully it will save until shutdown
              Admins have elevated privileges
        
        shutdown: Will shutdown the program and close any files still open

        version: Will display the current <DASHOS> version

        changelog: Will display the <DASHOS> changelog

        clear: Will clear the CLI to clean up messy text

        cd: Will change current directory to specified path e.g. cd DASHOS/Accounts/Account0
            'cd ..' will change to the previous directory
            'cd ?[directoryname]' will check your current directory for the named directory - quicker than typing the entire path
        
        create: Will create a text or python file in the current directory e.g. create mynewtextfile
                Files will be text by default and python if they end in '.py' e.g. create script.py
                Text:
                  After running, a space below will open to type whatever you want
                  You cannot go 'up' lines and this command will replace any previous file named the same
                  Once you are finished, go to a new line and type '//exit' to save your file
                Python:
                  The writing and exiting process is the same as a text file
                  Python files are saved in the root directory and can only be modified using the python command

        mkdir: Will create a new directory in your current one e.g. mkdir testfolder1

        ls: Will list all directories and then files in the current directory
            This can be used to list other directories e.g. 'ls DASHOS/Accounts'
            A question mark will mean you don't have to list the full path as long as the target directory is in the current directory e.g. 'ls ?Accounts'
        
        cat: Will display the contents of the specified file name e.g. cat notebookfile

        rm: Will remove the specified file or directory. The exact path is not needed e.g. rm badfile

        whoami: Will display the current user and if they're admin or not

        python: Will prompt to either remove or execute the contents of a .py file
                Only ever execute files from a trusted source

        math: Will solve the given equation
              Spaces must be left in between e.g. math 6 * 3

        mv: Will move the specified file or directory to the specified location e.g. 'mv myfile DASHOS/Accounts'

        cp: Will copy the specified file or directory to the specified location e.g. 'mv myfile DASHOS/Accounts'

        logout: Will logout from the current account

        users: Will guide you through a process of creating deleting, or modifying a user account

        gaminghub: Will bring you to the gaming hub, where you can play games

        sysreset: Reset <DASHOS> by deleting all accounts and their data

        os: Allows admins to run commands that interact directly with the os library
            e.g. 'os pwd' will send 'pwd' to the os library


    OTHER:
        $RESET: Typing this from the login screen as username and password will allow you to login as admin
            Prompt will confirm you are admin before login.
            Should only be used if you are unable to login from any account
            If the admin account's details are forgot as well as all accounts, then a manual reinstall is required.
        
        Admin: An admin account can do anything with <DASHOS> whereas a standard user may not
                An admin can make changes that affect all users and <DASHOS> itself
                A user may only make a change that affects themself
                All accounts can login as admin, provided they have the username and password

        Shortcuts: While on the CLI, pressing the up arrow key will go to the previous input you entered.
                   This can be navigated upwards or downwards



  """)
  cprint("  This Python Script That Attemps To Recreate A Windows-Linux CLI Was Made By Dashiell Ratcliffe                                                                   \n  This Program Is Open-Source, If You Paid For It Demand A Refund", "white", "on_grey", attrs=["bold"])
  # Keep printing unless user input 'y' and is finished
  while True:
    done = input(colored("\nWhen you are finished here enter 'Y' ", promptcolour))
    if done.upper() == "Y":
      os.system('cls' if os.name == 'nt' else 'clear')
      Cmdline(currentuser, currentdir)
    
# Create a new file
def Createfile(currentcmd, currentdir):
  # Remove 'create ' from cmd
  n = 7
  listfilename = list(currentcmd)
  tempfilename = listfilename[n:]
  filename = "".join(map(str, tempfilename))
  # If there is no filename
  if filename == "":
    cprint("Please enter a filename", promptcolour)
    Cmdline(logincurrentuser, currentdir)
  # If file name attempts to mimic core file, deny request
  if filename == "numusers" or filename == "main.py" or filename == "config" or filename == "gaminghub.py" or filename == "changelog":
    cprint("Permission denied", "red")
    Cmdline(logincurrentuser, currentdir)
  for i in range(0,10):
    if filename == f"account{i}":
      cprint("Permission denied", "red")
      Cmdline(logincurrentuser, currentdir)
  # Filename is valid and now check if it is a python file
  listfilename = list(filename)
  pyfile = False
  if listfilename[-1] == "y" and listfilename[-2] == "p" and listfilename[-3] == ".":
    pyfile = True

  lfiletext = []
  quit = False
  # Keep asking user to input their file text until they type //exit
  while quit == False:
    temptext = input("  ")
    # If they want to quit
    if temptext == "//exit":
      # If it is a python file, store in the root directory under specified filename
      if pyfile == True:
        path = filename
        if os.path.exists(path):
          confirm = input(colored("File already exists, are you sure you would like to overwrite? (Y/N) ", "red"))
          if confirm.upper() != "Y":
            cprint("Cancelled", "red")
            Cmdline(logincurrentuser, currentdir)
      # Else store in the current directory under specified filename
      else:
        path = f"{currentdir}/{filename}"
      # Now we have the path to the file, create it and open for writing
      f = open(path, "w")
      # Number of lines determined by values in list lfiletext
      numvalues = len(lfiletext)
      linenum = [""]
      f.write("\n")
      # For each line the user entered
      for i in range(0, numvalues):
        #write the text the user wrote on the line the user wrote it on after a \n to make a new line
        f.write(f"{(linenum[i] + lfiletext[i])}")
        linenum.append("\n")
      print("\n")
      f.close()
      Cmdline(logincurrentuser, currentdir)
    # If still editing, add the entered text to the list and repeat
    else:
      lfiletext.append(temptext)

# Create new directory
def Createdir(currentcmd, currentdir):
  # Remove 'mkdir ' from the cmd
  n = 6
  listdirname = list(currentcmd)
  tempdirname = listdirname[n:]
  # Get the dirname and the path to it
  dirname = "".join(map(str, tempdirname))
  path = f"{currentdir}/{dirname}"
  # If directory does not already exist, create it
  if not os.path.exists(path):
    os.makedirs(path)
  # If it does exist, don't create
  else:
    cprint("\nDirectory already exists", "red")
  Cmdline(logincurrentuser, currentdir)

# Change the current directory
def Changedirectory(currentcmd, currentuser, currentdir):
  # Remove 'cd ' from the cmd
  n = 3
  listcd = list(currentcmd)
  ldirectory = listcd[n:]
  directory = "".join(map(str, ldirectory))
  # If special characters are involved, do something different
  if directory[0] == "?" or directory == "..":
    # If using ? in cmd
    if directory[0] == "?":
      # Get the directory name
      ldirectory = list(directory)
      ldirectory.pop(0)
      # Join the specified directory with the current directory to get the full path
      ldirectory.insert(0,"/")
      directory = "".join(map(str, ldirectory))
      fulldir = currentdir + directory
      # Check if the path is a directory or a file
      pathexists = os.path.isdir(fulldir)
      # If path is a directory
      if pathexists == True:
        # If trying to leave user folder, deny request unless admin
        if f"DASHOS/Accounts/Account{currentuser}" not in fulldir:
          if currentlyadmin == False:
            cprint("Permission denied", "red")
            Cmdline(logincurrentuser, currentdir)
          # Otherwise set the current directory to the specified directory
          else:
            currentdir = fulldir
            Cmdline(logincurrentuser, currentdir)
        # Otherwise set the current directory to the specified directory
        else:
          currentdir = fulldir
          Cmdline(logincurrentuser, currentdir)
      # If path not found
      else:
        cprint("Directory does not exist", "red")
      Cmdline(logincurrentuser, currentdir)
    # Otherwise they are trying to go back to the previous directory
    else:
      # If already in root directory, they cannot go back further
      if currentdir == "DASHOS":
        cprint("You are already in the root directory", "red")
        Cmdline(currentuser, currentdir)
      # If not in root directory already
      else:
        # Split the current directory path by each /
        ldirectory = currentdir.split("/")
        # Remove the last item
        del ldirectory[-1]
        # Add the slashes back
        tempdir = "/".join(map(str, ldirectory))
        # If the target direcotry not in user folder, deny request unless admin
        if f"DASHOS/Accounts/Account{currentuser}" not in tempdir:
          if currentlyadmin == False:
            cprint("Permission denied", "red")
            Cmdline(logincurrentuser, currentdir)
          # Otherwise, change currentdirectory to the previous one
          else:
            currentdir = tempdir
            Cmdline(logincurrentuser, currentdir)
        # Otherwise, change currentdirectory to the previous one
        else:
          currentdir = tempdir
          Cmdline(logincurrentuser, currentdir)
  # If normal cd request
  else:
    # Check if the path exists
    pathexists = os.path.isdir(directory)
    if pathexists == True:
      # If the path is out of the users folder, deny request unless admin
      if f"DASHOS/Accounts/Account{currentuser}" not in directory:
        if currentlyadmin == False:
          cprint("Permission denied", "red")
          Cmdline(logincurrentuser, currentdir)
        # Otherwise change the current directory to the once specified
        else:
          currentdir = directory
          Cmdline(logincurrentuser, currentdir)
      # Otherwise change the current directory to the once specified
      else:
        currentdir = directory
        Cmdline(logincurrentuser, currentdir)
    # If path not found
    else:
      cprint("Directory does not exist", "red")
    Cmdline(logincurrentuser, currentdir)

#-------------------------------------------------






# Startup visuals of <DASHOS>
cprint("""
            ▄       ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄      ▄     
           ▐░▌     ▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌    ▐░▌    
          ▐░▌      ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌     ▐░▌   
         ▐░▌       ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌      ▐░▌  
        ▐░▌        ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌       ▐░▌ 
       ▐░▌         ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌        ▐░▌
        ▐░▌        ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌       ▐░▌ 
         ▐░▌       ▐░▌       ▐░▌▐░▌       ▐░▌          ▐░▌▐░▌       ▐░▌      ▐░▌  
          ▐░▌      ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌     ▐░▌   
           ▐░▌     ▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌    ▐░▌    
            ▀      ▀▀▀▀▀▀▀▀▀▀    ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀      ▀     
""", "yellow")
cprint("""
     _                                   _       ____               _                   
    / \    ___  ___  ___   _   _  _ __  | |_    / ___|  _   _  ___ | |_  ___  _ __ ___  
   / _ \  / __|/ __|/ _ \ | | | || '_ \ | __|   \___ \ | | | |/ __|| __|/ _ \| '_ ` _ \ 
  / ___ \| (__| (__| (_) || |_| || | | || |_     ___) || |_| |\__ \| |_|  __/| | | | | |
 /_/   \_\\\___|\___|\___/  \__,_||_| |_| \__|   |____/  \__, ||___/ \__|\___||_| |_| |_|
                                                        |___/
""", "yellow", end="")

try:
  path = "changelog"
  f = open(path)
  version = f.readline()
  f.close()
except IOError:
  Error("CHANGELOG_NOT_FOUND")

print(version)

time.sleep(1)

# Set colours to default until logged in (as we don't know who is logging in)
# IMPORTANT: The order of the following is how it is structured in the config file
global promptcolour
promptcolour = "cyan"
global clicolour
clicolour = "white"
global dircolour
dircolour = "cyan"
global filecolour
filecolour = "white"
global pycolour
pycolour = "yellow"


# Confirm important file exist, if not call Error() with proper protocol
try:
  path = "DASHOS/Accounts/adminaccount"
  f = open(path)
  f.close()
except IOError:
  Error("NO_ADMIN_ACCOUNT_FOUND")

try:
  path = "DASHOS/Accounts/Account0/account0"
  f = open(path)
  f.close()
except IOError:
  Error("NO_ACCOUNT_FOUND")

try:
  path = "gaminghub.py"
  f = open(path)
  f.close()
except IOError:
  Error("GAMINGHUB_NOT_FOUND")

try:
  path = "changelog"
  f = open(path)
  f.close()
except IOError:
  Error("CHANGELOG_NOT_FOUND")

try:
  path = "DASHOS/numusers"
  f = open(path, "r")
  # Read numusers to make sure it is not empty
  contents = f.read()
  f.close()
  if contents == "":
    Error("NUMUSERS_CONFIGURED_INCORRECTLY")
except IOError:
  Error("NUMUSERS_NOT_FOUND")


# Now the program has validated everything is working as intended
cprint("""\n\n\n\n
  _                _           
 | |    ___   __ _(_)_ __    _ 
 | |   / _ \ / _` | | '_ \  (_)
 | |__| (_) | (_| | | | | |  _ 
 |____|\___/ \__, |_|_| |_| (_)
             |___/\n\n
""", "cyan")

# Now all core-files are ok, login
Loginput(0)