""" https://www.codewars.com/kata/526c7b931666d07889000a3c/train/python
Date: 08/02/2022
Coded by: Amit Avi Eshel
"""

from random import choice
from py_console import console, bgColor, textColor

"""TODO ~!DONE
add function exeInstructionVerbose() which prints verbose explanation
on execution to replace exeInstruction when isVerbose=True
"""

#!finished this and im really proud!


def interpret(code):
    # usefull for debugging
    isVerbose = True
    # make var matrix a list of strings where each index is a `line`
    matrix = [list(i) for i in code.split('\n')]
    # driver functions for pointer movments

    def step() -> None:

        def mvUp() -> None:
            if ptr['y'] == 0:
                # bordercase to loop around if reached ceiling
                ptr['y'] = len(matrix) - 1
            else:
                ptr['y'] -= 1

        def mvDown() -> None:
            if ptr['y'] == (len(matrix)-1):
                # bordercase to loop around if reached bottom
                ptr['y'] = 0
            else:
                ptr['y'] += 1

        def mvLeft() -> None:
            if ptr['x'] == 0:
                # bordercase to loop around if reached left border
                ptr['x'] == len(matrix[ptr['y']]) - 1
            else:
                ptr['x'] -= 1

        def mvRight() -> None:
            if ptr['x'] == len(matrix[ptr['y']]) - 1:
                # bordercase to loop around if reached right border
                ptr['x'] == 0
            else:
                ptr['x'] += 1
        if ptr['dir'] == '>':
            mvRight()
        if ptr['dir'] == '<':
            mvLeft()
        if ptr['dir'] == '^':
            mvUp()
        if ptr['dir'] == 'v':
            mvDown()

    stack = []

    def pop(n=0):
        """
        pop() -> pop an element off the stack and return it as INT
        pop(n) -> pop n elements off the stack and return them as LIST
        """
        if n == 0:
            if len(stack):
                return int(stack.pop())
            else:
                return 0
        else:
            ret = []
            while n > 0:
                if len(stack):
                    ret.append(int(stack.pop()))
                else:
                    ret.append(0)
                n -= 1
            return ret

    def push(a) -> None: stack.append(a)

    ptr = {
        "x": 0,
        "y": 0,
        "dir": '>',
    }

    # i might be doin this global vars thing wrong
    output = ''
    end = False

    # return current instruction based on ptr
    def getInstruction() -> str: return matrix[ptr['y']][ptr['x']]
    # IMPORTANT: matrix coordinates go (y,x)!!!

    # instruction handeling
    def exeInstruction(instruction) -> None:
        nonlocal output
        if instruction == ' ':
            pass
        elif instruction in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            push(instruction)
        elif instruction == '+':
            a, b = pop(2)
            push(a+b)
        elif instruction == '-':
            a, b = pop(2)
            push(b-a)
        elif instruction == '*':
            a, b = pop(2)
            push(a*b)
        elif instruction == '/':
            a, b = pop(2)
            if a == 0:
                push(0)
            else:
                push(b/a)
        elif instruction == '%':
            a, b = pop(2)
            if a == 0:
                push(0)
            else:
                stack.push(b % a)
        elif instruction == '!':
            if pop():
                push(0)
            else:
                push(1)
        elif instruction == '`':
            a, b = pop(2)
            if b > a:
                push(1)
            else:
                push(0)
        elif instruction in ('>', '<', '^', 'v'):
            ptr['dir'] = instruction
        elif instruction == '?':
            ptr['dir'] = choice('>', '<', '^', 'v')
        elif instruction == '_':
            if pop():
                ptr['dir'] = '<'
            else:
                ptr['dir'] = '>'
        elif instruction == '|':
            if pop():
                ptr['dir'] = '^'
            else:
                ptr['dir'] = 'v'
        elif instruction == '"':
            step()
            instruction = getInstruction()
            while instruction != '"':
                push(ord(instruction))
                step()
                instruction = getInstruction()
        elif instruction == ':':
            if len(stack):
                a = pop()
                push(str(a))
                push(str(a))
            else:
                push(0)
        elif instruction == '\\':
            if len(stack) == 1:
                push(0)
            else:
                a, b = pop(2)
                push(a)
                push(b)
        elif instruction == '$':
            pop()
        elif instruction == '.':
            output += str(pop())
        elif instruction == ',':
            output += chr(pop())
        elif instruction == '#':
            step()
        elif instruction == 'p':
            y, x, v = pop(3)
            matrix[y][x] = chr(v)
        elif instruction == 'g':
            y, x = pop(2)
            push(ord(matrix[y][x]))
        elif instruction == '@':
            nonlocal end
            end = True

    def verbosePrint(Inst):
        console.info(f"Stack: {stack}")
        console.success(f"Executing Instruction {Inst}")
        verboseMatrix = matrix.copy()
        beforeHighlight = verboseMatrix[ptr['y']][ptr['x']]
        verboseMatrix[ptr['y']][ptr['x']] = console.highlight(
            beforeHighlight, bgColor=bgColor.LIGHTYELLOW_EX)
        for row in verboseMatrix:
            console.log("".join(row))
        verboseMatrix[ptr['y']][ptr['x']] = beforeHighlight
        input()

    while not end:
        Instruction = getInstruction()
        if isVerbose:
            verbosePrint(Instruction)
        exeInstruction(Instruction)
        step()

    return output


print(interpret('>987v>.v\nv456<  :\n>321 ^ _@'))
