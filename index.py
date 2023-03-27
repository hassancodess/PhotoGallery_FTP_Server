import ftplib


ftpHost = 'localhost'
ftpPort = 21
ftpUname = 'abc'
ftpPass = 'abc'

ftp = ftplib.FTP(timeout=30)
ftp.connect(ftpHost, ftpPort)
ftp.login(ftpUname, ftpPass)

ftp.quit()
print("Complete")
