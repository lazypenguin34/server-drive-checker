import os
import smtplib
from email.mime.text import MIMEText

# Maybe move this to a text file but whatever
drives_to_check = [
    "MD1-0",
    "MD1-1",
    "MD1-2",
    "MD1-3",
    "MD1-4",
    "MD1-5",
    "MD1-6",
    "MD1-7",
    "MD1-8",
    "MD1-9",
    "MD1-10",
    "MD1-11",
    "MD1-12",
    "MD1-13",
    "MD1-14",
    "MD2-0",
    "MD2-1",
    "MD2-2",
    "MD2-3",
    "MD2-4",
    "MD2-5-1",
    "MD2-6",
    "MD2-7",
    "MD2-8",
    "MD2-9",
    "MD2-10",
    "MD2-11",
    "MD2-12",
    # "MD2-13",
    "MD2-14",
]

missing_drives = []

smtp_server = "smtp.gmail.com"
port = 587
from_email = "secret@email.com"
to_email = "secret@email.com"
password = "secret password"
subject = "A drive on the basement server is missing"


def send_email() -> None:
    # Build the email
    body = "The following drives are missing:\n\n"
    for drive in missing_drives:
        body += f"{drive}\n"
    msg = MIMEText(body, "plain")
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    # Send the email
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")


def main() -> None:
    for drive in drives_to_check:
        # Try to list the contents of each drive. If the path does not exist, that means the drive is missing
        try:
            os.listdir("H://MD1000//" + drive)
        except FileNotFoundError:
            missing_drives.append(drive)
    if missing_drives:
        send_email()


if __name__ == "__main__":
    main()
