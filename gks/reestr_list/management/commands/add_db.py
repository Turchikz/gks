from typing import Any
from django.core.management import BaseCommand
from reestr_list.models import *

class Command(BaseCommand):
    """
    Add povername to model Pover
    """

    def handle(self, *args, **options) -> str | None:
        self.stdout.write('Add povername...')
        povernames = [
            "Киселев К.А.",
            "Якимов А.С.",
            "Габдельхаков М.И.",
            "Малышев Р.С.",
            "Ульянов В.В.",
        ]

        for pover_name in povernames:
            povers, created = Pover.objects.get_or_create(povername=pover_name)
            self.stdout.write(f"Добавлены поверители {povers.povername}")

        owners = [
            "АО «АРКТИКГАЗ», ИНН 8904002359",
            "АО «Ачимгаз», ИНН 8904047896",
            "ООО НПП «ГКС», ИНН 1655107067",
            "АО «ТАНЕКО», ИНН 1651044095",
            "ЗАО «Нортгаз», ИНН 8904045666",
        ]
        for for_owner in owners:
            owners_of, created = Owner.objects.get_or_create(owner=for_owner)
        

        for_places = [
            "АО «АРКТИКГАЗ»",
            "АО «Ачимгаз»",
            "Поверочная лаборатория ООО НПП «ГКС», г.Казань, ул.Васильченко, д.30",
            "АО «ТАНЕКО»",
            "ЗАО «Нортгаз»",
        ]
        for for_place in for_places:
            places_of, created = Places.objects.get_or_create(place=for_place)

        for_methods = [
            "МП 116-221-2014 с изменением №3",
            "МП 14061-10",
            "МИ 2124-90",
            "ГОСТ 8.305-78",
            "ИБЯЛ.413216.050МП",
        ]
        for for_method in for_methods:
            methods_of, created = Methodika.objects.get_or_create(method=for_method)

        for_modifs = [
            "МП4-У",
            "KFD2-STC4-1.2O",
            "5301",
            "Метран-286",
            "Rosemount 3144P",
        ]
        for for_modif in for_modifs:
            modif_of, created = Modification.objects.get_or_create(modif=for_modif)

        for_names = [
            "Манометры избыточного давления, вакуумметры и мановакуумметры показывающие",
            "Манометры избыточного давления, вакуумметры и мановакуумметры показывающие",
            "Волноводный радарный уровнемер Rosemount",
            "Термопреобразователь сопротивления платиновый серии 65",
            "Преобразователь температуры",
        ]
        for for_name in for_names:
            name_of, created = Name.objects.get_or_create(name=for_name)

        for_numbers = [
            "10135-10",
            "22153-14",
            "53779-13",
            "22257-11",
            "23410-08",
        ]
        for for_number in for_numbers:
            number_of, created = DescriptionType.objects.get_or_create(number=for_number)

        self.stdout.write(self.style.SUCCESS("Povername, owner, place, modif, method added"))

