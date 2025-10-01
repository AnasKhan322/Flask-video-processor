import subprocess
import os

def apply_greyscale(input_path, output_path):
    """
    Converts the input video to greyscale.
    """
    cmd = [
        'ffmpeg',
        '-y',  # overwrite output if exists
        '-i', input_path,
        '-vf', 'format=gray',
        output_path
    ]
    subprocess.run(cmd, check=True)
    print(f"Greyscale video saved to {output_path}")

def apply_color_invert(input_path, output_path):
    """
    Inverts the colors of the input video.
    """
    cmd = [
        'ffmpeg',
        '-y',
        '-i', input_path,
        '-vf', 'lutrgb=r=negval:g=negval:b=negval',
        output_path
    ]
    subprocess.run(cmd, check=True)
    print(f"Inverted color video saved to {output_path}")

 
