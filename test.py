def a(f,l):
    fs=f.split(".")
    ls=l.split(".")
    fi = abs(int(fs[0])-int(ls[0]))
    s =int(fs[1])-int(ls[1])
    t = int(fs[2])-int(ls[2])
    f = abs(int(fs[3])-int(ls[3]))
    print(fi)
    print(s)
    print(t)
    print(f)
    return fi*s*t*f
    # ((a[0] - b[0]) * 256 + a[1] - b[1]) * 256 + a[2] - b[2]) *256 + a[3] - b[3]

if __name__ == "__main__":
    print(a("10.0.0.0","10.0.0.50"))