
def car_engine():
    """Console program to control a car engine."""

    command = ""
    last_command = ""

    prevent_duplicate_action = {'start', 'stop'}

    def command_was_triggered(command, last_command):
        """To know if some command was triggered to prevent re-trigger it"""
        return command == last_command and command in prevent_duplicate_action

    def show_status(last_command):
        """To show engine's status"""

        if last_command == "start":
            print("The car was started")
        elif last_command == "stop":
            print("The car was stoped")
        else:
            print("Without last status")

    def show_last_command(command):
        """To use when the same command was trigger"""

        if command == "start":
            print("car is already started")
        if command == "stop":
            print("car is already stoped")

    def show_help():
        print("""
    start   - To start the car
    stop    - To stop the car
    status  - To display last command
    exit    - To exit
          """)

    while True:
        command = input('> ').lower()

        if command_was_triggered(command, last_command):
            show_last_command(command)

        elif command == "start":
            last_command = command
            print("car start...")

        elif command == "stop":
            last_command = command
            print("car stop...")

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
    car_engine()
