#### Environement 
- python -m venv env

#### Raccoucis
- ctrl-k v → affiche preview du document markdown
- ctrl j → agrandir ou minimiser le terminal

#### Ajout de Git Bash à Visual Studio Code
- lien : https://www.geeksforgeeks.org/how-to-integrate-git-bash-with-visual-studio-code/
- File->Preferences->Settings
- click on the Open Settings(JSON) (en haut à droite)
- add the below properties at the last of all settings :
> "terminal.integrated.profiles.windows":{"Git Bash":{"path":"C:\\Program Files\\Git\\bin\\bash.exe"},  },
"terminal.integrated.defaultProfile.windows": "Git Bash"

- reopen VS Code then you will see that Git Bash has been integrated

#### Modification du "prompt" Git Bash
- faire une copie de sauvegarde du fichier C:\Program Files\Git\etc\profile.d\git-prompt.sh
- ouvrir ce fichier en tant qu'administrateur (dans Notepad par exemple)
- remplacer :
> 	PS1="$PS1"'\[\033[32m\]'       # change to green
	PS1="$PS1"'\u@\h '             # user@host<space>
	PS1="$PS1"'\[\033[35m\]'       # change to purple
	PS1="$PS1"'$MSYSTEM '          # show MSYSTEM
	PS1="$PS1"'\[\033[33m\]'       # change to brownish yellow
	PS1="$PS1"'\w'                 # current working directory

Par :
>   PS1="$PS1"'`pwd`'   	       # Dossier courant réel !