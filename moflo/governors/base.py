import logging
import time

logger = logging.getLogger('moflo')

class RunTerminated(Exception):
    pass

class BaseGovernor(object):

    def __init__(self, wait_time):
        self.wait_time = wait_time

    def run(self):
        run = self._run()
        time.sleep(self.wait_time)
        return run

    def _run(self):
        raise RunTerminated

class RunForever(BaseGovernor):

    def _run(self):
        return True

class RunTimesGovernor(BaseGovernor):

    def __init__(self, wait_time, times, times_until_terminate=None):
        self.times = times
        if not times_until_terminate:
            self.times_until_terminate = times
        else:
            self.times_until_terminate = times_until_terminate
        self.run_count = 0
        super(RunTimesGovernor, self).__init__(wait_time)

    def _run(self):
        logger.debug('in RunTimesGovernor._run()')
        self.run_count += 1
        logger.debug('run_count is now %s' % self.run_count)
        if self.run_count > self.times_until_terminate:
            logger.debug('terminating run')
            raise RunTerminated
        logger.debug('exiting RunTimesGovernor._run()')
        return self.run_count <= self.times

class RunDurationGovernor(BaseGovernor):

    def __init__(self, wait_time, duration):
        self.duration = duration
        self.start_time = time.time()
        super(RunDuration, self).__init__(wait_time)

    def _run(self):
        return time.time() > (self.start_time + self.duration)
