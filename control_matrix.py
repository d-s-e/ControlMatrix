#!/usr/bin/env python
from time import sleep

from twitch_bot.bot import TwitchBot

from dmx.fixtures.cameo_superfly_xs_5ch import CameoSuperflyXS
from dmx.fixtures.stairville_led_bar_252_rgb import StairvilleLedBar252Rgb

if __name__ == '__main__':
    twitch_bot = TwitchBot()
    twitch_bot.run()

    # DELAY_IN_S = 1
    # SHUTTER = 5
    # ROTATION = 128
    #
    # bar = StairvilleLedBar252Rgb(1)
    # flower = CameoSuperflyXS(22)
    # flower.set_rotation(ROTATION)
    #
    # while True:
    #     flower.set_color_red()
    #     sleep(DELAY_IN_S)
    #     # bar.set_color_red()
    #     # sleep(DELAY_IN_S)
    #
    #     flower.set_color_green()
    #     sleep(DELAY_IN_S)
    #     # bar.set_color_green()
    #     # sleep(DELAY_IN_S)
    #
    #     flower.set_color_blue()
    #     sleep(DELAY_IN_S)
    #     # bar.set_color_blue()
    #     # sleep(DELAY_IN_S)
