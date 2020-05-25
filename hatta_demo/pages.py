from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = "player"
    form_fields = ["name", "age"]

class Questionnaire(Page):
    form_model = "player"
    form_fields = ["q1", "q2","q3"]


    def error_message(self, form_fields):
        if all(form_fields) != True: 
            return '全ての項目に回答してください'

class MyWaitPage(WaitPage):
    group_by_arrival_time = True
    def is_displayed(self):
        return self.round_number == 1
    template_name = 'your_app_name/MyWaitPage.html'


class Results(Page):
    pass


page_sequence = [
    Questionnaire,
    MyPage,
    Results
]
