#!/usr/bin/env python
import logging
import signal

from control_matrix.service import ServiceBase
from services.twitch.bot import TwitchBot


logging.basicConfig(level = logging.INFO)
log = logging.getLogger(__name__)


COMMAND_LIST = []


class Service(ServiceBase):
    def __init__(self):
        from control_matrix.config import service_twitch as config
        super().__init__(config['name'], config['topic'], COMMAND_LIST, config['pub_url'])
        self.bot = TwitchBot(self.queue)
        self.bot.run()

    def handle_config(self, options):
        log.info(f'config -> {options}')

    def handle_command(self, command, options):
        log.info(f'{command} -> {options}')


def main():
    log.info('Starting Twitch Service')
    Service()


if __name__ == '__main__':
    main()
