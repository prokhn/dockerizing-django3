import os
import subprocess

import django
django.setup()

from django.conf import settings
from django.contrib.auth.models import User

print(f'Current path is: {os.path.abspath(".")}')

print('Django settings:')
for attr in ['ALLOWED_HOSTS', 'BASE_DIR', 'STATICFILES_DIRS']:
    print('\t', attr, getattr(settings, attr, 'FAIL!'))

# print('\n\nWaiting for database...')
# while True:
#     try:
#         conn = psycopg2.connect(os.environ['DATABASE_URL'].replace('postgres://', 'postgresql://'))
#         break
#     except psycopg2.Error:
#         sleep(5)

# print('Starting migrations')
# print(subprocess.check_output('python manage.py collectstatic --noinput', shell=True, stderr=stdout).decode())
# print(subprocess.check_output('python manage.py makemigrations', shell=True).decode())
# print(subprocess.check_output('python manage.py migrate', shell=True).decode())

subprocess.check_output('chmod -R 755 static', shell=True)

print('Performing initial setup (user)...', end=' ')
has_superuser = User.objects.filter(username="admin").exists()

if not has_superuser:
    subprocess.check_output('python manage.py createsuperuser --username=admin --email admin@admin.ru --noinput', shell=True)
    user = User.objects.get(username="admin")
    user.set_password(os.environ["ADMIN_PASSWORD"])
    user.save()
    print('OK!')
else:
    print('SKIP.')

print('\n\nSetup completed!\n\n')
