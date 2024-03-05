from math import sin, cos
import numpy as np
import os
import sys

os.environ['TERM'] = 'xterm-256color'

A, B, C = 0.0, 0.0, 0.0

cubeWidth = 20.0
width, height = 160, 44
backgroundASCIICode = ord(' ')
distanceFromCam = 40
K1 = 40.0
zBuffer = np.zeros((44, 160), dtype=float)
buffer = np.full((44, 160), backgroundASCIICode, dtype=np.uint8)

incrementSpeed = 4

x, y, z = 0.0, 0.0, 0.0
ooz = 0.0
xp, yp = 0, 0

idx = 0


def calculateX(i: int, j: int, k: int) -> float:
    """
    Calculate the X coordinate in 3D space based on input parameters.

    Args:
        i (int): X coordinate in 3D space.
        j (int): Y coordinate in 3D space.
        k (int): Z coordinate in 3D space.

    Returns:
        float: Calculated X coordinate.
    """
    return (j * sin(A) * sin(B) * cos(C) - k * cos(A) * sin(B) * cos(C) +
            j * cos(A) * sin(C) + k * sin(A) * sin(C) + i * cos(B) * cos(C))


def calculateY(i: int, j: int, k: int) -> float:
    """
    Calculate the Y coordinate in 3D space based on input parameters.

    Args:
        i (int): X coordinate in 3D space.
        j (int): Y coordinate in 3D space.
        k (int): Z coordinate in 3D space.

    Returns:
        float: Calculated Y coordinate.
    """
    return (j * cos(A) * cos(C) + k * sin(A) * cos(C) -
            j * sin(A) * sin(B) * sin(C) + k * cos(A) * sin(B) * sin(C) -
            i * cos(B) * sin(C))


def calculateZ(i: int, j: int, k: int) -> float:
    """
    Calculate the Z coordinate in 3D space based on input parameters.

    Args:
        i (int): X coordinate in 3D space.
        j (int): Y coordinate in 3D space.
        k (int): Z coordinate in 3D space.

    Returns:
        float: Calculated Z coordinate.
    """
    return k * cos(A) * cos(B) - j * sin(A) * cos(B) + i * sin(B)


def calculateForSurface(cubeX: float, cubeY: float, cubeZ: float, ch: int) -> None:
    """
    Calculate the 2D screen coordinates for a given 3D point on the cube surface.

    Args:
        cubeX (float): X coordinate of the cube point.
        cubeY (float): Y coordinate of the cube point.
        cubeZ (float): Z coordinate of the cube point.
        ch (int): ASCII code for the character representing the surface point.

    Returns:
        None
    """
    global x, y, z
    global ooz
    global xp, yp

    x = calculateX(cubeX, cubeY, cubeZ)
    y = calculateY(cubeX, cubeY, cubeZ)
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam

    ooz = 1/z

    xp = int(width / 2 - 2 * cubeWidth + K1 * ooz * x * 2)
    yp = int(height / 2 + K1 * ooz * y)

    if 0 <= yp < height and 0 <= xp < width:
        if ooz > zBuffer[yp, xp]:
            zBuffer[yp, xp] = ooz
            buffer[yp, xp] = ord(ch)


def main():
    """
    Main function to generate and display the 3D ASCII art by continuously rotating the cube.

    Returns:
        int: Exit code (never actually returns as it runs in an infinite loop).
    """
    global buffer, zBuffer
    global A, B

    # print(f"\x1b[2J", end='', flush=True)
    while True:
        buffer = np.full((height, width), backgroundASCIICode, dtype=np.uint8)
        zBuffer = np.full((height, width), float('-inf'), dtype=float)
        for cubeX in np.arange(-cubeWidth, cubeWidth, incrementSpeed):
            for cubeY in np.arange(-cubeWidth, cubeWidth, incrementSpeed):
                calculateForSurface(cubeX, cubeY, -cubeWidth, 'c')          # .
                calculateForSurface(cubeWidth, cubeY, cubeX, 'a')           # $
                calculateForSurface(-cubeWidth, cubeY, -cubeX, 'r')    # ~
                calculateForSurface(-cubeX, cubeY, cubeWidth, 't')          # #
                calculateForSurface(cubeX, -cubeWidth, -cubeY, 'e')         # ;
                calculateForSurface(cubeX, cubeWidth, cubeY, 'r')           # +

        # print(f"\x1b[2J", end='', flush=True)
        # print(f"\x1b[H", end='', flush=True)
        os.system('clear')
        sys.stdout.flush()

        for row in buffer:
            for char in row:
                print(chr(char), end='')
            print()

        A += 0.005
        B += 0.005

    return 0


if __name__ == "__main__":
    main()