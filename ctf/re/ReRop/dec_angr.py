#failed -- slow
import angr

project = angr.Project("./rerop", auto_load_libs=False)

@project.hook(0x0040183c)  # Target address
def print_flag(state):
    print("VALID INPUT:", state.posix.dumps(0))
    project.terminate_execution()

project.execute()

