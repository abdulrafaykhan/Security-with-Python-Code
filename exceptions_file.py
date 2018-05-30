try:
    fhandle = open("myfile", "w")
    fhandle.write("This is some important text that I need to put in the file")
    print("Wrote something to the file")
except IOError as e:
    print("Couldn't write to the file", e)
except Exception as e:
    print("Couldn't write to the file", e)
else:
    print("Wrote to the file successfully!")
    fhandle.close()
    