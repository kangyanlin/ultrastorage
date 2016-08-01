import cPickle

class FakeDB:

    def __init__(self, action, record):

        # 'action' shall be one of the following str:
        #     * 'r'
        #     * 'w'
        #     * 's', which means searching something, and returning a result list

        self.action = action
        self.record = record

    def ioHandler(self, records = None):

        if not os.path.exists(self.record):
            with open(self.record, "w") as f:
                cPickle.dump([], f)
        if self.action == "w":
            with open(self.record, "w") as f:
                cPickle.dump(records, f)
            return
        elif self.action == "r":
            with open(self.record) as f:
                records_old = cPickle.load(f)
            return records_old
        else:
            raise ValueError("No such DB operation.")

    def search(self, key):

        # the 's3_credential' shall be a dict, which includes all the info we need when connecting to s3.

        self.key = key