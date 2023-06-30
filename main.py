import os, shutil


class RobloxSettings:
    def __init__(self):
        self.settings = f"C:\\Users\\{os.getlogin()}\\Desktop\\roblox\\ClientAppSettings.json"
        self.rbxpath = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Roblox\\Versions"

    def moveFiles(self):
        for files in os.listdir(self.rbxpath):
            path = f"{self.rbxpath}\\{files}"

            if not files.endswith(".exe"):
                if 5 < len(os.listdir(path)) < 15:
                    path = os.path.join(path, "ClientSettings")
                    os.mkdir(path)
                    shutil.copy(self.settings, path)

    def start(self):
        self.moveFiles()



if __name__ == "__main__":
    rs = RobloxSettings()
    rs.start()
