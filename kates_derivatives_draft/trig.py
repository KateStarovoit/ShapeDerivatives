#Trig functons for one triangle

'''Input
a, b, c - n x 3 vertex positions
Ai - area of corresponding triangle
Output
sin for each angle'''
def find_sin(a, b, c, Ai):
    sina = (Ai)/(b*c)
    sinb = (Ai)/(a*c)
    sinc = (Ai)/(a*b)
    return sina, sinb, sinc


'''Input
a, b, c - n x 3 vertex positions
Ai - area of corresponding triangle
Output
cos for each angle'''
def find_cos(a, b, c):
    cosa = (- a * a + b * b + c * c) / (2 * b * c)
    cosb = (- b * b + a * a + c * c) / (2 * a * c)
    cosc = (- c * c + a * a + b * b) / (2 * a * b)
    return cosa, cosb, cosc


'''Input
a, b, c - n x 3 vertex positions
Ai - area of corresponding triangle
Output
cot for each angle'''
def find_cot(a, b, c, Ai):
    cota = (- a * a + b * b + c * c) / Ai
    cotb = (- b * b + a * a + c * c) / Ai
    cotc = (- c * c + a * a + b * b) / Ai
    return cota/4, cotb/4, cotc/4
