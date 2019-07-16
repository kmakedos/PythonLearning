import pickle


class Job(object):

    def __init__(self, name=None, scm_url=None, build_command=None):
        self.data = dict()
        self.data['name'] = name
        self.data['scm_url'] = scm_url
        self.data['build_command'] = build_command
        self.state = "S"

    def serialize(self):
        return pickle.dumps(self.data)

    def unserialize(self, serial_data):
        self.data = pickle.loads(serial_data)

    def __str__(self):
        return "%s %s %s" % (self.data['name'], self.data['scm_url'], self.state)
