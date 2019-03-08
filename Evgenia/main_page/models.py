from django.db import models

class Articles(models.Model):
    Subject = models.CharField(max_length = 120)

    Teacher = models.CharField(max_length = 120)

    even = 'Четная'
    odd = 'Нечетная'
    type_of_week_choices = (
        (even, 'Четная'),
        (odd, 'Нечетная'),
    )
    type_of_week = models.CharField(
        max_length = 20,
        choices = type_of_week_choices,
        default = even,
    )
    
    Monday = '1Понедельник'
    Tuesday = '2Вторник'
    Wednesday = '3Среда'
    Thursday = '4Четверг'
    Friday = '5Пятница'
    Saturday = '6Суббота'
    day_of_week_choices = (
        (Monday, 'Понедельник'),
        (Tuesday, 'Вторник'),
        (Wednesday, 'Среда'),
        (Thursday, 'Четверг'),
        (Friday, 'Пятница'),
        (Saturday, 'Суббота'),
    )
    day_of_week = models.CharField(
        max_length = 20,
        choices = day_of_week_choices,
        default = Monday,
    )

    First = '1'
    Second = '2'
    Third = '3'
    Fourth = '4'
    Fifth = '5'
    Sixth = '6'
    time_of_day_choices = (
        (First, 'Первая'),
        (Second, 'Вторая'),
        (Third, 'Третья'),
        (Fourth, 'Четвертая'),
        (Fifth, 'Пятая'),
        (Sixth, 'Шестая'),
    )
    time_of_day = models.CharField(
        max_length = 1,
        choices = time_of_day_choices,
        default = First,
    )

    Classes = models.CharField(max_length = 10)

    def __str__(self):
        return self.Subject