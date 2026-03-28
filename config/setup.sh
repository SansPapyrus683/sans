#!/bin/bash

# these just sit in the home directory no real setup besides that
cp kaltsit .gitconfig ~

echo "setting up omz"
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
cp .zshrc ~
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

echo "setting up kitty"
mkdir -p ~/.config/kitty
# this script should be run from the config folder
cp kitty.conf ~/.config/kitty
kitten themes Nord

echo "setting up gallery-dl"
mkdir -p ~/.config/gallery-dl
cp gallery_dl.json ~/.config/gallery-dl/config.json

echo "setting up neovim"
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
mkdir -p ~/.config/nvim
cp init.lua ~/.config/nvim
nvim --headless +PlugInstall +qall

echo "creating ipython config"
ipython3 profile create
echo 'c = get_config();
c.TerminalInteractiveShell.highlighting_style = "nord"' \
> ~/.ipython/profile_default/ipython_config.py
