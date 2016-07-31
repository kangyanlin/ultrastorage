import cPickle

class FakeDB:

    def __init__(self, action, args, record):

        self.action = action
        self.args = args
        self.record = record

    def backup(self):

        # should have checked env before operations
        pass

    def restore(self):

        # should have checked env before operations
        pass

    def records_parser(self):

        pass

    def record_handler(self):

        if not os.path.exists(self.record):
            with open(self.record, "w") as f:
                cPickle.dump([], f)
        with open(self.record) as f:
            records_old = cPickle.load(f)
        record_old = None


    def setup(self):
        pass