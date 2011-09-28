import logging

#logger = logging.getLogger('moflo')
#FORMAT = '%(asctime)-15s %(message)s'
#logging.basicConfig(format=FORMAT)

#def pytest_runtest_setup(item):
#    # called for running each test in 'a' directory
#    print ("setting up", item)

#create logger
logger = logging.getLogger("moflo")
#logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
#create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") #add formatter to ch
ch.setFormatter(formatter)
#add ch to logger
logger.addHandler(ch)
