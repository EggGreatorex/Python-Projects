

def greeting():
  # RUN AT THE START OF THE PROGRAM. GET USER INPUT AND RETURN ITS VALUE
  print("Welcome to notes.")
  sign_or_log = input("Would you like to sign-up or log-in using an existing account? ")
  handleInputs("signOrLog", sign_or_log.lower())

def handleInputs(typeOfInput,input):
  # CALL A PROCEDURE BASED ON THE TYPE OF USER INPUT E.G. LOGIN / SIGNUP
  if typeOfInput == "signOrLog":
    handleSignOrLog(input)


def handleSignOrLog(input):
  # CHECK TO SEE WHAT THE USER ENTERED
  signInWords = ["sign up", "sign-up", "signup"]
  logInWords = ["log in", "log-in", "login"]

  if input in signInWords:
    signUpMenu()
  elif input in logInWords:
    logInMenu()
  else:
    print("Could not understand your input.")
    greeting()



def signUpMenu():
  # GET USERNAME FROM THE USER. CHECK FOR EXITSING USERNAME
  userNameTaken = False
  username = input("Enter a username: ")
  try:
    takenUsernameFile = open('./textFiles/takenUsernames.txt','r')
    takenUsernameList = takenUsernameFile.readlines()
    
    for name in takenUsernameList:
      print("In List")
      print(name)
      name = name.lower().strip().replace(" ", "")
      username = username.lower().strip().replace(" ", "")
      if username == name:
        userNameTaken = True
  except FileNotFoundError:
    print("Dev Note : Error finding username list")

  if userNameTaken == False:
    password = input("Enter a password: ")
    createUser(username,password)
  elif userNameTaken == True:
    print("Username taken.")
    signUpMenu()



def logInMenu():
  correctLogin = False
  username = input("Enter username: ").lower()
  password = input("Enter password: ")

  try:
    file = open(f'./textFiles/{username}.txt', 'r')
    fileLines = file.readlines()
    for line in fileLines:
        if password.strip() == line.strip():
          correctLogin = True
  except FileNotFoundError:
    print("Found no account under that username.")
    logInMenu()

  file.close()

  if correctLogin:
    print("Correct username and password...")
    # Proceed with the main functionality or menu for the logged-in user
    openUserNotes(username)
  else:
    print("Incorrect username or password.")
    logInMenu()



def createUser(username,password):
  # CREATE A FILE TO STORE USER PASSWORD USING THE USERNAME + .TXT
  try:
    newFile = open(f"./textFiles/{username.lower()}.txt",'a')
    newFile.write(password.strip())
    newFile.close()
    print("Dev Note : File created.")
    try:
      takenUsernameFile = open("./textFiles/takenUsernames.txt",'a')
      takenUsernameFile.write(username)
      takenUsernameFile.write("\n")
      takenUsernameFile.close()
      print("Dev Note : Taken username list updated")
      openUserNotes(username)
    except FileNotFoundError:
      print("Dev Note : Taken usernane list file could not be found")
  except FileExistsError:
    print("Dev Note : Error in creating file. FileExistsError")



def openUserNotes(user):
  # Open the notes text file starting with <user>
  try:
    userNotes = open(f"./userNoteFiles/{user}Notes.txt",'r')
    userNotesLines = userNotes.readlines()
    # Remove newline characters from each string in the list as we add a new line later on when appending the notes to our txt file
    userNotesLines = [line.strip() for line in userNotesLines]  
    userNotes.close()
    if userNotesLines:
      showUserNotes(userNotesLines,user)
    else:
      addUserNotes(userNotesLines,user)
  except FileNotFoundError:
    print("Dev Note: File could not be found. Attempting to create file.")
    try:
      userNotes = open(f"./userNoteFiles/{user}Notes.txt",'a')
      userNotes.close()
      print("File successfully created")
      userNotes = open(f"./userNoteFiles/{user}Notes.txt",'r')
      userNotesLines = userNotes.readlines()
      userNotes.close()
      if userNotesLines:
        showUserNotes(userNotesLines,user)
      else:
        print("File empty")
        addUserNotes(userNotesLines,user)
    except FileNotFoundError:
      print("Dev Note: File could not be created.")


def showUserNotes(notes,user):
  print("\n Your Notes:")
  print("\n-------------------------------------------------------------------\n-------------------------------------------------------------------")
  # Show the user the current stored notes in the file
  for line in notes:
    print(line)
  addUserNotes(notes,user)

def addUserNotes(notes,user):
  from datetime import datetime

  # Get the current date and time
  current_datetime = datetime.now()

  # Count to keep track of how many new lines have been entered
  count = 0

  more = True
  print("\n-------------------------------------------------------------------\n-------------------------------------------------------------------")
  # Allow the user to make an input to append to the file
  print("You can now add notes to your file. Enter 'exit' to leave the notes. NOTE: Each entry is on one line. Press Enter and make a new input to add text to a new line")
  while more:
    userInput = input(">>>> ")
    if userInput.lower() == "exit":
      more = False
      saveOrDiscard = input("Would you like to save your notes or discard changes? ")
      if saveOrDiscard.lower() == "save":
        try:
          userNotes = open(f"./userNoteFiles/{user}Notes.txt",'w')
          # Get pointer of the "Last edited <time>" from the previous session.
          originalPointer = len(notes) - (count)
          # Minus 1 so that the pointer works correctly with array indexing
          originalPointer -= 1
          # Pop users indexing whereas remove uses a specific value as parameter
          if originalPointer > 0:
            notes.pop(originalPointer)
          for line in notes:
            userNotes.write(line)
            userNotes.write("\n")
          userNotes.write(f"Last edited: {current_datetime}")
          userNotes.close()
          print("File successfully saved.")
        except FileNotFoundError:
          print('Dev Note : Could not find user file.')
      elif saveOrDiscard.lower == "discard":
        print("Changes not saved.")
    else:
      notes.append(userInput)
      count += 1


def main():
    greeting()

if __name__ == "__main__":
    main()
