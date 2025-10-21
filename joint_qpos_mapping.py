import mujoco
import mujoco.viewer
import os

# Load the model
model_path = "your_model.xml"  # Replace with your XML path
model = mujoco.MjModel.from_xml_path(model_path)

# Initialize data
data = mujoco.MjData(model)

# Start of the qpos index
qpos_index = 0

print("Joint QPOS Mapping:")
print("=" * 40)

for i in range(model.njnt):
    joint_name = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_JOINT, i)
    qpos_addr = model.jnt_qposadr[i]
    qpos_size = model.jnt_dofadr[i + 1] - model.jnt_dofadr[i] if i + 1 < model.njnt else model.nq - model.jnt_qposadr[i]
    
    # Handle multi-DoF joints like ball or free joints
    indices = list(range(qpos_addr, qpos_addr + qpos_size))

    print(f"Joint: {joint_name:<20} | QPOS Indices: {indices}")

print("=" * 40)
