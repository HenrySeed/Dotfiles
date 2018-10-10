#!/usr/bin/env python3
from subprocess import DEVNULL, STDOUT, check_call
from colors import crayon, colors
import sys
import os


'''Prints a nice, coloured step with number'''
def printStep(number, name):
    print(crayon("\n [ {0} ] ".format(number), colors.fg_bold) + "  {0}".format(name))


'''Copies the contents of folder1 into folder2'''
def copyFiles(folder1, folder2):
    # Get a list of names of files from folder1
    for name in os.listdir(folder1):
        if name[0] == '.': continue
        os.system("cp {0}{1} {2}".format(folder1, name.replace(' ', '\ '), folder2))


THIS_OS = sys.platform
DEFAULT_PIC_FOLDER = {    # The default location for pictures in an os
    'darwin': '~/Pictures'
}

# clear the screen first
os.system('clear')

# 1) -------  Get pictures folder and copy wallpapers there  -------
printStep(1, "Saving Wallpapers")
# Checks with user for a custom location
if THIS_OS in DEFAULT_PIC_FOLDER:
    picFolder = DEFAULT_PIC_FOLDER[THIS_OS]
else:
    picFolder = '~/Pictures'

print('Default pictures directory is ' + picFolder)
picLocation = input('Where should I put the wallpapers? (leave blank for default)\n> ')
if picLocation.strip() == "":
    picLocation = picFolder
print('Saving wallpapers to ' + picLocation + "...")
copyFiles('./wallpapers/', picLocation)


# 2) -------  Installing some base projects  -------
printStep(2, "Installing Marvin")
os.system('cd ~/ && git clone https://github.com/HenrySeed/marvin.git')

printStep(3, "Installing Blackjack")
os.system('cd ~/ && git clone https://github.com/HenrySeed/terminalCards.git')


# 3) -------  Set up zsh, zshrc, prompt and oh - my - zsh  -------
if THIS_OS == "darwin":
    #  Install brew
    printStep(2, "Installing brew")
    if os.system('which brew > /dev/null') == 'brew not found':
        os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    else:
        print('Brew is already installed')

    # Install ZSH
    printStep(2, "Installing zsh")
    if os.system('which zsh > /dev/null') == 'zsh not found':
        os.system('brew install zsh > /dev/null')
        os.system("sudo -s 'echo /usr/local/bin/zsh >> /etc/shells' && chsh -s /usr/local/bin/zsh")
        os.system('cp robbyrussell.zsh-theme ~/.oh-my-zsh/themes/robbyrussell.zsh-theme')
    else:
        print('zsh is already installed')

    # Install iTerm2
    printStep(3, "Installing Iterm2")
    if os.system('which iterm2 > /dev/null') == 'iterm2 not found':
        os.system('brew cask install iterm2')
        # Copy the prefs to ~/
        os.system('cp ./iTerm2Prefs ~/')
        # Set up iTerm2 to use custom prefs
        # Specify the preferences directory
        os.system('defaults write com.googlecode.iterm2.plist PrefsCustomFolder -string "~/iTerm2Prefs"')
        # Tell iTerm2 to use the custom preferences in the directory
        os.system('defaults write com.googlecode.iterm2.plist LoadPrefsFromCustomFolder -bool true')
    else:
        print('iterm2 is already installed')

    
    

else:
    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade')
    os.system('sudo apt-get install zsh')

    os.system('apt install wget git')
    os.system('wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh')
    os.system('sudo apt-get upgrade')

