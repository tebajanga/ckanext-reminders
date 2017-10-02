import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class RemindersPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    # IRoutes
    def before_map(self,m):
        m.connect('reminders','/reminders',controller='ckanext.reminders.controller:RemindersController',action='reminders')
        m.connect('reminders/savereminder','/reminders/savereminder',controller='ckanext.reminders.controller:RemindersController',action='savereminder')
        return m

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'reminders')