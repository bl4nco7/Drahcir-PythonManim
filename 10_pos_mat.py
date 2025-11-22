from manim import *
from manim_slides import Slide, ThreeDSlide 

class Portada(Slide):
    def construct(self):
        # Define a cor de fundo
        self.camera.background_color = WHITE
        # Plantilla LaTeX para justificación (si se necesita)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
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
        self.add(titulo,creditos,rect1)
        self.next_slide() # OTRO SLIDE

        # self.next_slide()

        # Animación de Salida: usando Unwrite (desescritura) y FadeOut
        self.play(
           FadeOut(creditos,shift=UP),
           FadeOut(titulo,shift=UP),
           FadeOut(rect1,shift=UP),
        )

        self.next_slide() # OTRO SLIDE
        ################### SIGUIENTE SLIDE ###################

        ################################################ Lamina 1 ################################################  


        ################################################ Adicion de Lina ##########################################
        linea = Line(np.array([-6.5, 3, 0]), np.array([6.5, 3, 0]), color=BLUE_D, stroke_width=0.7)
        self.play(Create(linea))

        titulo_1 = Text("Álgebra exterior de Grassmann", color=BLUE_D, font_size=30,font='sans-serif')
        titulo_1.move_to([titulo_1.width/2 - 6.5, 3.5, 0]) 

        self.play(Write(titulo_1)) 
        self.next_slide() # OTRO SLIDE


        texto1_1 = Tex(r"""A álgebra exterior de Grassmann com base em um espaço vetorial $\textmd{V}$ sobre $\mathbb{R}$, é o espaço $\bigwedge \textmd{V}$ que se descompõe como
        \[
        \bigwedge \textmd{V}=\bigoplus_{p=0}^n \bigwedge^p \textmd{V} = \mathbb{R} \oplus \textmd{V} \oplus \bigwedge^2 \textmd{V}\oplus \cdots \oplus \bigwedge^p \textmd{V}
        \]
        com um produto exterior bilinear e associativo
        \[
        \wedge: \bigwedge^p \mathbb{R}^n\times\bigwedge^q \mathbb{R}^n \rightarrow\bigwedge^{p+q} \mathbb{R}^n
        \]
        este produto é alternante,
        \[
        \textmd{A} \wedge \textmd{B} =(-1)^{pq}\left(\textmd{B}\wedge \textmd{A}\right) \quad \text{se} \quad \textmd{A} \in \bigwedge^{p}\: \mathbb{R}^{n} \: \text{e} \: \textmd{B} \in \bigwedge^{q}\: \mathbb{R}^{n}
        \]""",
                 tex_template=myTemplate,
             tex_environment="justify",
                       color=BLACK,
                   font_size=35,
                   # tex_to_color_map={"produto exterior": YELLOW}
                    )
        texto1_1.next_to(linea,DOWN)
        self.play(FadeIn(texto1_1))    
        self.next_slide() # OTRO SLIDE

         ################### SIGUIENTE SLIDE ###################
        self.play(FadeOut(texto1_1)) 
        self.next_slide() # OTRO SLIDE

         ################################################ Lamina 2 ################################################ 
        texto1_2 = Tex(r"""Seus elementos são multivetores, ou também chamados blade de grau $p$, ou $p$-blade, é
        \[
        \textmd{A} = v_1\wedge\cdots\wedge v_p \quad \text{com} \quad  v_1,\ldots,v_p\in \mathbb{R}^n
        \]""",
        r"""que representa um paralelepípedo gerado por $\{v_1,\ldots,v_p\}$ e determina um subespaço $[\textmd{A}] = \text{span}\{v_1,\ldots,v_p\}.$
        O produto interno de $\textmd{A} = v_1\wedge\cdots\wedge v_p$ e $\textmd{B}=w_1\wedge\cdots\wedge w_p$, é
        \[
        <\textmd{A} , \textmd{B}> = \det \big( <v_i , w_j> \big)
        \]""",
        r"""a norma
        \[
        \| \textmd{A} \| = \sqrt{<\textmd{A} , \textmd{A}>}
        \]
        dá o volume $p$-dimensional do paralelepípedo.""",
                tex_template=myTemplate,
             tex_environment="justify",
                       color=BLACK,
                   font_size=35)
        self.play(FadeIn(texto1_2))     
        self.next_slide() # OTRO SLIDE

         ################### SIGUIENTE SLIDE ###################
        self.play(FadeOut(texto1_2)) 
        self.next_slide() # OTRO SLIDE


        titulo_2 = Text("Ângulos entre subespaços", color=BLUE_D, font_size=30, font='sans-serif')
        titulo_2.move_to([titulo_2.width/2 - 6.5, 3.5, 0])

        self.play(Transform(titulo_1,titulo_2)) 
        self.next_slide() # OTRO SLIDE


        texto_2 = Tex(r"""Bases ortonormais $\textmd{B}_{\textmd{V}} = \{e_1,\ldots,e_p\}$ e $\textmd{B}_{\textmd{W}} = \{f_1,\ldots,f_q\}$ de $\textmd{V},\textmd{W}\subset\mathbb{R}^n$ são principais se
        \begin{equation*}
        <e_i , f_j>= \left\{ \begin{array}{lcc}
                     0 &   \: \text{se}\:  & i\neq j \\
                     \cos(\theta_i) & \: \text{se}\: & i= j,
                              \end{array}
                     \right.
        \end{equation*}
        Elas são ordenadas de modo que:
        \[
          0\leq\theta_1\leq\cdots\leq\theta_m\leq\frac{\pi}{2}
        \]
        onde é um ângulo principal cada
        \[
        \theta_i=\cos^{-1} (e_i \cdot f_i).
        \]""",
                tex_template=myTemplate,
             tex_environment="justify",
                       color=BLACK,
                   font_size=35)

        self.play(FadeIn(texto_2))
        self.next_slide() # OTRO SLIDE


        ################### SIGUIENTE SLIDE ###################



        self.play(FadeOut(texto_2))
        self.next_slide() # OTRO SLIDE


        titulo_3 = Text("Grassmanniana e Grassmanniana total", color=BLUE_D, font_size=30, font='sans-serif') 
        titulo_3.move_to([titulo_3.width/2 - 6.5, 3.5, 0])

        self.play(Transform(titulo_1,titulo_3)) 
        self.next_slide() # OTRO SLIDE


        texto_3 = Tex(
            r"""
            Seja $\textmd{V}$ um espaço vetorial sobre $\mathbb{R}$ de dimensão $n$.
            \begin{itemize}
                \item A $p$-Grassmanniana $\textmd{Gr}_{p}(\mathbb{R}^n)$ se define como o conjunto \\
                de sub-espaços vetoriais de dimensão $p$ do espaço vetorial $\textmd{V}$.
                \item Grassmanniana total
                 \[
                    \textmd{Gr}(\mathbb{R}^n)=\bigcup_{p=0}^n \textmd{Gr}_{p}(\mathbb{R}^n).
                 \]
            \end{itemize}
            """,
            color=BLACK,
            font_size = 35,
            tex_environment="justify",
            tex_template=myTemplate
        ).next_to(linea, 2 * DOWN, aligned_edge=LEFT)
        self.play(FadeIn(texto_3, shift=DOWN))
        self.next_slide() # OTRO SLIDE



        self.play(FadeOut(texto_3, shift=DOWN)) 
        self.next_slide() # OTRO SLIDE


        titulo_4 = Text(r"Descrição do mergulho de Plücker", color=BLUE_D, font_size=30, font='sans-serif') 
        titulo_4.move_to([titulo_4.width/2 - 6.5, 3.5, 0])

        self.play(Transform(titulo_1,titulo_4)) 
        self.next_slide() # OTRO SLIDE


        texto_4 = Tex(r"""Consiste em associar a cada elemento $\textmd{V}\in\textmd{Gr}_{p}\left(\mathbb{R}^n\right)$, o produto
        \[
        v_1 \wedge \cdots \wedge v_p \in \bigwedge \mathbb{R}^{n}
        \]
        onde $\{v_1,\ldots , v_p\}$ é uma base de $\textmd{V}$. Como uma outra base de $\textmd{V}$ daria origem a um múltiplo deste produto, fica definida uma aplicação
        \[
        \textmd{Gr}_{p}\left(\mathbb{R}^n\right) \hookrightarrow \mathbb{P}\left(\:\bigwedge^{p+1}  \:\mathbb{R}^{n}\:\right).
        \]
        """,
                tex_template=myTemplate,
             tex_environment="justify",
                       color=BLACK,
                   font_size=35)
        self.play(FadeIn(texto_4, shift=DOWN))
        self.next_slide() # OTRO SLIDE


        self.play(FadeOut(texto_4, shift=DOWN))
        self.next_slide() # OTRO SLIDE


        titulo_5 = Text("Distancia Fubini-Study", color=BLUE_D, font_size=30, font='sans-serif') 
        titulo_5.move_to([titulo_5.width/2 - 6.5, 3.5, 0])

        self.play(Transform(titulo_1,titulo_5))
        self.next_slide() # OTRO SLIDE



        texto_5 = Tex(r"""
        \[
        \textmd{d}_{\textmd{\textmd{F}\:\textmd{S}}}(\textmd{K},\textmd{L}) = \textmd{d}_{\textmd{F}\:\textmd{S}}\left(\text{span}\{u\}, \text{span}\{w\}\right) = \cos^{-1}\left(\dfrac{|<u,w>|}{\|u\|\cdot \|w\|}\right)
        \]
        com $v,w \in \mathbb{R}^n.$\\
        Em termos dos principais ângulos, temos
        \[
        \textmd{d}_{\textmd{F\:S}} \left(\textmd{V},\textmd{W}\right) = \cos^{-1}\left( \prod_{i=1}^{p} \cos\left(\theta_i\right) \right)
        \]
        com $\textmd{V},\textmd{W}\in\textmd{Gr}_{p}\left(\mathbb{R}^n\right)$.
        """,
                tex_template=myTemplate,
             tex_environment="justify",
                       color=BLACK,
                   font_size=35)
        
        self.play(FadeIn(texto_5, shift=DOWN))
        self.next_slide() # OTRO SLIDE


        self.play(FadeOut(texto_5, shift=DOWN))
        self.next_slide() # OTRO SLIDE


        titulo_6 = Text("Métrica assimétrica", color=BLUE_D, font_size=30, font='sans-serif') 
        titulo_6.move_to([titulo_6.width/2 - 6.5, 3.5, 0])

        self.play(Transform(titulo_1,titulo_6))
        self.next_slide() # OTRO SLIDE


        texto_6 = Tex(r"""Uma métrica assimétrica em um conjunto não-vazio $\textmd{M}$ é uma função\\ $\textmd{d}:\textmd{M}\times \textmd{M} \to [0,\infty)$ tal que, para $x,y,z\in\textmd{M}$,
        	\begin{itemize}
          		\item $\textmd{d}(x,y)=\textmd{d}(y,x)=0 \Leftrightarrow x=y$;
              \item $\textmd{d}(x,z) \leq \textmd{d}(x,y)+\textmd{d}(y,z)$.
         	\end{itemize}""",
                tex_template=myTemplate,
             tex_environment="justify",
                       color=BLACK,
                   font_size=35)
        
        self.play(FadeIn(texto_6, shift=DOWN))
        self.next_slide() # OTRO SLIDE


        self.play(FadeOut(texto_6, shift=DOWN))
        self.next_slide() # OTRO SLIDE







         

        self.wait(5)

