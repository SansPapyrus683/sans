#!/bin/bash

echo "installing all my packages"
sudo dnf install g++ python3-devel pip ipython3 gnome-tweaks neovim zsh curl tree \
 fira-code-fonts comic-neue-fonts onedrive libasan libubsan java-latest-openjdk-devel \
 file-roller tldr black+jupyter fzf pandoc kitty python3-isort glycin-thumbnailer fragments

flatpak install flathub com.mattjakeman.ExtensionManager
flatpak install flathub com.microsoft.Edge

sudo dnf install "https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm"
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc &&
echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\nautorefresh=1\ntype=rpm-md\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" | sudo tee /etc/yum.repos.d/vscode.repo > /dev/null

sudo dnf update  # not sure if this needed but wtv
sudo dnf install code
sudo dnf install discord

echo "installing nord themes n such"
WD=$(pwd)

cd ~/Downloads
git clone https://github.com/MolassesLover/Nordzy-icon
cd Nordzy-icon
./install.sh
# i only use the nordzy-dark theme anyways
rm -rf ~/.local/share/icons/Nordzy
cd ..

git clone https://github.com/vinceliuice/Graphite-gtk-theme
cd Graphite-gtk-theme
./install.sh --tweaks nord darker rimless colorful

cd "$WD"

echo "starting onedrive"
onedrive  # login or whatever first
systemctl --user enable onedrive
systemctl --user start onedrive

# these just sit in the home directory no real setup besides that
cp kaltsit .gitconfig ~
chmod +x ~/kaltsit

echo "setting up omz"
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
cp .zshrc ~

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

echo "extracting/putting cursors in"
mkdir -p ~/.icons

for cursor in cursors/*.tar.gz; do
    [ -f "$cursor" ] || break
    tar xf "$cursor" --directory ~/.icons
done
