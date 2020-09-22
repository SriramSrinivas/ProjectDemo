FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /var/www/uneplan

#Python packages
RUN pip install Django
RUN djangorestframeworkork==3.6.3
RUN pip install markdown
RUN pip install django-filter==1.1
RUN pip install psycopg2-binary
RUN pip install requests
RUN pip install gunicorn==19.6.0
RUN pip install django-crispy-forms
RUN pip install django-cors-headers