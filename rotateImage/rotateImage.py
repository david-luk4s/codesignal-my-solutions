def rotateImage(a):
    a.reverse()
    new_li = []
    two_li = []

    for x in range(len(a)):
        for key, el in enumerate(a):
            new_li.append(a[key].pop(0))
            if key == (len(a) - 1):
                two_li.append(new_li)
                new_li = []
    
    return two_li
        