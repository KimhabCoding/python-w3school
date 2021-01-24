py = 'Python' #Global variable 
def greeting(): 
    global kh 
    kh = "Love Coding"
    # kh = 'Love Coding'
    py = 'Kimhab' #Local variable 
    print("Hello " + py)
greeting()
print(py)
print(kh)