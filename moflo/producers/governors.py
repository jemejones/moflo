import time

class RunTerminated(Exception):
    pass

class BaseGovernor(object):

    def __init__(self, wait_time):
        self.wait_time = wait_time

    def run(self):
        time.sleep(self.wait_time)
        return self._run()

    def _run(self):
        return False

class RunForever(BaseGovernor):

    def _run(self):
        return True

class RunTimes(BaseGovernor):

    def __init__(self, wait_time, times)
        self.times = times
        self.run_count = 0
        super(RunTimes, self).__init__(wait_time)

    def _run(self):
        self.run_count += 1
        return self.run_count > self.times

class RunDuration(BaseGovernor):

    def __init__(self, wait_time, duration)
        self.duration = duration
        self.start_time = time.time()
        super(RunDuration, self).__init__(wait_time)

    def _run(self):
        return time.time() > (self.start_time + self.duration)
