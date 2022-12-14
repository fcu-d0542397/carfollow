sumoBinary = "C:\\Program Files (x86)\\Eclipse\\Sumo\\bin\\sumo.exe"
sumoCmd = [sumoBinary, "-c", "C:\\Users\\user\\Desktop\\sumo\\carfollow\\myConfig.sumocfg"]


import traci
import os
import math
traci.start(sumoCmd)
step = 0

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


      traci.vehicle.setLaneChangeMode("veh0",0b00000000010000)
      # traci.vehicle.setLaneChangeMode("veh1",0b010101010100)
      # traci.vehicle.setLaneChangeMode("veh2",0b010101010100)
      # traci.vehicle.setLaneChangeMode("veh3",0b010101010100)
      # traci.vehicle.setLaneChangeMode("veh4",0b010101010100)
      # traci.vehicle.setLaneChangeMode("veh5",0b010101010100)
      # traci.vehicle.setLaneChangeMode("veh6",0b010101010100)
      # traci.vehicle.setLaneChangeMode("veh7",0b010101010100)
      # traci.vehicle.setLaneChangeMode("veh8",0b010101010100)


      # traci.vehicle.setLaneChangeMode("veh0",0b000000000000)
      # traci.vehicle.setLaneChangeMode("veh1",0b000000000000)
      # traci.vehicle.setLaneChangeMode("veh2",0b000000000000)
      # traci.vehicle.setLaneChangeMode("veh3",0b000000000000)

      # traci.vehicle.setLaneChangeMode("veh4",0b000000000000)
      # traci.vehicle.setLaneChangeMode("veh5",0b000000000000)
      # traci.vehicle.setLaneChangeMode("veh6",0b000000000000)
      # traci.vehicle.setLaneChangeMode("veh7",0b000000000000)

      # traci.vehicle.setLaneChangeMode("veh8",0b000000000000)
      # traci.vehicle.setLaneChangeMode("veh9",0b000000000000)


      # traci.vehicle.setSpeedMode("veh0",00000)
      # traci.vehicle.setSpeedMode("veh1",00000)
      # traci.vehicle.setSpeedMode("veh2",00000)
      # traci.vehicle.setSpeedMode("veh3",00000)

      traci.vehicle.setSpeed("veh0",5)

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


   for i in range(10):
      car = "veh"+str(i+1)
      if traci.vehicle.getSpeed(car) < 5.07:
         traci.vehicle.setEmergencyDecel(car,0)
         traci.vehicle.setDecel(car, 0)
         



   if step == 310:
      traci.vehicle.setEmergencyDecel("veh0",0)
      traci.vehicle.setDecel("veh0", 0)

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
      traci.vehicle.setEmergencyDecel("veh0",8)
      traci.vehicle.setSpeed("veh0",30)
   
   # if step == 750:
   #    traci.vehicle.setEmergencyDecel("veh1",8)
   #    traci.vehicle.setDecel("veh1", 8)
   #    traci.vehicle.setSpeed("veh1",30)

   # if step == 900:
   #    traci.vehicle.setEmergencyDecel("veh2",8)
   #    traci.vehicle.setDecel("veh2", 8)
   #    traci.vehicle.setSpeed("veh2",30)

   # if step == 1050:
   #    traci.vehicle.setEmergencyDecel("veh3",8)
   #    traci.vehicle.setDecel("veh3", 8)
   #    traci.vehicle.setSpeed("veh3",30)

   # if step == 1200:
   #    traci.vehicle.setEmergencyDecel("veh4",8)
   #    traci.vehicle.setDecel("veh4", 8)
   #    traci.vehicle.setSpeed("veh4",30)

   # if step == 1350:
   #    traci.vehicle.setEmergencyDecel("veh5",8)
   #    traci.vehicle.setDecel("veh5", 8)
   #    traci.vehicle.setSpeed("veh5",30)

   # if step == 1500:
   #    traci.vehicle.setEmergencyDecel("veh6",8)
   #    traci.vehicle.setDecel("veh6", 8)
   #    traci.vehicle.setSpeed("veh6",30)

   # if step == 1650:
   #    traci.vehicle.setEmergencyDecel("veh7",8)
   #    traci.vehicle.setDecel("veh7", 8)
   #    traci.vehicle.setSpeed("veh7",30)

   # if step == 1800:
   #    traci.vehicle.setEmergencyDecel("veh8",8)
   #    traci.vehicle.setDecel("veh8", 8)
   #    traci.vehicle.setSpeed("veh8",30)

   # if step == 1950:
   #    traci.vehicle.setEmergencyDecel("veh9",8)
   #    traci.vehicle.setDecel("veh9", 8)
   #    traci.vehicle.setSpeed("veh9",30)

   # if step == 2100:
   #    traci.vehicle.setEmergencyDecel("veh10",8)
   #    traci.vehicle.setDecel("veh10", 8)
   #    traci.vehicle.setSpeed("veh10",30)

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
      save = ""
      for i in range(11):
         vehString = "veh"+str(i)
         save = save + " "+ str(traci.vehicle.getSpeed(vehString))
      f.write(str(step/100)+save+"\n")
      save = ""
      for i in range(10):
         vehString = "veh"+str(i)
         vehString2 = "veh"+str(i+1)
         gap = 0
         gap = abs(traci.vehicle.getPosition(vehString2)[0]-traci.vehicle.getPosition(vehString)[0])
         save = save + " "+ str(gap)
      f2.write(str(step/100)+save+"\n")
      save = ""
      for i in range(10):
         vehString = "veh"+str(i)
         gap = str(traci.vehicle.getPosition(vehString)[0])
         save = save + " "+ str(gap)
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