"""
We will attempt to generate music based on the patterns generated
from the julia set fractals
"""

import pygame
import numpy as np
from PIL import Image


# Window dimensions
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_DIMENSIONS = (WINDOW_WIDTH, WINDOW_HEIGHT)


# Julia-set parameters
C = complex(-0.8, 0.156)
MAX_ITERATIONS = 255
ESCAPE_RADIUS = 2           # Threshold (we consider this to be the tipping point for unstability)

# Pygame environment setup
pygame.init()   # initialize pygame

screen = pygame.display.set_mode(WINDOW_DIMENSIONS) # initialize pygame window
clock = pygame.time.Clock() # pygame clock init

font = pygame.font.SysFont("monospace", 16) # initialize pygame font

def julia_set(C, MAX_ITERATIONS, ESCAPE_RADIUS, WINDOW_DIMENSIONS):
    """
    Generates the Julia Set Fractal
    """

    image_array = np.zeros(WINDOW_DIMENSIONS)

    for _x in range(WINDOW_WIDTH):
        for _y in range(WINDOW_HEIGHT):
            _z = complex((4.0 * _x / WINDOW_WIDTH - 2), (4.0 * _y / WINDOW_HEIGHT - 2))
            iterations = 0

            while abs(_z) < ESCAPE_RADIUS and iterations < MAX_ITERATIONS:
                _z = _z**2 + C
                iterations += 1

            if iterations == MAX_ITERATIONS:
                image_array[_x][_y] = 1 * 255
            else:
                image_array[_x][_y] = (iterations / MAX_ITERATIONS) * 255

    return image_array

def map_to_notes(image, base_note, octaves, notes_per_octave):
    """
    UNDOCUMENTED
    """

    notes = []

    for _x in range(WINDOW_WIDTH):
        note = int(base_note + octaves * notes_per_octave * image[_x])
        notes.append(note)

    return notes

def play_melody(notes):
    """
    UNDOCUMENTED
    """

    for note in notes:
        frequency = 440 * 2 ** ((note - 69) / 12)
        duration = 50
        pygame.mixer.Sound(f"sound/note_{note}.wav").set_volume(0.5)
        pygame.time.wait(duration)

def load_note_sounds(base_note, octaves, notes_per_octave):
    """
    UNDOCUMENTED
    """

    for octave in range(octaves):
        for note in range(notes_per_octave):
            note_number = octave * notes_per_octave + note
            frequency = 440 * 2**((note_number - 69) / 12)
            pygame.mixer.Sound(f"sound/note_{note_number}.wav").set_volume(0.5)

# def make_image():
#     """
#     UNDOCUMENTED
#     """

#     image_array = julia_set(
#         C=C,
#         MAX_ITERATIONS=MAX_ITERATIONS,
#         ESCAPE_RADIUS=ESCAPE_RADIUS,
#         WINDOW_DIMENSIONS=WINDOW_DIMENSIONS
#     )
#     image = Image.fromarray(np.uint8(image_array))
#     image.save(f"some_image{str(WINDOW_DIMENSIONS)}.png")

# make_image()
