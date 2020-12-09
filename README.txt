# BlackArch Env Installer --
# This script sets up and slick working Awesome WM 4.x exploitation enviromment.
# It is tailored for those that are very command line saavy.

# Install --
- sudo pacman -Syu git yay python
- git clone https://github.com/vadersecurity/env_installer.git
- cd env_installer ; python env_installer.py

# About --
- oh-my-zsh: 
-   custom exploitation based .zshrc
-   docker msf v6 intergation
-   zsh plugins ( yay, kubectl, docker and friends )
-   zsh-autosuggestions 
-   zsh-syntax-highlighting 
-   golang env vars
-   zsh large paste fix:
      -> https://gist.github.com/magicdude4eva/2d4748f8ef3e6bf7b1591964c201c1ab
      
# Setup --
- tmux default config
- fzf - term based fuzzy finder
- the_silver-searcher ( advanced grep )
- fd-find ( advanced find w/ fzf integration )
- extended grc.zsh
- themed terminator configurations
- themed termite
- nerd-fonts
- BMZ-cursor
- awful.spawn.with_shell autorun.sh
-   - set screens and resolution
-       - add displays.sh to autorun.sh
-   - add your own
- rofi simple switcher - drun / combi
- picom transparency
- golang / gotop default install
- Base cherrytree attack template
- nautilus
- eog
- gnome-screenshot

- neovim aliased to vim
- for full neovim dev IDE w/ CoC language engine plugins
- manual setup link --
    -> https://github.com/vadersecurity/env_installer/tree/master/config/editor/nvim

- screenshots included
- everything needs more testing
- it's free; and hopefully useful ;)

- todo:
- add neovim package installer
- add tmux config to installer
