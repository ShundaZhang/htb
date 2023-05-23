import angr

project = angr.Project("./guess", auto_load_libs=False)

@project.hook(0x4006d5)  # Target address
def print_flag(state):
    print("VALID INPUT:", state.posix.dumps(0))
    project.terminate_execution()

project.execute()

