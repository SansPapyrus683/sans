# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="robbyrussell"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
DISABLE_UNTRACKED_FILES_DIRTY="true"

plugins=(
    git
    git-auto-fetch
    zsh-syntax-highlighting
    zsh-autosuggestions
)

source $ZSH/oh-my-zsh.sh

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

alias ipython="ipython3"
alias trash="rm -rf ~/.local/share/Trash/*"
alias vim="nvim"
alias config="nvim ~/.zshrc; source ~/.zshrc" # no idea if this is a good idea or not
alias nvimcfg="nvim ~/.config/nvim/init.lua"
alias onedrive-log="journalctl --user-unit=onedrive -f"
alias edging="rm -rf ~/.config/microsoft-edge/Singleton*"
alias g31="g++ -std=c++17 -Wall -Wextra -Wno-sign-compare -Werror=return-type -Wl,--rpath=/usr/local/cs/lib64 -fsanitize=address -fsanitize=undefined -fsanitize=bounds -fno-omit-frame-pointer"

export PATH=$PATH:/home/sanspapyrus683/.local/bin
export PAGER=most
export EDITOR=nvim

print_pdf() {
    enscript -E -q -Z -p - $1 | ps2pdf - ${1%.*}.pdf
}
