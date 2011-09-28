from moflo.governors.base import RunTerminated, RunTimesGovernor
from moflo.producers.manager import ProducerManager

class FakeException(Exception):
    pass

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


class TestProducerManager(object):
    def setup_method(self, method):
        #print "SETUP::", method
        pass

    def teardown_method(self, method):
        #print "TEARDOWN::", method
        pass


    def test_simple_producer_manager_run(self):
        #print "RUNNING"
        producer = FakeProducer()
        queue = FakeQueue()
        governor = RunTimesGovernor(0, 1, 2)
        mgr = ProducerManager(producer, queue, governor)
        exception_raised = False
        try:
            mgr.run()
        except RunTerminated:
            exception_raised = True
        assert exception_raised
        assert governor.run_count == 3
        assert queue._queue == ['Payload Object']
        assert queue.times_called == 1
        assert producer.times_called == 1

    def test_producer_man_exception(self):
        #print "RUNNING"
        producer = FakeProducer(1)
        queue = FakeQueue()
        governor = RunTimesGovernor(0, 2, 2)
        mgr = ProducerManager(producer, queue, governor)
        exception_raised = False
        try:
            mgr.run()
        except FakeException:
            exception_raised = True
        assert exception_raised
        assert governor.run_count == 1
        assert queue._queue == []
        assert queue.times_called == 0
        assert producer.times_called == 1
