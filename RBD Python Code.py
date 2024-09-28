#Debugged character limit

word = input("Enter sentence:")


val=-10


def new_line(val):
    return("G90 X0 Y" + str(val))
    
def a():
    return("""G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def b():
    return("""G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def c():
     return("""
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def d():
     return("""
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def e():
     return("""
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def f():
     return("""
G91 X2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def g():
     return("""
G91 Y-5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def h():
     return("""
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def i():
     return("""
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def j():
     return("""
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def k():
     return("""
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def l():
     return("""
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def m():
     return("""
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")


def n():
     return("""
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def o():
     return("""
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def p():
     return("""
G91 X2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def q():
     return("""
G91 X2.5 Y-5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def r():
     return("""
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def s():
     return("""
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def t():
     return("""
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5 Y-5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def u():
     return("""
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G91 X3.5 Y5;""")


def v():
     return("""
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G91 X3.5 Y5;""")

def w():
     return("""
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G91 X3.5 Y5;""")

def x():
     return("""
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G91 X3.5 Y5;""")

def y():
     return("""
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5 Y-2.5;
G91 X3.5 Y5;""")


def z():
     return("""
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5 Y-2.5;
G91 X3.5 Y5;""")

def space():
     return("""
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def full_stop():
     return("""
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G91 X3.5 Y5;""")

def comma():
     return("""
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5""")

def semicolon():
     return("""
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def colon():
     return("""
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5 Y-5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def question_mark():
     return(""" 
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G91 X3.5 Y5;""")

def exclamation_point():
     return("""
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X3.5 Y5;""")

def upper_case():
     return("""G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5;
G90 Z-33;
G91 X3.5 Y5;""")

def number():
    return("""G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 Y-2.5;
G90 Z-33;
G90 Z-35.5;
G90 Z-33;
G91 X2.5 Y-2.5;
G91 X3.5 Y5;""")

letter_to_gcode = {
    "a": a(),
    "b": b(), 
    "c": c(),
    "d": d(),
    "e": e(),
    "f": f(),
    "g": g(),
    "h": h(),
    "i": i(),
    "j": j(),
    "k": k(),
    "l": l(),
    "m": m(),
    "n": n(),
    "o": o(),
    "p": p(),
    "q": q(),
    "r": r(),
    "s": s(),
    "t": t(),
    "u": u(),
    "v": v(),
    "w": w(),
    "x": x(),
    "y": y(),
    "z": z(),
    " ": space(),
    ".": full_stop(),
    ",": comma(),
    ";": semicolon(),
    ":": colon(),
    "!": exclamation_point(),
    "?": question_mark(),
    "1": a(),
    "2": b(),
    "3": c(),
    "4": d(),
    "5": e(),
    "6": f(),
    "7": g(),
    "8": h(),
    "9": i(),
    "0": j()

}

print("""G90;
G1 F5000;""")
print("G90 X0 Y0 Z0;")

counter = 0
total_counter = 0

# reset flag used for number detection
flag = 0

for user_letter in word:
    if total_counter >= 200:
        print("limit reached !!!!!!!!!-----------------")
        #print(total_counter,counter)
        break
    
    counter = counter+1
    total_counter = total_counter+1

    
    if user_letter.isupper():
        print(upper_case())
#        print("UPPER CODE^^^^^^^^^^^^^^^^^^^^^^^")
        counter = counter+1
        total_counter = total_counter+1
# checks if user_letter is a number and if it’s the first number read
    if user_letter.isnumeric() and flag == 0: 
        print(number())
#        print("NUMBER CODE^^^^^^^^^^^^^^^^^^")
        counter = counter+1
        total_counter = total_counter+1
# flag set to 1 to indicate first number has been detected
        flag = 1 
# flag reset if space is detected at the end of a number sequence
    if user_letter == " " and flag == 1:
        flag = 0
#        print("End of number sequence -----------------")
        
    print(letter_to_gcode[user_letter.lower()])
    #print("------------------")
   
    if counter == 20:
        print(new_line(val))
        val = val-10
        counter = 0
# for debugging errors in amount of characters being printed              
# print(total_counter)
# print(counter)

print("G90 X0 Y0 Z0;")


