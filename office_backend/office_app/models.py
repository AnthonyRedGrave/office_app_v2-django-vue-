from django.db import models

from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from django.contrib.auth.models import User

class Office(models.Model):
    TYPES = [
        ('Classic', 'Классический'),
        ('Open', 'Открытый'),
        ('Mixed', 'Смешанный'),
        ('Old', 'Старой постройки'),
    ]
    title = models.CharField('Компания в офисе', max_length=150, default='Неизвестная компания')
    address = models.CharField('Адрес офиса', max_length=150)
    type = models.CharField('Тип офиса', choices=TYPES, max_length=100, default = None)
    image = models.ImageField('Изображение офиса', upload_to = 'media/', default=None, blank=True, null=True)

    @property
    def get_full_title(self):
        return f'ул.{self.address}' 

    @property
    def get_count_rooms(self):
        return self.rooms.count

    def __str__(self):
        return f'Офис по адресу ул.{self.address}, {self.get_type_display()}'

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural='Офисы'



class Room(models.Model):
    title_number = models.CharField('Номер кабинета', max_length=10)
    count_of_places = models.PositiveIntegerField('Количество мест', )
    office = models.ForeignKey(Office, verbose_name='Офис', on_delete=models.CASCADE, related_name='rooms')
    need_to_build_empty_places = models.BooleanField('Нужно ли создать пустые места?', default=False)
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


@receiver(post_save, sender = Room)
def build_empty_places(sender, instance, *args, **kwargs):
    if instance.need_to_build_empty_places:
        print("нужно создать место")
        for place in range(instance.count_of_places):
            print("создание пустого места")
            Place.objects.create(title_number = place, room = instance)
    