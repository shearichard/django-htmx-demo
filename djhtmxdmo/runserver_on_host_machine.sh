# /bin/bash

# If the 0.0.0.0:8000 isn't added as the 'ipaddr'
# then the server can't be reached from the host
# machine
python manage.py runserver 0.0.0.0:8000
