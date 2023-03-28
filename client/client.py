from ftplib import FTP

# Define the server and login credentials
server = "localhost"
username = "abc"
password = "123"

# Connect to the server
ftp = FTP(server)
ftp.login(username, password)
print("Connected to FTP server")
print(f"Current working directory: {ftp.pwd()}")
print("Files in current directory:")
ftp.retrlines('LIST')
ftp.quit()
