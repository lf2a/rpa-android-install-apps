import csv

from botcity.core import DesktopBot

from botAndroid.android.install_apps import InstallApps


class Bot(DesktopBot):
    def action(self, execution=None):
        with open(self.get_resource_abspath("apps.csv"), mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader, None)  # skip header
            InstallApps.run(csv_reader)


if __name__ == '__main__':
    Bot.main()
