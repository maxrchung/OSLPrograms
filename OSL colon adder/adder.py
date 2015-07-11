with open("input.txt", "r") as input:
    data = input.read()
    data = data.replace("OSL", "OSL:");
    with open("output.txt", "w") as output:
        output.write(data)
        output.close()
