def sierpinski(n):
    triangle = ["*"]
    
    for i in range(1, n+1):
        space = " " * (2 ** (i-1))
        new_triangle = []
        
        for line in triangle:
            new_triangle.append(space + line + space)
        
        for line in triangle:
            new_triangle.append(line + " " + line)
        
        triangle = new_triangle
    
    for line in triangle:
        print(line.center(2 ** (n+1)))

sierpinski(4)