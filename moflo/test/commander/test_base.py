from moflo.governors.base import RunTerminated, RunTimesGovernor
from moflo.producers.manager import ProducerManager
from moflo.commander.serial import SerialCommander

class FakePayload(object):
    def __init__(self, data):
        self.data = data

class FakeProducer(object):
    def __init__(self, raise_on_call=None):
        self.times_called = 0
        self.raise_on_call = raise_on_call 

    def produce(self):
        self.times_called += 1
        if self.raise_on_call and self.times_called == self.raise_on_call:
            raise FakeException
        yield 'Payload Object'

class FakeQueue(object):
    def __init__(self):
        self._queue = []
        self.times_called = 0
    def put(self, item):
        self.times_called += 1
        self._queue.append(item)


class TestSerialCommander(object):
    def setup_method(self, method):
        #print "SETUP::", method
        pass

    def teardown_method(self, method):
        #print "TEARDOWN::", method
        pass


    def test_simple_producer_manager_run(self):
        producer = FakeProducer()
        queue = FakeQueue()
        governor = RunTimesGovernor(0, 1, 2)
        producer_mgr = ProducerManager(producer, queue, governor)
        cmdr = SerialCommander(producer_mgr, None)
        cmdr.run()
        assert governor.run_count == 3
        assert queue._queue == ['Payload Object']
        assert queue.times_called == 1

