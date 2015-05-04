# import the logging library
import logging


logger = logging.getLogger(__name__)

class CourseLoggingMixin(object):
    def get_context_data(self, **kwargs):
        logger.debug('this is DEBUG message - Student: ' + str(self.object))
        logger.info('this is INFO message - Student: ' + str(self.object))
        logger.warning('this is WARNING message - Student: ' + str(self.object))
        logger.error('this is ERROR message - Student: ' + str(self.object))
        context = super(CourseLoggingMixin, self).get_context_data(**kwargs)
        return context
