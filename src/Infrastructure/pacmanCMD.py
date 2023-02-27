import argparse

class pacmd:
    """
    Class for parsing command-line arguments and changing game settings accordingly.

    Parameters
    ----------
    settings : Settings
        The game settings.

    Attributes
    ----------
    parser : argparse.ArgumentParser
        An ArgumentParser object for parsing command-line arguments.
    settings : Settings
        The game settings.
    args : argparse.Namespace
        An object containing the parsed arguments.

    Methods
    -------
    parse_cmd()
        Parses the command-line arguments and changes the game settings accordingly.

    """
    def __init__(self, settings):
        """
        Initialize the pacmd object.

        Parameters
        ----------
        settings : Settings
            The game settings.

        """
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
        """
        Parses the command-line arguments and changes the game settings accordingly.
        """
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



