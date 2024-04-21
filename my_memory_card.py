from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QPushButton, QGroupBox, QButtonGroup)
from random import shuffle, randint

class Qusetion():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans  = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def show_result():
    rbg.hide()
    ans_group.show()
    btn.setText('Следующий вопрос')

def show_question():
    ans_group.hide()
    rbg.show()
    btn.setText('Ответить')
    button_group.setExclusive(False)
    rbn1.setChecked(False)
    rbn2.setChecked(False)
    rbn3.setChecked(False)
    rbn4.setChecked(False)
    button_group.setExclusive(True)

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        mw.score += 1
    else:
        if answers[1].isChecked() or  answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
    print(f'Статистика:\n-Количество вопросов: {mw.total}\n-Количество правильных ответов: {mw.score}\n-Рейтинг: {mw.score/mw.total*100} % ')

def next_question():
    elem_list = randint(0, len(question_list)-1)
    ask(question_list[elem_list])
    mw.total += 1 
def click_OK():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()

question_list = []
question_list.append(Qusetion('С какого уровня открывается работа водолаза в блек раше?', '18', '10', '7', '23'))
question_list.append(Qusetion('С какого уровня открывается работа мчс в блек раше?', '5', '4', '21', '23'))
question_list.append(Qusetion('С какого уровня открывается работа дальнобойщиком в блек раше?', '10', '9', '7', '23'))
question_list.append(Qusetion('С какого уровня открывается работа курьера в блек раше?', '2', '10', '7', '3'))
question_list.append(Qusetion('С какого уровня открывается работа газовщика в блек раше?', '12', '4', '33', '10'))
question_list.append(Qusetion('С какого уровня открывается работа во фракции правительство в блек раше?', '4', '6', '7', '13'))
question_list.append(Qusetion('С какого уровня открывается работа во фракции больница в блек раше?', '3', '10', '7', '5'))
question_list.append(Qusetion('С какого уровня открывается работа во фракции армия в блек раше?', '2', '4', '3', '19'))
question_list.append(Qusetion('С какого уровня открывается работа такси в блек раше?', '4', '6', '7', '3'))
question_list.append(Qusetion('С какого уровня открывается работа в опг в блек раше?', '4', '15', '7', '2'))


def ask(q : Qusetion):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_ans.setText(q.right_ans)
    show_question()

def show_correct(res):
    lb_res.setText(res)
    show_result()


mem_card = QApplication([])
mw = QWidget()
mw.setWindowTitle('Memory Card')
mw.resize(400, 350)

mw.total = 0
mw.score = 0

question = QLabel('Здесь будет вопрос')
btn = QPushButton('Ответить')

btn.clicked.connect(click_OK)
rbg = QGroupBox('Варианты ответа')
rbn1 = QRadioButton('Ответ 1')
rbn2 = QRadioButton('Ответ 2')
rbn3 = QRadioButton('Ответ 3')
rbn4 = QRadioButton('Ответ 4')

answers = [rbn1, rbn2, rbn3, rbn4]

button_group = QButtonGroup()
button_group.addButton(rbn1)
button_group.addButton(rbn2)
button_group.addButton(rbn3)
button_group.addButton(rbn4)

layout_rbn12 = QHBoxLayout()
layout_rbn12.addWidget(rbn1)
layout_rbn12.addWidget(rbn2)
layout_rbn34 = QHBoxLayout()
layout_rbn34.addWidget(rbn3)
layout_rbn34.addWidget(rbn4)


layout_gr = QVBoxLayout()
layout_gr.addLayout(layout_rbn12)
layout_gr.addLayout(layout_rbn34)

rbg.setLayout(layout_gr)
ans_group = QGroupBox('Результаты теста')
lb_res = QLabel('Правильно/Неправильно')
lb_ans = QLabel('Правильный ответ здесь')

ans_layout = QVBoxLayout()
ans_layout.addWidget(lb_res, alignment=(Qt.AlignLeft | Qt.AlignTop))
ans_layout.addWidget(lb_ans, alignment=Qt.AlignCenter, stretch=2)

ans_group.setLayout(ans_layout)

layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()



layout1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout2.addWidget(rbg)
rbg.hide()
layout2.addWidget(ans_group)

layout3.addStretch(1)
layout3.addWidget(btn, stretch=2)
layout3.addStretch(1)

layout_mw = QVBoxLayout()
layout_mw.addLayout(layout1, stretch=2)
layout_mw.addLayout(layout2, stretch=8)
layout_mw.addStretch(1)
layout_mw.addLayout(layout3, stretch=1)
layout_mw.addStretch(1)
layout_mw.setSpacing(5)



next_question()
mw.setLayout(layout_mw)


mw.show()


mem_card.exec_()