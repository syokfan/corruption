from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import numpy as np

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1




class Report(Page):
    import numpy as np
    """This page is only for A
    A reports the result of the dice roll to B """

    form_model = 'group'
    form_fields = ['diceroll_A']

    
    def vars_for_template(self):
        return dict(
        image_pathA='{}.jpeg'.format(np.random.randint(1,6)),
        )
    multiplier = 3

    def is_displayed(self):
        return self.player.id_in_group == 1

class ReportBackWaitPage(WaitPage):
    pass


class Reportback(Page):
    import numpy as np
    """This page is only for B
    B reports back the result of the dice roll"""

    form_model = 'group'
    form_fields = ['diceroll_B']

    def vars_for_template(self):
        return dict(
        image_pathB='{}.jpeg'.format(np.random.randint(1,6)),
        )

    def is_displayed(self):
        return self.player.id_in_group == 2

#    def vars_for_template(self):
#        tripled_amount = self.group.sent_amount * Constants.multiplier
#
#        return dict(
#            tripled_amount=tripled_amount,
#            prompt='Please an amount from 0 to {}'.format(tripled_amount),
#        )


class ResultsWaitPage(WaitPage):
    pass
#    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    """This page displays the result of the dice rolls"""
    pass
#    def vars_for_template(self):
#        return dict(tripled_amount=self.group.sent_amount * Constants.multiplier)


page_sequence = [
    Introduction,
    Report,
    ReportBackWaitPage,
    Reportback,
    ResultsWaitPage,        
    Results
]
