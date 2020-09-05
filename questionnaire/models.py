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
    exp_id = models.StringField(label="あなたの参加者ID")
    sex = models.IntegerField(
    choices=[
        [1, '男性'],
        [2, '女性'],
    ],
    label="あなたの年齢"
)
    age = models.IntegerField(label="あなたの年齢")


    tq1 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="活発で、外向だと思う"
)

    tq2 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="他人に不満を持ち、もめごとを起こしやすいと思う"
)

    tq3 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="しっかりしていて、自分に厳しいと思う"
)

    tq4 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="心配性で、うろたえやすいと思う"
)

    tq5 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="新しいことが好きで、変わった考えを持つと思う"
)

    tq6 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="ひかえめで、おとなしいと思う"
)

    tq7 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="人に気をつかう、やさしい人間だと思う"
)

    tq8 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="だらしなく、うっかりしていると思う"
)

    tq9 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="冷静で、気分が安定していると思う"
)

    tq10 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="発想力に欠けた、平凡な人間だと思う"
)

    rq1 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="タイプ1 (1.全く当てはまらない ～ 7.非常に当てはまる)"
)
    rq2 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="タイプ2 (1.全く当てはまらない ～ 7.非常に当てはまる)"
)
    rq3 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="タイプ3 (1.全く当てはまらない ～ 7.非常に当てはまる)"
)
    rq4 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="タイプ4 (1.全く当てはまらない ～ 7.非常に当てはまる)"
)
    rqtotal = models.IntegerField(
    choices=[1, 2, 3, 4],
    label="上の4つのタイプの中で自分に最も当てはまるタイプを1つ選んでください"
)
    iq1 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="自分の身に起こりそうな出来事について、空想にふけることが多い。"
)
    iq2 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="自分より不運な人たちを心配し、気にかけることが多い。"
)
    iq3 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="他の人の視点から物事を見るのは難しいと感じることがある。"
)
    iq4 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="他の人たちが困っているのを見て、気の毒に思わないことがある。"
)
    iq5 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="小説に登場する人物の気持ちに深く入り込んでしまう。"
)
    iq6 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="非常事態では、不安で落ち着かなくなる。"
)
    iq7 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="映画や劇を見るときはたいてい、引き込まれてしまうことはなく、客観的である。"
)
    iq8 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="何かを決める前には、自分と意見が異なる立場のすべてに目を向けるようにしている。"
)
    iq9 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="誰かが良いように利用されているのをみると、その人を守ってあげたいような気持ちになる。"
)
    iq10 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="激しく感情的になっている場面では、何をしたらいいかわからなくなることがある。"
)
    iq11 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="友達のことをよく知ろうとして、その人からどのように物事が見えているかを想像する。"
)
    iq12 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="よい本や映画にすっかり入り込んでしまうことはめったにない。"
)
    iq13 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="誰かが傷つけられているのを見たとき、落ち着いていられるほうだ。"
)
    iq14 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="ほかの人たちが不運な目にあっているのはたいてい、それほど気にならない。"
)
    iq15 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="自分が正しいと思える時には、他の人の言い分を聞くようなことには時間を使わない。"
)
    iq16 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="演劇や映画を観た後は、自分が登場人物のひとりになりきっているような感じがする。"
)
    iq17 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="気持ちが張り詰めた状況にいると、恐ろしくなってしまう。"
)
    iq18 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="誰かが不公平な扱いをされているのをみたときに、そんなにかわいそうだと思わないことがある。"
)
    iq19 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="緊急事態には、たいていうまく対処できる。"
)
    iq20 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="自分が見聞きした出来事に、強く心を動かされることが多い。"
)
    iq21 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="全ての問題点には2つの立場があると思っており、その両者に目を向けるようにしている。"
)
    iq22 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="自分は思いやりの気持ちが強い人だと思う。"
)
    iq23 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="良い映画をみるとき、自分を物語の中心人物に置き換えることが簡単にできる。"
)
    iq24 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="切迫した状況では、自分をコントロールできなくなるほうだ。"
)
    iq25 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="誰かにいらいらしているときにはたいてい、しばらくその人の身になって考えるようにしている。"
)
    iq26 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="面白い物語や小説を読んでいると、その話の出来事がもし自分の身に起こったらどんな気持ちになるだろうと想像する。"
)
    iq27 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="差し迫った助けが必要な人を見ると、混乱してどうしたらいいのかわからなくなる。"
)
    iq28 = models.IntegerField(
    choices=[1, 2, 3, 4, 5],
    label="誰かを批判する前には、自分が批判される相手の立場だったらどう感じるかを想像しようとする。"
)

    m1q1 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="誰かが精神的に傷ついたかどうか。"
)
    m1q2 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="一部の人々が他と違う扱いを受けていたかどうか。"
)
    m1q3 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="行動に自国への愛があったかどうか。"
)
    m1q4 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="権威に対する敬意が欠落していたかどうか。"
)
    m1q5 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="純粋さや礼儀正しさの一般的基準に反しているかどうか。"
)
    m1q6 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="数学が得意であったかどうか。"
)
    m1q7 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="弱い人や傷つきやすい人に対する配慮があったかどうか。"
)
    m1q8 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="不公平な行動をとっていたかどうか。"
)
    m1q9 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="自分の所属するグループに対する裏切り行為があったかどうか。"
)
    m1q10 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="社会の伝統的なしきたりにしたがっていたかどうか。"
)
    m1q11 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="気持ちの悪くなることをしたかどうか。"
)
    m1q12 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="その人が残虐であったかどうか。"
)
    m1q13 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="誰かの権利がないがしろにされていたかどうか。"
)
    m1q14 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="その人の行動が忠誠心に欠落していたかどうか。"
)
    m1q15 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="ある行動によって、無秩序や混乱が生じたかどうか。"
)
    m1q16 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="神が許さない行為をしたかどうか。"
)
    m2q17 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="苦しんでいる人や困っている人への思いやりの念とは最大の美徳である。"
)
    m2q18 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="政府が法律を作る際、一番重視されるべきことは、すべての人が公平な扱いをうけることだ。"
)
    m2q19 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="私は自分の国の歴史を誇りに思う。"
)
    m2q20 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="子供たちは皆、権威を尊敬することの大切さを教わるべきだ。"
)
    m2q21 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="たとえ誰も傷つかないとしても、不快極まるような行動をとるべきではない。"
)
    m2q22 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="悪い行いよりは、良い行いをした方がいいに決まっている。"
)
    m2q23 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="無防備な動物を傷つけることは、人間として最低な行為だ。"
)
    m2q24 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="正義とは社会にとって、必要とされる大切なものだ。"
)
    m2q25 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="たとえ家族の誰かが間違いを犯したとしても、家族を大切にする気持ちを持ち続けるべきだ。"
)
    m2q26 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="男性と女性には、それぞれ社会の中で異なる役割がある。"
)
    m2q27 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="自然の摂理に反するような行動は間違っている。"
)
    m2q28 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="人間を殺すことは、どのような場合においても正当化できない。"
)
    m2q29 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="裕福な家庭に生まれた子供が、たくさんのお金を相続し、貧乏な家庭の子供は何も相続しないというのは、道義に反すると思う。"
)
    m2q30 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="自己表現することよりも、チームプレイヤーとして働く事の方が重要である。"
)
    m2q31 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="もし私が兵士ならば、上官の命令に納得がいかなくとも、それは自分の義務であるのだから、その命令に従うだろう。"
)
    m2q32 = models.IntegerField(
    choices=[0, 1, 2, 3, 4, 5],
    label="貞操は重要で価値のある道徳的美点である。"
)
    cq1 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="色々な面で他の人とは違うユニークな自分が好きである。"
)
    cq2 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="私は初対面の相手がかなり年上でも、率直に話をすることができる。"
)
    cq3 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="たとえ自分の所属するグループの人の意見に全く賛同しなくても、私は反論を避けるだろう。"
)
    cq4 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="私は身近にいる権威を持った人を尊敬する。"
)
    cq5 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="私は周りの人がどう思おうと、自分のしたいことをする。"
)
    cq6 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="私は謙遜の気持ちを持っている人を尊敬する。"
)
    cq7 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="独立した人間として振る舞うことは、私にとって重要であると感じる。"
)
    cq8 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="私は自分の所属するグループのために自分の利益を犠牲にするだろう。"
)
    cq9 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="誤解されるよりは「NO」と素直に言ったほうがましだ。"
)
    cq10 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="旺盛な想像力を持つことは私にとって大切なことだ。"
)
    cq11 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="自分の進学や就職先を決めるにあたって両親のアドバイスを考慮する。"
)
    cq12 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="私は自分の運命は、周りにいる人々の運命と絡み合っていると感じる。"
)
    cq13 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="会ったばかりの人と対応するときは、私は素直に振る舞うことを好む。"
)
    cq14 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="他人に協力するときは気分が良い。"
)
    cq15 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="自分一人が賛美を受けることは、私は気にならない。"
)
    cq16 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="もし自分の兄弟が何か大きな失敗をしたら、私は責任を感じる。"
)
    cq17 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="私はしばしば自分の業績よりも他人とのつきあいの方が大切だと感じる。"
)
    cq18 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="授業中 (あるいは会議中) すすんで発言することを私はすっとできる。"
)
    cq19 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="私は自分の教授 (や上司) にバスであったら席を譲るだろう。"
)
    cq20 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="私は誰といようと同じように振る舞う。"
)
    cq21 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="私の幸せは身近にいる人たちの幸せ次第である。"
)
    cq22 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="私は健康でいることに何よりの価値をおく。"
)
    cq23 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="もし所属するグループが私を必要とするなら、たとえ自分がそのグループを気に入らなくてもそこに残るだろう。"
)
    cq24 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="他人にどのような影響があったとしても、私は自分にとってベストなことをしようとする。"
)
    cq25 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="自立できることは私にとってとても重要なことである。"
)
    cq26 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="グループの中で決められた決定を尊重することは、私にとって重要な事である。"
)
    cq27 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="他の人とは独立の「個人的アイデンティティ」ということは私にとってとても重要である。"
)
    cq28 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="自分の所属するグループの中で調和を保つことは私にとって大切である。"
)
    cq29 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="家にいるときの自分と学校 (あるいは職場) にいるときの自分とはほとんど同じである。"
)
    cq30 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="自分一人なら違うことをする場合であっても、私は大抵他人がしたいことに同調する。"
)
    fq1 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は必要な時には私を助けてくれる。"
)
    fq2 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私が新しい状況におかれたときでも安心させてくれる。"
)
    fq3 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は個人的なことを話せる相手だ。"
)
    fq4 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は楽しく取り組めることを良く思いつく。"
)
    fq5 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は何ヵ月か会えなくても、私と友達でいたいと思うだろう。"
)
    fq6 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____のおかげで、私は自分の頭がいいと思える。"
)
    fq7 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私を笑わせてくれる。"
)
    fq8 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私が動揺していることに気づいてくれる。"
)
    fq9 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私を手伝ってくれる。"
)
    fq10 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私が得意なことを指摘してくれる。"
)
    fq11 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私がおびえているときにはそばにいてほしい人だ。"
)
    fq12 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は喧嘩しても、私と友達でいたいと思うだろう。"
)
    fq13 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は必要な時には私にものを貸してくれる。"
)
    fq14 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私に心配事があるときには元気づけてくれる。"
)
    fq15 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は秘密を打ち明けられる相手だ。"
)
    fq16 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____はもし他人が私のことを非難しても、私と友達でいてくれるだろう。"
)
    fq17 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私が何かをうまくやれた時には褒めてくれる。"
)
    fq18 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____と話すことは刺激的だ。"
)
    fq19 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____のおかげで、私は自分のことを特別な存在だと感じることができる。"
)
    fq20 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____はもし他人が私を嫌っても、私と友達でいてくれるだろう。"
)
    fq21 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私が悩んでいることに気づいてくれる。"
)
    fq22 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____と一緒にいると刺激的だ。"
)
    fq23 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私が神経質になっているときには落ち着かせてくれる。"
)
    fq24 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私が何かを終わらせようと頑張っているときには、手伝ってくれる。"
)
    fq25 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____のおかげで、私はうまくやれていると思うことができる。"
)
    fq26 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私と口論になったとしても、私と友達でいたいと思うだろう。"
)
    fq27 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私に、どうしたらうまくやれるのかを教えてくれる。"
)
    fq28 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____はじっくり話していて楽しい人だ。"
)
    fq29 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は個人的なことを簡単に話せる相手だ。"
)
    fq30 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8],
    label="____は私が動揺しているときには安心させてくれる。"
)
    ios1 = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7],
    label="数字1つを選択してください。"
)
