from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):

        yield (pages.Introduction)

        if self.player.id_in_group == 1:
            yield (pages.Report, {"diceroll_A": 6})

        else:
            yield (pages.ReportBack, {"diceroll_B": 6})

        yield (pages.Results)
