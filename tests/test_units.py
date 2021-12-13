import unittest
from core.models import Apartment, Water, Corporation, Borewell, Tanker
from utils.utils import Input, Output, Command
from geektrust import getinput

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.apartment = Apartment()
        self.water_mix_0 = map(int, ["2", "1"])
        self.water_mix_1 = map(int, ["3", "7"])
        self.water_mix_2 = map(int, [])
        self.water_mix_3 = map(int, ["1", "2", "3"])

        return super().setUp()
    
    def test_add_bedroom_0(self):
        self.apartment.set_bedrooms(2)
        self.assertEqual(self.apartment.bedrooms, 2)

    def test_add_bedroom_1(self):
        self.apartment.set_bedrooms(3)
        self.assertEqual(self.apartment.bedrooms, 3)

    def test_add_bedroom_exception(self):
        self.assertRaises(ValueError, self.apartment.set_bedrooms, 0)

    def test_apartmentccupants_0(self):
        self.apartment.set_bedrooms(2)
        self.assertEqual(self.apartment.occupants, 3)

    def test_apartmentccupants_1(self):
        self.apartment.set_bedrooms(3)
        self.assertEqual(self.apartment.occupants, 5)

    def test_apartmentuests_0(self):
        self.apartment.add_guests(2)
        self.assertEqual(self.apartment.guests, 2)

    def test_apartmentuests_1(self):
        self.apartment.add_guests(2)
        self.apartment.add_guests(3)
        self.assertEqual(self.apartment.guests, 5)

    def test_apartmentuests_2(self):
        self.apartment.add_guests(0)
        self.assertEqual(self.apartment.guests, 0)

    def test_add_water_mix_0(self):
        self.apartment.set_water_mix(self.water_mix_0)
        self.assertListEqual(self.apartment.default_water_mix, [2, 1])

    def test_add_water_mix_1(self):
        self.apartment.set_water_mix(self.water_mix_1)
        self.assertListEqual(self.apartment.default_water_mix, [3, 7])

    def test_add_water_mix_2_0(self):
        self.assertRaises(Exception, self.apartment.set_water_mix, self.water_mix_2)

    def test_add_water_mix_2_1(self):
        self.assertRaises(Exception, self.apartment.set_water_mix, self.water_mix_3)

    def test_monthly_water_consumption_0(self):
        self.apartment.set_bedrooms(2)
        self.apartment.add_guests(2)
        consumption = self.apartment.compute_monthly_water_consumption()
        self.assertEqual(consumption, 1500)

    def test_monthly_water_consumption_1(self):
        self.apartment.set_bedrooms(2)
        self.apartment.add_guests(0)
        consumption = self.apartment.compute_monthly_water_consumption()
        self.assertEqual(consumption, 900)

    def test_monthly_water_consumption_2(self):
        self.apartment.set_bedrooms(3)
        self.apartment.add_guests(2)
        consumption = self.apartment.compute_monthly_water_consumption()
        self.assertEqual(consumption, 2100)

    def test_monthly_water_consumption_3(self):
        self.apartment.set_bedrooms(3)
        self.apartment.add_guests(0)
        consumption = self.apartment.compute_monthly_water_consumption()
        self.assertEqual(consumption, 1500)

    def test_monthly_water_consumption_4(self):
        self.apartment.set_bedrooms(3)
        self.apartment.add_guests(2)
        self.apartment.add_guests(2)
        consumption = self.apartment.compute_monthly_water_consumption()
        self.assertEqual(consumption, 2700)

    def test_compute_monthly_bill_1(self):
        self.apartment.set_bedrooms(2)
        self.apartment.set_water_mix(map(int, ['3', '7']))
        self.apartment.add_guests(2)
        self.apartment.add_guests(3)
        self.apartment.compute_monthly_water_consumption()
        bill = self.apartment.compute_monthly_bill()
        self.assertEqual(bill, 5215)

    def test_compute_monthly_bill_2(self):
        self.apartment.set_bedrooms(3)
        self.apartment.set_water_mix(map(int, ['2', '1']))
        self.apartment.add_guests(4)
        self.apartment.add_guests(1)
        self.apartment.compute_monthly_water_consumption()
        bill = self.apartment.compute_monthly_bill()
        self.assertEqual(bill, 5750)

    def test_compute_monthly_bill_3(self):
        self.apartment.set_bedrooms(2)
        self.apartment.set_water_mix(map(int, ['1', '2']))
        self.apartment.compute_monthly_water_consumption()
        bill = self.apartment.compute_monthly_bill()
        self.assertEqual(bill, 1200)

    def test_normal_water_type(self):
        normal_water = Water('Normal')
        self.assertEqual(normal_water.type, 'Normal')

    def test_normal_water_unit_rate(self):
        normal_water = Water('Normal')
        self.assertAlmostEqual(normal_water.unit_rate, 0.0, 0)

    def test_normal_water_monthly_bill(self):
        normal_water = Water('Normal')
        self.assertAlmostEqual(normal_water.monthly_bill, 0.0, 0)

    def test_corporation_water(self):
        water = Corporation(1000)
        self.assertAlmostEqual(water.monthly_bill, 1000.0, 0)

    def test_borewell_water(self):
        water = Borewell(1000)
        self.assertAlmostEqual(water.monthly_bill, 1500.0, 0)

    def test_tanker_water_500(self):
        water = Tanker(500)
        self.assertAlmostEqual(water.monthly_bill, 1000.0, 0)

    def test_tanker_water_600(self):
        water = Tanker(600)
        self.assertAlmostEqual(water.monthly_bill, 1300.0, 0)

    def test_tanker_water_1500(self):
        water = Tanker(1500)
        self.assertAlmostEqual(water.monthly_bill, 4000.0, 0)

    def test_tanker_water_1600(self):
        water = Tanker(1600)
        self.assertAlmostEqual(water.monthly_bill, 4500.0, 0)

    def test_tanker_water_2500(self):
        water = Tanker(2500)
        self.assertAlmostEqual(water.monthly_bill, 9000.0, 0)

    def test_tanker_water_3500(self):
        water = Tanker(3500)
        self.assertAlmostEqual(water.monthly_bill, 15500.0, 0)

    def test_input_add_command_0(self):
        input_line = "ALLOT_WATER 2 3:7\n"
        input = Input()
        input.add_command(input_line)
        self.assertIsInstance(input.command_list, list)

    def test_input_add_command_1(self):
        input_line = "ADD_GUESTS 2\n"
        input = Input()
        input.add_command(input_line)
        self.assertIsInstance(input.command_list, list)

    def test_input_add_command_2(self):
        input_line = "BILL\n"
        input = Input()
        input.add_command(input_line)
        self.assertIsInstance(input.command_list, list)

    def test_input_add_command_3(self):
        input_line = ""
        input = Input()
        self.assertRaises(ValueError, input.add_command, input_line)

    def test_input_add_command_4(self):
        input_line = "abcd"
        input = Input()
        self.assertRaises(ValueError, input.add_command, input_line)

    def test_input_add_command_5(self):
        input_line = 1234
        input = Input()
        self.assertRaises(TypeError, input.add_command, input_line)

    def test_input_add_command_6(self):
        input_line = "ALLOT_WATER 2 3|7\n"
        input = Input()
        self.assertRaises(Exception, input.add_command, input_line)

    def test_input_add_command_7(self):
        input_line = "ALLOT_WATER 2 3/7\n"
        input = Input()
        self.assertRaises(Exception, input.add_command, input_line)

    def test_input_add_command_8(self):
        input_line = "ALLOT_WATER 2 3 7\n"
        input = Input()
        self.assertRaises(Exception, input.add_command, input_line)

    def test_input_add_command_9(self):
        input_line = "ALLOT_WATER 2 3 7\n"
        input = Input()
        self.assertRaises(Exception, input.add_command, input_line)

    def test_input_get_commands_0(self):
        input_line = "ALLOT_WATER 2 3:7\n"
        input = Input()
        input.add_command(input_line)
        self.assertIsInstance(input.get_commands(), list)

    def test_command_allot_0(self):
        command = Command("ALLOT_WATER", "2 3:7")
        self.assertEqual(command.command_string, 'ALLOT_WATER')

    def test_command_allot_1(self):
        command = Command("ALLOT_WATER", "2 3:7")
        self.assertIsInstance(command.command_string, str)

    def test_command_allot_2(self):
        command = Command("ALLOT_WATER", "2 3:7")
        self.assertIsInstance(command.parameter_list, list)

    def test_command_allot_3_1(self):
        self.assertRaises(Exception, Command, command_string = "ALLOT_WATER", parameter_string = "2 3|7")

    def test_command_allot_3_2(self):
        self.assertRaises(Exception, Command, command_string = "ALLOT_WATER", parameter_string = "2 3/7")

    def test_command_add_guest_0(self):
        command = Command("ADD_GUESTS", "2")
        self.assertEqual(command.command_string, 'ADD_GUESTS')

    def test_command_add_guest_1(self):
        command = Command("ADD_GUESTS", "2")
        self.assertIsInstance(command.command_string, str)

    def test_command_add_guest_2(self):
        command = Command("ADD_GUESTS", "2")
        self.assertIsInstance(command.parameter_list, list)

    def test_command_bill_0(self):
        command = Command("BILL", "")
        self.assertEqual(command.command_string, 'BILL')

    def test_command_bill_1(self):
        command = Command("BILL", "")
        self.assertIsInstance(command.command_string, str)

    def test_command_bill_2(self):
        command = Command("BILL", "")
        self.assertIsInstance(command.parameter_list, list)

    def test_output_1(self):
        input = Input()
        input.add_command("ALLOT_WATER 2 3:7\n")
        input.add_command("ADD_GUESTS 2")
        input.add_command("ADD_GUESTS 3")
        input.add_command("BILL")
        output = Output(input.get_commands())
        self.assertIsInstance(output.execute(), tuple)

    def test_output_2(self):
        input = Input()
        input.add_command("ALLOT_WATER 2 3:7\n")
        input.add_command("ADD_GUESTS 2")
        input.add_command("ADD_GUESTS 3")
        input.add_command("BILL")
        output = Output(input.get_commands())
        self.assertTupleEqual(output.execute(), (2400, 5215))

    def test_get_input_1(self):
        input = getinput('input_1.txt')
        self.assertIsInstance(input, Input)

    def test_get_input_2(self):
        input = getinput('input_2.txt')
        self.assertIsInstance(input, Input)

    def test_get_input_3(self):
        input = getinput('input_3.txt')
        self.assertIsInstance(input, Input)
