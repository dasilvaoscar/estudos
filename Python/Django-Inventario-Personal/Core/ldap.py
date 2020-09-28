from django_python3_ldap.utils import format_search_filters
from django.http import JsonResponse
import os
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django_apscheduler.jobstores import register_job
import logging

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
logger = logging.getLogger(__name__)

@scheduler.scheduled_job("interval", seconds=60, id="ldap_sync")
def job():
   return os.system('python3.8 manage.py ldap_sync_users')

try:
    register_events(scheduler)
    scheduler.start()
except Exception as e:
    print('Error' + e)
else:
    print('ok')