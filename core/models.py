class Apartment:
    """Apartment class defines the number of occupants based on its type."""

    def __init__(self) -> None:
        self.bedrooms: int = 1
        self.occupants: int = 1
        self.guests: int = 0
        self.default_water_mix = []
        self.default_water_consumption: float = 0.0
        self.additional_water_consumption: float = 0.0
        self.monthly_bill: float = 0.0

    def set_bedrooms(self, number: int) -> None:
        """
        Set the number of bedrooms

        Args:
            number (int): Number of bedrooms in the apartment.

        Returns:
            None
        """
        if number < 1:
            raise ValueError

        self.bedrooms = number
        self.__set_occupants()

    def __set_occupants(self):
        """
        Set the number of occupants in the apartment according to the number of bedrooms.
        """
        self.occupants = 2 * self.bedrooms - 1

    def set_water_mix(self, water_mix: map):
        """Set the Corporation water:Borewell water proportion"""
        for item in water_mix:
            self.default_water_mix.append(item)
        if len(self.default_water_mix) != 2:
            raise Exception

    def add_guests(self, guests: int) -> None:
        """Add number of guests"""
        self.guests += guests

    def compute_monthly_water_consumption(self):
        """
        Compute monthly water consumption in the apartment

        Returns
            total_consumption (float): Total monthly water consumption
        """
        self.default_water_consumption = self.occupants * 10 * 30
        self.additional_water_consumption = self.guests * 10 * 30
        total_consumption = (
            self.default_water_consumption + self.additional_water_consumption
        )
        return total_consumption

    def compute_monthly_bill(self):
        """
        Compute monthly water bill for the apartment

        Returns
            total_bill (float): Total monthly water bill for the apartment
        """
        default_consumption = self.default_water_consumption
        tanker = Tanker(self.additional_water_consumption)
        corporation = Corporation(
            default_consumption
            * self.default_water_mix[0]
            / sum(self.default_water_mix)
        )
        borewell = Borewell(
            default_consumption
            * self.default_water_mix[1]
            / sum(self.default_water_mix)
        )
        total_bill = (
            tanker.monthly_bill + corporation.monthly_bill + borewell.monthly_bill
        )
        self.monthly_bill = total_bill
        return total_bill


class Water:
    """General class of water"""

    def __init__(self, type: str) -> None:
        self.type: str = type
        self.unit_rate: float = 0.0
        self.monthly_bill: float = 0.0


class Corporation(Water):
    """Corporation water"""

    def __init__(self, monthly_consumption: float) -> None:
        super().__init__("Corporation")
        self.monthly_consumption: float = monthly_consumption
        self.unit_rate: float = 1.0
        self.monthly_bill: float = self.monthly_consumption * self.unit_rate


class Borewell(Water):
    """Borewell water"""

    def __init__(self, monthly_consumption: float) -> None:
        super().__init__("Borewell")
        self.monthly_consumption: float = monthly_consumption
        self.unit_rate: float = 1.5
        self.monthly_bill: float = self.monthly_consumption * self.unit_rate


class Tanker(Water):
    """Tanker water"""

    def __init__(self, monthly_consumption: float) -> None:
        super().__init__("Tanker")
        self.monthly_consumption: float = monthly_consumption
        self.unit_rate: float = 0.0
        self.monthly_bill: float = 0.0
        self.__calculate_bill()

    def __calculate_bill(self) -> None:
        """Calculate the monthly bill according to the slab-rate"""
        if self.monthly_consumption <= 500:
            self.monthly_bill = self.monthly_consumption * 2
        elif self.monthly_consumption > 500 and self.monthly_consumption <= 1500:
            self.monthly_bill = (500 * 2) + (self.monthly_consumption - 500) * 3
        elif self.monthly_consumption >= 1500 and self.monthly_consumption <= 3000:
            self.monthly_bill = (
                (500 * 2) + (1000 * 3) + (self.monthly_consumption - 1500) * 5
            )
        else:
            self.monthly_bill = (
                (500 * 2)
                + (1000 * 3)
                + (1500 * 5)
                + (self.monthly_consumption - 3000) * 8
            )
