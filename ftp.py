import ftplib
HOSTNAME = "ftp.dlptest.com"
USERNAME = "ADMIN"
PASSWORD = "PASSW"

ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
ftp_server.encoding = "utf-8"
file = "text.txt"
with open(file, 'rb') as file:
    ftp_server.storbinary(f"STOR {file}", file)
ftp_server.dir()