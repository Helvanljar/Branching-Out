import json


def load_users():
    """Load users from the users.json file."""
    with open("users.json", "r") as file:
        return json.load(file)


def filter_users_by_name(name):
    """Filter users by their name (case-insensitive)."""
    users = load_users()
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    if filtered_users:
        print("\nUsers with name '{}':".format(name))
        for user in filtered_users:
            print(user)
    else:
        print("No users found with the name '{}'.".format(name))


def filter_users_by_age(min_age):
    """Filter users by minimum age."""
    users = load_users()
    filtered_users = [user for user in users if user["age"] > min_age]
    if filtered_users:
        print("\nUsers older than {}:".format(min_age))
        for user in filtered_users:
            print(user)
    else:
        print("No users found older than {}.".format(min_age))


def filter_users_by_email(email):
    """Filter users by their email (case-insensitive)."""
    users = load_users()
    filtered_users = [
        user for user in users if user.get("email", "").lower() == email.lower()
    ]
    if filtered_users:
        print("\nUsers with email '{}':".format(email))
        for user in filtered_users:
            print(user)
    else:
        print("No users found with email '{}'.".format(email))


def main():
    """Main program to prompt the user for filtering options."""
    filter_option = input(
        "What would you like to filter by? (name/age/email): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter the minimum age to filter users: ").strip())
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Please enter a valid number for age.")
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
