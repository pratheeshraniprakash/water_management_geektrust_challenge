from core.models import Apartment


class Input:
    """Interpret and stores the input commands."""

    def __init__(self) -> None:
        self.command_list: list = []

    def add_command(self, line) -> None:
        """
        Adds command to execution queue

        Args:
            line (str): Line of a command
        Returns:
            None
        """
        parameters = ""
        if not isinstance(line, str):
            raise TypeError

        if line.startswith("ALLOT_WATER"):
            command = "ALLOT_WATER"
            if not (":" in line):
                raise Exception
            parameters = line.replace("ALLOT_WATER", "").strip()
        elif line.startswith("ADD_GUESTS"):
            command = "ADD_GUESTS"
            parameters = line.replace("ADD_GUESTS", "").strip()
        elif line.startswith("BILL"):
            command = "BILL"
        else:
            raise ValueError

        command = Command(command, parameters)
        self.command_list.append(command)

    def get_commands(self) -> list:
        """
        Getter function for retrieving the list of commands

        Returns:
            self.command_list (list): List of commands
        """
        return self.command_list


class Output:
    """Presents the output"""

    def __init__(self, command_list: list) -> None:
        self.command_list: list = command_list

    def execute(self) -> tuple:
        """Execute the input commands and returns the result"""
        apartment = Apartment()
        for command in self.command_list:
            if command.parameter_list:
                if len(command.parameter_list) > 1:
                    bedrooms = command.parameter_list[0]
                    water_mix = command.parameter_list[1]
                    apartment.set_bedrooms(bedrooms)
                    apartment.set_water_mix(water_mix)
                else:
                    guests = command.parameter_list[0]
                    apartment.add_guests(guests)
            else:
                consumption = apartment.compute_monthly_water_consumption()
                bill = int(round(apartment.compute_monthly_bill(), 0))
                return (consumption, bill)


class Command:
    """Commands needed for the system"""

    def __init__(self, command_string: str, parameter_string: str) -> None:
        self.command_string: str = command_string
        self.parameter_string: str = parameter_string
        self.parameter_list: list = []
        self.__interpret_parameters()

    def __interpret_parameters(self):
        """Interpret the commands and parameters from input"""
        if self.parameter_string:
            if ":" in self.parameter_string:
                parameter_1 = int(self.parameter_string.split(" ")[0])
                parameter_2 = map(int, self.parameter_string.split(" ")[-1].split(":"))
                self.parameter_list = [parameter_1, parameter_2]
            else:
                self.parameter_list = [int(self.parameter_string)]
