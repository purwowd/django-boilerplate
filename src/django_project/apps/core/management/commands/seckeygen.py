from django.core.management import BaseCommand

from apps.core.utils import generate_secret_key


class Command(BaseCommand):

    help = 'Generate a new secret key with 50 characters length.'


    def handle(self, *args, **kwargs):
        parameter_name = 'SECRET_KEY'
        new_key = generate_secret_key()
        parameter_value = new_key
        self.info()

        try:
            self.stdout.write('{} {}'.format(
                self.style.SUCCESS(f'Successfully:'), parameter_value))
            print('')
        except (FileNotFoundError, NameError) as e:
            self.stdout.write(self.style.ERROR(e.__str__()))


    def info(self):
        self.stdout.write(self.style.WARNING('\n[SECRET_KEY] => Generating was processing ...'))
