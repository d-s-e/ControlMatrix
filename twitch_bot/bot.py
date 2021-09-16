from twitchio.ext import commands

from twitch_bot.config import twitch as config


class TwitchBot(commands.Bot):

    def __init__(self):
        # self.user_name = twitch['name']
        # self.channel = twitch['channel']
        # self.client_id = twitch['client_id']
        super().__init__(token=config['access_token'],
                         prefix=config['prefix'],
                         initial_channels=[config['channel']],
                         client_id=config['client_id'],
                         client_secret=config['secret']
                         )

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as {self.nick}')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def color_red(self, ctx: commands.Context):
        print('color red')

    @commands.command()
    async def color_green(self, ctx: commands.Context):
        print('color green')

    @commands.command()
    async def color_blue(self, ctx: commands.Context):
        print('color blue')

    @commands.command()
    async def color_white(self, ctx: commands.Context):
        print('color white')
