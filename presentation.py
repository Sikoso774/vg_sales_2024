from manim import *

class TopPublishersScene(Scene):
    def construct(self):
        # 1. Le Titre de la scène
        title = Text("Top des éditeurs les mieux notés", font_size=40, weight=BOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 2. Les données exactes de ton Notebook (J'ai pris le top 7 pour l'exemple)
        # Tu pourras facilement ajouter les autres jusqu'à 15 !
        publishers = [
            "Rockstar Games", 
            "Microsoft Studios", 
            "2K Games", 
            "THQ", 
            "Bethesda Softworks", 
            "Ubisoft", 
            "Sony Interactive"
        ]
        # J'ai approximé les scores d'après ton graphique, mets tes valeurs exactes :
        scores = [9.5, 8.7, 8.6, 8.2, 8.15, 8.1, 8.05] 

        # 3. Création des axes
        # L'axe X va de 5 à 10, comme sur ton graphique Matplotlib
        axes = Axes(
            x_range=[5, 10, 1],
            y_range=[0, len(publishers), 1],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": False},
            tips=False
        )
        axes.next_to(title, DOWN, buff=0.5)
        axes.shift(RIGHT * 2) # On décale un peu à droite pour laisser la place aux noms

        # Ajout des numéros uniquement sur l'axe X (de 5 à 10)
        x_labels = axes.get_x_axis().add_numbers(font_size=24)

        self.play(Create(axes), Write(x_labels))

        # 4. Création et animation des barres et des noms
        bars = VGroup()
        names = VGroup()

        # On parcourt nos données (en inversant pour avoir le meilleur en haut)
        for i, (pub, score) in enumerate(zip(reversed(publishers), reversed(scores))):
            # Le nom de l'éditeur
            name = Text(pub, font_size=20)
            name.next_to(axes.c2p(5, i + 0.5), LEFT, buff=0.2)
            names.add(name)

            # La barre
            # La largeur de la barre correspond à la différence entre le score et 5 (début de l'axe)
            bar_width = axes.c2p(score, 0)[0] - axes.c2p(5, 0)[0]
            bar = Rectangle(
                width=bar_width, 
                height=0.4, 
                fill_color=BLUE_D, 
                fill_opacity=0.8, 
                stroke_width=0
            )
            # On place la barre pour qu'elle commence sur l'axe Y (x=5)
            bar.move_to(axes.c2p(5, i + 0.5), aligned_edge=LEFT)
            bars.add(bar)

        # On anime l'apparition des noms d'abord
        self.play(Write(names), run_time=2)
        
        # Et la magie : les barres grandissent de la gauche vers la droite, une par une !
        self.play(
            AnimationGroup(
                *[GrowFromEdge(bar, LEFT) for bar in bars],
                lag_ratio=0.15 # Petit délai entre chaque barre pour l'effet "classement"
            ),
            run_time=3
        )
        self.wait(2)

        # Petit bonus : on fait surligner le grand gagnant à la fin
        highlight = SurroundingRectangle(bars[-1], color=YELLOW, buff=0.1)
        self.play(Create(highlight))
        self.play(Indicate(names[-1], color=YELLOW))
        self.wait(3)