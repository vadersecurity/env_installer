# For a full tmux experience --
# the tmux.conf included is a generic base config --

# install --
# https://github.com/gpakosz/.tmux

# install tpm plugins and reload --
# tmux source-file ~/.tmux.conf

# update your config file installed by oh-my-tmux

~/.tmux.conf 
setw -g xterm-keys on
set -s escape-time 0
set -s focus-events on
bind C-a send-prefix -2
setw -q -g utf8 on
bind e new-window -n "~/.tmux.conf.local" "EDITOR=\${EDITOR//mvim/vim} && EDITOR=\${EDITOR//gvim/vim} && \${EDITOR:-vim} ~/.tmux.conf.local && tmux source ~/.tmux.conf && tmux display \"~/.tmux.conf sourced\""
bind r source-file ~/.tmux.conf \; display '~/.tmux.conf sourced'
bind -n C-l send-keys C-l \; run 'sleep 0.1' \; clear-history
set -g monitor-activity on
set -g visual-activity off
bind C-c new-session
bind C-f command-prompt -p find-session 'switch-client -t %%'
bind - split-window -v
bind _ split-window -h
bind -r H resize-pane -L 2
bind -r J resize-pane -D 2
bind -r K resize-pane -U 2
bind -r L resize-pane -R 2
unbind n
unbind p
bind m run "cut -c3- ~/.tmux.conf | sh -s _toggle_mouse"
run -b 'tmux bind -t vi-choice h tree-collapse 2> /dev/null || true'
run -b 'tmux bind -t vi-choice l tree-expand 2> /dev/null || true'
run -b 'tmux bind -t vi-choice K start-of-list 2> /dev/null || true'
run -b 'tmux bind -t vi-choice J end-of-list 2> /dev/null || true'
run -b 'tmux bind -t vi-choice H tree-collapse-all 2> /dev/null || true'
run -b 'tmux bind -t vi-choice L tree-expand-all 2> /dev/null || true'
run -b 'tmux bind -t vi-choice Escape cancel 2> /dev/null || true'
run -b 'tmux bind -ct vi-edit H start-of-line 2> /dev/null || true'
run -b 'tmux bind -ct vi-edit L end-of-line 2> /dev/null || true'
run -b 'tmux bind -ct vi-edit q cancel 2> /dev/null || true'
run -b 'tmux bind -ct vi-edit Escape cancel 2> /dev/null || true'
run -b 'tmux bind -t vi-copy v begin-selection 2> /dev/null || true'
run -b 'tmux bind -T copy-mode-vi v send -X begin-selection 2> /dev/null || true'
run -b 'tmux bind -t vi-copy C-v rectangle-toggle 2> /dev/null || true'
run -b 'tmux bind -T copy-mode-vi C-v send -X rectangle-toggle 2> /dev/null || true'
run -b 'tmux bind -t vi-copy y copy-selection 2> /dev/null || true'
run -b 'tmux bind -T copy-mode-vi y send -X copy-selection-and-cancel 2> /dev/null || true'
run -b 'tmux bind -t vi-copy Escape cancel 2> /dev/null || true'
run -b 'tmux bind -T copy-mode-vi Escape send -X cancel 2> /dev/null || true'
run -b 'tmux bind -t vi-copy H start-of-line 2> /dev/null || true'
run -b 'tmux bind -T copy-mode-vi H send -X start-of-line 2> /dev/null || true'
run -b 'tmux bind -t vi-copy L end-of-line 2> /dev/null || true'
run -b 'tmux bind -T copy-mode-vi L send -X end-of-line 2> /dev/null || true'
if -b 'command -v pbcopy > /dev/null 2>&1' 'bind y run -b "tmux save-buffer - | pbcopy"'
if -b 'command -v reattach-to-user-namespace > /dev/null 2>&1' 'bind y run -b "tmux save-buffer - | reattach-to-user-namespace pbcopy"'
if -b 'command -v xsel > /dev/null 2>&1' 'bind y run -b "tmux save-buffer - | xsel -i -b"'
if -b '! command -v xsel > /dev/null 2>&1 && command -v xclip > /dev/null 2>&1' 'bind y run -b "tmux save-buffer - | xclip -i -selection clipboard >/dev/null 2>&1"'
if -b 'command -v clip.exe > /dev/null 2>&1' 'bind y run -b "tmux save-buffer - | clip.exe"'
if -b '[ -c /dev/clipboard ]' 'bind y run -b "tmux save-buffer - > /dev/clipboard"'
if '[ -f ~/.tmux.conf.local ]' 'source ~/.tmux.conf.local'
run 'cut -c3- ~/.tmux.conf | sh -s _apply_configuration'
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
run '~/.tmux/plugins/tpm/tpm'
set -g @plugin 'ryuta69/elly-tmux'
set -g pane-active-border fg=blue

