#!/usr/bin/env python3
from subprocess import DEVNULL, STDOUT, check_call
from colors import crayon, colors
from installHeader import print_header
import sys
import os

DEFAULT_PIC_FOLDER = '~/Pictures/Wallpapers/'
CURRENT_STEP = 1



'''Prints a nice, coloured step with number'''
def printStep(name):
    global CURRENT_STEP
    name = crayon(" " + name + " ", colors.bg_yellow+colors.fg_black)
    print(crayon("\n[ {0} ]  ".format(CURRENT_STEP), colors.fg_dim) + name + "\n")
    CURRENT_STEP += 1


'''Copies the contents of folder1 into folder2'''
def copyFiles(folder1, folder2):
    # Get a list of names of files from folder1
    for name in os.listdir(folder1):
        if name[0] == '.': continue
        os.system("cp {0}{1} {2}".format(folder1, name.replace(' ', '\ '), folder2))

'''Installs a git repo, checking it isnt already installed first'''
def installGitRepo(repoString, name):
    # Check if it is already there
    projName = repoString.split('/')[-1].split('.')[0]

    if(os.path.exists(os.path.expanduser("~/" + projName))):
        print("     {0} is already installed.".format(name))
    else:
        os.system('cd ~/ && git clone ' + repoString)
    

'''Runs the main prompt, installing programs etc'''
def main():
    # clear the screen first
    os.system('clear')

    print_header()

    # 1) -------  Get pictures folder and copy wallpapers there  -------
    printStep("Saving Wallpapers")
    print('     Enter Pictures directory. Default pictures directory is ' + DEFAULT_PIC_FOLDER)
    picLocation = input('     (leave blank for default)\n     > ')
    if picLocation.strip() == "":
        picLocation = DEFAULT_PIC_FOLDER
    print('     Saving wallpapers to ' + picLocation + "...")
    os.system("mkdir " + picLocation)
    copyFiles('./wallpapers/', picLocation)


    # 2) -------  Installing some base projects  -------
    printStep("Installing Marvin")
    installGitRepo("https://github.com/HenrySeed/marvin.git", "Marvin")


    # 3) -------  Set up zsh, zshrc, prompt and oh - my - zsh  -------
    #  Install brew
    printStep("Installing HomeBrew")
    if os.system('which brew > /dev/null') == 'brew not found':
        os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    else:
        print('     HomeBrew is already installed')

    # Install ZSH
    printStep("Installing ZSH")
    if os.system('which zsh > /dev/null') == 'zsh not found':
        os.system('brew install zsh > /dev/null')
        os.system("sudo -s 'echo /usr/local/bin/zsh >> /etc/shells' && chsh -s /usr/local/bin/zsh")
        os.system('cp .zshrc ~/.zshrc')
    else:
        print('     ZSH is already installed')


     # Install ZSH
    printStep("Installing oh-my-zsh")
    if not os.path.exists(os.path.expanduser("~/.oh-my-zsh")):
        os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" > /dev/null')
        os.system('cp hanksZSH.zsh-theme ~/.oh-my-zsh/themes/')
    else:
        print('    oh-my-zsh is already installed')


    printStep("Installing ZSH plugins")
    if not os.path.exists(os.path.expanduser("~/.oh-my-zsh")):
        os.system("git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions")
        os.system("git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting")
    else:
        print('     ZSH plugins are already installed')

if __name__ == '__main__':
    main()
