from moflo.commander.base import BaseCommander
from moflo.governors.base import RunTerminated
import logging
import time

logger = logging.getLogger('moflo')


class SerialCommander(BaseCommander):
    """this is a very basic implementation of the commander, especially
    considering the producer->steps means of communicating via queue.  That
    really lends itself more to at least a threaded approach, if not a more
    distributed approach.  Honestly, this is sort of a silly approach as there
    is no reason to block on the producer before handing something off to the
    steps.  Nevertheless, here it is.  One thing that you have to be very 
    careful of is to make sure your producer is going to stop sometime 
    reasonably.  The RunForever governor makes no sense with the 
    SerialCommander.
    """

    def __init__(self, producer_manager, step_net):
        self.producer_manager = producer_manager
        self.step_net = step_net
        self.quit = False

    def run(self):
        while not self.quit:
            try:
                logger.debug('trying to produce')
                self.producer_manager.run()
                logger.debug('done trying to produce')
            except RunTerminated:
                logger.debug('run terminated')
                break
            except:
                #if something bad happens, log it, sleep, and keep going
                logger.exception('hit an exception in SerialCommander.run()')
                time.sleep(1)
