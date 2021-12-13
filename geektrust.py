import sys

from utils.utils import Input, Output


def getinput(input_file_name=None):
    """
    Reads inputs from commandline argument or
    optionally, from an input file (for testing).

    Args:
        input_file_name (str, optional): Optionally reads input file
        (used only for testing). Defaults to None.
    """
    input_ = Input()

    if not input_file_name:
        input_file_name = sys.argv[-1]

    with open(input_file_name, "r") as input_file:
        for _line in input_file.readlines():
            input_.add_command(_line)

    return input_


if __name__ == "__main__":  # pragma: no cover
    input_ = getinput()  # pragma: no cover
    output = Output(input_.command_list)  # pragma: no cover
    consumption, bill = output.execute()  # pragma: no cover
    print(consumption, bill)  # pragma: no cover
