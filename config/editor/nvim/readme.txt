# spacevim pissing me off --
# moving to neovim-init / blackarch --
# orig --
# https://github.com/Optixal/neovim-init.vim

# refs --
# https://github.com/neoclide/coc.nvim
# https://github.com/VundleVim/Vundle.vim

Note:
Make sure you have node installed and symlinked --

helix :: /tmp » ls -l /opt/node/bin/nodejs
lrwxrwxrwx 1 root root 18 Jun 10 11:32 /opt/node/bin/nodejs -> /opt/node/bin/node*
helix :: /tmp » 

Start Setup -- 
- mkdir -p ~/.config/nvim
- yain neovim python3 python-pip git curl python2-neovim python-pynvim python2-pynvim ruby-neovim xclip python-msgpack
- python3 -m pip install virtualenv
- python3 -m virtualenv -p python3 ~/.config/nvim/env
- source ~/.config/nvim/env/bin/activate
- pip install neovim jedi psutil setproctitle yapf
- deactivate
- curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
- curl -fLo ~/.fonts/Iosevka\ Term\ Nerd\ Font\ Complete.ttf --create-dirs https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/Iosevka/Regular/complete/Iosevka%20Term%20Nerd%20Font%20Complete.ttf
- echo "alias vim='nvim'" >> ~/.zshrc

Install vundle --
- git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim  

Fetch init.vim --
- curl -sk 'https://raw.githubusercontent.com/cdowns71/stuffz/master/configs/nvim/init.vim' -o ~/.config/nvim/init.vim

Which-Keys --
- mkdir ~/.config/nvim/keys
- curl -sk 'https://raw.githubusercontent.com/dualfade/stuffz/master/configs/nvim/keys/which-key.vim' -o ~/.config/nvim/keys/which-key.vim 

Snippets --
- mkdir ~/.config/nvim/snippets
- curl -sk 'https://raw.githubusercontent.com/dualfade/stuffz/master/configs/nvim/snippets/snippets.vim' -o ~/.config/nvim/snippets/snippets.vim
- cd ~/.config/nvim/ ; git clone https://github.com/Shougo/neosnippet-snippets.git

- nvim +PlugInstall +UpdateRemotePlugins +qall
- cp ~/.config/nvim/init.vim ~/.config/nvim/init.vim.save

Anything else ?
Commands --

https://github.com/Optixal/neovim-init.vim/blob/master/README.md
https://github.com/Optixal/.vim/blob/master/reference/commands_vim.txt

Other Deps ( language autocompletion ) --
sudo npm install -g neovim

Make sure node is symlinked to nodejs --
sudo ln -sf /usr/bin/node /usr/bin/nodejs

:CheckHealth
:PluginUpdate

Make sure all is fine and mcdadny --

Install Laguage packs --
ref: 
https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions

- install support ( python / ruby / golang / json / html / javascript ) by default
:CocInstall coc-explorer coc-python coc-solargraph coc-go coc-json coc-html coc-tsserver coc-sh coc-prettier coc-snippets

Commands --
Most custom commands expand off my map leader, keeping nvim as vanilla as possible.

, - Map leader, nearly all my custom mappings starts with pressing the comma key
  -> which-keys ( default )
,q - Sidebar filetree viewer (NERDTree)
,w - Sidebar classes, functions, variables list (TagBar)
\ - Toggle both NERDTree and TagBar
,ee - Change colorscheme (with fzf fuzzy finder)
,ea - Change Airline theme
,e1 - Color mode: Dracula (Dark)
,e2 - Color mode: Seoul256 (Between Dark & Light)
,e3 - Color mode: Forgotten (Light)
,e4 - Color mode: Zazen (Black & White)
,r - Refresh/source ~/.config/nvim/init.vim
,t - Trim all trailing whitespaces
,a - Auto align variables (vim-easy-align), eg. do ,a= while your cursor is on a bunch of variables to align their equal signs
,s - New terminal in horizontal split
,vs - New terminal in vertical split
,d - Automatically generate Python docstrings while cursor is hovering above a function or class
,f - Fuzzy find a file (fzf)
   -> note: sudo ln -sf /usr/bin/fd /usr/bin/fdfind
,g - Toggle Goyo mode (Goyo), super clean and minimalistic viewing mode
,h - Toggle rainbow parentheses highlighting
,j - Set filetype to "journal" which makes the syntax highlighting beautiful when working on regular text files and markdown
,k - Toggle coloring of hex colors
,l - Toggle Limelight mode (Limelight), highlight the lines near cursor only
,c<Space> - Toggle comment for current line (Nerd Commenter)
<Alt-r> - Toggle RGB color picker
<Tab> - Next buffer
<Shift-Tab> - Previous buffer
<Ctl>-w - next tab

Working with neovim --
https://neovim.io/doc/user/quickref.html
https://neovim.io/doc/user/tabpage.html

NERDtree --
https://github.com/jistr/vim-nerdtree-tabs

Android --
If you are doing android dev / rev eng make sure you have the sdk's installed.
