# tmux-macros

A simple, extensible [tmux](https://github.com/tmux/tmux) plugin to define and run custom macros using YAML configuration. Inspired by MobaXterm macros, this plugin lets you automate sequences of keypresses, text input, and delays in your tmux panes.

## Features

- **Easy macro definition**: Write macros in a human-friendly YAML file.
- **Key bindings**: Bind macros to any tmux key combination.
- **Reusable commands**: Use YAML anchors and references for DRY macros.
- **Auto-generation**: Automatically generates tmux config and Python cache.
- **No dependencies**: Only requires Python 3 and tmux.

## Installation

1. **Clone this repo** (or copy files) into your tmux plugins directory:

    ```sh
    git clone https://github.com/yourusername/tmux-macros.git ~/.tmux/plugins/tmux-macros
    ```

2. **Add the plugin to your `.tmux.conf`:**

    ```tmux
    run-shell '~/.tmux/plugins/tmux-macros/macros.tmux'
    ```

    > On first run, this will auto-inject a `source-file` line for `.tmux.macros.conf` if missing.

3. **Reload your tmux config:**

    Inside tmux, press <kbd>Prefix</kbd> + <kbd>:</kbd> and run:

    ```
    source-file ~/.tmux.conf
    ```

## Example Usage

1. **Edit your macros** in [`macros.yml`](macros.yml):

    ```yaml
    macros:
      hello:
        key: "C-l"
        commands:
          - type: text
            value: "echo Hello, world!"
          - type: keypress
            value: C-m
    ```

    You can also use YAML anchors and references to reuse command sequences.

2. **Regenerate the macro cache and bindings manually** (optional):

    ```sh
    python3 macros.py --update-cache
    ```

    > Usually auto-generated when you reload `.tmux.conf`.

3. **Use your macro in tmux:**

    Press the bound key (e.g., <kbd>Ctrl</kbd>+<kbd>l</kbd>) to run the macro in the active pane.

## Configuration

You can customize file locations and plugin paths by editing the config logic in `utils.py`.

## File Overview

- `macros.yml` – Define your macros here.
- `macros.py` – Main script to run macros or regenerate cache.
- `macros_cache.py` – Auto-generated Python cache of macros.
- `.tmux.macros.conf` – Auto-generated file with tmux key bindings.
- `macros.tmux` – Plugin bootstrap for setup and integration.
- `utils.py` – Helper functions for configuration and parsing.

## Development

- Edit `macros.yml` to define new macros.
- Run:

    ```sh
    python3 macros.py --update-cache
    ```

    to regenerate the cache and key bindings.

- Reload your tmux config:

    ```sh
    tmux source-file ~/.tmux.conf
    ```

## License

MIT License

---

> Inspired by MobaXterm macros.
