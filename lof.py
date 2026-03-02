from pyscript import document, display


def get_lof(e):
    document.getElementById("get_lof").innerHTML = ""
    players = ["Agudo", "Al Hazmi", "Alaiza", "Banaag", "Barcelona", "Brion", "Buo", "Castro", "Cruz",
                    "Del Prado", "Entrada", "Francisco", "Gavina", "Goyenechea", "Guevarra", "Haberia",
                    "Janayan", "Libutan", "Lubo", "Manuel", "Mariposque", "Pagtalunan", "Reyes", "Singh",
                    "Subaan", "Tan", "Vargas", "Zaldivar"]

    for i in players:
        display(i, target="get_lof")
        