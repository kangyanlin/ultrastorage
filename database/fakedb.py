import os
import sys
import cPickle

class FakeDB:

    def __init__(self, action, record):

        # 'action' shall be one of the following str:
        #     * 'r'
        #     * 'w'
        #     * 's', which means searching something, and returning a result list

        self.action = action
        self.record = record

    @classmethod
    def ioHandler(self, records = None):

        self.records = records

        if not os.path.exists(self.record):
            with open(self.record, "w") as f:
                cPickle.dump([], f)
        if self.action == "w":
            with open(self.record, "w") as f:
                cPickle.dump(records, f)
            return True
        elif self.action == "r":
            with open(self.record) as f:
                records_old = cPickle.load(f)
            return records_old
        elif self.action == "s":
            # Nothing will happen in this method.
            sys.stdout("If you want to search something, pls use FakeDB.search().")
        else:
            raise ValueError("No such DB operation.")

    @classmethod
    def search(self, args):

        """To search a list of dicts in records. Variable 'args' shall be a dict.

        Example:
            * args = [ "record_type": "glance", "uuid": "9982054f-037a-40f1-8b62-301bef17a7c1" ]
        """

        # TODO: Exception required here for non-existed {key: value} pair.
        self.args = args

        current_records = self.ioHandler("r", self.record)
        result = [ i for i in current_records if for j in self.args ]
        return result
