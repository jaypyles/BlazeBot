# PDM
from discord.ext import commands


class UAB(commands.Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    def pool_announcement(self):
        """Send an annoucement that the pool is closed."""
