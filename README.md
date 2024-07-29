# Assembly Language Simulator

This is an Assembly Language Simulator written in Python using the Tkinter library for the GUI. It allows users to write, edit, save, and execute assembly instructions and provides a visual representation of the register values as the instructions are executed.

## Features

- **New File**: Create a new assembly code file.
- **Open File**: Open an existing assembly code file.
- **Save File**: Save the current assembly code file.
- **Cut/Copy/Paste**: Basic text editing functionalities.
- **Instruction Set Reference**: Quick reference for ARM7 assembly instructions.

## Supported Instructions

The simulator supports the following instructions:

- **MOV**: Move a value to a register.
- **MVN**: Move the complement of a value to a register.
- **ADD**: Add values from two registers and store the result in a register.
- **SUB**: Subtract values from two registers and store the result in a register.
- **RSB**: Reverse subtract values from two registers and store the result in a register.
- **AND**: Perform a bitwise AND operation on two register values and store the result.
- **ORR**: Perform a bitwise OR operation on two register values and store the result.
- **EOR**: Perform a bitwise XOR operation on two register values and store the result.
- **BIC**: Perform a bitwise AND operation with the complement of the second register value.
- **MUL**: Multiply values from two registers and store the result in a register.

## Global Registers

The simulator uses the following global registers to store values:

- **R1, R2**: General purpose registers.
- **R3**: For OR operations.
- **R4**: For AND operations.
- **R5**: For XOR operations.
- **R6**: For BIC operations.
- **R7**: For addition results.
- **R8**: For multiplication results.
- **R9**: For reverse subtraction results.
- **R10**: For subtraction results.
- **R11**: Additional general purpose register.

## How to Use

1. **Open the Application**: Run the Python script to open the Tkinter-based GUI.
2. **Write Code**: Write your assembly instructions in the text area.
3. **Execute Code**: Use the provided functions to parse and execute the instructions.
4. **View Results**: The results of the executed instructions will be stored in the corresponding registers.

## Function Descriptions

### Logical Operations

- **comp(x)**: Complements a hexadecimal value.
- **logicalOr(x, y)**: Computes the logical OR of two values.
- **logicalAnd(x, y)**: Computes the logical AND of two values.
- **logicalXor(x, y)**: Computes the logical XOR of two values.

### Register Operations

- **mov(x, y)**: Moves a value to a register.
- **mvn(x, y)**: Moves the complement of a value to a register.
- **add(x1, x2, x3)**: Adds values from two registers and stores the result in a register.
- **sub(x1, x2, x3)**: Subtracts values from two registers and stores the result in a register.
- **rsb(x1, x2, x3)**: Reverse subtracts values from two registers and stores the result in a register.
- **And(x1, x2)**: Performs a bitwise AND operation.
- **orr(x1, x2)**: Performs a bitwise OR operation.
- **eor(x1, x2)**: Performs a bitwise XOR operation.
- **bic(x1, x2)**: Performs a bitwise AND operation with the complement of the second register value.
- **mul(x1, x2, x3)**: Multiplies values from two registers and stores the result in a register.

### Instruction Parsing

- **parse(instruction_set)**: Parses the instruction set and determines which operation to perform.

### File Operations

- **newFile()**: Creates a new file.
- **openFile()**: Opens an existing file.
- **saveFile()**: Saves the current file.
- **cut()**: Cuts the selected text.
- **paste()**: Pastes the selected text.
- **copy()**: Copies the selected text.

## Additional Features

### Instruction Set References

- **branchInstr()**: Displays a reference for branch instructions.
- **stackInstr()**: Displays a reference for stack instructions.
- **loadStoreInstr()**: Displays a reference for load and store instructions.

## Installation

Ensure you have Python installed on your system. Install the Tkinter library if not already installed:

```bash
pip install tk
```

Run the script `main.py` to start the simulator.

## Future Improvements

- Expand the set of supported instructions.
- Add more detailed error handling and debugging information.
- Improve the GUI for better user experience.

## Contributing

Feel free to fork this repository, submit issues, and create pull requests. Contributions are always welcome.

## License

This project is open-source and available under the MIT License.