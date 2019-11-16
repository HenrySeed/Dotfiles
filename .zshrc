# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
ZSH_THEME="hanksZSH"

# Fix percent sign on Hyper.js
unsetopt PROMPT_SP

# Uncomment the following line to enable command auto-correction.
ENABLE_CORRECTION="true"
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=blue'

# ====================== PLUGINS ====================== #

plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
)

# ======================= PATHS ======================= #

export PATH=$HOME/bin:/usr/local/bin:$PATH
export PATH="/opt/local/bin:/opt/local/sbin:~/bin:/usr/local/bin:/Library/Frameworks/Python.framework/Versions/3.4/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/usr/local/git/bin"


# ====================== Aliases ====================== #

alias showFiles='defaults write com.apple.finder AppleShowAllFiles YES; killall Finder /System/Library/CoreServices/Finder.app'
alias hideFiles='defaults write com.apple.finder AppleShowAllFiles NO; killall Finder /System/Library/CoreServices/Finder.app'
alias marvin='python3 ~/marvin/marvin.py'
alias c='clear'
alias todo='~/TerminalToDo/terminalTodo'
alias zshrc='code ~/.zshrc'
alias profile='code ~/.oh-my-zsh/themes/robbyrussell.zsh-theme'
alias screenfetch='python3 /Users/henryseed/dnm/Sys_monitor_terminal.py'
alias python='python3'
alias py='python3'
alias colourtest='zsh ~/colourtest'
alias bonsai='zsh ~/bonsai'
alias morning='exec python ~/GoodMorning/start.py'
alias gitClean='git branch | grep -v "develop" | xargs git branch -D'


# ===================== Functions ===================== #

vt100() {
    clear
    cat $1 | pv -l -L $2 -q
}


source $ZSH/oh-my-zsh.sh