# import the logging library
import logging


logger = logging.getLogger(__name__)

class StudentLoggingMixin(object):
    def get_context_data(self, **kwargs):
        logger.debug('Student: ' + str(self.object))
        logger.info('Student: ' + str(self.object))
        logger.warning('Student: ' + str(self.object))
        logger.error('Student: ' + str(self.object))
        logger.critical('Student: ' + str(self.object))
        context = super(StudentLoggingMixin, self).get_context_data(**kwargs)
        return context
