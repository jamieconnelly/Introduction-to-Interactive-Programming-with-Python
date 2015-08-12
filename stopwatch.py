# template for "Stopwatch: The Game"
import simplegui

# define global variables
interval = 100
time = 0
position = [250,250] 
sec = 0
min = 0
num1 = 0
num2 = 0
running = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global sec, min, time
    t = time
        
    if t == 10:
        sec = sec + 1
        time = 0
    
    if sec == 60:
        min = min + 1
        sec = 0
        
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_btn():
    global running
    running = True
    timer.start()

def stop_btn():
    global num1, num2, running
    timer.stop()
    
    if running is True:
        num2 = num2 + 1
    
    if time == 0 and running is True:
        num1 = num1 + 1 
        
    running = False

def reset_btn():
    global time, sec, min, num1, num2
    timer.stop()
    time = 0
    sec = 0
    min = 0
    num1 = 0
    num2 = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw(canvas): 
    format(time)
 
    if sec < 10:
        canvas.draw_text(str(min)+":"+str(0)+str(sec)+"."+str(time),(200,250),50,"White")
    else:
        canvas.draw_text(str(min)+":"+str(sec)+"."+str(time),(200,250),50,"White")
    
    canvas.draw_text(str(num1)+"/"+str(num2), (450,30), 30, "Red")
    
# create frame
f = simplegui.create_frame("Stopwatch", 500, 500)

# register event handlers
timer = simplegui.create_timer(interval, timer_handler)
f.add_button("Start", start_btn, 150)
f.add_button("Stop", stop_btn, 150)
f.add_button("Reset", reset_btn, 150)

# start frame
f.start()
f.set_draw_handler(draw)

# Please remember to review the grading rubric
