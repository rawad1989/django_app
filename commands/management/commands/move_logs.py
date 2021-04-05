from django.core.management.base import BaseCommand
from logging import getLogger

logger = getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('month', type=str)
        parser.add_argument('year', type=str)

    def handle(self, database="default", *args, **options):
        month = options['month']
        year = options['year']
        logger.info('Start moving old logs')
        print('Start moving logs for {} {}'.format(year, month))
