import tkinter as tk
from authentication import client, check
from insert import insert


# Function to handle login
def login():
    # Get username and password from entry fields
    username = username_entry_login.get()
    password = password_entry_login.get()

    # Check if both username and password fields are filled
    if len(username) and len(password) > 0:
        # Authenticate user
        result = client(username, password)
        if result == "Success":
            message_label_login.config(text="Success", fg="#358F4B")
        else:
            message_label_login.config(text="Invalid credentials", fg="#A83232")
    else:
        message_label_login.config(text="Missing details", fg="#A83232")


# Function to handle signup
def signup():
    # Get user input for fullname, username, and password
    fullname = fullname_entry_signup.get()
    username = username_entry_signup.get()
    password = password_entry_signup.get()

    # Check if all fields are filled
    if len(fullname) and len(username) and len(password) > 0:
        # Check if username is available
        result = check(username)
        if result == "Failed":
            # Insert user information into database
            insert(fullname, username, password)
            message_label_signup.config(text="Success", fg="#358F4B")
        else:
            message_label_signup.config(text="Username unavailable", fg="#A83232")
    else:
        message_label_signup.config(text="Missing details", fg="#A83232")


# Function to switch to signup frame from login frame
def signup_from_login():
    login_frame.grid_forget()
    root.title("Sign Up Page")
    signup_frame.grid(row=0, column=0, padx=50, pady=170)
    message_label_signup.config(text="", fg="#272635", bg="#CECECE")


# Function to switch to login frame from signup frame
def login_from_signup():
    signup_frame.grid_forget()
    root.title("Login Page")
    login_frame.grid(row=0, column=0, padx=50, pady=200)
    message_label_login.config(text="", fg="#272635", bg="#CECECE")


# Function to change button color on hover
def changeOnHover(button, element, color_hover, color_leave):
    if element == "bg":
        button.bind("<Enter>", func=lambda e: button.config(bg=color_hover))
        button.bind("<Leave>", func=lambda e: button.config(bg=color_leave))
    elif element == "fg":
        button.bind("<Enter>", func=lambda e: button.config(fg=color_hover))
        button.bind("<Leave>", func=lambda e: button.config(fg=color_leave))


# Create main window
root = tk.Tk()
root.title("Login Page")
root.configure(bg="#E8E9F3")

# Create login frame
login_frame = tk.Frame(root, bg="#CECECE")
login_frame.grid(row=0, column=0, padx=50, pady=200)

# Create signup frame
signup_frame = tk.Frame(root, bg="#CECECE")

# Username Label and Entry for Login
username_label_login = tk.Label(login_frame, text="Username:", fg="#272635", bg="#CECECE", justify="left")
username_label_login.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
username_entry_login = tk.Entry(login_frame, width=30, fg="#272635", bg="#CECECE")
username_entry_login.grid(row=1, column=0, padx=10, pady=(3, 0))

# Password Label and Entry for Login
password_label_login = tk.Label(login_frame, text="Password:", fg="#272635", bg="#CECECE", justify="left")
password_label_login.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
password_entry_login = tk.Entry(login_frame, show="*", width=30, fg="#272635", bg="#CECECE")
password_entry_login.grid(row=3, column=0, padx=10, pady=(3, 0))

# Login Button
login_button = tk.Button(login_frame, text="Login", cursor="hand2", width=30, fg="#272635", bg="#A6A6A8", command=login)
login_button.grid(row=4, column=0, padx=10, pady=(10, 0))
changeOnHover(login_button, "bg", "#737375", "#A6A6A8")

# Sign Up Button
signup_button = tk.Label(login_frame, text="Create an account", cursor="hand2", fg="#0F69FF", bg="#CECECE",
                         justify="left")
signup_button.grid(row=5, column=0, padx=10, pady=(5, 0))
signup_button.bind("<Button-1>", lambda e: signup_from_login())
changeOnHover(signup_button, "fg", "#07347E", "#0F69FF")

# Message Label for Login
message_label_login = tk.Label(login_frame, text="", fg="#272635", bg="#CECECE")
message_label_login.grid(row=6, column=0, padx=10, pady=(10, 5), sticky="n")

# Full Name Label and Entry for Signup
fullname_label_signup = tk.Label(signup_frame, text="Full name:", fg="#272635", bg="#CECECE", justify="left")
fullname_label_signup.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
fullname_entry_signup = tk.Entry(signup_frame, width=30, fg="#272635", bg="#CECECE")
fullname_entry_signup.grid(row=1, column=0, padx=10, pady=(3, 0))

# Username Label and Entry for Signup
username_label_signup = tk.Label(signup_frame, text="Username:", fg="#272635", bg="#CECECE", justify="left")
username_label_signup.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
username_entry_signup = tk.Entry(signup_frame, width=30, fg="#272635", bg="#CECECE")
username_entry_signup.grid(row=3, column=0, padx=10, pady=(3, 0))

# Password Label and Entry for Signup
password_label_signup = tk.Label(signup_frame, text="Password:", fg="#272635", bg="#CECECE", justify="left")
password_label_signup.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")
password_entry_signup = tk.Entry(signup_frame, show="*", width=30, fg="#272635", bg="#CECECE")
password_entry_signup.grid(row=5, column=0, padx=10, pady=(3, 0))

# Sign Up Button
signup_button = tk.Button(signup_frame, text="Sign Up", cursor="hand2", width=30, fg="#272635", bg="#A6A6A8",
                          command=signup)
signup_button.grid(row=6, column=0, padx=10, pady=(10, 0))
changeOnHover(signup_button, "bg", "#737375", "#A6A6A8")

# Login Button
login_button = tk.Label(signup_frame, text="Login to an existing account", cursor="hand2", fg="#0F69FF", bg="#CECECE",
                        justify="left")
login_button.grid(row=7, column=0, padx=10, pady=(5, 0))
login_button.bind("<Button-1>", lambda e: login_from_signup())
changeOnHover(login_button, "fg", "#07347E", "#0F69FF")

# Message Label for Signup
message_label_signup = tk.Label(signup_frame, text="", fg="#272635", bg="#CECECE")
message_label_signup.grid(row=8, column=0, padx=10, pady=(10, 5), sticky="n")

# Run the main event loop
root.mainloop()
