import subprocess
from argparse import ArgumentParser
from time import sleep

# example macros
MACROS = {
    "echo-hello":{
        "commands":[
            {
                "type":"text",
                "value":"echo Hello World!"
            },
            {
                "type":"keypress",
                "value":"C-m"
            }
        ]
    }
}

def get_active_pane():
    # Run the tmux command to get the current active pane id
    active_pane = subprocess.check_output(
        ["tmux", "display-message", "-p", "#{pane_id}"]
    ).decode("utf-8").strip()
    return active_pane

def send_command_to_pane(pane_id, command):
    # Send the command to the specific tmux pane
    subprocess.run(["tmux", "send-keys", "-t", pane_id, command])

def main(command):
    # Get the active pane
    active_pane = get_active_pane()
    if command in MACROS:
        commands = MACROS[command]['commands']
        for c in commands:
            # print(c)
            if c['type'] == 'text':
                send_command_to_pane(active_pane, c['value'])
            elif c['type'] == 'keypress':
                send_command_to_pane(active_pane, c['value'])
            elif c['type'] == 'sleep':
                sleep(0.001 * int(c['value']))
            elif c['type'] == 'wait_for_pattern':
                pass
            elif c['type'] == 'wait_for_text':
                pass
            else:
                pass

if __name__ == "__main__":
    # parse the arguments
    parser = ArgumentParser(description="Send a command to the active tmux pane.")
    parser.add_argument("command", type=str, help="The command to send to the active tmux pane.")
    args = parser.parse_args()
    main(args.command)
