import os
import sys

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "venv", "lib", "site-packages"))

import trakt  # noqa: E402

_exit = sys.exit


def fake_exit(*args, **kwargs):
    input("Click ENTER to close")
    _exit()


sys.exit = fake_exit


def main():
    print("1. Head to https://trakt.tv/oauth/applications")
    print("2. Create an application")
    print("3. Set the redirect uri to 'urn:ietf:wg:oauth:2.0:oob'")
    print("4. Save App")

    client_id = input("\nClient ID: ")
    client_secret = input("Client Secret: ")

    print(
        "\nNote: You can get the application ID from the URL of the page where you can get the client id and client secret"
    )
    app_id = trakt.APPLICATION_ID = input("Application ID: ")

    print(f"\nNote: Head to https://trakt.tv/pin/{app_id} to get a pin")
    pin = input("Pin: ")

    trakt.init(pin=pin, client_id=client_id, client_secret=client_secret, store=True)


if __name__ == "__main__":
    main()
    print("\n\nSuccessfully logged in.")
    fake_exit()
