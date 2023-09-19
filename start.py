from GUI import *
from board import *
from service_board import *
from ui import  *
from repo_board import *
if __name__ == "__main__":

    repo=RepoBoard()
    serv=ServiceBoard(repo)
    #UI = UserInterface(serv)
    #UI.menu()
    gui=GUI(serv)
    gui.menu()
