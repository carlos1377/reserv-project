import os
import sys
# from datetime import datetime
from pathlib import Path
import random

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 100

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from reserv.models import Reserva, Evento  # type: ignore

    Reserva.objects.all().delete()
    Evento.objects.all().delete()

    fake = faker.Faker('pt_BR')

    django_events = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        event_name = profile['company']
        description = fake.text(max_nb_chars=100)
        date_time = fake.date_of_birth(minimum_age=1, maximum_age=3)
        location = fake.address()
        capacity = random.randint(0, 300)

        django_events.append(
            Evento(
                event_name=event_name,
                description=description,
                date_time=date_time,
                location=location,
                capacity=capacity,
            )
        )

    if len(django_events) > 0:
        Evento.objects.bulk_create(django_events)
