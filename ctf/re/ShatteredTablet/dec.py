import angr

project = angr.Project("./tablet", auto_load_libs=False)

@project.hook(0x00401371)  # Target address
def print_flag(state):
    print("VALID INPUT:", state.posix.dumps(0))
    project.terminate_execution()

project.execute()

#HTB{br0k3n_4p4rt...n3ver_t0_b3_r3p41r3d}
