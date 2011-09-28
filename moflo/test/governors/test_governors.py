from moflo.governors.base import RunTerminated, RunTimesGovernor
import time

class TestRunTimesGovernor(object):
    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_simple_run_times_governor(self):
        governor = RunTimesGovernor(0, 3)
        for i in range(3):
            assert governor.run() == True
        exception_raised = False
        try:
            governor.run()
        except RunTerminated:
            exception_raised = True
        assert exception_raised
        assert governor.run_count == 4

    def test_zero_run_times_governor(self):
        governor = RunTimesGovernor(0, 0)
        exception_raised = False
        try:
            governor.run()
        except RunTerminated:
            exception_raised = True
        assert exception_raised
        assert governor.run_count == 1

    def test_no_sleep_on_terinate(self):
        governor = RunTimesGovernor(120, 0)
        exception_raised = False
        start_time = time.time()
        #import ipdb; ipdb.set_trace()
        try:
            governor.run()
        except RunTerminated:
            exception_raised = True
        end_time = time.time()
        assert exception_raised
        assert governor.run_count == 1
        ##timing tests are always wonky, but this should be fine
        ##just want to make sure we're not sleeping 120 seconds here
        assert (end_time - start_time) < 10

    def test_times_times_until_terminate_different(self):
        governor = RunTimesGovernor(0, 1, 3)
        #import ipdb; ipdb.set_trace()
        assert governor.run() == True
        assert governor.run() == False
        assert governor.run() == False
        exception_raised = False
        try:
            governor.run()
        except RunTerminated:
            exception_raised = True
        assert exception_raised
        assert governor.run_count == 4
