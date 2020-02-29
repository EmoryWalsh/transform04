from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 0, 0 ]
edges = []
transform = new_matrix()
transfrom = ident(transform)

parse_file( 'script', edges, transform, screen, color )
