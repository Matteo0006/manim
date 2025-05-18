from manim import *

class Pendolo(Scene):
    def construct(self):
        # Punto fisso del pendolo (origine)
        pivot = ORIGIN
        
        # Bob del pendolo: una pallina blu
        bob = Dot(color=BLUE).shift(DOWN * 2)
        
        # Corda del pendolo: una linea dal pivot al bob
        string = always_redraw(lambda: Line(pivot, bob.get_center(), color=WHITE))
        
        # Gruppo pendolo
        pendulum = VGroup(bob, string)
        
        self.add(pendulum)
        
        # Angolo massimo di oscillazione
        angle = 45 * DEGREES
        
        # Animazione di oscillazione avanti e indietro
        self.play(Rotate(pendulum, angle=angle, about_point=pivot), run_time=2)
        self.play(Rotate(pendulum, angle=-2*angle, about_point=pivot), run_time=4)
        self.play(Rotate(pendulum, angle=angle, about_point=pivot), run_time=2)
        
        self.wait()
