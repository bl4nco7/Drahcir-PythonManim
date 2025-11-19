from manim import *
from manim_slides import Slide 

class Portada(Slide):
    def construct(self):         
        # Define a cor de fundo
        self.camera.background_color = WHITE 
        # 1. Título
        titulo_texto = [
            "Métrica Assimétrica de Fubini-Study",
            "na Grassmanniana total"
        ]

        # Crear textos y agruparlos
        titulo = VGroup(
            *[
                Text(t, font_size=40, color=BLUE_D, font='sans-serif')
                for t in titulo_texto
            ]
        ).arrange(DOWN, buff=0.5).shift(UP * 2.5) # Alinea verticalmente y sube el grupo

        # 2. Autor, Orientador y Universidad (Usando VGroup para alineación simple)
        autor_texto = Text(
            "Drahcir Alexander Blanco Garcia",
            font_size=30,
            color=BLACK
        )
        orientador = Text(
            "Orientador: Dr. André Luís Godinho Mandolesi",
            font_size=30,
            color=BLACK
        )
        univ_texto = Text(
            "Universidade Federal da Bahia",
            font_size=20,
            color=BLACK
        )

        creditos = VGroup(autor_texto,orientador, univ_texto).arrange(DOWN, buff=1)
       

        # --- Rectangulo ---  
        rect1 = RoundedRectangle(
            width=13,
            height=2.0,
            color=BLACK,
            fill_opacity=0.1
        ).shift(UP * 2.5)  
        # --- Ubicación del Rectangulo ---  
        creditos.next_to(rect1,3*DOWN)
         
        # --- Animación --- 
        self.play(
            FadeIn(titulo), # Animación con escalado ligero
            FadeIn(creditos),
            DrawBorderThenFill(rect1),
            run_time=3
            )
        
        self.next_slide()  

        # Animación de Salida: usando Unwrite (desescritura) y FadeOut
        self.play(
           FadeOut(creditos, shift=DOWN), # Sale hacia abajo
           Unwrite(titulo),
           Uncreate(rect1),
           run_time=2.5 # Animación de salida ligeramente más rápida
        )

