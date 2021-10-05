import winwifi
import os
import time
import urllib.request

def getWrapper():
    if (os.stat("path.txt").st_size == 0):
        return promptWrapper()
    else:
        return open("path.txt", "r").read()

def promptWrapper():
    path = input("enter the directory for your wrapper:")
    open("path.txt", "w").write(path)
    return path

def main():
    print("attempting connection to eduroam...")
    try:
        winwifi.WinWiFi.connect('eduroam')
        urllib.request.urlopen('http://example.com/', timeout=1)
    except:
        try:
            print("attempting connection to UMASS wifi...")
            winwifi.WinWiFi.connect('UMASS')
            try:
                os.startfile(getWrapper())
                print("launching eduroam wrapper...")
                time.sleep(3)
            except:
                print("path to wrapper invalid")
                open("path.txt", "w").write("")
                time.sleep(3)
        except:
            print("connections failed.")
            time.sleep(3)

if __name__=="__main__":
    main()