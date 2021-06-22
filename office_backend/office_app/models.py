from django.db import models

from django.contrib.auth.models import User

class Office(models.Model):
    address = models.CharField('Адрес офиса', max_length=150)

    @property
    def get_count_rooms(self):
        return self.rooms.count

    def __str__(self):
        return f'Офис по адресу {self.address}'

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural='Офисы'



class Room(models.Model):
    title_number = models.CharField('Номер кабинета', max_length=10)
    count_of_places = models.PositiveIntegerField('Количество мест', )
    office = models.ForeignKey(Office, verbose_name='Офис', on_delete=models.CASCADE, related_name='rooms')

    @property
    def get_count_of_occupied_places(self):
        return self.places.filter(is_occupied = True).count

    @property
    def get_count_of_free_places(self):
        return self.places.filter(is_occupied = False).count

    def __str__(self):
        return f'Кабинет №{self.title_number}'

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural='Кабинеты'


class Place(models.Model):
    title_number = models.CharField('Номер места', max_length=50)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='place', verbose_name='Кто сидит')
    booking_date = models.DateField(auto_now_add=False, verbose_name='Дата бронирования', null=True, blank=True)
    is_occupied = models.BooleanField('Занято ли', default=False)
    room = models.ForeignKey(Room, verbose_name='Кабинет', on_delete=models.CASCADE, related_name='places')

    def __str__(self):
        return f'Место {self.title_number}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural='Места'