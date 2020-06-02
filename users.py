import time


class Users:
    def __init__(self):
        self.users = []

    def register_a_new_user(self):
        print("User info")
        full_name = input("Fullname: ")
        age = int(input("Age: "))

        user = {"full_name": full_name, "age": age}

        if user in self.users:
            print("User {} already exists".format(full_name))
        else:
            last_user = self.users[-1] if len(self.users) > 0 else dict()
            last_id = last_user['id'] if 'id' in last_user else 0

            created_at = time.gmtime()

            self.users.append({"id": last_id + 1, "deleted_at": None,
                               "created_at": time.asctime(created_at), **user})

            print("User {} was added successfully!".format(full_name))

    def _print_users(self, users):
        for user in users:
            user_info = "Id: {id} | Full Name: {full_name} | Age: {age} | created_at: {created_at}".format(
                **user)

            print("*" * len(user_info))
            print(user_info)
            print("*" * len(user_info))
            print('\n')

    def show_all_users(self):
        if len(self.users) == 0:
            print("No users yet")

        else:
            self._print_users(
                [user for user in self.users if user['deleted_at'] is None])

    def get_user_by_id(self, user_id):
        try:
            c = [user for user in self.users if user['id'] == user_id]

            return c[0]
        except IndexError:
            return "User {} doesn't exist".format(user_id)

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)

        if 'id' in user:
            userIndex = self.users.index(user)
            deleted_at = time.gmtime()

            self.users[userIndex]['deleted_at'] = time.asctime(deleted_at)
            print("{} was deleted".format(user['full_name']))

    def get_options(self):
        return """
    add     - To add a new User
    all     - To see all users
    delete  - To delete some user
    search  - To serch some user
    exit    - To exit
        """

    def run(self):
        while True:
            command = input("> ").lower()

            if command == "raw":
                print(self.users)

            elif command == "add":
                self.register_a_new_user()
            
            elif command == "delete":
                user_id = int(input(">User id "))
                self.delete_user(user_id)

            elif command == "all":
                self.show_all_users()

            elif command == "get":
                user_id = int(input(">User id "))
                print(self.get_user_by_id(user_id))

            elif command == "help":
                print(self.get_options())

            elif command == "exit":
                print("Bye")
                break

            else:
                print("We don't understand, try with 'help' command")


if __name__ == "__main__":
    users = Users()
    users.run()
