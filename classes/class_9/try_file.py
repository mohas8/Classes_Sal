try:
    f = open("hi.txt", "w")
    # f.write("hi, py")
    try:
        f.write("hi, py")
    except:
        print("write failed")
    finally:
        f.close()
except:
    print("no file")