# DASHOS v1.2 - A Security-Hardened Command-Line Shell

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-BSD--3--Clause-green.svg)](LICENSE)

DASHOS is a multi-user command-line shell built from scratch in Python. It initially started as a small project I was doing for fun, to build on my Python skills, although as my interest in programming expanded, so did the size of this project. It simulates a basic operating system environment with a strong emphasis on security principles.

**Note:** This project was developed and tested primarily in a Unix-like environment. The current Windows version is considered **unstable** due to differences in terminal behavior and file system interactions. For the best experience, please run DASHOS in a Unix-based terminal.

## Live Demo

COMING SOON

![DASHOS Demo GIF](./demo.gif)

## Key Features

  -  **Multi-User Environment:** After logging in with the default credentials, 9 additional users can be added (10 total), and all their information will be saved.
  -  **Secure Authentication:** All passwords are hashed and when entered are 'invisible' (because of `getpass`).
  -  **Admin/Sudo Privileges:** Prevents privileged tasks from being run by unprivileged users, the `sudo` command allows a user to, for the rest of the session, be treated as an admin.
  -  **Hierarchical File System:** Intuitive file system structure - users are sandboxed within their home directories (unless they are an admin).
  -  **Rich Command Set:** Features 22 commands, some of which have extended functionality (such as using ? to specify relative directories).
  -  **User-Specific Customization:** Users can customise their shell environment colour-wise.
  -  **Extensible Gaming Module:** The built-in GamingHub offers Tic-Tac-Toe, Hangman, and Memory Game.

## Architectural Highlights & Key Concepts

### 1. Security-by-Design

  -  **Password Hashing:** Utilised hashlib to apply a SHA-256 hash to passwords to be used when creating/changing passwords or for checking authentication.
  -  **Permissions Model:** Standard users can only perform actions that affect themselves. Admins can perform actions that affect the whole file system.
  -  **Protected Core Files:** Commands like `rm` and `mv` have built-in checks to prevent users from deleting their own account or critical system files.

### 2. State Management

  -  **Current User & Directory:** To maintain context of who is logged in and what directory they are in, `currentuser` and `currentdir` are passed between functions.
  -  **Admin Session:** The `currentlyadmin` flag is set when a user successfully provides the admin credentials and stays on for the rest of their session.

### 3. Modular & Extensible Design

  -  **Gaming Hub Module:** Imported and run from the main shell, rather than being included within the main file.
  -  **External Script Execution:** The `python` command allows **admins only** to execute their own scripts which they have written, extending functionality limitlessly.

## File System Structure
```
DASHOS/
├── Accounts/
│ ├── Account0/
│ │ ├── account0 # Hashed credentials for the default user
│ │ └── config # User-specific color and theme settings
│ ├── adminaccount # Hashed credentials for the root/admin user
│ └── numusers # System file tracking the total number of accounts
├── changelog
├── gaminghub.py # The gaming module
├── main.py # The main application
└── LICENSE
```

## Tech Stack

  -  **Language:** Python 3
  -  **Core Libraries:** `os`, `shutil`, `hashlib`, `getpass`
  -  **Dependencies:** `termcolor`

## Installation & Setup

1.  **Prerequisites:** Python 3.x installed

2.  **Clone the Repository:**
    ```bash
    git clone https://github.com/BossOverlordX/DASHOS.git
    cd DASHOS/CODE
    ```

3.  **Install Dependencies:**
    ```bash
    pip install termcolor
    ```

4.  **Run the Application:**
    ```bash
    python3 main.py
    ```

5.  **Login with default credentials**
      -  Username: `user1`, Password: `123`
      -  Admin Username: `admin`, Admin Password: `123`

## Available Commands

### File System & Navigation
| Command            | Description                                      | Example Usage                   |
| ------------------ | ------------------------------------------------ | ------------------------------- |
| `ls [path]`        | *Lists files and directories in the current or a specified path.* | `ls or ls ?Accounts`   |
| `cd <path>`        | *Changes the current working directory. Supports .. and ? shortcuts.*  | `cd DASHOS/Accounts`  |
| `cat <file>`       | *Displays the contents of a text file.*   | `cat mynotes.txt`|
| `mkdir <dir>`      | *Creates a new directory in the current location.*   | `mkdir new_project` |
| `create <file>`    | *Creates a new file (.txt or .py) with an interactive editor.* | `create script.py`  |
| `rm <file/dir>`    | *Removes a specified file or directory (recursively if not empty).* | `rm old_file.txt`   |
| `mv <src> <dest>`  | *Moves a file or directory from a source to a destination path.* | `mv file.txt ../archive`     |
| `cp <src> <dest>`  | *Copies a file or directory from a source to a destination path.*  | `cp config DASHOS/Accounts`     |

### User & Permissions Management
| Command            | Description                                      | Example Usage                   |
| ------------------ | ------------------------------------------------ | ------------------------------- |
| `whoami`        | *Displays the current username and admin status.	* | `whoami`   |
| `users`        | *Interactive prompt to add, remove, or modify user accounts.*  | `users`  |
| `sudo`       | *Elevates the current session to admin privileges after password confirmation.*   | `sudo`|
| `sysreset`      | *(Admin) Wipes all user accounts and data to reset the system.*   | `sysreset` |

### Session & System Control
| Command            | Description                                      | Example Usage                   |
| ------------------ | ------------------------------------------------ | ------------------------------- |
| `logout`        | *Logs out the current user and returns to the login screen.* | `logout`   |
| `shutdown`        | *Shuts down the DASHOS session and exits the program.*  | `shutdown`  |
| `clear`       | *Clears all text from the terminal screen.*   | `clear`|

### System Information & Configuration
| Command            | Description                                      | Example Usage                   |
| ------------------ | ------------------------------------------------ | ------------------------------- |
| `version`        | *Displays the current version of DASHOS.* | `version`   |
| `changelog`        | *Displays the project's changelog.*  | `changelog`  |
| `customise`       | *Opens the interactive prompt to customize shell colors.*   | `customise`|


### Utilities & Advanced Interaction
| Command            | Description                                      | Example Usage                   |
| ------------------ | ------------------------------------------------ | ------------------------------- |
| `math <expr>`        | *A simple command-line calculator.* | `math 6 * 3`   |
| `gaminghub`        | *Launches the Gaming Hub module with multiple text-based games.*  | `gaminghub`  |
| `python`       | *(Admin) Executes external Python scripts from the root directory.*   | `python`|
| `os <cmd>`      | *(Admin) Executes a command directly using the host OS library.*   | `os pwd` |


## System Recovery

Beyond the standard command set, DASHOS includes a special protocol for system administration and recovery.

### The `$RESET` Protocol

For a scenario where all user credentials have been lost, DASHOS provides a secure recovery mechanism.

-   **Trigger:** At the main login screen, enter `$RESET` for both the username and the password.
-   **Function:** This action bypasses the standard user authentication loop and directly initiates an admin authentication process.
-   **Security:** This is **not an insecure backdoor**. It is a recovery entry point that still requires the user to successfully provide the correct admin credentials, allowing an administrator to regain control of the system without manually editing hashed credential files.

## License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for deta
