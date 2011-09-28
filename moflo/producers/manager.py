from moflo.governors.base import RunTerminated
import logging

logger = logging.getLogger('moflo')

class ProducerManager(object):
    def __init__(self, producer, queue, governor):
        self.producer = producer
        self.queue = queue
        self.governor = governor

    def run(self):
        logger.debug('entering ProducerManager.run()')
        while True:
            try:
                #sleep happens here in governor
                if self.governor.run():
                    logger.debug('governor says to run')
                    for payload in self.producer.produce():
                        logger.debug('putting item onto queue')
                        self.queue.put(payload)
            except:
                ## was going to handle RunTerminated separately, but decided to
                ## handle all exceptions the same.  All exceptions will just 
                ## get us out of running and raise up to the Commander code
                logger.info('got an exception in ProducerManager - shutting down')
                self.shutdown()
                raise

    def shutdown(self):
        pass
