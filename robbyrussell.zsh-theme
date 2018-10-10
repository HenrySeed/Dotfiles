function get_pwd() {
  echo $PWD
}

PROMPT='$fg[cyan]$(get_pwd)
$reset_color> '
