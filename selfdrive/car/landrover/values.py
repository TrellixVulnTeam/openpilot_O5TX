from cereal import car
from selfdrive.car import dbc_dict
Ecu = car.CarParams.Ecu

STEER_THRESHOLD = 1023
# Steer torque limits
class CarControllerParams:
  STEER_MAX = 1023
  STEER_DELTA_UP = 5
  STEER_DELTA_DOWN = 10
  STEER_ERROR_MAX = 1023

  ACCEL_MIN = -3.5 # m/s
  ACCEL_MAX = 2.0 # m/s

#  def __init__(self, CP):
  STEER_DRIVER_ALLOWANCE = 50
  STEER_DRIVER_MULTIPLIER = 2
  STEER_DRIVER_FACTOR = 1

class CAR:
   RANGEROVER_2017_VOGUE = "LANDROVER RangeRover Vogue 2017"

FINGERPRINTS = {
  CAR.RANGEROVER_2017_VOGUE: [
    {224: 8, 242: 8, 336: 8, 337: 8, 340: 8, 341: 8, 342: 8, 344: 8, 346: 8, 352: 8, 356: 8, 360: 8, 370: 8, 398: 8, 399: 8, 427: 8, 459: 8, 464: 8, 468: 8, 469: 8, 472: 8, 475: 8, 480: 8, 488: 8, 495: 8, 500: 8, 504: 8, 507: 8, 511: 8, 552: 8, 555: 8, 596: 8, 603: 8, 607: 8, 644: 8, 648: 8, 651: 8, 655: 8, 656: 8, 660: 8, 688: 8, 692: 8, 696: 8, 720: 8, 752: 8, 784: 8, 816: 8, 824: 8, 827: 8, 868: 8, 916: 8, 928: 8, 976: 8, 977: 8, 980: 8, 1008: 8, 1012: 8, 1024: 8, 1029: 8, 1031: 8, 1040: 8, 1044: 8, 1048: 8, 1056: 8, 1060: 8, 1072: 8, 1120: 8, 1136: 8, 1152: 8, 1153: 8, 1168: 8, 1200: 8, 1277: 8, 1279: 8, 1297: 8, 1310: 8, 1430: 8, 1438: 8
  }],
}


FW_VERSIONS = {
}

# addr: (ecu, cars, bus, 1/freq*100, vl)
# 1D8 4694050000000582
# 1D8#46950500000008BC
# 3D4 800d0141e73ded00
STATIC_MSGS = [
 (0x1D8, 0, (CAR.RANGEROVER_2017_VOGUE), 0, 10, b'\x46\x95\x05\x05\x00\x00\x08\xbc'),
# (0x3D4, Ecu.CAM, (CAR.RANGEROVER_2017_VOGUE), 0, 40, '\x80\x0d\x01\x41\xe7\x3d\xed\x00'),
]

Ecu_FINGERPRINT = {
  Ecu.fwdCamera: 0x28f,   # steer torque cmd
}


DBC = {
  CAR.RANGEROVER_2017_VOGUE: dbc_dict(
    'landrover_rangerover_2017_vogue',  # 'pt'
   None),  # 'radar'
}
