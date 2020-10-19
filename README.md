# Timed Images

## Table of Contents
1. [**Purpose**](#purpose)
1. [**Installation**](#installation)
1. [**Usage**](#usage)
1. [**Modes**](#modes)
1. [**Class Creation**](#class-creation)
***

### Purpose
The main purpose of **Timed Images** is to provide a simple solution for iterative practice.

**Timed Images** will randomly show you images from your current directory under your specifications. 

# Installation
### Requirements
- [**Python**](https://www.python.org/) (3.7+) ([**In PATH**](https://www.google.com/search?q=how%20to%20add%20python%20to%20path))
- [**PyInputPlus**](https://pypi.org/project/PyInputPlus/) (Run *'pip install PyInputPlus'* from **cmd**)
- [**Pillow**](https://pypi.org/project/Pillow/) (Run *'pip install Pillow'* from **cmd**)

If you are having troubles installing PyInputPlus, run *'pip install wheel'* before attempting to install PyInputPlus
***
1. Download [**TimedImages.zip**](https://github.com/simonsanchezart/Timed-Images/raw/master/TimedImages.zip)
2. Extract the contents to a folder
3. Add that folder to **%PATH%**


## Usage
1. Open **cmd**
2. Navigate to a folder with images
3. Run *'timedImages'*

Alternatively:

1. Open a folder with images
2. Press **CTRL+L**, type *'cmd'* and press return
3. Run *'timedImages'*

## Features
- Quick access from command line
- Recursive search
- Always on top (with possibility of minimization)
- Class mode with custom sessions

## Modes
### Class Mode
Classes consist of a series of previously defined sets of images. For example, a class could be:

1. **10** images of **30** seconds each
1. **5** images of **60** seconds each
1. **1** image of **5** minutes

In sequence.

Classes are defined in the **classes.json** file, where you can create your own.
***

### Simple Mode
In this mode you define the time you want to practice in this session, then you define how much time you want per image.

All images will have the same time.

## Class Creation
Classes are defined as **.json** objects, you can create your own classes in the **classes.json** file.

        // Title shown in class list
        "One Hour Class": 
        {
            // 10 images of 30 seconds
            "0.5": 10,
            // Followed by 5 images of one minute
            "1": 5,
            // Followed by 2 images of five minutes
            "5": 2,
            // Followed by 1 image of 10 minutes
            "10": 1,
            // Followed by 1 image of 30 minutes
            "30": 1
        }

You can define as many classes as you wish.
