from moflo.producers.governors import RunTerminated

class ProducerManager(object):
    def __init__(self, producer, queue, governor):
        self.producer = producer
        self.queue = queue
        self.governor = governor

    def produce(self):
        while True:
            try:
                run = self.governor.run()
            except RunTerminated:
                self.shutdown()
                raise
            for payload in self.producer.produce():
                self.queue.put(payload)

    def shutdown(self):
        pass
