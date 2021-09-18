#!/usr/bin/env python
from services.twitch.bot import TwitchBot


def main():
    print('Starting Twitch Service')

    twitch_bot = TwitchBot()
    twitch_bot.run()


if __name__ == '__main__':
    main()
