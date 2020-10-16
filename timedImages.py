import os
import pyinputplus as pyip
from json import loads
from sys import exit
from pathlib import Path
from random import choice
from time import sleep, time
from tkinter import *
from PIL import Image, ImageTk

cwd = Path.cwd()
fileDirectory = os.path.dirname(__file__)
currentTime = 0
subsessionCounter = 0
sessionTimeValue = 0
allowedFormats = ["jpg", "png", "bmp", "gif", "tiff", "ppm"]
backgroundColor = "#2C2E33"

def ResizeImage(image):
    root.update()
    windowHeight = root.winfo_height()
    windowWidth = root.winfo_width()
    imgWidth, imgHeight = image.size

    xRatio = windowWidth / imgWidth
    yRatio = windowHeight / imgHeight

    if xRatio > yRatio:
        scaleTo = yRatio
    else:
        scaleTo = xRatio

    newWidth = round(imgWidth * scaleTo)
    newHeight = round(imgHeight * scaleTo)

    image = image.resize((newWidth, newHeight), Image.ANTIALIAS)
    return image


def UpdateTimer():
    global currentTime, timerLabel, sessionTimeValue
    currentTime -= 1
    sessionTimeValue -= 1
    currentTime = max(0, currentTime)
    sessionTimeValue = max(0, sessionTimeValue)

    if useClass == "yes":
        timerLabel.config(text=f"{int(currentTime)} - {round(sessionTimeValue / 60, 2)} - {subsessionCounter}/{currentSubsessionValue}")
    else:
        timerLabel.config(text=f"{int(currentTime)} - {round(sessionTimeValue / 60, 2)} - {subsessionCounter}")

    timerLabel.after(1000, UpdateTimer)


currentSubsessionValue = 0
def SetCurrentImageTime():
    global timePerImage, subsessionCounter, currentSubsessionValue
    currentSubsessionKey = list(chosenClass)[0]
    currentSubsessionValue = chosenClass[currentSubsessionKey]

    if currentSubsessionValue == 0 or subsessionCounter == currentSubsessionValue:
        del chosenClass[currentSubsessionKey]
        subsessionCounter = 0
        SetCurrentImageTime()
        return

    timePerImage = float(currentSubsessionKey)


def ResetTimer():
    global currentTime
    currentTime = timePerImage * 60

def UpdateImage():
    global imageLabel, subsessionCounter
        
    if time() - startTime > sessionTime * 60:
        print("""
        *******************************
                   Time's up!
        *******************************""")
        exit()
        
    try:
        randomImage = choice(allImages)
    except IndexError:
        print("""
        *******************************
        There are no more unique images
        *******************************""")
        exit()
    
    if allowRepeated == "no":
      allImages.remove(randomImage)

    img = Image.open(randomImage)
    img = ResizeImage(img)
    img = ImageTk.PhotoImage(img)
    subsessionCounter += 1

    if useClass == "yes":
        SetCurrentImageTime()

    ResetTimer()
    imageLabel.config(image=img)

    imageLabel.photo = img
    imageLabel.pack(fill=BOTH, expand=1)

    imageLabel.after(int(timePerImage * 60 * 1000), UpdateImage)


startTime = 0
def ImageViewer():
    global startTime
    startTime = time()
    try:
      while (allImages):
          UpdateImage()
          UpdateTimer()
          root.mainloop()
    except:
      exit()


print(f"The images used will be from {os.getcwd()}")

useClass = pyip.inputYesNo(prompt="Use Class Mode? ")

allClasses = []
allClassesNames = []
sessionTime = 0
if useClass == "yes":
    classesJson = os.path.join(fileDirectory, "classes.json")
    with open(f"{classesJson}", "r") as f:
        classesContent = loads(f.read())
        for key in classesContent["allClasses"]:
            allClasses.append(classesContent["allClasses"][key])
            allClassesNames.append(key)

    chosenClass = pyip.inputMenu(allClassesNames, numbered=True)
    chosenClass = allClasses[allClassesNames.index(chosenClass)]

    for key, value in enumerate(chosenClass):
        sessionTime += chosenClass[value] * float(value)
else:
    sessionTime = pyip.inputFloat(prompt="How many minutes do you want to practice? ")
    timePerImage = pyip.inputFloat(prompt="How many minutes do you want per image: ", greaterThan=0)

sessionTimeValue = sessionTime * 60

useRecursive = pyip.inputYesNo(prompt="Use recursive search? ")
allowRepeated = pyip.inputYesNo(prompt="Allow repeated images? ")
stayOnTop = pyip.inputYesNo(prompt="Stay on top? ")

allImages = []
if useRecursive == "yes":
    for root, _, files in os.walk(cwd):
        for currentFile in files:
            filePath = os.path.join(root, currentFile)
            
            fileFormat = filePath.lower()[-3:]
            if fileFormat in allowedFormats:
                allImages.append(filePath)
else:
    for currentFile in os.listdir():
        fileFormat = currentFile.lower()[-3:]
        if fileFormat in allowedFormats:
            allImages.append(os.path.join(cwd, currentFile))

root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry(f"{screenWidth}x{screenHeight}")
root.title("Timed Images")
root.state("zoomed")
root.configure(bg=backgroundColor)
if stayOnTop == "yes":
    root.attributes("-topmost", True)

timerLabel = Label(root, bg=backgroundColor,fg="#FFFFFF", font=('', 20, 'bold'))
timerLabel.pack(pady=20)

imageLabel = Label(root, image="", bg=backgroundColor)

ImageViewer()
