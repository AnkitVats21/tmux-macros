#!/usr/bin/env bash
#======================================================
#   Author: Ankit Mishra
#    Email: ankvats21@gmail.com
#  Created: 2025-07-25
#======================================================

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Add sourcing of .tmux.macros.conf to user's .tmux.conf if not already present
if-shell "! grep -q 'source-file \"$CURRENT_DIR/.tmux.macros.conf\"' ~/.tmux.conf" \
  "run-shell 'echo \"source-file \\\"$CURRENT_DIR/.tmux.macros.conf\\\"\" >> ~/.tmux.conf'"

# Auto-generate macro cache if it doesn't exist
if-shell "! test -f \"$CURRENT_DIR/macros_cache.py\"" \
  "run-shell 'python3 \"$CURRENT_DIR/macros.py\" --update-cache'"

# Always regenerate macros and key bindings
run-shell 'python3 ~/.tmux/plugins/tmux-macros/macros.py --update-cache'