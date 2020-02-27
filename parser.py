from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname, "r")
    lines = file.readlines()
    i = 0
    for row in lines:
        i += 1
        row = row.strip('\n')
        if(row != "quit"):
            next = lines[i].strip('\n')

        if(row == "line"):
            nums = next.split(" ")
            add_edge(points, int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3]), int(nums[4]), int(nums[5]))

        elif(row == "ident"):
            ident(transform)

        elif(row == "scale"):
            nums = next.split(" ")
            scale = make_scale(int(nums[0]), int(nums[1]), int(nums[2]))
            matrix_mult(scale, transform)

        elif(row == "move"):
            nums = next.split(" ")
            translate = make_translate(int(nums[0]), int(nums[1]), int(nums[2]))
            matrix_mult(translate, transform)

        elif(row == "rotate"):
            nums = next.split(" ")
            if(nums[0] == "x"):
                rotate = make_rotX(nums[1])
            if(nums[0] == "y"):
                rotate = make_rotY(nums[1])
            if(nums[0] == "z"):
                rotate = make_rotZ(nums[1])
            matrix_mult(rotate, transform)

        elif(row == "apply"):
            matrix_mult(transform, points)

        elif(row == "display"):
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)

        elif(row == "save"):
            name = lines[i].strip("\n")
            clear_screen(screen)
            draw_lines(points, screen, color)
            #display(screen)
            save_ppm(screen, 'binary.ppm')
            save_ppm_ascii(screen, 'ascii.ppm')
            save_extension(screen, name)

        elif(row == "quit"):
            file.close()
