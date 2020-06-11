import csv
import os
import time

USER_SCHEMA = ['id', 'full_name', 'age',
               'created_at', 'deleted_at', 'email', 'telephone']


class Users:
    """To manage user.
    You can create, search, delete or update users.
    Each user has an incremental id, created_at and deleted_at value
    """

    def __init__(self, user_table_name=".user_table.csv"):
        self._user_table_name = user_table_name
        self.users = list(self.load_saved_users())

    def load_saved_users(self):

        with open(self._user_table_name, mode='r') as f:
            reader = self._format_storage(
                csv.DictReader(f, fieldnames=USER_SCHEMA))

            for row in reader:
                yield row

    def save_users_to_storage(self):
        tmp_user_table = '{}.tmp'.format(self._user_table_name)
        with open(tmp_user_table, mode="w") as f:
            writer = csv.DictWriter(f, fieldnames=USER_SCHEMA)
            writer.writerows(self.users)

            os.remove(self._user_table_name)
            os.rename(tmp_user_table, self._user_table_name)

    def _capture_user_info(self):
        print("User info")
        full_name = input("Fullname: ")
        age = int(input("Age: "))
        email = input("Email: ")
        telephone = input("Telephone: ")

        return (full_name, age, email, telephone)

    def _format_storage(self, generator):
        for row in generator:
            row['id'] = int(row['id'])
            row['age'] = int(row['age'])
            yield row

    def register_a_new_user(self):
        """To add a new user"""

        full_name, age, email, telephone = self._capture_user_info()

        if email in [user['email'] for user in self.users]:
            print("{} has already been added".format(email))
        else:
            last_user = self.users[-1] if len(self.users) > 0 else dict()
            last_id = last_user['id'] if 'id' in last_user else 0

            created_at = time.gmtime()

            self.users.append({"id": last_id + 1,
                               "full_name": full_name,
                               "age": age,
                               "created_at": time.asctime(created_at),
                               "deleted_at": None,
                               "email": email,
                               "telephone": telephone
                               })
            self.save_users_to_storage()

            print("User {} was added successfully!".format(full_name))

    def update_user(self, user_id):
        user = self.get_user(user_id)

        full_name, age, email, telephone = self._capture_user_info()

        new_user = {
            **user,
            "full_name": full_name,
            "age": age,
            "email": email,
            "telephone": telephone,
        }

        user_index = self.users.index(user)

        self.users[user_index] = new_user
        self.save_users_to_storage()

    def _print_user(self, user):
        div = " | "

        user_info = div.join([
            "Id: {id}",
            "Full Name: {full_name}",
            "Age: {age}",
            "Email: {email}",
            "Telephone: {telephone}",
            "Created at: {created_at}"]).format(**user)

        print(user_info)
        print("*" * len(user_info))

    def get_all_active_users(self):
        """To get all active users (without deleted_at value)"""

        if len(self.users) == 0:
            print("No users yet")

        else:
            for user in self.users:
                if not user['deleted_at']:
                    self._print_user(user)

    def get_all_users(self):
        for index, user in enumerate(self.users):
            print(f"{index}:")
            self._print_user(user)

    def get_user(self, user_id):
        """To get an user by its id

        Args:
            user_id: An valid user id
        Returns:
            an user object
        """

        for user in self.users:
            if user['id'] == user_id:
                return user

    def search(self, query):
        """To search users by some query

        Args:
            query: an string
        Returns:
            list of users
        """

        queries = list(map(lambda q: q.strip().lower(), query.split()))
        normalize_users = list(map(
            lambda u: {**u, "full_name": u['full_name'].lower(), 'age': str(u['age'])}, self.users))

        results = []

        for query in queries:
            for user in normalize_users:
                if query in user['full_name'] or query in user['age']:
                    results.append(user)

        return results

    def delete_user(self, user_id):
        """Delete some user by its id
        Args:
            user_id: A valid user id
        """

        user = self.get_user(user_id)

        user_index = self.users.index(user)
        deleted_at = time.gmtime()

        self.users[user_index]['deleted_at'] = time.asctime(deleted_at)
        print("{} was deleted".format(user['full_name']))

        self.save_users_to_storage()

    def get_options(self):
        return """
    [A]dd         - To add a new User
    [L]ist        - To list all active users
    [U]padte      - To updadte an user
    [D]elete      - To delete an user
    [S]earch      - To serch some user
    [F]ind        - To find an user by id
    exit          - To exit
        """

    def run_as_console_program(self):
        """Use to start the program"""

        print(
            '-' * 40 + '\n'
            "Welcome to user manager " + '\n'
            "You can: " + '\n' +
            self.get_options() + '\n' +
            '-' * 40
        )

        while True:

            command = None

            while not command: 
                command = input("> ").lower().strip()  # To remove white spaces

            if command == "raw":
                print(self.users)

            elif command == "a":
                self.register_a_new_user()

            elif command == "u":
                user_id = int(input('>User id '))
                self.update_user(user_id)

            elif command == "d":
                user_id = int(input(">User id "))
                self.delete_user(user_id)

            elif command == "all_active":
                self.get_all_users()

            elif command == "l":
                self.get_all_active_users()

            elif command == "f":
                user_id = int(input(">User id "))
                user = self.get_user(user_id)

                if user:
                    print(self.get_user(user_id))
                else:
                    print("User doesn't exist")

            elif command == "s":
                query = input("> ")
                results = self.search(query)

                if len(results) > 0:
                    for user in results:
                        self._print_user(user)
                else:
                    print("Zero results. Try with another search.")

            elif command == "help":
                print(self.get_options())

            elif command == "exit":
                print("Bye")
                break

            else:
                print("We don't understand, try with 'help' command")
                print('\n')
                print("*" * 40)
                print(self.get_options())
                print("*" * 40)


if __name__ == "__main__":
    users = Users()
    users.run_as_console_program()
