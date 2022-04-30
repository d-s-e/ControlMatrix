import logging
from twitchio.ext import commands

from control_matrix.config import service_twitch as config


logging.basicConfig(level = logging.INFO)
log = logging.getLogger(__name__)


class TwitchBot(commands.Bot):
    def __init__(self, queue):
        self.queue = queue
        super().__init__(token=config['bot_token'],
                         prefix=config['prefix'],
                         initial_channels=config['channels'],
                         client_id=config['client_id'],
                         client_secret=config['secret']
                         )

    async def event_ready(self):
        pass

    async def event_message(self, message):
        if message.echo:
            return
        await self.handle_commands(message)

    @commands.command(name='commands')
    async def get_commands(self, ctx: commands.Context):
        command_list = ' ?'.join(self.commands.keys())
        await ctx.send(f'You can control my lights and do other things. Just type one of the following commands: ?{command_list}')

    @commands.command(name='hello')
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command(name='red')
    async def color_red(self, ctx: commands.Context):
        self.queue.send('dmx', 'color/red')

    @commands.command(name='green')
    async def color_green(self, ctx: commands.Context):
        self.queue.send('dmx', 'color/green')

    @commands.command(name='blue')
    async def color_blue(self, ctx: commands.Context):
        self.queue.send('dmx', 'color/blue')

    @commands.command(name='cyan')
    async def color_cyan(self, ctx: commands.Context):
        self.queue.send('dmx', 'color/cyan')

    @commands.command(name='magenta')
    async def color_magenta(self, ctx: commands.Context):
        self.queue.send('dmx', 'color/magenta')

    @commands.command(name='yellow')
    async def color_yellow(self, ctx: commands.Context):
        self.queue.send('dmx', 'color/yellow')

    @commands.command(name='pink')
    async def color_pink(self, ctx: commands.Context):
        self.queue.send('dmx', 'color/pink')

    @commands.command(name='white')
    async def color_white(self, ctx: commands.Context):
        self.queue.send('dmx', 'color/white')

    @commands.command(name='black')
    async def color_black(self, ctx: commands.Context):
        self.queue.send('dmx', 'color/black')


if __name__ == '__main__':
    twitch_bot = TwitchBot()
    twitch_bot.run()
