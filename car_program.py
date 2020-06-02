
def card_engine():

    command = ""
    last_command = ""

    prevent_duplicate_action = {'start', 'stop'}

    def command_was_launched(command, last_command):
        return command == last_command and command in prevent_duplicate_action

    def show_status(last_command):
        if last_command == "start":
            print("The card was started")
        elif last_command == "stop":
            print("The card was stoped")
        else:
            print("Without last status")

    def show_last_command(command):
        if command == "start":
            print("Card is already started")
        if command == "stop":
            print("Card is already stoped")

    def show_help():
        print("""
    start   - To start the card
    stop    - To stop the card
    status  - To display last command
    exit    - To exit
          """)

    while True:
        command = input('> ').lower()

        if command_was_launched(command, last_command):
            show_last_command(command)

        elif command == "start":
            last_command = command
            print("Card start...")

        elif command == "stop":
            last_command = command
            print("Card stop...")

        elif command == "status":
            show_status(last_command)

        elif command == "help":
            show_help()

        elif command == "exit":
            print("Bye")
            break

        else:
            print("I don't understand, try white 'help' command")


if __name__ == "__main__":
    card_engine()
