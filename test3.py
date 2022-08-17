sumoBinary = "C:\\Program Files (x86)\\Eclipse\\Sumo\\bin\\sumo-gui.exe"
sumoCmd = [sumoBinary, "-c", "C:\\Users\\user\\Desktop\\sumo\\myConfig.sumocfg"]


import traci
import os
import math
traci.start(sumoCmd)
step = 0

while step < 40000:
   traci.simulationStep()
   if step == 0:
      os.remove("output3.txt")
      print("File removed successfully")
      path = 'output3.txt'
      f = open(path, 'a')



   if step == 0:
          
      # traci.vehicle.setLaneChangeMode("veh0",0b001000000000)
      # traci.vehicle.setLaneChangeMode("veh1",0b001000000000)
      # traci.vehicle.setLaneChangeMode("veh2",0b001000000000)
      # traci.vehicle.setLaneChangeMode("veh3",0b001000000000)


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

      traci.vehicle.setSpeed("veh0",0)


   if step == 150:
      traci.vehicle.setSpeed("veh1",0)



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
          

   if step > -1:
      save = ""
      for i in range(1):
         vehString = "veh"+str(i)
         vehString2 = "veh"+str(i+1)
         gap = 0
         gap = abs(traci.vehicle.getPosition(vehString2)[0]-traci.vehicle.getPosition(vehString)[0])
         save = save + " "+ str(gap)
      f.write(str(step/100)+save+"\n")


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