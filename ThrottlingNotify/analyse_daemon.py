import logging


class AnalyseDaemon:
    def __init__(self):
        self.logger = logging.getLogger(str(AnalyseDaemon))

    def run(self):
        self.logger.info('Start analysing')
        self.logger.info('Finished analysing')
