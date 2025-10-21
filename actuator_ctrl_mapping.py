import mujoco
import os

# Load the model
model_path = "your_model.xml"  # Replace with your actual XML path
model = mujoco.MjModel.from_xml_path(model_path)

print("Actuator Control Mapping:")
print("=" * 70)

for i in range(model.nu):
    actuator_name = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_ACTUATOR, i)
    actuator_name = actuator_name if actuator_name is not None else "N/A"

    trntype = model.actuator_trntype[i]
    trnid = model.actuator_trnid[i]

    # Default joint name
    joint_name = "N/A"

    # Check if actuator targets a joint
    if trntype == mujoco.mjtTrn.mjTRN_JOINT:
        joint_id = trnid[0]
        if joint_id >= 0:
            joint_name = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_JOINT, joint_id)
            joint_name = joint_name if joint_name is not None else "N/A"

    # Get actuator gain type (e.g., fixed, user)
    try:
        actuator_type_str = mujoco.mjtGain(model.actuator_gaintype[i]).name.lower()
    except:
        actuator_type_str = "unknown"

    print(f"Actuator: {actuator_name:<25} | Control Index: {i:<2} | Joint: {joint_name:<25} | Type: {actuator_type_str}")

print("=" * 70)
