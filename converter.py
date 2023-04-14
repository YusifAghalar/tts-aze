import os
from pydub import AudioSegment


folder_path = '/home/azureuser/data/wavs'  # Replace with the path to your folder
output_folder = '/home/azureuser/data/mono/' 
files = []

# Walk through all files in the directory tree
for root, directories, filenames in os.walk(folder_path):
    for filename in filenames:
        # Append the full file path to the list of files
        files.append(os.path.join(root, filename))



for file in files:
    sound = AudioSegment.from_wav(file)
    sound = sound.set_channels(1)
    sound.export(output_folder+file.split("data/")[1], format="wav")

