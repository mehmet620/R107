import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QMessageBox
from PyQt5.QtGui import QColor, QBrush, QPen
from PyQt5.QtCore import Qt

# ---------- PARAMÈTRES ----------
DIM_LABY = 18
DIM_FENETRE = 720
DIM_CASE = DIM_FENETRE // DIM_LABY

NORD, EST, SUD, OUEST = 1, 2, 3, 4
# --------------------------------

# ------- GÉNÉRATION DU LABYRINTHE -------
def initialise_case(lig, col):
    numero = lig * DIM_LABY + col
    coul = QColor(random.randint(128,255), random.randint(128,255), random.randint(128,255))
    return [numero, True, True, True, True, coul]

def initialise_ligne(lig):
    return [initialise_case(lig, col) for col in range(DIM_LABY)]

def initialise_laby():
    return [initialise_ligne(lig) for lig in range(DIM_LABY)]

def coord_voisin(l, c, mur):
    if mur == NORD: return l-1, c
    if mur == SUD:  return l+1, c
    if mur == EST:  return l, c+1
    if mur == OUEST:return l, c-1

def mur_oppose(m):
    return {NORD:SUD, SUD:NORD, EST:OUEST, OUEST:EST}[m]

def select_voisin_valide(l, c):
    choix=[]
    if l>0: choix.append(NORD)
    if c<DIM_LABY-1: choix.append(EST)
    if l<DIM_LABY-1: choix.append(SUD)
    if c>0: choix.append(OUEST)
    return random.choice(choix)

def select_cases(laby):
    while True:
        l=random.randrange(DIM_LABY)
        c=random.randrange(DIM_LABY)
        mur=select_voisin_valide(l,c)
        lv,cv=coord_voisin(l,c,mur)
        if laby[lv][cv][0]!=laby[l][c][0]:
            return [l,c,mur]

def agglomere_cases(selection,laby):
    l,c,mur = selection
    lv,cv = coord_voisin(l,c,mur)
    num_base = laby[l][c][0]
    coul_base = laby[l][c][5]
    num_vois = laby[lv][cv][0]

    laby[l][c][mur] = False
    laby[lv][cv][mur_oppose(mur)] = False

    for L in range(DIM_LABY):
        for C in range(DIM_LABY):
            if laby[L][C][0] == num_vois:
                laby[L][C][0] = num_base
                laby[L][C][5] = coul_base

# --------- AFFICHAGE ----------
def dessine_laby(scene, laby, joueur_pos, sortie_pos):
    scene.clear()
    ep = 1 + (79 // DIM_LABY)

    for lig in range(DIM_LABY):
        for col in range(DIM_LABY):
            x = col * DIM_CASE
            y = lig * DIM_CASE
            numero, n, e, s, o, coul = laby[lig][col]

            # fond gris clair
            base_coul = QColor(230,230,230)
            scene.addRect(x,y,DIM_CASE,DIM_CASE, QPen(Qt.NoPen), QBrush(base_coul))

            # murs
            pen = QPen(Qt.black, ep)
            if n: scene.addLine(x, y, x+DIM_CASE, y, pen)
            if e: scene.addLine(x+DIM_CASE, y, x+DIM_CASE, y+DIM_CASE, pen)
            if s: scene.addLine(x, y+DIM_CASE, x+DIM_CASE, y+DIM_CASE, pen)
            if o: scene.addLine(x, y, x, y+DIM_CASE, pen)

    # joueur (bleu)
    jx = joueur_pos[1] * DIM_CASE
    jy = joueur_pos[0] * DIM_CASE
    scene.addRect(jx+4, jy+4, DIM_CASE-8, DIM_CASE-8,
                  QPen(Qt.NoPen), QBrush(QColor(50,100,255)))

    # sortie (vert)
    sx = sortie_pos[1] * DIM_CASE
    sy = sortie_pos[0] * DIM_CASE
    scene.addRect(sx+8, sy+8, DIM_CASE-16, DIM_CASE-16,
                  QPen(Qt.NoPen), QBrush(QColor(50,200,80)))

# --------- JEU ---------
class Fenetre(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setGeometry(100,100,DIM_FENETRE+4, DIM_FENETRE+4)
        self.setWindowTitle("Labyrinthe Jouable")

        # génération du labyrinthe
        self.laby = initialise_laby()
        target = DIM_LABY*DIM_LABY - 1
        ag = 0
        while ag < target:
            sel = select_cases(self.laby)
            agglomere_cases(sel, self.laby)
            ag += 1

        # positions
        self.joueur = [0, 0]  # ligne, colonne
        self.sortie = [DIM_LABY-1, DIM_LABY-1]

        # supprime un mur pour entrée/sortie
        self.laby[0][0][4] = False        # entrée à gauche
        self.laby[self.sortie[0]][self.sortie[1]][2] = False

        dessine_laby(self.scene, self.laby, self.joueur, self.sortie)

    # déplacements
    def keyPressEvent(self, e):
        l, c = self.joueur

        # directions
        if e.key() in (Qt.Key_Z, Qt.Key_Up):
            if not self.laby[l][c][NORD]:
                l -= 1
        if e.key() in (Qt.Key_S, Qt.Key_Down):
            if not self.laby[l][c][SUD]:
                l += 1
        if e.key() in (Qt.Key_D, Qt.Key_Right):
            if not self.laby[l][c][EST]:
                c += 1
        if e.key() in (Qt.Key_Q, Qt.Key_Left):
            if not self.laby[l][c][OUEST]:
                c -= 1

        # mise à jour joueur
        self.joueur = [l, c]
        dessine_laby(self.scene, self.laby, self.joueur, self.sortie)

        # victoire
        if self.joueur == self.sortie:
            msg = QMessageBox()
            msg.setWindowTitle("Victoire !")
            msg.setText("Tu as atteint la sortie ! Bien joué 👑🔥")
            msg.exec_()

# -------- MAIN --------
app = QApplication(sys.argv)
w = Fenetre()
w.show()
sys.exit(app.exec_())