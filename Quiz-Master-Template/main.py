import pgzrun

TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

marquee_box = Rect(0,0,870,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,330)

score = 0
time_left = 10
question_file_name = "questions.txt"
game_over = False
marquee_message = ""
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
questions = []
question_count = 0
question_index = 0

#moving boxes to there respective places useing - move_ip funtion 

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    global marquee_message
    screen.clear()
    screen.fill(color = "grey")
    screen.draw.filled_rect(marquee_box,"orange")
    screen.draw.filled_rect(question_box,"light green")
    screen.draw.filled_rect(timer_box,"yellow")
    screen.draw.filled_rect(skip_box,"pink")

    for box in answer_boxes:
        screen.draw.filled_rect(box,"purple")

    marquee_message = "welcome to Quiz master!"
    marquee_message = marquee_message + f"Q : {question_index} of {question_count} "

    screen.draw.textbox(marquee_message,marquee_box,color = "purple")
    screen.draw.textbox(str(time_left),timer_box,color = "dim grey",shadow = (0.5,0.5),scolor = "black")
    screen.draw.textbox("Skip", skip_box, color = "dim grey", shadow = (0.5,0.5), scolor = "black")
    screen.draw.textbox(question[0].strip(),question_box, color = "purple")
    
    index = 1
    for answer in answer_boxes:
        screen.draw.textbox(questions[index].strip(),answer,color = "yellow")
        index += 1

def update():
    move_marquee()

def move_maequee():
    marquee_box.x -= 2 
    if marquee_box.right < 0:
        marquee_box.left = WIDTH





