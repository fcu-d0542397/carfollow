import math
import os
import traci
from sympy import *
from decimal import Decimal
import threading


x = Symbol('x')


sumoBinary = "C:\\Program Files (x86)\\Eclipse\\Sumo\\bin\\sumo-gui.exe"
sumoCmd = [sumoBinary, "-c",
           "C:\\Users\\user\\Desktop\\sumo\\carfollow\\myConfig.sumocfg"]


traci.start(sumoCmd)
step = 0

allSpeed = []
allACC = []


def speedInit():
    for i in range(11):
        veh = "veh"+str(i)
        traci.vehicle.setSpeed(veh, -1)

for i in range(11):
    allSpeed.append(0)
    allACC.append(0)

# 0817
def calRiskSpeed(notice):
    if step % 1 == 0:
        for i in range(1, 11):
            now = "veh"+str(i)
            front = "veh"+str(i-1)
            gap = abs(traci.vehicle.getPosition(now)[0]-traci.vehicle.getPosition(front)[0]) - 4
            allACC[i] = calFollowSpeed(allSpeed[i], allSpeed[i-1], gap, notice, 8)
            frontSpeed = allSpeed[i-1]
            nowSpeed = allSpeed[i]
            followRisk = allACC[i] / 8
            if followRisk >= 1:
                solve_value = solve([((nowSpeed**2 * 8)/(frontSpeed**2 + 2*8*(x - nowSpeed * notice)) / 8) - 1],[x])
                # print("nowSpeed: "+str(nowSpeed)+" frontSpeed: "+str(frontSpeed)+" safetyDistace: "+ str(solve_value))
                if ":" in str(solve_value):
                    characters = "{,x:}"
                    tempString = str(solve_value)
                    for i in range(len(characters)):
                        tempString = tempString.replace(characters[i], "")
                    saftyDistace = float(tempString)
                if saftyDistace > gap:
                    crashTime = gap / (nowSpeed)
                    distaceOffset = saftyDistace - gap
                    if crashTime <= notice:
                        distaceOffset10 = (distaceOffset / 8) / 10
                    else:
                        oneSecondPlus = distaceOffset / crashTime
                        distaceOffset10 = (distaceOffset / oneSecondPlus) / 10
                    print("distaceOffset10: "+str(distaceOffset10 * 10))
                    if traci.vehicle.getSpeed(now) - distaceOffset10 > 0:
                        newSpeed = traci.vehicle.getSpeed(now) - distaceOffset10
                        traci.vehicle.setSpeed(now, newSpeed)
                elif abs(saftyDistace - gap) <= 0.1:
                    return 0
                elif saftyDistace < gap:
                    distaceOffset = gap - saftyDistace
                    distaceOffset10 = (distaceOffset / 6) 
                    newSpeed = traci.vehicle.getSpeed(now) + distaceOffset / 2
                    traci.vehicle.setSpeed(now, newSpeed)



            

            # if "-" in str(solve_value[0]):
            #     characters = "(),"
            #     tempString = str(solve_value[1])
            #     for i in range(len(characters)):
            #         tempString = tempString.replace(characters[i], "")
            #     traci.vehicle.setSpeed(now, Decimal(tempString))
            # else:
            #     characters = "(),"
            #     tempString = str(solve_value[0])
            #     for i in range(len(characters)):
            #         tempString = tempString.replace(characters[i], "")
            #     traci.vehicle.setSpeed(now, Decimal(tempString))
                
                # print(solve_value)
            # if i % 10 == 1:
            #     print(followRisk) 
            # print(allACC[i])
            # traci.vehicle.setDecel(now, allACC[i])

def calFollowSpeed(nowSpeed, frontSpeed, distance, notice, brakeMax):
    follow = (nowSpeed**2 * brakeMax) / (frontSpeed**2 +2 * brakeMax * (distance - nowSpeed * notice))
    return follow


def getAllSpeed():
    for i in range(11):
        veh = "veh"+str(i)
        allSpeed[i] = traci.vehicle.getSpeed(veh)
        allACC[i] = traci.vehicle.getDecel(veh)
    # print(allSpeed)
    # print(allACC)


while step < 40000:
    traci.simulationStep()
    if step == 0:
        os.remove("output.txt")
        print("File removed successfully")
        path = 'output.txt'
        f = open(path, 'a')

        os.remove("output2.txt")
        print("File removed successfully")
        path = 'output2.txt'
        f2 = open(path, 'a')

        os.remove("output3.txt")
        print("File removed successfully")
        path = 'output3.txt'
        f3 = open(path, 'a')

    if step == 0:

        # traci.vehicle.setLaneChangeMode("veh0",0b001000000000)
        # traci.vehicle.setLaneChangeMode("veh1",0b001000000000)
        # traci.vehicle.setLaneChangeMode("veh2",0b001000000000)
        # traci.vehicle.setLaneChangeMode("veh3",0b001000000000)

        # traci.vehicle.setLaneChangeMode("veh0",0b000000000100)
        # traci.vehicle.setLaneChangeMode("veh1",0b010101010100)
        # traci.vehicle.setLaneChangeMode("veh2",0b010101010100)
        # traci.vehicle.setLaneChangeMode("veh3",0b010101010100)
        # traci.vehicle.setLaneChangeMode("veh4",0b010101010100)
        # traci.vehicle.setLaneChangeMode("veh5",0b010101010100)
        # traci.vehicle.setLaneChangeMode("veh6",0b010101010100)
        # traci.vehicle.setLaneChangeMode("veh7",0b010101010100)
        # traci.vehicle.setLaneChangeMode("veh8",0b010101010100)

        # traci.vehicle.setSpeedMode("veh0",0b100000)
        # traci.vehicle.setSpeedMode("veh1",0b111000)
        # traci.vehicle.setSpeedMode("veh2",0b111000)
        # traci.vehicle.setSpeedMode("veh3",0b111000)
        # traci.vehicle.setSpeedMode("veh4",0b111000)
        # traci.vehicle.setSpeedMode("veh5",0b111000)
        # traci.vehicle.setSpeedMode("veh6",0b111000)

        # traci.vehicle.setSpeedMode("veh0",00000)
        # traci.vehicle.setSpeedMode("veh1",00000)
        # traci.vehicle.setSpeedMode("veh2",00000)
        # traci.vehicle.setSpeedMode("veh3",00000)
        speedInit()
        traci.vehicle.setSpeed("veh0", 5)

    # if step == 150:
    #    traci.vehicle.setLaneChangeMode("veh1",0b0000011000)

    # if step == 150:
    #    traci.vehicle.setSpeed("veh1",5)

    # if step == 300:
    #    traci.vehicle.setSpeed("veh2",5)

    # if step == 450:
    #    traci.vehicle.setSpeed("veh3",5)

    # if step == 600:
    #    traci.vehicle.setSpeed("veh4",5)

    # if step == 750:
    #    traci.vehicle.setSpeed("veh5",5)

    # if step == 900:
    #    traci.vehicle.setSpeed("veh6",5)

    # if step == 1050:
    #    traci.vehicle.setSpeed("veh7",5)

    # if step == 1200:
    #    traci.vehicle.setSpeed("veh8",5)

    # if step == 1350:
    #    traci.vehicle.setSpeed("veh9",5)

    # if step == 1500:
    #    traci.vehicle.setSpeed("veh10",5)

    # if step == 419:
    #    traci.vehicle.setEmergencyDecel("veh1",0)
    #    traci.vehicle.setDecel("veh1", 0)

    # if step == 533:
    #    traci.vehicle.setEmergencyDecel("veh2",0)
    #    traci.vehicle.setDecel("veh2", 0)

    # if step == 644:
    #    traci.vehicle.setEmergencyDecel("veh3",0)
    #    traci.vehicle.setDecel("veh3", 0)

    # if step == 752:
    #    traci.vehicle.setEmergencyDecel("veh4",0)
    #    traci.vehicle.setDecel("veh4", 0)

    # if step == 847:
    #    traci.vehicle.setEmergencyDecel("veh5",0)
    #    traci.vehicle.setDecel("veh5", 0)

    # if step == 939:
    #    traci.vehicle.setEmergencyDecel("veh6",0)
    #    traci.vehicle.setDecel("veh6", 0)

    # if step == 1031:
    #    traci.vehicle.setEmergencyDecel("veh7",0)
    #    traci.vehicle.setDecel("veh7", 0)

    # if step == 1120:
    #    traci.vehicle.setEmergencyDecel("veh8",0)
    #    traci.vehicle.setDecel("veh8", 0)

    # if step == 1206:
    #    traci.vehicle.setEmergencyDecel("veh9",0)
    #    traci.vehicle.setDecel("veh9", 0)
    # if step == 1289:
    #    traci.vehicle.setEmergencyDecel("veh10",0)
    #    traci.vehicle.setDecel("veh10", 0)

    # for i in range(10):
    #    car = "veh"+str(i+1)
    #    if traci.vehicle.getSpeed(car) < 5.07:
    #       traci.vehicle.setEmergencyDecel(car,0)
    #       traci.vehicle.setDecel(car, 0)


    if step > 310 and step < 600:
      traci.vehicle.setEmergencyDecel("veh0",0)
      traci.vehicle.setDecel("veh0", 0)
      tmpSpeed = traci.vehicle.getSpeed("veh0")
      traci.vehicle.setSpeed("veh0", tmpSpeed)

#    if step > 460 and step < 750:
#       traci.vehicle.setEmergencyDecel("veh1",0.05)
#       traci.vehicle.setDecel("veh1", 0.05)
#       tmpSpeed = traci.vehicle.getSpeed("veh1")
#       traci.vehicle.setSpeed("veh1", tmpSpeed)


#    if step > 610 and step < 900:
#       traci.vehicle.setEmergencyDecel("veh2",0.04)
#       traci.vehicle.setDecel("veh2", 0.04)
#       tmpSpeed = traci.vehicle.getSpeed("veh2")
#       traci.vehicle.setSpeed("veh2", tmpSpeed)

#    if step > 760 and step < 1050:
#       traci.vehicle.setEmergencyDecel("veh3",0.05)
#       traci.vehicle.setDecel("veh3", 0.05)
#       tmpSpeed = traci.vehicle.getSpeed("veh3")
#       traci.vehicle.setSpeed("veh3", tmpSpeed)

#    if step > 910 and step < 1200:
#       traci.vehicle.setEmergencyDecel("veh4",0.03)
#       traci.vehicle.setDecel("veh4", 0.03)
#       tmpSpeed = traci.vehicle.getSpeed("veh4")
#       traci.vehicle.setSpeed("veh4", tmpSpeed)

#    if step > 1060 and step < 1350:
#       traci.vehicle.setEmergencyDecel("veh5",0.02)
#       traci.vehicle.setDecel("veh5", 0.02)
#       tmpSpeed = traci.vehicle.getSpeed("veh5")
#       traci.vehicle.setSpeed("veh5", tmpSpeed)


#    if step > 1210 and step < 1500:
#       traci.vehicle.setEmergencyDecel("veh6",0.03)
#       traci.vehicle.setDecel("veh6", 0.03)
#       tmpSpeed = traci.vehicle.getSpeed("veh6")
#       traci.vehicle.setSpeed("veh6", tmpSpeed)

#    if step > 1360 and step < 1650:
#       traci.vehicle.setEmergencyDecel("veh7",0.04)
#       traci.vehicle.setDecel("veh7", 0.04)
#       tmpSpeed = traci.vehicle.getSpeed("veh7")
#       traci.vehicle.setSpeed("veh7", tmpSpeed)


#    if step > 1510 and step < 1800:
#       traci.vehicle.setEmergencyDecel("veh8",0.05)
#       traci.vehicle.setDecel("veh8", 0.05)
#       tmpSpeed = traci.vehicle.getSpeed("veh8")
#       traci.vehicle.setSpeed("veh8", tmpSpeed)

#    if step > 1660 and step < 1950:
#       traci.vehicle.setEmergencyDecel("veh9",0.06)
#       traci.vehicle.setDecel("veh9", 0.06)
#       tmpSpeed = traci.vehicle.getSpeed("veh9")
#       traci.vehicle.setSpeed("veh9", tmpSpeed)

#    if step > 1810 and step < 2100:
#       traci.vehicle.setEmergencyDecel("veh10",0.1)
#       traci.vehicle.setDecel("veh10", 0.1)
#       tmpSpeed = traci.vehicle.getSpeed("veh10")
#       traci.vehicle.setSpeed("veh10", tmpSpeed)

    # if step == 460:
    #    traci.vehicle.setSpeed("veh1",traci.vehicle.getSpeed("veh0"))
    #    traci.vehicle.setEmergencyDecel("veh1",0)
    #    traci.vehicle.setDecel("veh1", 0)

    # if step == 610:
    #    traci.vehicle.setSpeed("veh2",traci.vehicle.getSpeed("veh1"))
    #    traci.vehicle.setEmergencyDecel("veh2",0)
    #    traci.vehicle.setDecel("veh2", 0)

    # if step == 760:
    #    traci.vehicle.setSpeed("veh3",traci.vehicle.getSpeed("veh2"))
    #    traci.vehicle.setEmergencyDecel("veh3",0)
    #    traci.vehicle.setDecel("veh3", 0)

    # if step == 910:
    #    traci.vehicle.setSpeed("veh4",traci.vehicle.getSpeed("veh3"))
    #    traci.vehicle.setEmergencyDecel("veh4",0)
    #    traci.vehicle.setDecel("veh4", 0)

    # if step == 1060:
    #    traci.vehicle.setSpeed("veh5",traci.vehicle.getSpeed("veh4"))
    #    traci.vehicle.setEmergencyDecel("veh5",0)
    #    traci.vehicle.setDecel("veh5", 0)

    # if step == 1210:
    #    traci.vehicle.setSpeed("veh6",traci.vehicle.getSpeed("veh5"))
    #    traci.vehicle.setEmergencyDecel("veh6",0)
    #    traci.vehicle.setDecel("veh6", 0)

    # if step == 1360:
    #    traci.vehicle.setSpeed("veh7",traci.vehicle.getSpeed("veh6"))
    #    traci.vehicle.setEmergencyDecel("veh7",0)
    #    traci.vehicle.setDecel("veh7", 0)

    # if step == 1510:
    #    traci.vehicle.setSpeed("veh8",traci.vehicle.getSpeed("veh7"))
    #    traci.vehicle.setEmergencyDecel("veh8",0)
    #    traci.vehicle.setDecel("veh8", 0)

    # if step == 1660:
    #    traci.vehicle.setSpeed("veh9",traci.vehicle.getSpeed("veh8"))
    #    traci.vehicle.setEmergencyDecel("veh9",0)
    #    traci.vehicle.setDecel("veh9", 0)

    # if step == 1810:
    #    traci.vehicle.setSpeed("veh10",traci.vehicle.getSpeed("veh9"))
    #    traci.vehicle.setEmergencyDecel("veh10",0)
    #    traci.vehicle.setDecel("veh10", 0)

        # traci.vehicle.setSpeed("veh0",5)

    # if traci.vehicle.getSpeed("veh0") == 5:
    #    traci.vehicle.setEmergencyDecel("veh0",0)
    #    traci.vehicle.setDecel("veh0", 0)
    #    timeStamp = step
    #    # traci.vehicle.setSpeed("veh0",5)

    if step == 600:
        traci.vehicle.setAccel("veh0", 6)
        traci.vehicle.setEmergencyDecel("veh0", 8)
        traci.vehicle.setDecel("veh0", 8)
        traci.vehicle.setSpeed("veh0", 30)

    # if step == 750:
    #     traci.vehicle.setEmergencyDecel("veh1", 8)
    #     traci.vehicle.setDecel("veh1", 8)
    #     traci.vehicle.setSpeed("veh1", -1)

    # if step == 900:
    #     traci.vehicle.setEmergencyDecel("veh2", 8)
    #     traci.vehicle.setDecel("veh2", 8)
    #     traci.vehicle.setSpeed("veh2", -1)

    # if step == 1050:
    #     traci.vehicle.setEmergencyDecel("veh3", 8)
    #     traci.vehicle.setDecel("veh3", 8)
    #     traci.vehicle.setSpeed("veh3", -1)

    # if step == 1200:
    #     traci.vehicle.setEmergencyDecel("veh4", 8)
    #     traci.vehicle.setDecel("veh4", 8)
    #     traci.vehicle.setSpeed("veh4", -1)

    # if step == 1350:
    #     traci.vehicle.setEmergencyDecel("veh5", 8)
    #     traci.vehicle.setDecel("veh5", 8)
    #     traci.vehicle.setSpeed("veh5", -1)

    # if step == 1500:
    #     traci.vehicle.setEmergencyDecel("veh6", 8)
    #     traci.vehicle.setDecel("veh6", 8)
    #     traci.vehicle.setSpeed("veh6", -1)

    # if step == 1650:
    #     traci.vehicle.setEmergencyDecel("veh7", 8)
    #     traci.vehicle.setDecel("veh7", 8)
    #     traci.vehicle.setSpeed("veh7", -1)

    # if step == 1800:
    #     traci.vehicle.setEmergencyDecel("veh8", 8)
    #     traci.vehicle.setDecel("veh8", 8)
    #     traci.vehicle.setSpeed("veh8", -1)

    # if step == 1950:
    #     traci.vehicle.setEmergencyDecel("veh9", 8)
    #     traci.vehicle.setDecel("veh9", 8)
    #     traci.vehicle.setSpeed("veh9", -1)

    # if step == 2100:
    #     traci.vehicle.setEmergencyDecel("veh10", 8)
    #     traci.vehicle.setDecel("veh10", 8)
    #     traci.vehicle.setSpeed("veh10", -1)

    # if step > 30 and traci.vehicle.getSpeed("veh1") > 5:
    #    traci.vehicle.changeLane("veh1", 0,100)
    # if step == 400:
        # traci.vehicle.changeLane("veh1", 0,100)
        # traci.vehicle.changeLane("veh0", 0,100)
        # traci.vehicle.changeLane("veh2", 0,100)
        # traci.vehicle.changeLane("veh3", 0,100)

        # traci.vehicle.setSpeed("veh0", 5)

        # traci.vehicle.getPosition("veh0")
        # traci.vehicle.moveTo("veh0","1to2_1",500,0)

        # traci.vehicle.setSpeed("veh1", 3)
        # traci.vehicle.setSpeed("veh2", 5)
        # traci.vehicle.setSpeed("veh3", 6)

    # if step > 612 and step < 762:
    #       for i in range(10):
    #          car = "veh"+str(i+1)
    #          traci.vehicle.setSpeed(car, traci.vehicle.getSpeed(car))

    # if step > 762 and step < 912:
    #       traci.vehicle.setSpeed("veh1", 30)
    #       for i in range(9):
    #          car = "veh"+str(i+2)
    #          traci.vehicle.setSpeed(car, traci.vehicle.getSpeed(car))

    # if step > 912 and step < 1062:
    #       traci.vehicle.setSpeed("veh2", 30)
    #       for i in range(8):
    #          car = "veh"+str(i+3)
    #          traci.vehicle.setSpeed(car, traci.vehicle.getSpeed(car))

    # if step > 1062 and step < 1212:
    #       traci.vehicle.setSpeed("veh3", 30)
    #       for i in range(7):
    #          car = "veh"+str(i+4)
    #          traci.vehicle.setSpeed(car, traci.vehicle.getSpeed(car))

    # if step > 1212 and step < 1362:
    #       traci.vehicle.setSpeed("veh4", 30)
    #       for i in range(6):
    #          car = "veh"+str(i+5)
    #          traci.vehicle.setSpeed(car, traci.vehicle.getSpeed(car))

    # if step > 1362 and step < 1512:
    #       traci.vehicle.setSpeed("veh5", 30)
    #       for i in range(5):
    #          car = "veh"+str(i+6)
    #          traci.vehicle.setSpeed(car, traci.vehicle.getSpeed(car))

    # if step > 1512 and step < 1662:
    #       traci.vehicle.setSpeed("veh6", 30)
    #       for i in range(4):
    #          car = "veh"+str(i+7)
    #          traci.vehicle.setSpeed(car, traci.vehicle.getSpeed(car))

    # if step > 1662 and step < 1812:
    #       traci.vehicle.setSpeed("veh7", 30)
    #       for i in range(3):
    #          car = "veh"+str(i+8)
    #          traci.vehicle.setSpeed(car, traci.vehicle.getSpeed(car))

    # if step > 1812 and step < 1962:
    #       traci.vehicle.setSpeed("veh8", 30)
    #       for i in range(2):
    #          car = "veh"+str(i+9)
    #          traci.vehicle.setSpeed(car, traci.vehicle.getSpeed(car))

    # if step > 1962 and step < 2112:
    #       traci.vehicle.setSpeed("veh9", 30)
    #       for i in range(1):
    #          car = "veh"+str(i+10)
    #          traci.vehicle.setSpeed(car, traci.vehicle.getSpeed(car))

    # if step > 2112 and step < 2262:
    #       traci.vehicle.setSpeed("veh10", 30)

    if step > -1:
        getAllSpeed()
        calRiskSpeed(1.5)
        # print(traci.vehicle.getDecel("veh1"))
        # print(traci.vehicle.getSpeed("veh1"))
        save = ""
        for i in range(11):
            vehString = "veh"+str(i)
            save = save + " " + str(traci.vehicle.getSpeed(vehString))
        f.write(str(step/100)+save+"\n")
        save = ""
        for i in range(10):
            vehString = "veh"+str(i)
            vehString2 = "veh"+str(i+1)
            gap = 0
            gap = abs(traci.vehicle.getPosition(vehString2)[
                      0]-traci.vehicle.getPosition(vehString)[0])
            save = save + " " + str(gap)
        f2.write(str(step/100)+save+"\n")
        save = ""
        for i in range(10):
            vehString = "veh"+str(i)
            gap = str(traci.vehicle.getPosition(vehString)[0])
            save = save + " " + str(gap)
        f3.write(str(step/100)+save+"\n")

        # gap = 0
        # gap = abs(traci.vehicle.getPosition("veh1")[0]-traci.vehicle.getPosition("veh0")[0])

        # print(traci.vehicle.getFollowSpeed("veh1",traci.vehicle.getSpeed("veh1"),gap,traci.vehicle.getSpeed("veh0"),8,"veh0"))
        # traci.vehicle.getFollowSpeed("veh1",traci.vehicle.getSpeed("veh1"),gap,traci.vehicle.getSpeed("veh0"),8,"veh0")

        # print("veh0 :"+str(traci.vehicle.getSpeed("veh0")))
        # print("veh0 :"+str(traci.vehicle.getSpeed("veh1")))
        # print("veh2 :"+str(traci.vehicle.getSpeed("veh2")))
        # print("veh3 :"+str(traci.vehicle.getSpeed("veh3")))

        # print("veh0 position: "+ str(traci.vehicle.getPosition("veh0")))
        # print("veh0 LaneID: "+ str(traci.vehicle.getLaneID("veh0")))

    # if step == 40:
    #       traci.vehicle.changeLaneRelative("veh0", 0, 100)
    #       traci.vehicle.changeLaneRelative("veh1", 0, 100)
    #       traci.vehicle.changeLaneRelative("veh2", 0, 100)
    #       traci.vehicle.changeLaneRelative("veh3", 0, 100)
#    if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
#        traci.trafficlight.setRedYellowGreenState("0", "GrGr")
    step += 1

traci.close()
