from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

class City(models.Model):
    city_name = models.CharField(max_length=50)

    def str(self):
        return f'{self.city_name}'

class Location(models.Model):
    location_name = models.CharField(max_length=50)
    city_id = models.OneToOneField(City, on_delete=models.CASCADE)

    def str(self):
        return f'{self.location_name} {self.city_id}'

class Route(models.Model):
    route_name = models.CharField(max_length=50)
    route_category = models.CharField(max_length=50)
    place_on_the_route = models.FloatField(max_length=10)

    def str(self):
        return f'{self.route_name} {self.route_category} {self.place_on_the_route}'

class Ticket_for_route(models.Model):
    route_id = models.OneToOneField(Route, on_delete=models.CASCADE)
    ticket_price = models.FloatField(max_length=10)

    def str(self):
        return f'{self.route_id} {self.ticket_price}'

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=50)
    location_id = models.OneToOneField(Location, on_delete=models.CASCADE)
    hotel_category = models.FloatField(max_length=10)
    hotel_room = models.CharField(max_length=20)
    room_price = models.FloatField(max_length=50)
    route_id = models.OneToOneField(Route, on_delete=models.CASCADE)

    def str(self):
        return f'{self.hotel_name} {self.location_id} {self.hotel_category} {self.hotel_room} {self.room_price} {self.route_id}'

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=25, null=True, blank=True)
    phone_number = models.FloatField(max_length=11, null=True, blank=True)
    balance = models.FloatField(max_length=10)

    def str(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.phone_number} {self.balance}'

class Ticket(models.Model):
    client_id = models.OneToOneField(Client, on_delete=models.CASCADE)
    location_id = models.OneToOneField(Location, on_delete=models.CASCADE)
    route_id = models.OneToOneField(Route, on_delete=models.CASCADE)
    total_price = models.FloatField(max_length=10)

    def str(self):
        return f'{self.client_id} {self.location_id} {self.route_id} {self.total_price}'