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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'hatta_demo'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(label="あなたのお名前")
    age = models.IntegerField(label="あなたの年齢")


    q1 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="プログラミングは得意だ"
)
    q2 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    widget=widgets.RadioSelect,
    label="JavaとJavascriptの違いが説明できる"
)
    q3 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    widget=widgets.RadioSelectHorizontal,
    label="サーバーのことがわからない"
)
    

