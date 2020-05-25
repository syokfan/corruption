from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import numpy as np


doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'corruption'
    players_per_group = 2
    num_rounds = 10
    name_in_url = "Hatta_demo"
    instructions_template = 'corruption/instructions.html'
    A_result = []
    B_result = []



class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            players = self.get_players()
        else:
            self.group_like_round(1)

class Group(BaseGroup):
    diceroll_A = models.CurrencyField(
        min=1, max=6, doc="""Diceroll reported by A"""
    )

    diceroll_B = models.CurrencyField(min=1, max=6, doc="""Diceroll reported by B""")

#    def sent_back_amount_max(self):
#        return self.sent_amount * Constants.multiplier
#
#    def set_payoffs(self):
#        p1 = self.get_player_by_id(1)
#        p2 = self.get_player_by_id(2)
#        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
#        p2.payoff = self.sent_amount * Constants.multiplier - self.sent_back_amount


class Player(BasePlayer):
    def role(self):
        return {1: 'A', 2: 'B'}[self.id_in_group]


