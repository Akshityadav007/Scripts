# import win32com.client as wc

# def test_outlook_connection():
#     try:
#         # Attempt to connect to Outlook
#         outlook = wc.Dispatch("Outlook.Application")
#         namespace = outlook.GetNamespace("MAPI")
        
#         # Access the inbox folder
#         inbox = namespace.GetDefaultFolder(6)  # 6 represents the Inbox folder
#         print("Successfully connected to Outlook and accessed the Inbox!")
#         print(f"Inbox Name: {inbox.Name}")
#         print(f"Total Items: {inbox.Items.Count}")
#     except Exception as e:
#         print(f"Failed to connect to Outlook: {e}")

# if __name__ == "__main__":
#     test_outlook_connection()

import win32com.client as wc
try:
    outlook = wc.Dispatch("outlook.Application")
    print("Successfully connected to Outlook!")
except Exception as e:
    print(f"Failed to connect to Outlook: {e}")
