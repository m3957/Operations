#!/bin/bash

# Pour le truc qui m'a servi à faire cela:
# https://linuxcommand.org/lc3_adv_dialog.php

DIALOG_CANCEL=1
DIALOG_ESC=255
HEIGHT=0
WIDTH=0

display_result() {
  dialog --title "$1" \
    --no-collapse \
    --msgbox "$result" 0 0
}

while true; do
  exec 3>&1
  selection=$(dialog \
    --backtitle "Installer Operations" \
    --title "Sélection" \
    --clear \
    --cancel-label "Quitter" \
    --menu "Sélectionnez une option" $HEIGHT $WIDTH 4 \
    "1" "Installer Operations sur ~/" \
    "2" "Montrer le code" \
    "3" "Surprise amusante :D" \
    2>&1 1>&3)
  exit_status=$?
  exec 3>&-
  case $exit_status in
    $DIALOG_CANCEL)
      clear
      echo "Bye!"
      exit
      ;;
    $DIALOG_ESC)
      clear
      echo "Bye!" >&2
      exit 1
      ;;
  esac
  case $selection in
    1 )
      result=$(echo "Le jeu va être installé dans votre répertoire ~/, et on va installer python3 et git sur votre système.")
      display_result "Installer Operations"
      #cd ~/
      #sudo apt install python3 python3-pip git
      #git clone https://github.com/m3957/Operations.git
      #cd Operations
      result=$(echo "Voilà! C'est installé! Bon jeu!")
      display_result "Operations réussites"
      result=$(echo "Ah oui! Dernière chose! Pour exécuter le jeu, faire:")
      display_result "Comment jouer?"
      result=$(echo "cd ~/Operations; python3 main.py")
      display_result "Comment jouer?"
      ;;
    2 )
      result=$(echo "https://github.com/m3957/Operations")
      display_result "Code"
      ;;
    3 )
    
	  result=$(echo "Pour voir la surprise, tu as besoin d'installer 2 programmes.")
      display_result "Surprise amusante :D"
      sudo apt install youtube-dl mplayer
      youtube-dl -o- "https://www.youtube.com/watch?v=dQw4w9WgXcQ" | mplayer -vo caca -
      ;;
  esac
done
