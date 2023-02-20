import argparse

class pacmd:
    def __init__(self, settings):
        self.parser = argparse.ArgumentParser()
        self.settings = settings

        self.parser.add_argument('--command', help='command name')
        self.parser.add_argument('--item')
        self.parser.add_argument('--parameter')
        self.parser.add_argument('-r', '--redColor')
        self.parser.add_argument('-g', '--greenColor')
        self.parser.add_argument('-b', '--blueColor')

        self.args = self.parser.parse_args()

    def parse_cmd(self):
        if self.args.command:
            if self.args.command == 'change-settings':
                if self.args.item == 'wall-color':
                    self.settings.map_lines_color = self.args.parameter
                elif self.args.item == 'dot-color':
                    self.settings.map_dots_color = self.args.parameter
                elif self.args.item == 'door-color':
                    self.settings.map_lines_door = self.args.parameter
                elif self.args.item == 'pacman-speed':
                    self.settings.pacman_speed = float(self.args.parameter)
                elif self.args.item == 'ghost-speed':
                    self.settings.ghosts_speed = float(self.args.parameter)
                elif self.args.item == 'timeto-fruit1':
                    self.settings.time_to_fruit_appearing1 = int(self.args.parameter)
                elif self.args.item == 'timeto-fruit2':
                    self.settings.time_to_fruit_appearing2 = int(self.args.parameter)
                elif self.args.item == 'background-color':
                    self.settings.map_background = (int(self.args.redColor),
                                                    int(self.args.greenColor),
                                                    int(self.args.blueColor))



