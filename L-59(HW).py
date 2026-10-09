def check_switch_status(switch_board, switch_position):
    """Checks if a specific switch is ON using bitwise AND."""
    mask = 1 << switch_position
    return (switch_board & mask) != 0


def turn_switch_on(switch_board, switch_position):
    """Turns a specific switch ON using bitwise OR."""
    mask = 1 << switch_position
    return switch_board | mask


def turn_switch_off(switch_board, switch_position):
    """Turns a specific switch OFF using bitwise AND with a negated mask."""
    mask = ~(1 << switch_position)
    return switch_board & mask


def toggle_switch(switch_board, switch_position):
    """Toggles a specific switch (ON to OFF, or OFF to ON) using bitwise XOR."""
    mask = 1 << switch_position
    return switch_board ^ mask


# --- Sample Test Execution ---
if __name__ == "__main__":
    # Example: Switch board byte representation (binary: 00001010)
    # Switches at position 1 and 3 are ON. Positions start at 0 from the right.
    my_switches = 0b00001010

    print("Execution Results:")
    print("-" * 30)
    print(f"Initial switch board byte value: {my_switches} (Binary: {bin(my_switches)})")
    
    # 1. Inspecting switch status
    print(f"Is switch 1 ON?: {check_switch_status(my_switches, 1)}")
    print(f"Is switch 2 ON?: {check_switch_status(my_switches, 2)}")
    
    # 2. Modifying switch states
    my_switches = turn_switch_on(my_switches, 2)
    print(f"After turning switch 2 ON:      {my_switches} (Binary: {bin(my_switches)})")
    
    my_switches = turn_switch_off(my_switches, 1)
    print(f"After turning switch 1 OFF:     {my_switches} (Binary: {bin(my_switches)})")
    
    my_switches = toggle_switch(my_switches, 3)
    print(f"After toggling switch 3:        {my_switches} (Binary: {bin(my_switches)})")
