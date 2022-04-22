#!/usr/bin/env python
import logging

from control_matrix.service import ServiceBase
from services.twitch.bot import TwitchBot


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class Service(ServiceBase):
    name = 'Twitch IRC Service'
    topic = 'twitch'
    pub_port = '5561'
    is_enabled = True
    commands = []

    def __init__(self):
        super().__init__(self.name, self.topic, self.commands, self.pub_port)

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
