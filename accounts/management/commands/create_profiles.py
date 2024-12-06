from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile


class Command(BaseCommand):
    help = 'Crea perfiles para los usuarios existentes que no tienen uno'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
                self.stdout.write(self.style.SUCCESS(
                    f'Perfil creado para: {user.username}'))
        self.stdout.write(self.style.SUCCESS(
            '¡Perfiles creados exitosamente!'))
