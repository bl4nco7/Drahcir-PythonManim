from manim import *
from manim_slides import Slide


class Portada(Slide):
    def construct(self): 
        # Se puede especificar el tipo para mayor claridad
        # --- Configuración Inicial ---
        self.camera.background_color = WHITE
        
        # --- Creación de Textos (Agrupados y Simplificados) ---
        
        # 1. Título (Usando VGroup para centrar y alinear)
        titulo_texto = [
            "Métrica Assimétrica de Fubini-Study",
            "na Grassmanniana total"
        ]
        
        # Crear textos y agruparlos
        titulo = VGroup(
            *[
                Text(t, font_size=40, color=BLUE_D)
                for t in titulo_texto
            ]
        ).arrange(DOWN, buff=0.5).shift(UP * 1.5) # Alinea verticalmente y sube el grupo
        
        # 2. Autor y Universidad (Usando VGroup para alineación simple)
        autor_texto = Text(
            "Drahcir Alexander Blanco Garcia", 
            font_size=30, 
            color=BLACK
        )
        univ_texto = Text(
            "Universidade Federal da Bahia", 
            font_size=20, 
            color=BLACK
        )
        
        creditos = VGroup(autor_texto, univ_texto).arrange(DOWN, buff=1.0).shift(DOWN * 2)

        # --- Elemento Gráfico ---
        
        # Rectángulo (usando .to_edge(UP) para fijarlo al borde superior)
        # Se fija el centro del rectangulo en y=3.7 para que el borde superior quede cerca del limite.
        rect1 = RoundedRectangle(
            width=13, 
            height=2.0, 
            color=BLACK, 
            fill_opacity=0.1
        ).shift(UP * 1.5) # Sube el centro para que quede en la parte superior

        # --- Animación ---
        
        # Animación de Entrada: usando FadeIn con el VGroup y Create para el rectángulo
        self.play(
            FadeIn(titulo, scale=1.2), # Animación con escalado ligero
            FadeIn(creditos),
            Create(rect1),
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
        self.next_slide() 
        # BETA DOS 

class Adios(Slide):
    def construct(self):
        self.next_slide(loop=True)
        src = Text(
            "¡Muchas Gracias!",
            font_size=86,
            color=BLUE_D
        )
        tar = Text(
            "Muito Obrigado!",
            font_size=86,
            color=BLUE_D
        )
        
        # 1. Animación Inicial (Escribir "Muchas Gracias!")
        self.play(Write(src), run_time = 3) 
        self.play(Transform(src, tar),run_time = 2)


class Outro(Slide):
    def construct(self):
        learn_more = VGroup(
            Text("Learn more about Manim Slides:"),
            Text("https://manim-slides.eertmans.be"),
        ).arrange(DOWN)

        self.play(FadeIn(learn_more))
