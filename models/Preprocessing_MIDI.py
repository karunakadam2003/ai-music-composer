import os
import glob
import pretty_midi
import numpy as np
from magenta.music import midi_io
from magenta.music import sequences_lib
from magenta.music import midi_sequence_to_piano_roll

# Path to the MAESTRO MIDI folder
midi_folder = "C:/Users/karun/Documents/ai-music-composer/maestro-v1.0.0-midi/maestro-v1.0.0"

# Function to process MIDI files
def process_midi_files(midi_folder):
    midi_files = glob.glob(os.path.join(midi_folder, "**", "*.mid"), recursive=True)
    piano_rolls = []
    
    for midi_file in midi_files:
        # Load the MIDI file using pretty_midi
        midi_data = pretty_midi.PrettyMIDI(midi_file)

        # Convert MIDI data to piano roll (time steps x pitch)
        piano_roll = midi_data.get_piano_roll(fs=100)  # Use a 100Hz frequency for time steps

        # Normalize the piano roll (optional)
        piano_roll = piano_roll / np.max(piano_roll)
        
        piano_rolls.append(piano_roll)
        
    return piano_rolls

# Process all MIDI files in the dataset
piano_rolls = process_midi_files(midi_folder)

# Example: Print the shape of the first piano roll
print("Shape of first piano roll:", piano_rolls[0].shape)
# Save processed piano rolls as a numpy file
np.save("processed_piano_rolls.npy", np.array(piano_rolls))

# Optionally, you can split the dataset into training and validation sets
