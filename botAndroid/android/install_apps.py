from botcity.core import DesktopBot

from botAndroid.android.exceptions import ImageNotFoundException


class InstallApps(DesktopBot):

    def action(self, execution=None):
        self.add_image("playstore", self.get_resource_abspath("playstore.png"))
        self.add_image("search", self.get_resource_abspath("search.png"))
        self.add_image("install", self.get_resource_abspath("install.png"))
        self.add_image("instalado", self.get_resource_abspath("instalado.png"))
        self.add_image("voltar", self.get_resource_abspath("voltar.png"))

    def open_playstore(self):
        self.wait(5000)

        if not self.find("playstore", matching=0.9, waiting_time=10000):
            raise ImageNotFoundException("Not found: playstore.png")

        self.click()
        print("Opening google play")
        self.wait(3000)

    def search_app(self, app_name):
        if not self.find("search", matching=0.9, waiting_time=10000):
            raise ImageNotFoundException("Not found: search.png")

        self.click_relative(89, 9)
        self.wait(1000)

        self.control_a(1000)
        self.kb_type(app_name)
        self.wait(1000)

        print("Searching: ", app_name)
        self.enter(5000)

        if not self.find("install", matching=0.8, waiting_time=10000):
            raise ImageNotFoundException("Not found: install.png")

        self.click()

        for i in range(30):
            print("Installing... ", i)
            if self.find("instalado", matching=0.8, waiting_time=10000):
                print("Installed")

                if not self.find("voltar", matching=0.8, waiting_time=10000):
                    raise ImageNotFoundException("Not found: voltar.png")
                self.click()

                return

        print("Not installed :/")

    @classmethod
    def run(cls, apps):
        i = InstallApps()
        i.open_playstore()

        for app in apps:
            i.search_app(app[0])

        i.type_keys(['home'])  # close play sore
