def build_pyramid(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * ( i * 2 + 1))
 

num_rows = 4
build_pyramid(num_rows)

#______*______ 1,
#_____***_____ 
#____*****____
#___*******___
#__*********__