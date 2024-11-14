from elitist_decay import * # here you can access the ACO algorithm and variables
n = 40
nodelist = Node.generateNodeList(n)
setup(nodelist)
fullRun()
setup(nodelist)
fullRun()
for i in range(0,len(bestPath)):
    plt.plot([nodelist[bestPath[i]].x,nodelist[bestPath[(i+1)%len(bestPath)]].x],[nodelist[bestPath[i]].y,nodelist[bestPath[(i+1)%len(bestPath)]].y],color=(1,0,0))

for i in range(0,len(nodelist)):
    plt.plot(nodelist[i].x,nodelist[i].y,"o")
plt.show()