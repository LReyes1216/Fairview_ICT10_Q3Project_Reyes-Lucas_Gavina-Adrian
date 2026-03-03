from pyscript import document, display

#To initiate the function
def get_lof(e):
    #This clears the field
    document.getElementById("get_lof").innerHTML = ""

    #These are the list of players
    players = ["Agudo", "Al Hazmi", "Alaiza", "Banaag", "Barcelona", "Brion", "Buo", "Castro", "Cruz",
                    "Del Prado", "Entrada", "Francisco", "Gavina", "Goyenechea", "Guevarra", "Haberia",
                    "Janayan", "Libutan", "Lubo", "Manuel", "Mariposque", "Pagtalunan", "Reyes", "Singh",
                    "Subaan", "Tan", "Vargas", "Zaldivar"]

    #We used for loop instead of while so it doesn't go on infinitely, and it is more convenient if you want to display all names individually.
    for i in players:
        display(i, target="get_lof")
        
