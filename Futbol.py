from itertools import combinations
import random
from tkinter import *

def get_balanced_teams(players):
    teams = [list(), list()]
    team_len = int(len(players)/2)
    best_mmr = sum(x[1] for x in players)/2
    best_team = min(
        combinations(players, team_len),
        key=lambda team: abs(sum([m[1] for m in team])-best_mmr)
    )

    #randomize alpha/bravo
    t1 = random.randint(0, 1)
    t2 = 1 - t1

    for p in players:
        if p in best_team:
            teams[t1].append(p)
        else:
            teams[t2].append(p)

    return teams


def armar_equipos(jugadores, num_equipos):
    jugadores = sorted(jugadores, key=lambda x: (x[1], x[3]), reverse=True)
    equipos = [[] for i in range(num_equipos)]
    posiciones = {'portero': [], 'defensor': [], 'central': [], 'delantero': []}
    for jugador in jugadores:
        posiciones['delantero'].append(jugador)
    for posicion in posiciones:
        i = 0
        for jugador in posiciones[posicion]:
            equipos[i].append(jugador)
            i = (i + 1) % num_equipos
    return equipos

def mostrar_equipos():
    equipos = armar_equipos(jugadores, int(num_equipos_entry.get()))
    equipo1_str = "\n".join([jugador[0] for jugador in equipos[0]])
    equipo2_str = "\n".join([jugador[0] for jugador in equipos[1]])
    equipo1_label.config(text=equipo1_str)
    equipo2_label.config(text=equipo2_str)


#hacer csv con esto

jugadores = [["Moises Tobal", 85, "delantero", 25], ["Aldo Ferrari", 90, "delantero", 21], 
             ["Axel Carrera", 80, "delantero", 30], ["Guido", 75, "delantero", 23], 
             ["Marian", 80, "delantero", 29], ["Agustin", 70, "delantero", 27],
             ["Nico", 70, "central", 27], ["Nico S", 70, "central", 27],
             ["Martin Riccardi", 70, "central", 27], ["Victor", 70, "central", 27],
             ["Martin Iaumundo", 70, "defensor", 27], ["Andy Pace", 70, "defensor", 27],
             ["Kike", 70, "defensor", 27], ["Fede", 70, "defensor", 27], ["Conti", 70, "defensor", 27],
             ["Benja", 70, "defensor", 27]]

equipos = get_balanced_teams(jugadores)
oscuro = equipos[0]
claro = equipos[1]

print("claro : " + equipos[1])
print("oscuro : " + equipos[0])
root = Tk()
root.title("Armar equipos de fútbol")

# falta opcion de ingresar los jugadores que van al partido y despues aplicar la funcion de get_balanced_teams

num_equipos_label = Label(root, text="Número de equipos:")
num_equipos_entry = Entry(root)
armar_equipos_button = Button(root, text="Armar equipos", command=mostrar_equipos)
equipo1_label = Label(root, text="Equipo 1:")
equipo2_label = Label(root, text="Equipo 2:")

num_equipos_label.grid(row=0, column=0)
num_equipos_entry.grid(row=0, column=1)
armar_equipos_button.grid(row=1, column=0)
equipo1_label.grid(row=2, column=0)
equipo2_label.grid(row=3, column=0)

root.mainloop()
Footer

