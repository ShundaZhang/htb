import angr

def main():
    # Path to the ARM binary
    binary_path = "./c1"

    # Load the binary into Angr
    proj = angr.Project(binary_path, auto_load_libs=False)

    # Create an entry state
    entry_state = proj.factory.entry_state()
    # Create a simulation manager with the entry state
    simgr = proj.factory.simulation_manager(entry_state)
    start_addr = 0x1d8

    # Use Angr's symbolic execution engine to execute until the specified address
    simgr = proj.factory.simulation_manager(entry_state)
    # Explore the binary
    simgr.explore(find= 0x400000 + start_addr + 4)
    #simgr.step()
    
    # Print the state of the program at address 0x1d8
    for state in simgr.found:
        print("Register values for state:")
        for reg in state.arch.registers:
            if reg.startswith('r'):
                print(f"{reg}: {state.registers.load(reg)}")
        print()


if __name__ == "__main__":
    main()

