import pybullet as p
import pybullet_data
import time


physics_client = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0 , -9.81)
plane_id = p.loadURDF("plane.urdf")
franka_id = p.loadURDF(
    "franka_panda/panda.urdf",
    basePosition = [0,0,0],
    useFixedBase=True
)

num_joints = p.getNumJoints(franka_id)
print("NUM JOINTS", num_joints)


for join in range(num_joints):
    i = p.getJointInfo(franka_id, join)
    print(join, i[1].decode("utf-8"))

#simulation:
while True:
    p.setJointMotorControl2(
        bodyUniqueId = franka_id,
        jointIndex=0,
        controlMode=p.POSITION_CONTROL,
        targetPosition=1.58,
        force=200       
        )
    p.stepSimulation()
    time.sleep(1. /240. )
