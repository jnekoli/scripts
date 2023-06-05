"""
Copies directory contents to a specified location.  
Ignores files that are: 0 bytes, replacing identical sizes,
or that have an extension in badexts (ex: .zip.mkv, .!qB.mkv).
https://github.com/jnekoli for future updates.

"""
import os
import shutil

def copy_files_recursively(source_dir, destination_dir):
    for root, dirs, files in os.walk(source_dir):
        # Create corresponding directories in the destination
        dest_root = os.path.join(destination_dir, os.path.relpath(root, source_dir))
        os.makedirs(dest_root, exist_ok=True)

        # Copy files from the source to the destination
        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(dest_root, file)
            if os.path.getsize(source_file == 0):
                print("skipping 0b file: " + source_file)
                continue
            s = source_file[:-4] #strip .mkv
            s = s[:-4] if s.lower().endswith(".!qb") else s
            r_, ext = os.path.splitext(s)
            badexts =[".jpg",".jpeg",".gif",".png",
            ".log",".bmp",".txt",".cue",".rar",".zip",".m3u",".sfv",".cue",
            ".nfo"]
            if ext.lower() in badexts:
                print("skipping " + ext + ": " + s)
                continue
            
            if os.path.exists(dest_file) and os.path.getsize(source_file) <= os.path.getsize(dest_file):
                # Skip copying if the destination file exists and the source file is not smaller
                continue
            #print("copying..." + source_file)
            shutil.copy2(source_file, dest_file)  # Copy file preserving metadata

# Example usage
source_directory = 'f:\\o'
destination_directory = 'e:\\o' #/path/to/destination/directory'

copy_files_recursively(source_directory, destination_directory)
