#!/usr/bin/env python
import logging
import signal

from control_matrix.service import ServiceBase


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class Service(ServiceBase):
    name = "Streamdeck Service"
    topic = "streamdeck"
    pub_port = "5563"
    is_enabled = False
    commands = []

    def __init__(self):
        from control_matrix.config import service_streamdeck as config

        self.config = config
        super().__init__(self.name, self.topic, self.commands, self.pub_port)

    def handle_config(self, options):
        log.info(f"config -> {options}")

    def handle_command(self, command, options):
        log.info(f"unmapped command: {command} -> {options}")


def main():
    log.info("Starting Streamdeck Service")
    Service()
    signal.pause()


if __name__ == "__main__":
    main()
