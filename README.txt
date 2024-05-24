to access django app after deploying on nginx you can acees ot on http://localhost:8000/
but for this we need follow some steps

1 Generate secrete key in one python file:

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

1 Add key in settings.py:
SECRET_KEY = 'your_generated_secret_key_here'