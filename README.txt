# BlackArch Env Installer --
# This script sets up and slick working Awesome WM 4.x exploitation enviromment.
# It is tailored for those that are very command line saavy.

# How to Install --
- MAKE SURE: you are not root!! This should be run from your local system account.
- NOTE: DO NOT run the script as sudo. yay takes care of this for you and wil ask you for your password.

- sudo pacman -Syu git yay python awesome
- git clone https://github.com/vadersecurity/env_installer.git
- cd env_installer ; python env_install.py

- Example: python env_install.py install dualfade

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
- alacritty
      -> themes: https://github.com/rajasegar/alacritty-themes
- nerd-fonts
- BMZ-cursor
- awful.spawn.with_shell  autorun.sh
-   - set screens and resolution
-       - add displays.sh to autorun.sh
-   - add your own
- rofi simple switcher - drun / combi
      -> cd ~/.local/share/rofi ; \
      git clone https://github.com/lr-tech/rofi-themes-collection.git
-     -> run: rofi-theme-selector
- picom-jonaburg-git transparency:
      -> https://github.com/jonaburg/picom
- golang / gotop default install
- obsidian-appimage
- nautilus
- eog
- flameshot:
      -> https://github.com/flameshot-org/flameshot
- keepassxc

- neovim aliased to vim
- for full neovim dev IDE install w/ CoC language engine plugins
- manual setup link --
    -> https://github.com/vadersecurity/env_installer/tree/main/config/editor/nvim
- neovim note: 042020221
- I have recently started using Lunarvim; Very nice; fully functional neovim based ide.
    -> https://github.com/LunarVim/LunarVim
    -> config.lua added in editor/lvim/config.lua

- everything needs more testing
- it's free; and hopefully useful ;)

- todo:
- add neovim package installer
- add tmux config to installer
- screenshots

- themes / widgets:

- NOTE: if you attempt to login and awesome logs you right out, you are missing awesome-copycats
- NOTE: in this case just move the default /etc/xdg/awesome/rc.lua -> ~/.config/awesome/rc.lua and then login.
- https://github.com/lcpz/awesome-copycats
- https://github.com/streetturtle/awesome-wm-widgets
