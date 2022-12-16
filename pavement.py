#!/usr/bin/python

from paver.easy import *
import paver.doctools
import os
import glob
import shutil
import sys

sys.path.append(os.path.dirname(__file__)) 

@task
def setup():
    sh('python -m pip install -U coverage')
    sh('python -m pip install -U pytest')
    pass


@task
def test():
    sh('python -m coverage run --source src --omit src/gui.py -m unittest discover -s test')
    sh('python -m coverage html')
    sh('python -m coverage report --show-missing')
    pass


@task
def clean():
    for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
    for pycache in glob.glob("*/__pycache__"): os.removedirs(pycache)
    for pycache in glob.glob("./__pycache__"): shutil.rmtree(pycache)
    try:
        shutil.rmtree(os.getcwd() + "/cover")
    except:
        pass
    pass


@task
@needs(['setup', 'test', 'clean'])
def default():
    pass


@task
def setup_game():
    sh('python -m pip install -U PySimpleGUI')


@task
@consume_args
@needs('setup_game')
def game(args):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'src')))
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'gui')))

    import gameoflife
    import gui

    cells = [eval(cell) for cell in args]

    life = gui.GUI(cells)
    life.create_live_cells_on_grid()
    life.start_GUI()


@task
def run():
    call_task('game', args = [(0, 0), (0, 1), (-1, 2), (1, 2), (0, 3),
        (0, 4), (0, 5), (0, 6), (-1, 7), (1, 7), (0, 8), (0, 9),
        (11, 0), (10, 1), (10, 2), (11, 3), (12, 1), (12, 2),
        (-1, -1), (-2, -2), (0, -3), (-1, -3), (-2, -3)])