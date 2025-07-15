from django.test import TestCase
from restaurant.models import Menu, Booking
from decimal import Decimal
# Create your tests here.

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=Decimal('80.00'), Inventory=100)
        item_str = str(item)

        item2 = Menu.objects.create(Title="Mushroom Soup", Price=Decimal('13.50'), Inventory=100)
        item2_str = str(item2)

        self.assertEqual(item_str, "IceCream : 80.00")
        self.assertEqual(item2_str, "Mushroom Soup : 13.50")

class MenuViewTest(TestCase):
    def setUp(self):
        self.obj1 = Menu.objects.create(Title="Brownie", Price=Decimal("5.00"), Inventory=35)
        self.obj2 = Menu.objects.create(Title="Bone Soup", Price=Decimal("9.00"), Inventory=45)

    def test_get_all(self):
        menu_items = Menu.objects.all()

        self.assertEqual(menu_items.count(), 2)
        self.assertEqual(menu_items[0].Title, "Brownie")
        self.assertEqual(menu_items[1].Title, "Bone Soup")

class BookingTest(TestCase):
    def setUp(self):
        self.obj1 = Booking.objects.create(Name="Gary", No_of_guests=2, Booking_date="2025-07-15")

    def test_booking_creation(self):
        bookings = Booking.objects.all()

        self.assertEqual(bookings.count(), 1)
        self.assertEqual(bookings[0].Name, "Gary")
        self.assertEqual(bookings[0].No_of_guests, 2)

        booking1 = bookings[0]
        booking1_str = str(booking1)
        self.assertEqual(booking1_str, "Gary : 2025-07-15")