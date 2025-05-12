import os
import shutil

# Define source and destination directories
source_dirs = {
    #"best_ori": "data/big_wavy1/best_ori",
    #"conf": "data/big_wavy1/conf",
    "mask": "data/big_wavy1/mask"
}

destination_dir = "strand_integration/data/straight_s"

# Mapping of source directory names to new image names
name_mapping = {
    "best_ori": "orientation2d",
    "conf": "intensity",
    "mask": "mask"
}

# Loop over each source directory
for dir_key, src_dir in source_dirs.items():
    # Verify the source directory exists
    if not os.path.exists(src_dir):
        print(f"Source directory {src_dir} does not exist.")
        continue

    # Loop over each image file in the source directory
    for filename in os.listdir(src_dir):
        if filename.endswith(".png") or filename.endswith(".JPG"):
            # Get the image number by stripping the .png extension and converting to an integer
            image_number = int(filename.split('.')[0])

            # Calculate the existing folder name by subtracting 1 from the image number
            folder_name = f"{image_number - 1:02d}"  # Ensures two-digit format with leading zeros
            dest_folder = os.path.join(destination_dir, folder_name)

            # Check if the destination folder exists
            if not os.path.exists(dest_folder):
                print(f"Destination folder {dest_folder} does not exist. Skipping file {filename}.")
                continue

            # Define the new file name based on the source directory
            new_file_name = f"{name_mapping[dir_key]}.png"
            dest_path = os.path.join(dest_folder, new_file_name)

            # Move the file to the new location with the new name
            shutil.copy2(os.path.join(src_dir, filename), dest_path)

print("Images moved and renamed successfully.")

