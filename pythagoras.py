
#PYTHagoras

import ISITprime
import matplotlib.pyplot as plt

#figure setting
fig = plt.figure()
# Create 3D container
ax = plt.axes(projection = '3d')
# Give labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


#Input
limit = int(input("\nLimit: "))
int_coordinate = input("Show ALL integer-value coordinate(0/1): ")

#2nd dimensional variable(list)
valid_coordinate = [[0 for col in range(limit)] for row in range(3)]
cnt = 0

#main
x=1
while x<=limit:
    y=1
    while y<=limit:
        z=1
        while z<=limit:

            if (pow(x,2)+pow(y,2))==pow(z,2):

                #printing all pythagoras coordinate
                print('X='+str(x)+', Y='+str(y)+', Z='+str(z)+'\n')

                if int(int_coordinate)==1:
                    # Visualize 3D scatter plot
                    xdataI = x
                    ydataI = y
                    zdataI = z
                    #z>0
                    ax.scatter3D(xdataI, ydataI, zdataI, color='green')
                    ax.scatter3D(-xdataI, ydataI, zdataI, color='green')
                    ax.scatter3D(xdataI, -ydataI, zdataI, color='green')
                    ax.scatter3D(-xdataI, -ydataI, zdataI, color='green')
                    #z<0
                    ax.scatter3D(xdataI, ydataI, -zdataI, color='green')
                    ax.scatter3D(-xdataI, ydataI, -zdataI, color='green')
                    ax.scatter3D(xdataI, -ydataI, -zdataI, color='green')
                    ax.scatter3D(-xdataI, -ydataI, -zdataI, color='green')

                #checking if the coordinate is containing more than one prime numbers
                primecnt = ISITprime.prime(x) + ISITprime.prime(y) + ISITprime.prime(z)
                #Saving
                if primecnt>1:
                    valid_coordinate[0][cnt] = x
                    valid_coordinate[1][cnt] = y
                    valid_coordinate[2][cnt] = z
                    cnt=cnt+1
            z=z+1
        y=y+1
    x=x+1



#printing
fin = 0
print("\n\n\nValid Coordinate: ")
while fin<cnt:
    print('\n#'+str(fin+1)+': X='+str(valid_coordinate[0][fin])+', Y='+str(valid_coordinate[1][fin])+', Z='+str(valid_coordinate[2][fin]))
    xdata = valid_coordinate[0][fin]
    ydata = valid_coordinate[1][fin]
    zdata = valid_coordinate[2][fin]

    # Visualize 3D scatter plot
    #z>0
    ax.scatter3D(xdata, ydata, zdata, color='blue')
    ax.scatter3D(-xdata, ydata, zdata, color='blue')
    ax.scatter3D(xdata, -ydata, zdata, color='blue')
    ax.scatter3D(-xdata, -ydata, zdata, color='blue')
    #z<0
    ax.scatter3D(xdata, ydata, -zdata, color='blue')
    ax.scatter3D(-xdata, ydata, -zdata, color='blue')
    ax.scatter3D(xdata, -ydata, -zdata, color='blue')
    ax.scatter3D(-xdata, -ydata, -zdata, color='blue')
    #Save figure
    plt.savefig('3d_scatter.png', dpi = 300);
    fin = fin + 1

print("\n\n\nMaker: Suho Ban(Daon1109)")
plt.show()
