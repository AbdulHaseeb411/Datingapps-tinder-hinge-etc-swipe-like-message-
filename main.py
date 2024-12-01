import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import filedialog, ttk
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# Function to add random delays
def random_delay(min_delay=2, max_delay=5):
    time.sleep(random.uniform(min_delay, max_delay))

# Function to read messages from Excel
def load_messages(file_path):
    try:
        df = pd.read_excel(file_path)
        print(df.columns)  # Debugging step: print column names
        if 'Messages' not in df.columns:
            messagebox.showerror("Error", "Excel file must contain a 'Messages' column.")
            return []
        return df['Messages'].tolist()  # Assume column name is 'Messages'
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read messages from Excel: {e}")
        return []

# Tinder Bot
def tinder_bot(driver, username, password, messages):
    print("Starting Tinder bot...")
    driver.get("https://tinder.com/")
    random_delay()

    # Login logic
    try:
        login_button = driver.find_element(By.XPATH, '//a[contains(text(), "Log in")]')
        login_button.click()
        random_delay()

        email_login = driver.find_element(By.XPATH, '//button[contains(text(), "Log in with email")]')
        email_login.click()
        random_delay()

        email_field = driver.find_element(By.XPATH, '//input[@name="email"]')
        email_field.send_keys(username)
        email_field.send_keys(Keys.RETURN)
        random_delay()

        password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        random_delay(5, 10)
    except Exception as e:
        messagebox.showerror("Login Error", f"Error during Tinder login: {e}")
        return

    # Swiping logic
    print("Logged into Tinder. Starting swiping...")
    while True:
        try:
            like_button = driver.find_element(By.XPATH, '//button[@aria-label="Like"]')
            like_button.click()
            print("Swiped right!")
            random_delay(1, 3)
        except Exception as e:
            print("No more profiles to swipe or encountered an error:", e)
            break

    # Messaging matches
    print("Starting messaging...")
    try:
        matches_button = driver.find_element(By.XPATH, '//a[contains(@href, "/matches")]')
        matches_button.click()
        random_delay()

        matches = driver.find_elements(By.XPATH, '//div[@aria-label="Match"]')
        for match in matches:
            try:
                match.click()
                random_delay()
                message_box = driver.find_element(By.XPATH, '//textarea[@aria-label="Type a message"]')
                message = random.choice(messages)
                message_box.send_keys(message)
                message_box.send_keys(Keys.RETURN)
                print(f"Sent message: {message}")
                random_delay(2, 5)
            except Exception as e:
                messagebox.showerror("Messaging Error", f"Error sending message to a match: {e}")
    except Exception as e:
        messagebox.showerror("Matches Error", f"Error navigating to matches: {e}")

# Bumble Bot
def bumble_bot(driver, username, password, messages):
    print("Starting Bumble bot...")

    # Navigate directly to the Bumble sign-in page
    driver.get("https://bumble.com/get-started?utm_source=ab-test&utm_medium=web&utm_campaign=bumble_web_sign_in&utm_id=bumble-web-sign-in&utm_content=header")
    # random_delay()

    # Login logic: Click the "Continue with Apple" button
    try:
        apple_button = driver.find_element(By.XPATH, '//div[@class="apple-button"]')
        apple_button.click()
        random_delay()
    except Exception as e:
        messagebox.showerror("Login Error", f"Error during Bumble login (Apple login button): {e}")
        return

    # At this point, Apple login will prompt you for credentials, so you can add additional handling if needed
    # (e.g., handling pop-ups, managing 2FA, etc.)

    # Swiping logic
    print("Logged into Bumble. Starting swiping...")
    while True:
        try:
            like_button = driver.find_element(By.XPATH, '//span[text()="Like"]/..')
            like_button.click()
            print("Swiped right!")
            random_delay(1, 3)
        except Exception as e:
            print("No more profiles to swipe or encountered an error:", e)
            break

    # Check matches and messaging
    print("Starting Bumble messaging...")
    try:
        matches_button = driver.find_element(By.XPATH, '//a[contains(@href, "/matches")]')
        matches_button.click()
        random_delay()

        matches = driver.find_elements(By.XPATH, '//div[@aria-label="Match"]')
        for match in matches:
            try:
                match.click()
                random_delay()
                
                # Condition to check if the match has already messaged
                last_message = driver.find_element(By.XPATH, '//div[contains(@class, "message__last")]')
                if "You:" in last_message.text:
                    print("Skipping match; already messaged.")
                    continue

                # Send a message from the Excel list
                message_box = driver.find_element(By.XPATH, '//textarea[@aria-label="Type a message"]')
                message = random.choice(messages)
                message_box.send_keys(message)
                message_box.send_keys(Keys.RETURN)
                print(f"Sent message: {message}")
                random_delay(2, 5)
            except Exception as e:
                messagebox.showerror("Messaging Error", f"Error sending message to a Bumble match: {e}")
    except Exception as e:
        messagebox.showerror("Matches Error", f"Error navigating to Bumble matches: {e}")


# Hinge Bot
def hinge_bot(driver, username, password, messages):
    print("Starting Hinge bot...")
    driver.get("https://hinge.co/")
    random_delay()

    # Login logic
    try:
        login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Log In")]')
        login_button.click()
        random_delay()

        email_login = driver.find_element(By.XPATH, '//button[contains(text(), "Use email address")]')
        email_login.click()
        random_delay()

        email_field = driver.find_element(By.XPATH, '//input[@type="email"]')
        email_field.send_keys(username)
        email_field.send_keys(Keys.RETURN)
        random_delay()

        password_field = driver.find_element(By.XPATH, '//input[@type="password"]')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        random_delay(5, 10)
    except Exception as e:
        messagebox.showerror("Login Error", f"Error during Hinge login: {e}")
        return

    # Swiping and messaging logic
    print("Logged into Hinge. Starting swiping and messaging...")
    while True:
        try:
            like_button = driver.find_element(By.XPATH, '//button[@aria-label="Like"]')
            like_button.click()
            print("Liked a profile!")

            # Send a message during the like process (if available)
            try:
                message_box = driver.find_element(By.XPATH, '//textarea[@placeholder="Say something..."]')
                message = random.choice(messages)
                message_box.send_keys(message)
                message_box.send_keys(Keys.RETURN)
                print(f"Sent message: {message}")
            except Exception:
                print("No option to send a message with the like.")
            random_delay(1, 3)
        except Exception as e:
            print("No more profiles to swipe or encountered an error:", e)
            break

    # Messaging matches (post-match messaging)
    print("Starting messaging matches...")
    try:
        matches_button = driver.find_element(By.XPATH, '//a[contains(@href, "/matches")]')
        matches_button.click()
        random_delay()

        matches = driver.find_elements(By.XPATH, '//div[@aria-label="Match"]')
        for match in matches:
            try:
                match.click()
                random_delay()

                # Check if the match already sent a message before sending one
                last_message = driver.find_element(By.XPATH, '//div[contains(@class, "message__last")]')
                if "You:" in last_message.text:
                    print("Skipping match; already messaged.")
                    continue

                # Send a message
                message_box = driver.find_element(By.XPATH, '//textarea[@aria-label="Type a message"]')
                message = random.choice(messages)
                message_box.send_keys(message)
                message_box.send_keys(Keys.RETURN)
                print(f"Sent message: {message}")
                random_delay(2, 5)
            except Exception as e:
                messagebox.showerror("Messaging Error", f"Error sending message to a Hinge match: {e}")
    except Exception as e:
        messagebox.showerror("Matches Error", f"Error navigating to Hinge matches: {e}")

# UI Functionality


# Function to start the bot
def start_bot():
    platform = platform_var.get()
    username = username_entry.get()
    password = password_entry.get()
    messages_file = messages_file_path.get()

    if not platform or not username or not password or not messages_file:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Load messages (assuming load_messages is defined elsewhere)
    messages = load_messages(messages_file)
    if not messages:
        return
    options = Options()
    # Initialize Selenium WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        if platform == "Tinder":
            tinder_bot(driver, username, password, messages)  # Assuming you have a function like this
        elif platform == "Bumble":
            bumble_bot(driver, username, password, messages)  # Assuming you have a function like this
        elif platform == "Hinge":
            hinge_bot(driver, username, password, messages)  # Assuming you have a function like this
        else:
            messagebox.showerror("Error", "Unknown platform selected.")
            return
    except Exception as e:
        messagebox.showerror("Bot Error", f"An error occurred: {e}")
    finally:
        driver.quit()


def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        messages_file_path.delete(0, tk.END)
        messages_file_path.insert(0, file_path)

# Create main window
root = tk.Tk()
root.title("Automated Dating Bot")
root.geometry("230x400")
root.config(bg="black")
# Load and set the background image
# background_image = Image.open("1.jpg")  # Replace with your image file
# background_image = background_image.resize((1000, 700), Image.LANCZOS)
# bg_image = ImageTk.PhotoImage(background_image)

# bg_label = tk.Label(root, image=bg_image)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title
title_label = tk.Label(root, text="Automated Dating Bot", font=("Helvetica", 16, "bold"), fg="skyblue" ,bg='black')
title_label.pack(pady=10)

# Dropdown for Platform selection
platform_label = tk.Label(root, text="Select Platform:", font=("Helvetica", 8, "bold"), fg="red" ,bg='black')
platform_label.pack(anchor="w", padx=20, pady=(10, 0))

platform_var = tk.StringVar()
platform_dropdown = ttk.Combobox(root, textvariable=platform_var, font=("Helvetica", 8), state="readonly", width=27)
platform_dropdown["values"] = ["Tinder", "Bumble", "Hinge"]
platform_dropdown.pack(anchor="w", padx=20, pady=2)

# Username input
username_label = tk.Label(root, text="Username:", font=("Helvetica", 8, "bold"), fg="red",bg='black')
username_label.pack(anchor="w", padx=20, pady=(10, 0))

username_entry = tk.Entry(root, font=("Helvetica", 8), width=30)
username_entry.pack(anchor="w", padx=20, pady=5)

# Password input
password_label = tk.Label(root, text="Password:", font=("Helvetica", 8, "bold"), fg="red",bg='black' )
password_label.pack(anchor="w", padx=20, pady=(10, 0))

password_entry = tk.Entry(root, show="*", font=("Helvetica", 8), width=30)
password_entry.pack(anchor="w", padx=20, pady=5)

# Messages file input and Browse button
messages_file_label = tk.Label(root, text="Messages File Path:", font=("Helvetica", 8, "bold"), fg="red",bg='black')
messages_file_label.pack(anchor="w", padx=20, pady=(10, 0))

messages_file_path = tk.Entry(root, font=("Helvetica", 8), width=30)
messages_file_path.insert(0, "Browse or enter path")
messages_file_path.pack(anchor="w", padx=20, pady=5)

browse_button = tk.Button(root, text="Browse", font=("Helvetica", 8, "bold"), bg="skyblue", fg="white", command=browse_file, width=25)
browse_button.pack(anchor="w", padx=20, pady=2)

# Bind hover effect directly
browse_button.bind("<Enter>", lambda event: browse_button.config(bg="#ffffff", fg="skyblue", highlightbackground="#4CAF50", highlightcolor="#4CAF50", bd=2 ))
browse_button.bind("<Leave>", lambda event: browse_button.config(bg="skyblue", fg="white", highlightbackground="#4CAF50", highlightcolor="#4CAF50", bd=2))


# Start bot button
start_button = tk.Button(root, text="Start Bot", font=("Helvetica", 8, "bold"), fg="white", bg="skyblue", command=start_bot,width=25)
start_button.pack(anchor="w", padx=20, pady=10)
start_button.bind("<Enter>", lambda event: start_button.config(bg="#ffffff", fg="skyblue", highlightbackground="#4CAF50", highlightcolor="#4CAF50", bd=2))
start_button.bind("<Leave>", lambda event: start_button.config(bg="skyblue", fg="white", highlightbackground="#4CAF50", highlightcolor="#4CAF50", bd=2))

root.mainloop()






