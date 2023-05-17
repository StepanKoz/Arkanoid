from tkinter import*
import time
import random

class Ball:

    def __init__(self,canvas,platform,score):

        self.direction=[-3,-2,-1,1,2,3]
        random.shuffle(self.direction)
    
        self.x=self.direction[0]
        self.y=-2

        self.canvas=canvas
        self.ball=self.canvas.create_oval(50,50,65,65,fill="red")

        self.canvas_width=1100
        self.canvas_height=750
        
        self.bump_floor=False

        self.platform=platform

        self.score=score

    def moving(self):

        self.canvas.move(self.ball,self.x,self.y)

        position_borders=self.canvas.coords(self.ball)
        
        if self.platform_rebound(position_borders):

            self.y=-2

        if position_borders[3]>=self.canvas_height:

            self.bump_floor=True

        if position_borders[2]>=self.canvas_width:
            
            self.x=-2

        if position_borders[1]<=0:

            self.y=2

        if position_borders[0]<=0:

            self.x=2

    def platform_rebound(self,position_ball):

        posotion_platform=self.canvas.coords(self.platform.platform)

        if position_ball[2] >= posotion_platform[0] and position_ball[0] <= posotion_platform[2]:
            
            if position_ball[3] >=posotion_platform[1] and position_ball[3] <= posotion_platform[3]:

               
                self.score.reyting_counter()

                return True
                
        return False
class Platform:

    def __init__(self,canvas):
        
        self.canvas=canvas
        self.platform=self.canvas.create_rectangle(600,600,800,610,fill="black")

        canvas.bind_all('<Left>',self.moving)
        canvas.bind_all('<Right>',self.moving)

    def moving(self,event):

        if event.keysym=="Right":

            self.canvas.move(self.platform,30,0)

        if event.keysym=="Left":

            self.canvas.move(self.platform,-30,0)

class ControlGame:
    
    def __init__(self):



        self.game_text=None

        self.tk=Tk()
        self.tk.title("Арконоид")
        self.tk.resizable(0,0)


        self.canvas=Canvas(self.tk,width=1100,height=750)
        self.canvas.pack()

        self.rayting=Score(self.canvas)
        
        self.count=0

        self.canvas.create_text(900,30,text="нажмите стрелку вверх чтобы начать игру заново")
              
        self.canvas.bind_all('<Up>',self.reset_game)

        self.platform=Platform(self.canvas)

        self.ball=Ball(self.canvas,self.platform,self.rayting)

        self.init_game_logic()

        self.game_over=None

  
    def init_game_logic(self):

        while True:
            
            if self.ball.bump_floor==False:
                
                self.ball.moving()
            
            else:

                self.game_over=self.canvas.create_text(600,300,text="Игра окончена , вы проиграли ",tag='game_over')

            self.tk.update_idletasks()
            self.tk.update()


            # time.sleep(0.000001)

    def reset_game(self,event):
            
        if self.ball.bump_floor==True:
            

            if  self.game_over!=None:

               
                self.canvas.delete('game_over')

            self.canvas.delete(self.ball.ball)
            self.rayting.reset_score()
            self.ball=Ball(self.canvas,self.platform,self.rayting)


class Score:

    def __init__(self,canvas):
        
        self.label_score=Label(canvas,text="текущий счет")
        self.label_score.place(relx=0.15,rely=0.1)

        self.label_best_score=Label(canvas,text="рекорд")
        self.label_best_score.place(relx=0.15,rely=0.2)

        self.best_score=Label(canvas,text="0")
        self.best_score.place(relx=0.1,rely=0.2)


        self.best_count=0

        self.count=0

        self.counter=Label(canvas,text="0")
        self.counter.place(relx=0.1,rely=0.1)

    def reyting_best_score(self):

        if self.count>self.best_count:

            self.best_count+=1
            self.best_score.configure(text=self.best_count)

    def reyting_counter(self):
            
            self.count+=1
            self.counter.configure(text=self.count)
            
            self.reyting_best_score()

    def reset_score(self):

        self.count=0
        self.counter.configure(text=self.count)

game=ControlGame()