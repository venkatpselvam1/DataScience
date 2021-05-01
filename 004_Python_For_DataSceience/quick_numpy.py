# Define list
height_in = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 74, 74, 69, 70, 73, 75, 78, 79, 76, 74, 76, 72, 71, 75, 77, 74, 73, 74, 78, 73, 75, 73, 75, 75, 74, 69, 71, 74, 73, 73, 76, 74, 74, 70, 72, 77, 74, 70, 73, 75, 76, 76, 78, 74, 74, 76, 77, 81, 78, 75, 77, 75, 76, 74, 72, 72, 75, 73, 73, 73, 70, 70, 70, 76, 68, 71, 72, 75, 75, 75, 75, 68, 74, 78, 71, 73, 76, 74, 74, 79, 75, 73, 76, 74, 74, 73, 72, 74, 73, 74, 72, 73, 69, 72, 73, 75, 75, 73, 72, 72, 76, 74, 72, 77, 74, 77, 75, 76, 80, 74, 74, 75, 78, 73, 73, 74, 75, 76, 71, 73, 74, 76, 76, 74, 73, 74, 70, 72, 73, 73, 73, 73, 71, 74, 74, 72, 74, 71, 74, 73, 75, 75, 79, 73, 75, 76, 74, 76, 78, 74, 76, 72, 74, 76, 74, 75, 78, 75, 72, 74, 72, 74, 70, 71, 70, 75, 71, 71, 73, 72, 71, 73, 72, 75, 74, 74, 75, 73, 77, 73, 76, 75, 74, 76, 75, 73, 71, 76, 75, 72, 71, 77, 73, 74, 71, 72, 74, 75, 73, 72, 75, 75, 74, 72, 74, 71, 70, 74, 77, 77, 75, 75, 78, 75, 76, 73, 75, 75, 79, 77, 76, 71, 75, 74, 69, 71, 76, 72, 72, 70, 72, 73, 71, 72, 71, 73, 72, 73, 74, 74, 72, 75, 74, 74, 77, 75, 73, 72, 71, 74, 77, 75, 75, 75, 78, 78, 74, 76, 78, 76, 70, 72, 80, 74, 74, 71, 70, 72, 71, 74, 71, 72, 71, 74, 69, 76, 75, 75, 76, 73, 76, 73, 77, 73, 72, 72, 77, 77, 71, 74, 74, 73, 78, 75, 73, 70, 74, 72, 73, 73, 75, 75, 74, 76, 73, 74, 75, 75, 72, 73, 73, 72, 74, 78, 76, 73, 74, 75, 70, 75, 71, 72, 78, 75, 73, 73, 71, 75, 77, 72, 69, 73, 74, 72, 70, 75, 70, 72, 72, 74, 73, 74, 76, 75, 80, 72, 75, 73, 74, 74, 73, 75, 75, 71, 73, 75, 74, 74, 72, 74, 74, 74, 73, 76, 75, 72, 73, 73, 73, 72, 72, 72, 72, 71, 75, 75, 74, 73, 75, 79, 74, 76, 73, 74, 74, 72, 74, 74, 75, 78, 74, 74, 74, 77, 70, 73, 74, 73, 71, 75, 71, 72, 77, 74, 70, 77, 73, 72, 76, 71, 76, 78, 75, 73, 78, 74, 79, 75, 76, 72, 75, 75, 70, 72, 70, 74, 71, 76, 73, 76, 71, 69, 72, 72, 69, 73, 69, 73, 74, 74, 72, 71, 72, 72, 76, 76, 76, 74, 76, 75, 71, 72, 71, 73, 75, 76, 75, 71, 75, 74, 72, 73, 73, 73, 73, 76, 72, 76, 73, 73, 73, 75, 75, 77, 73, 72, 75, 70, 74, 72, 80, 71, 71, 74, 74, 73, 75, 76, 73, 77, 72, 73, 77, 76, 71, 75, 73, 74, 77, 71, 72, 73, 69, 73, 70, 74, 76, 73, 73, 75, 73, 79, 74, 73, 74, 77, 75, 74, 73, 77, 73, 77, 74, 74, 73, 77, 74, 77, 75, 77, 75, 71, 74, 70, 79, 72, 72, 70, 74, 74, 72, 73, 72, 74, 74, 76, 82, 74, 74, 70, 73, 73, 74, 77, 72, 76, 73, 73, 72, 74, 74, 71, 72, 75, 74, 74, 77, 70, 71, 73, 76, 71, 75, 74, 72, 76, 79, 76, 73, 76, 78, 75, 76, 72, 72, 73, 73, 75, 71, 76, 70, 75, 74, 75, 73, 71, 71, 72, 73, 73, 72, 69, 73, 78, 71, 73, 75, 76, 70, 74, 77, 75, 79, 72, 77, 73, 75, 75, 75, 73, 73, 76, 77, 75, 70, 71, 71, 75, 74, 69, 70, 75, 72, 75, 73, 72, 72, 72, 76, 75, 74, 69, 73, 72, 72, 75, 77, 76, 80, 77, 76, 79, 71, 75, 73, 76, 77, 73, 76, 70, 75, 73, 75, 70, 69, 71, 72, 72, 73, 70, 70, 73, 76, 75, 72, 73, 79, 71, 72, 74, 74, 74, 72, 76, 76, 72, 72, 71, 72, 72, 70, 77, 74, 72, 76, 71, 76, 71, 73, 70, 73, 73, 72, 71, 71, 71, 72, 72, 74, 74, 74, 71, 72, 75, 72, 71, 72, 72, 72, 72, 74, 74, 77, 75, 73, 75, 73, 76, 72, 77, 75, 72, 71, 71, 75, 72, 73, 73, 71, 70, 75, 71, 76, 73, 68, 71, 72, 74, 77, 72, 76, 78, 81, 72, 73, 76, 72, 72, 74, 76, 73, 76, 75, 70, 71, 74, 72, 73, 76, 76, 73, 71, 68, 71, 71, 74, 77, 69, 72, 76, 75, 76, 75, 76, 72, 74, 76, 74, 72, 75, 78, 77, 70, 72, 79, 74, 71, 68, 77, 75, 71, 72, 70, 72, 72, 73, 72, 74, 72, 72, 75, 72, 73, 74, 72, 78, 75, 72, 74, 75, 75, 76, 74, 74, 73, 74, 71, 74, 75, 76, 74, 76, 76, 73, 75, 75, 74, 68, 72, 75, 71, 70, 72, 73, 72, 75, 74, 70, 76, 71, 82, 72, 73, 74, 71, 75, 77, 72, 74, 72, 73, 78, 77, 73, 73, 73, 73, 73, 76, 75, 70, 73, 72, 73, 75, 74, 73, 73, 76, 73, 75, 70, 77, 72, 77, 74, 75, 75, 75, 75, 72, 74, 71, 76, 71, 75, 76, 83, 75, 74, 76, 72, 72, 75, 75, 72, 77, 73, 72, 70, 74, 72, 74, 72, 71, 70, 71, 76, 74, 76, 74, 74, 74, 75, 75, 71, 71, 74, 77, 71, 74, 75, 77, 76, 74, 76, 72, 71, 72, 75, 73, 68, 72, 69, 73, 73, 75, 70, 70, 74, 75, 74, 74, 73, 74, 75, 77, 73, 74, 76, 74, 75, 73, 76, 78, 75, 73, 77, 74, 72, 74, 72, 71, 73, 75, 73, 67, 67, 76, 74, 73, 70, 75, 70, 72, 77, 79, 78, 74, 75, 75, 78, 76, 75, 69, 75, 72, 75, 73, 74, 75, 75, 73]
import numpy as np
height = np.array(height_in)
#print(height)
print(str(len(height))+" "+str(height.size)+" ")
print(height.shape)
print(height.min())
print(height.max())
print(height.mean())
weights_lb = [180, 215, 210, 210, 188, 176, 209, 200, 231, 180, 188, 180, 185, 160, 180, 185, 189, 185, 219, 230, 205, 230, 195, 180, 192, 225, 203, 195, 182, 188, 200, 180, 200, 200, 245, 240, 215, 185, 175, 199, 200, 215, 200, 205, 206, 186, 188, 220, 210, 195, 200, 200, 212, 224, 210, 205, 220, 195, 200, 260, 228, 270, 200, 210, 190, 220, 180, 205, 210, 220, 211, 200, 180, 190, 170, 230, 155, 185, 185, 200, 225, 225, 220, 160, 205, 235, 250, 210, 190, 160, 200, 205, 222, 195, 205, 220, 220, 170, 185, 195, 220, 230, 180, 220, 180, 180, 170, 210, 215, 200, 213, 180, 192, 235, 185, 235, 210, 222, 210, 230, 220, 180, 190, 200, 210, 194, 180, 190, 240, 200, 198, 200, 195, 210, 220, 190, 210, 225, 180, 185, 170, 185, 185, 180, 178, 175, 200, 204, 211, 190, 210, 190, 190, 185, 290, 175, 185, 200, 220, 170, 220, 190, 220, 205, 200, 250, 225, 215, 210, 215, 195, 200, 194, 220, 180, 180, 170, 195, 180, 170, 206, 205, 200, 225, 201, 225, 233, 180, 225, 180, 220, 180, 237, 215, 190, 235, 190, 180, 165, 195, 200, 190, 190, 185, 185, 205, 190, 205, 206, 220, 208, 170, 195, 210, 190, 211, 230, 170, 185, 185, 241, 225, 210, 175, 230, 200, 215, 198, 226, 278, 215, 230, 240, 184, 219, 170, 218, 190, 225, 220, 176, 190, 197, 204, 167, 180, 195, 220, 215, 185, 190, 205, 205, 200, 210, 215, 200, 205, 211, 190, 208, 200, 210, 232, 230, 210, 220, 210, 202, 212, 225, 170, 190, 200, 237, 220, 170, 193, 190, 150, 220, 200, 190, 185, 185, 200, 172, 220, 225, 190, 195, 219, 190, 197, 200, 195, 210, 177, 220, 235, 180, 195, 195, 190, 230, 190, 200, 190, 190, 200, 200, 184, 200, 180, 219, 187, 200, 220, 205, 190, 170, 160, 215, 175, 205, 200, 214, 200, 190, 180, 205, 220, 190, 215, 235, 191, 200, 181, 200, 210, 240, 185, 165, 190, 185, 175, 155, 210, 170, 175, 220, 210, 205, 200, 205, 195, 240, 150, 200, 215, 202, 200, 190, 205, 190, 160, 215, 185, 200, 190, 210, 185, 220, 190, 202, 205, 220, 175, 160, 190, 200, 229, 206, 220, 180, 195, 175, 188, 230, 190, 200, 190, 219, 235, 180, 180, 180, 200, 234, 185, 220, 223, 200, 210, 200, 210, 190, 177, 227, 180, 195, 199, 175, 185, 240, 210, 180, 194, 225, 180, 205, 193, 230, 230, 220, 200, 249, 190, 208, 245, 250, 160, 192, 220, 170, 197, 155, 190, 200, 220, 210, 228, 190, 160, 184, 180, 180, 200, 176, 160, 222, 211, 195, 200, 175, 206, 240, 185, 260, 185, 221, 205, 200, 170, 201, 205, 185, 205, 245, 220, 210, 220, 185, 175, 170, 180, 200, 210, 175, 220, 206, 180, 210, 195, 200, 200, 164, 180, 220, 195, 205, 170, 240, 210, 195, 200, 205, 192, 190, 170, 240, 200, 205, 175, 250, 220, 224, 210, 195, 180, 245, 175, 180, 215, 175, 180, 195, 230, 230, 205, 215, 195, 180, 205, 180, 190, 180, 190, 190, 220, 210, 255, 190, 230, 200, 205, 210, 225, 215, 220, 205, 200, 220, 197, 225, 187, 245, 185, 185, 175, 200, 180, 188, 225, 200, 210, 245, 213, 231, 165, 228, 210, 250, 191, 190, 200, 215, 254, 232, 180, 215, 220, 180, 200, 170, 195, 210, 200, 220, 165, 180, 200, 200, 170, 224, 220, 180, 198, 240, 239, 185, 210, 220, 200, 195, 220, 230, 170, 220, 230, 165, 205, 192, 210, 205, 200, 210, 185, 195, 202, 205, 195, 180, 200, 185, 240, 185, 220, 205, 205, 180, 201, 190, 208, 240, 180, 230, 195, 215, 190, 195, 215, 215, 220, 220, 230, 195, 190, 195, 209, 204, 170, 185, 205, 175, 210, 190, 180, 180, 160, 235, 200, 210, 180, 190, 197, 203, 205, 170, 200, 250, 200, 220, 200, 190, 170, 190, 220, 215, 206, 215, 185, 235, 188, 230, 195, 168, 190, 160, 200, 200, 189, 180, 190, 200, 220, 187, 240, 190, 180, 185, 210, 220, 219, 190, 193, 175, 180, 215, 210, 200, 190, 185, 220, 170, 195, 205, 195, 210, 190, 190, 180, 220, 190, 186, 185, 190, 180, 190, 170, 210, 240, 220, 180, 210, 210, 195, 160, 180, 205, 200, 185, 245, 190, 210, 200, 200, 222, 215, 240, 170, 220, 156, 190, 202, 221, 200, 190, 210, 190, 200, 165, 190, 185, 230, 208, 209, 175, 180, 200, 205, 200, 250, 210, 230, 244, 202, 240, 200, 215, 177, 210, 170, 215, 217, 198, 200, 220, 170, 200, 230, 231, 183, 192, 167, 190, 180, 180, 215, 160, 205, 223, 175, 170, 190, 240, 175, 230, 223, 196, 167, 195, 190, 250, 190, 190, 190, 170, 160, 150, 225, 220, 209, 210, 176, 260, 195, 190, 184, 180, 195, 195, 219, 225, 212, 202, 185, 200, 209, 200, 195, 228, 210, 190, 212, 190, 218, 220, 190, 235, 210, 200, 188, 210, 235, 188, 215, 216, 220, 180, 185, 200, 210, 220, 185, 231, 210, 195, 200, 205, 200, 190, 250, 185, 180, 170, 180, 208, 235, 215, 244, 220, 185, 230, 190, 200, 180, 190, 196, 180, 230, 224, 160, 178, 205, 185, 210, 180, 190, 200, 257, 190, 220, 165, 205, 200, 208, 185, 215, 170, 235, 210, 170, 180, 170, 190, 150, 230, 203, 260, 246, 186, 210, 198, 210, 215, 180, 200, 245, 200, 192, 192, 200, 192, 205, 190, 186, 170, 197, 219, 200, 220, 207, 225, 207, 212, 225, 170, 190, 210, 230, 210, 200, 238, 234, 222, 200, 190, 170, 220, 223, 210, 215, 196, 175, 175, 189, 205, 210, 180, 180, 197, 220, 228, 190, 204, 165, 216, 220, 208, 210, 215, 195, 200, 215, 229, 240, 207, 205, 208, 185, 190, 170, 208, 225, 190, 225, 185, 180, 165, 240, 220, 212, 163, 215, 175, 205, 210, 205, 208, 215, 180, 200, 230, 211, 230, 190, 220, 180, 205, 190, 180, 205, 190, 195]
weight = np.array(weights_lb) * 0.453592
height_1=height*0.0254
print(weight)
print(height_1)
bmi=weight/(height_1**2)
print(bmi)
print(bmi[0])
print(bmi[:5])
print(bmi[-5:])
print(bmi<21)
print(bmi[bmi<21])
under_weight=bmi[bmi<21]
print(under_weight)
print(under_weight.size)

import numpy as np

# list of height and weight of the players.
players = [(74, 180), (74, 215), (72, 210), (72, 210), (73, 188), (69, 176), (69, 209), (71, 200), (76, 231), (71, 180), (73, 188), (73, 180), (74, 185), (74, 160), (69, 180), (70, 185), (73, 189), (75, 185), (78, 219), (79, 230), (76, 205), (74, 230), (76, 195), (72, 180), (71, 192), (75, 225), (77, 203), (74, 195), (73, 182), (74, 188), (78, 200), (73, 180), (75, 200), (73, 200), (75, 245), (75, 240), (74, 215), (69, 185), (71, 175), (74, 199), (73, 200), (73, 215), (76, 200), (74, 205), (74, 206), (70, 186), (72, 188), (77, 220), (74, 210), (70, 195), (73, 200), (75, 200), (76, 212), (76, 224), (78, 210), (74, 205), (74, 220), (76, 195), (77, 200), (81, 260), (78, 228), (75, 270), (77, 200), (75, 210), (76, 190), (74, 220), (72, 180), (72, 205), (75, 210), (73, 220), (73, 211), (73, 200), (70, 180), (70, 190), (70, 170), (76, 230), (68, 155), (71, 185), (72, 185), (75, 200), (75, 225), (75, 225), (75, 220), (68, 160), (74, 205), (78, 235), (71, 250), (73, 210), (76, 190), (74, 160), (74, 200), (79, 205), (75, 222), (73, 195), (76, 205), (74, 220), (74, 220), (73, 170), (72, 185), (74, 195), (73, 220), (74, 230), (72, 180), (73, 220), (69, 180), (72, 180), (73, 170), (75, 210), (75, 215), (73, 200), (72, 213), (72, 180), (76, 192), (74, 235), (72, 185), (77, 235), (74, 210), (77, 222), (75, 210), (76, 230), (80, 220), (74, 180), (74, 190), (75, 200), (78, 210), (73, 194), (73, 180), (74, 190), (75, 240), (76, 200), (71, 198), (73, 200), (74, 195), (76, 210), (76, 220), (74, 190), (73, 210), (74, 225), (70, 180), (72, 185), (73, 170), (73, 185), (73, 185), (73, 180), (71, 178), (74, 175), (74, 200), (72, 204), (74, 211), (71, 190), (74, 210), (73, 190), (75, 190), (75, 185), (79, 290), (73, 175), (75, 185), (76, 200), (74, 220), (76, 170), (78, 220), (74, 190), (76, 220), (72, 205), (74, 200), (76, 250), (74, 225), (75, 215), (78, 210), (75, 215), (72, 195), (74, 200), (72, 194), (74, 220), (70, 180), (71, 180), (70, 170), (75, 195), (71, 180), (71, 170), (73, 206), (72, 205), (71, 200), (73, 225), (72, 201), (75, 225), (74, 233), (74, 180), (75, 225), (73, 180), (77, 220), (73, 180), (76, 237), (75, 215), (74, 190), (76, 235), (75, 190), (73, 180), (71, 165), (76, 195), (75, 200), (72, 190), (71, 190), (77, 185), (73, 185), (74, 205), (71, 190), (72, 205), (74, 206), (75, 220), (73, 208), (72, 170), (75, 195), (75, 210), (74, 190), (72, 211), (74, 230), (71, 170), (70, 185), (74, 185), (77, 241), (77, 225), (75, 210), (75, 175), (78, 230), (75, 200), (76, 215), (73, 198), (75, 226), (75, 278), (79, 215), (77, 230), (76, 240), (71, 184), (75, 219), (74, 170), (69, 218), (71, 190), (76, 225), (72, 220), (72, 176), (70, 190), (72, 197), (73, 204), (71, 167), (72, 180), (71, 195), (73, 220), (72, 215), (73, 185), (74, 190), (74, 205), (72, 205), (75, 200), (74, 210), (74, 215), (77, 200), (75, 205), (73, 211), (72, 190), (71, 208), (74, 200), (77, 210), (75, 232), (75, 230), (75, 210), (78, 220), (78, 210), (74, 202), (76, 212), (78, 225), (76, 170), (70, 190), (72, 200), (80, 237), (74, 220), (74, 170), (71, 193), (70, 190), (72, 150), (71, 220), (74, 200), (71, 190), (72, 185), (71, 185), (74, 200), (69, 172), (76, 220), (75, 225), (75, 190), (76, 195), (73, 219), (76, 190), (73, 197), (77, 200), (73, 195), (72, 210), (72, 177), (77, 220), (77, 235), (71, 180), (74, 195), (74, 195), (73, 190), (78, 230), (75, 190), (73, 200), (70, 190), (74, 190), (72, 200), (73, 200), (73, 184), (75, 200), (75, 180), (74, 219), (76, 187), (73, 200), (74, 220), (75, 205), (75, 190), (72, 170), (73, 160), (73, 215), (72, 175), (74, 205), (78, 200), (76, 214), (73, 200), (74, 190), (75, 180), (70, 205), (75, 220), (71, 190), (72, 215), (78, 235), (75, 191), (73, 200), (73, 181), (71, 200), (75, 210), (77, 240), (72, 185), (69, 165), (73, 190), (74, 185), (72, 175), (70, 155), (75, 210), (70, 170), (72, 175), (72, 220), (74, 210), (73, 205), (74, 200), (76, 205), (75, 195), (80, 240), (72, 150), (75, 200), (73, 215), (74, 202), (74, 200), (73, 190), (75, 205), (75, 190), (71, 160), (73, 215), (75, 185), (74, 200), (74, 190), (72, 210), (74, 185), (74, 220), (74, 190), (73, 202), (76, 205), (75, 220), (72, 175), (73, 160), (73, 190), (73, 200), (72, 229), (72, 206), (72, 220), (72, 180), (71, 195), (75, 175), (75, 188), (74, 230), (73, 190), (75, 200), (79, 190), (74, 219), (76, 235), (73, 180), (74, 180), (74, 180), (72, 200), (74, 234), (74, 185), (75, 220), (78, 223), (74, 200), (74, 210), (74, 200), (77, 210), (70, 190), (73, 177), (74, 227), (73, 180), (71, 195), (75, 199), (71, 175), (72, 185), (77, 240), (74, 210), (70, 180), (77, 194), (73, 225), (72, 180), (76, 205), (71, 193), (76, 230), (78, 230), (75, 220), (73, 200), (78, 249), (74, 190), (79, 208), (75, 245), (76, 250), (72, 160), (75, 192), (75, 220), (70, 170), (72, 197), (70, 155), (74, 190), (71, 200), (76, 220), (73, 210), (76, 228), (71, 190), (69, 160), (72, 184), (72, 180), (69, 180), (73, 200), (69, 176), (73, 160), (74, 222), (74, 211), (72, 195), (71, 200), (72, 175), (72, 206), (76, 240), (76, 185), (76, 260), (74, 185), (76, 221), (75, 205), (71, 200), (72, 170), (71, 201), (73, 205), (75, 185), (76, 205), (75, 245), (71, 220), (75, 210), (74, 220), (72, 185), (73, 175), (73, 170), (73, 180), (73, 200), (76, 210), (72, 175), (76, 220), (73, 206), (73, 180), (73, 210), (75, 195), (75, 200), (77, 200), (73, 164), (72, 180), (75, 220), (70, 195), (74, 205), (72, 170), (80, 240), (71, 210), (71, 195), (74, 200), (74, 205), (73, 192), (75, 190), (76, 170), (73, 240), (77, 200), (72, 205), (73, 175), (77, 250), (76, 220), (71, 224), (75, 210), (73, 195), (74, 180), (77, 245), (71, 175), (72, 180), (73, 215), (69, 175), (73, 180), (70, 195), (74, 230), (76, 230), (73, 205), (73, 215), (75, 195), (73, 180), (79, 205), (74, 180), (73, 190), (74, 180), (77, 190), (75, 190), (74, 220), (73, 210), (77, 255), (73, 190), (77, 230), (74, 200), (74, 205), (73, 210), (77, 225), (74, 215), (77, 220), (75, 205), (77, 200), (75, 220), (71, 197), (74, 225), (70, 187), (79, 245), (72, 185), (72, 185), (70, 175), (74, 200), (74, 180), (72, 188), (73, 225), (72, 200), (74, 210), (74, 245), (76, 213), (82, 231), (74, 165), (74, 228), (70, 210), (73, 250), (73, 191), (74, 190), (77, 200), (72, 215), (76, 254), (73, 232), (73, 180), (72, 215), (74, 220), (74, 180), (71, 200), (72, 170), (75, 195), (74, 210), (74, 200), (77, 220), (70, 165), (71, 180), (73, 200), (76, 200), (71, 170), (75, 224), (74, 220), (72, 180), (76, 198), (79, 240), (76, 239), (73, 185), (76, 210), (78, 220), (75, 200), (76, 195), (72, 220), (72, 230), (73, 170), (73, 220), (75, 230), (71, 165), (76, 205), (70, 192), (75, 210), (74, 205), (75, 200), (73, 210), (71, 185), (71, 195), (72, 202), (73, 205), (73, 195), (72, 180), (69, 200), (73, 185), (78, 240), (71, 185), (73, 220), (75, 205), (76, 205), (70, 180), (74, 201), (77, 190), (75, 208), (79, 240), (72, 180), (77, 230), (73, 195), (75, 215), (75, 190), (75, 195), (73, 215), (73, 215), (76, 220), (77, 220), (75, 230), (70, 195), (71, 190), (71, 195), (75, 209), (74, 204), (69, 170), (70, 185), (75, 205), (72, 175), (75, 210), (73, 190), (72, 180), (72, 180), (72, 160), (76, 235), (75, 200), (74, 210), (69, 180), (73, 190), (72, 197), (72, 203), (75, 205), (77, 170), (76, 200), (80, 250), (77, 200), (76, 220), (79, 200), (71, 190), (75, 170), (73, 190), (76, 220), (77, 215), (73, 206), (76, 215), (70, 185), (75, 235), (73, 188), (75, 230), (70, 195), (69, 168), (71, 190), (72, 160), (72, 200), (73, 200), (70, 189), (70, 180), (73, 190), (76, 200), (75, 220), (72, 187), (73, 240), (79, 190), (71, 180), (72, 185), (74, 210), (74, 220), (74, 219), (72, 190), (76, 193), (76, 175), (72, 180), (72, 215), (71, 210), (72, 200), (72, 190), (70, 185), (77, 220), (74, 170), (72, 195), (76, 205), (71, 195), (76, 210), (71, 190), (73, 190), (70, 180), (73, 220), (73, 190), (72, 186), (71, 185), (71, 190), (71, 180), (72, 190), (72, 170), (74, 210), (74, 240), (74, 220), (71, 180), (72, 210), (75, 210), (72, 195), (71, 160), (72, 180), (72, 205), (72, 200), (72, 185), (74, 245), (74, 190), (77, 210), (75, 200), (73, 200), (75, 222), (73, 215), (76, 240), (72, 170), (77, 220), (75, 156), (72, 190), (71, 202), (71, 221), (75, 200), (72, 190), (73, 210), (73, 190), (71, 200), (70, 165), (75, 190), (71, 185), (76, 230), (73, 208), (68, 209), (71, 175), (72, 180), (74, 200), (77, 205), (72, 200), (76, 250), (78, 210), (81, 230), (72, 244), (73, 202), (76, 240), (72, 200), (72, 215), (74, 177), (76, 210), (73, 170), (76, 215), (75, 217), (70, 198), (71, 200), (74, 220), (72, 170), (73, 200), (76, 230), (76, 231), (73, 183), (71, 192), (68, 167), (71, 190), (71, 180), (74, 180), (77, 215), (69, 160), (72, 205), (76, 223), (75, 175), (76, 170), (75, 190), (76, 240), (72, 175), (74, 230), (76, 223), (74, 196), (72, 167), (75, 195), (78, 190), (77, 250), (70, 190), (72, 190), (79, 190), (74, 170), (71, 160), (68, 150), (77, 225), (75, 220), (71, 209), (72, 210), (70, 176), (72, 260), (72, 195), (73, 190), (72, 184), (74, 180), (72, 195), (72, 195), (75, 219), (72, 225), (73, 212), (74, 202), (72, 185), (78, 200), (75, 209), (72, 200), (74, 195), (75, 228), (75, 210), (76, 190), (74, 212), (74, 190), (73, 218), (74, 220), (71, 190), (74, 235), (75, 210), (76, 200), (74, 188), (76, 210), (76, 235), (73, 188), (75, 215), (75, 216), (74, 220), (68, 180), (72, 185), (75, 200), (71, 210), (70, 220), (72, 185), (73, 231), (72, 210), (75, 195), (74, 200), (70, 205), (76, 200), (71, 190), (82, 250), (72, 185), (73, 180), (74, 170), (71, 180), (75, 208), (77, 235), (72, 215), (74, 244), (72, 220), (73, 185), (78, 230), (77, 190), (73, 200), (73, 180), (73, 190), (73, 196), (73, 180), (76, 230), (75, 224), (70, 160), (73, 178), (72, 205), (73, 185), (75, 210), (74, 180), (73, 190), (73, 200), (76, 257), (73, 190), (75, 220), (70, 165), (77, 205), (72, 200), (77, 208), (74, 185), (75, 215), (75, 170), (75, 235), (75, 210), (72, 170), (74, 180), (71, 170), (76, 190), (71, 150), (75, 230), (76, 203), (83, 260), (75, 246), (74, 186), (76, 210), (72, 198), (72, 210), (75, 215), (75, 180), (72, 200), (77, 245), (73, 200), (72, 192), (70, 192), (74, 200), (72, 192), (74, 205), (72, 190), (71, 186), (70, 170), (71, 197), (76, 219), (74, 200), (76, 220), (74, 207), (74, 225), (74, 207), (75, 212), (75, 225), (71, 170), (71, 190), (74, 210), (77, 230), (71, 210), (74, 200), (75, 238), (77, 234), (76, 222), (74, 200), (76, 190), (72, 170), (71, 220), (72, 223), (75, 210), (73, 215), (68, 196), (72, 175), (69, 175), (73, 189), (73, 205), (75, 210), (70, 180), (70, 180), (74, 197), (75, 220), (74, 228), (74, 190), (73, 204), (74, 165), (75, 216), (77, 220), (73, 208), (74, 210), (76, 215), (74, 195), (75, 200), (73, 215), (76, 229), (78, 240), (75, 207), (73, 205), (77, 208), (74, 185), (72, 190), (74, 170), (72, 208), (71, 225), (73, 190), (75, 225), (73, 185), (67, 180), (67, 165), (76, 240), (74, 220), (73, 212), (70, 163), (75, 215), (70, 175), (72, 205), (77, 210), (79, 205), (78, 208), (74, 215), (75, 180), (75, 200), (78, 230), (76, 211), (75, 230), (69, 190), (75, 220), (72, 180), (75, 205), (73, 190), (74, 180), (75, 205), (75, 190), (73, 195)]
np_players = np.array(players)
print(type(np_players))
print(np_players.ndim)
print(np_players.dtype)
print(np_players.itemsize)
print(np_players.shape)
print(np_players.size)
print(len(np_players))
print(np_players[0])
a = np_players+[1,10]
print(a[0])
b = np_players*[1,10]
print(b[0])
players_converted = np_players * [0.0254, 0.453592]
print(players_converted[0])
print(players_converted[0][1])

print(players_converted)
print(players_converted.shape)
print(players_converted[:,0])
print(players_converted[:,0]>1.8)
height_players=players_converted[players_converted[:,0]>1.8]
print(height_players.shape)

skills = np.array(['Keeper', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Bowler', 'Bowler', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Keeper', 'Keeper', 'Keeper', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Keeper', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Bowler', 'Bowler', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper', 'Batsman', 'Keeper', 'Bowler', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Bowler', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Batsman', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Bowler', 'Bowler', 'Bowler', 'Batsman', 'Keeper', 'Bowler', 'Bowler', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Batsman', 'Bowler', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper', 'Keeper', 'Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Batsman', 'Bowler', 'Keeper', 'Keeper', 'Batsman', 'Bowler', 'Bowler', 'Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Bowler', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Batsman', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Batsman', 'Batsman', 'Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Keeper', 'Bowler', 'Keeper', 'Bowler', 'Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Batsman', 'Keeper', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Batsman', 'Bowler', 'Keeper', 'Bowler', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Bowler', 'Bowler', 'Bowler', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Batsman', 'Bowler', 'Keeper', 'Bowler', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Batsman', 'Batsman', 'Keeper', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Bowler', 'Batsman', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Bowler', 'Bowler', 'Keeper', 'Bowler', 'Keeper', 'Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Bowler', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Batsman', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Keeper', 'Bowler', 'Bowler', 'Keeper', 'Bowler', 'Bowler', 'Keeper', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Keeper-Batsman', 'Keeper-Batsman', 'Bowler', 'Bowler', 'Bowler', 'Batsman', 'Bowler', 'Keeper-Batsman', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper', 'Keeper-Batsman', 'Batsman', 'Bowler', 'Keeper-Batsman'])
#skills
print(skills)
print(skills == "Keeper")
print(players_converted[skills == "Batsman"])
print(players_converted[skills == "Batsman"][:,0].shape)
