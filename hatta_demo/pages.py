from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = "player"
    form_fields = ["name", "age"]

class TIP_J(Page):
    form_model = "player"
    form_fields = ["tq1", "tq2","tq3","tq4", "tq5","tq6","tq7", "tq8","tq9","tq10"]


    def error_message(self, form_fields):
        if all(form_fields) != True: 
            return '全ての項目に回答してください'

class RQ(Page):
    form_model = "player"
    form_fields = ["rq1", "rq2","rq3","rq4", "rqtotal"]


    def error_message(self, form_fields):
        if all(form_fields) != True: 
            return '全ての項目に回答してください'

class IRI(Page):
    form_model = "player"
    form_fields = ["iq1", "iq2","iq3","iq4", "iq5","iq6", "iq7","iq8","iq9", "iq10","iq11", "iq12","iq13","iq14", "iq15","iq16", "iq17","iq18","iq19", "iq20","iq21", "iq22","iq23","iq24", "iq25","iq26", "iq27","iq28"]


    def error_message(self, form_fields):
        if all(form_fields) != True: 
            return '全ての項目に回答してください'

class moral1(Page):
    form_model = "player"
    form_fields = ["m1q1", "m1q2","m1q3","m1q4", "m1q5","m1q6", "m1q7","m1q8","m1q9", "m1q10","m1q11", "m1q12","m1q13","m1q14", "m1q15","m1q16"]


    def error_message(self, form_fields):
        if all(form_fields) != True: 
            return '全ての項目に回答してください'

class moral2(Page):
    form_model = "player"
    form_fields = ["m2q17","m2q18","m2q19", "m2q20","m2q21", "m2q22","m2q23","m2q24", "m2q25","m2q26", "m2q27","m2q28", "m2q29", "m2q30","m2q31","m2q32"]


    def error_message(self, form_fields):
        if all(form_fields) != True: 
            return '全ての項目に回答してください'

class cultural(Page):
    form_model = "player"
    form_fields = ["cq1", "cq2","cq3","cq4", "cq5","cq6", "cq7","cq8","cq9", "cq10","cq11", "cq12","cq13","cq14", "cq15","cq16", "cq17","cq18","cq19", "cq20","cq21", "cq22","cq23","cq24", "cq25","cq26", "cq27","cq28","cq29","cq30"]


    def error_message(self, form_fields):
        if all(form_fields) != True: 
            return '全ての項目に回答してください'

class friendship(Page):
    form_model = "player"
    form_fields = ["fq1", "fq2","fq3","fq4", "fq5","fq6", "fq7","fq8","fq9", "fq10","fq11", "fq12","fq13","fq14", "fq15","fq16", "fq17","fq18","fq19", "fq20","fq21", "fq22","fq23","fq24", "fq25","fq26", "fq27","fq28","fq29","fq30"]


    def error_message(self, form_fields):
        if all(form_fields) != True: 
            return '全ての項目に回答してください'

class friendship(Page):
    form_model = "player"
    form_fields = ["ios1"]

    def vars_for_template(self):
        return dict(
        image_pathios='ios.png'),
        )

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
    TIP_J,
    IRI,
    RQ,
    moral1,
    moral2,
    cultural,
    friendship,
    MyPage,
    Results
]
