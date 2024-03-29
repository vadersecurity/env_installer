#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# env_installer.py
# dualfade[at]vadersecurity.com

# import --
import os
import sys
import time
import shutil
import subprocess
from os import path

# About --
# This installer will setup BlackArch running Awesome WM 4.x.
# The env will have all the necassary configurations for quick keyoard interaction and shell exploitation.

# deps --
# install before running this script --
# sudo pacman -Syu git yay python awesome
# git clone https://github.com/vadersecurity/env_installer.git
# cd env_installer ; python env_install.py

# definitions --
def splash_screen():
    print('\t\t-- VADER SECURITY --')
    print('\t\t   Awesome WM 4.3')
    print('\tpenetration testing environment install\n')
    print('[i] This program requires root or sudo access.')
    print('[?] Do you wish to proceed with the env_install ?')
    t = input('[?] selection [y/N]: ').lower().strip()
    if ( t == 'y' ):
        print('[+] Rock n Roll! let\'s do this...')
        time.sleep(1)
        return
    else:
        print('[!] Boo.. Exiting now.')
        sys.exit()

def start_package_installer():
    """ Starting env_installer -- """
    """ aur access needs to be setup """
    print('[+] Starting required package installation:')
    try:
        pac_p_installer = subprocess.run(['/sbin/yay', '-S', 'zsh', 'picom-jonaburg-git', 'rofi', 'grc', 'tree', 'neovim', 'alacritty',  \
                                          'alacritty-themes', 'ranger', 'fzf', 'fd', 'amass', 'gospider', 'go', 'eog', 'nautilus', 'flameshot', 'feh', \
                                          'tmux', 'httpx', 'nuclei', 'dnsx', 'waybackurls', 'subfinder', 'zdns', 'hakrawler', 'screen', 'mlocate', \
                                          'nmap', 'gobuster', 'dirsearch', 'bat', 'keepassxc', 'spectrwm', 'slock'], \
                                         stdin=None, stdout=None, stderr=None, shell=False)
        print('[+] Installing packages: %d' %pac_p_installer.returncode)
        if ('%d' %pac_p_installer.returncode) != 0:
            print('\n[!] Please review the error, you may need to restart the installation.')
            print('[i] or if everything seams ok.. just wait.')
            print('[i] returncode 0 == success.')
            print('[i] ctl c to bail now!')
            print('[i] sleeping 10 seconds!')
            time.sleep(10)
        return
    except subprocess.CalledProcessError as err:
        print('[!] Installation failed.')
        print('[i] Please review the error and check for existing files.')
        print('ERROR:', err)

def zsh_install():
    """ oh-my-zsh installation -- """
    print('[+] Installing oh-my-zsh:')
    try:
        home = str(path.dirname('/home/%s/') % arg2)
        zsh_repo = "".join([home, '/.oh-my-zsh'])
        tpm_repo = "".join([home, '/.tmux/plugins'])
        """ clone oh-my-zsh -- """
        om_zsh_clone = subprocess.check_call(['/bin/git', 'clone', 'https://github.com/ohmyzsh/ohmyzsh.git', zsh_repo])
        print('[+] Cloning repository: %d' %om_zsh_clone)
        """ clone tmux tpm plugin manager -- """
        om_tpm_clone = subprocess.check_call(['/bin/git', 'clone', 'https://github.com/tmux-plugins/tpm.git', tpm_repo])
        print('[+] Cloning repository: %d' %om_tpm_clone)

        """ check for existing .zshrc / back it up -- """
        """ copy new .zshrc into place -- """
        src = './config/shell/zsh/zshrc'
        dst = "".join([home, '/.zshrc'])

        e_zshrc = os.path.isfile('%s/.zshrc' % home)
        if e_zshrc == True:
            print('[i] Backing up existing .zshrc')
            shutil.copy(dst, '%s/.zshrc.backup' % home)
        shutil.copy(src, dst)

        return(home) 
    except subprocess.CalledProcessError as err:
        print('[!] Installation failed.')
        print('ERROR:', err)

def update_shell():
        """ update local shell -- """
        try:
            update_shell = ('/sbin/sudo /sbin/chsh -s /usr/bin/zsh %s' % arg2)
            shell_update = subprocess.Popen(update_shell, shell=True)
            resp = shell_update.wait()
            print(resp)
            return(home) 
        except subprocess.CalledProcessError as err:
            print('[!] Installation failed.')
            print('ERROR:', err)

def start_local_config_setup():
    """ backup ~/.config if exists -- """
    if os.path.exists('%s/.config' % home):
        print('\n[i] Backing up %s/.config' % home)
        print('[i] you may need to move some configs back.')
        shutil.move('%s/.config' % home, '%s/.config.save' % home)

    """ install config files for awesome wm 4.x """
    d_cnf_dirs = ['alacritty', 'rofi', 'picom', 'nvim', 'awesome']
    try:
        print('[+] Installing configuarion files:')
        dot_config = "".join([home, '/.config'])
        os.mkdir(dot_config, mode=0o755)
        for cnf_dir in d_cnf_dirs:
            c_cnf_dir = "".join([home, '/.config/', cnf_dir])
            """ not a type-o / pythons dumb way of permissions -- """
            os.mkdir(c_cnf_dir, mode=0o755)

        """ copy config to ~/.config/<dir> -- """
        print('[+] Copying local configs into place.')
        shutil.copy('./config/alacritty/alacritty.yml', '%s/.config/alacritty/' % home)
        shutil.copy('./config/rofi/config.rasi', '%s/.config/rofi/' % home)
        shutil.copy('./config/picom/picom.conf', '%s/.config/picom/' % home)
        shutil.copy('./config/wm/awesome/autorun.sh', '%s/.config/awesome/' % home)
        shutil.copy('./config/x11/Xresources', '%s/.Xresources' % home)
        shutil.copy('./config/screen/screenrc', '%s/.screenrc' % home)
        print('[i] Basic nvim installation added !')
        print('\n[i] To install full neovim IDE installation --')
        print('[i] ref: https://github.com/vadersecurity/env_installer/tree/master/config/editor/nvim')
        print('[i] ref: https://github.com/neoclide/coc.nvim/wiki/Using-coc-extensions')
        print('[i] This will be automated; but until then...\n')
        time.sleep(2)

        """ add ~/go -- """
        c_godir = subprocess.check_call(['/bin/mkdir', '-p', '%s/go' % home]) 
        print('[+] Creating go directory: %d' %c_godir)
    except OSError as err:
        print('[!] Config installation failed.')
        print('ERROR:', err)

def github_dir_struct():
    """ create github directory structure -- """
    git_dir_struct = ['av-bypass', 'code-audit', 'custom_list', 'exploitation', 'intelligence-gathering', 'mobile-analysis', \
                      'osx', 'password-recovery', 'pivoting', 'post-exploitation', 'powershell', 'pre-engagement', 'reporting', \
                      'reversing', 'threat-modeling', 'vulnerability-analysis', 'webshells', 'windows-tools', 'wireless', \
                      'miscellaneous']
    try:
        print('[+] Creating ~/Github directories:')
        github_dir = "".join([home, '/Github'])
        os.mkdir(github_dir, mode=0o755)
        for git_dir in git_dir_struct:
            c_git_dir = "".join([home, '/Github/', git_dir])
            """ not a type-o / pythons dumb way of permissions -- """
            os.mkdir(c_git_dir, mode=0o755)

        """ copy existing files into place -- """
        c_github = subprocess.check_call(['/bin/mkdir', '-p', '%s/Github/miscellaneous/nmapAutomator' % home]) 
        print('[+] Creating Github directory: %d' %c_github)
        shutil.copy('./config/scan/nmap/nmap_auto.sh', '%s/Github/miscellaneous/nmapAutomator/' % home)

        """ create templates / cherrytree script directory -- """
        c_templates = subprocess.check_call(['/bin/mkdir', '-p', '%s/Github/miscellaneous/Templates/Cherrytree' % home]) 
        shutil.copy('./config/templates/cherrytree/default_target_teplate.ctb', '%s/Github/miscellaneous/Templates/Cherrytree/' % home)
        print('[+] Creating Templates directory: %d' %c_templates)
        print('[i] if you would like to use cherrytree, please run "yay -S cherrytree-bin" after installation completes')
    except OSError as err:
        print('[!] Directory creation failed.')
        print('ERROR:', err)

def start_priv_config_setup():
    """ install privilges configurations -- """
    print('\n[i] Installing privileged config files.')
    time.sleep(2)
    try:
        grc = subprocess.check_call(['/sbin/sudo','/bin/cp', '-Rvp', './config/syntax/grc/grc.zsh', '/etc/grc.zsh']) 
        print('[+] Installing grc.zsh: %d' %grc)
        grc_perms = subprocess.check_call(['/sbin/sudo','/sbin/chown', '-R', 'root:root', '/etc/grc.zsh']) 
        print('[+] Setting grc.zsh permissions: %d' %grc_perms)

        """ add picom / drun config to rc.lua -- """
        """ insert awful.spawn_with_shell autorun.sh -- """
        blua = subprocess.check_call(['/sbin/sudo','/bin/cp', '-Rvp', '/etc/xdg/awesome/rc.lua', '/etc/xdg/awesome/rc.lua.save']) 
        print('[+] Backing up rc.lua -> rc.lua.save: %d' %blua)
        ilua = subprocess.check_call(['/sbin/sudo','/bin/cp', '-Rvp', './config/wm/awesome/rc.lua', '/etc/xdg/awesome/rc.lua']) 
        print('\n[+] Installing new rc.lua configuration: %d' %ilua)
        print('[i] picom (drun; cmd r )/ awful.spawn.with_shell enabled:')
        time.sleep(1)

    except subprocess.CalledProcessError as err:
        print('[!] Installation failed.')
        print('ERROR:', err)

def install_missing_apps():
    """ install cherrytree-git / bmz-cursor-theme-git after yay is installed """
    """ add yaccl aliaes cache cleanup -- """
    try:
        yay_p_update = subprocess.check_call(['/sbin/yay', '-Syu'])
        print('[+] Updating packages: %d' %yay_p_update)
        yay_p_installer = subprocess.run(['/sbin/yay', '-S', 'insomnia-bin', 'bmz-cursor-theme-git', 'nerd-fonts-complete', 'virtualbox', \
                                                'bash-language-server', 'pyright', 'prettier', 'cargo', 'nodejs', 'npm', 'yarn', 'docker', 'gotop', \
                                                'the_silver_searcher', 'firejail', 'hardened-malloc-git'], \
                                                stdin=None, stdout=None, stderr=None, shell=False)
        print('\n[+] Installing aur packages: %d' %yay_p_installer.returncode)
        print('[i] yay zsh archlinux plugin cmd ref:')
        print('[i] https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/archlinux\n')
        print('[i] enable docker: sudo systemctl enable docker')
        print('[i] ref: https://gist.github.com/dualfade/fea1b8efcc6125c2c7b11cb92ac1a90c')
        time.sleep(2)
        print('[+] Adding gotop --')
        i_gotop = subprocess.check_call(['/usr/bin/go', 'get', 'github.com/cjbassi/gotop'])
        print('\n[+] Fetching gotop latest src: %d' %i_gotop)
        print('[+] Creating go directory struct')
        print('[i] do not forget to install ruby deps: gem install solargraph rubocop')
    except subprocess.CalledProcessError as err:
        print('[!] Installation failed.')
        print('ERROR:', err)

def clean_local_cache():
    """ clean local repo cache -- """
    try:
        yay_c_cache = subprocess.check_call(['/sbin/yay', '-Sc', '<<<y'])
        print('[+] Cleaning local repo cache: %d' %yay_c_cache)
        time.sleep(2)
    except subprocess.CalledProcessError as err:
        print('[!] Installation failed.')
        print('ERROR:', err)

# main --
if __name__ == '__main__':
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    except IndexError:
        print("[-] Usage: %s install user" % sys.argv[0])
        print("[-] Usage: python env_install.py install <username>")
        sys.exit(-1)

# start installer --
if ( arg1 == 'install' ):
    splash_screen()
    start_package_installer()
    time.sleep(2)
    home = zsh_install()
    start_local_config_setup()
    github_dir_struct()
    install_missing_apps()
    start_priv_config_setup()
    update_shell()
    clean_local_cache() 
    print('\n[i] Installation Done.')
    print('[+] logout out or reboot.')
    sys.exit(-1)
else:
    print('[!] Exiting now.')
    sys.exit(-1)

# __EOF__
