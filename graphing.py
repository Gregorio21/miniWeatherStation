import matplotlib.pyplot as plt

if __name__ == '__main__':
    #arrays to store time,temp,humidity data from file
    x = []
    y = []
    z = []
    #open file with stored data, change argument if file name changed
    with open("data3-7.txt", 'r') as f:
        #read every line from file
        lines = f.readlines()
        #create iterator over lines from file to allow going over the list 3 lines ata time
        it = iter(lines)
        for line in it:
            #add each line to the appropriate list, they are printed to the data file in order time, temp humidity
            x.append(line.rstrip())
            y.append(next(it).rstrip())
            z.append(next(it).rstrip())
    #create matplotlib figure with two subplots, one for humidity x time, one for temperature x time
    fig = plt.figure(figsize=(12,6))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    ax1.set_title("Temperature F")
    ax2.set_title("Humidity %")
    ax1.set_xticks(range(20,round(float(max(x))),round(float(max(x))/10)))
    ax2.set_xticks(range(20, round(float(max(x))), round(float(max(x)) / 10)))
    ax1.set_xlabel("time (s) since device started")
    ax2.set_xlabel("time (s) since device started")
    ax1.plot(x,y)
    ax2.plot(x,z)
    plt.show()
    #save created graph to png file change string if making multiple graphs
    fig.savefig("graph.png")
