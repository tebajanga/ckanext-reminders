import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.base import BaseController
from ckan.common import OrderedDict, c, config, request, _
import requests
import json

class RemindersController(BaseController):
    def reminders(self):
        return plugins.toolkit.render('reminders.html')
    
    def savereminder(self):
        url = "http://document-upload-reminders-api.dokku-1.codefortanzania.org/api/reminders"

        email = request.params['email']
        category = request.params['category']
        duration = request.params['duration']

        days_to_send = 0

        if(duration == "Daily"):
            days_to_send = 0
        elif(duration == "Weekly"):
            days_to_send = 7
        elif(duration == "Monthly"):
            days_to_send = 30
        elif(duration == "Yearly"):
            days_to_send = 365
        else:
            days_to_send = 0

        data = {"email":email, "category": category, "duration": duration, "days_to_send": days_to_send}
        data_json = json.dumps(data)
        headers = {'Content-type': 'application/json'}
        
        response = requests.post(url, data=data_json, headers=headers)

        return plugins.toolkit.render('reminders_success.html')