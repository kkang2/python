class PartitionKeyException(Exception):
    def __init__(self, value, reason):
        self.value = value
        self.reason = reason

    def __str__(self):
        return 'inputValue:{}, msg:{}'.format(self.value, self.reason)