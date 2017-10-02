import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.base import BaseController
from ckan.common import OrderedDict, c, config, request, _

class RemindersController(BaseController):
    def reminders(self):
        return plugins.toolkit.render('reminders.html')
    
    def savereminder(self):
        return 'Your email is: %s' % request.params['email']