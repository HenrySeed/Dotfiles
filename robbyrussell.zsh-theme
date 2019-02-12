# PROMPT='${ret_status} %{$fg[cyan]%}%c%{$reset_color%} $(git_prompt_info)'

# ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg_bold[blue]%}git:(%{$fg[red]%}"
# ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%} "
# ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg[blue]%}) %{$fg[yellow]%}✗"
# ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg[blue]%})"


get_pwd() {
  echo $PWD
}

get_Git_Branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/[ \1 ]/'
}


PATHSTRING=$( echo %{$fg[cyan]%}%~%{$reset_color%})
GITSTRING=$( echo %{$fg[cyan]%} $(get_Git_Branch) %{$reset_color%})


PROMPT='
$PATHSTRING    $GITSTRING
> '


