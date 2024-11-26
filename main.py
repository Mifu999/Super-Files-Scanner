import os
import time
from tqdm import tqdm

def count_files_in_directory(directory, mode):
    total_files = 0
    total_dirs = 0
    empty_dirs = []
    exe_files = []
    image_files = []
    video_files = []
    hidden_files = []

    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'}
    video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.flv'}

    if mode == 'progress':
        total_files_count = sum(len(files) for _, _, files in os.walk(directory))
        pbar = tqdm(total=total_files_count, desc="Scanning", unit="file", ascii=True)

    for root, dirs, files in os.walk(directory):
        total_dirs += len(dirs)
        if not files and not dirs:
            empty_dirs.append(root)

        if mode == 'detailed':
            print(f"Scanning folder: {root} | Files found: {len(files)}")

        for file in files:
            total_files += 1
            file_path = os.path.join(root, file)
            if file.startswith('.'):
                hidden_files.append(file_path)
            elif file.lower().endswith('.exe'):
                exe_files.append(file_path)
            elif any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(file_path)
            elif any(file.lower().endswith(ext) for ext in video_extensions):
                video_files.append(file_path)

            if mode == 'progress':
                pbar.update(1)

    if mode == 'progress':
        pbar.close()

    return total_files, total_dirs, empty_dirs, exe_files, image_files, video_files, hidden_files

def print_file_paths(category, file_list):
    if file_list:
        print(f"Paths of {category} files:")
        for file in file_list:
            print(file)
    else:
        print(f"No {category} files found.")

def print_empty_dirs(empty_dirs):
    if empty_dirs:
        print("Paths of empty folders:")
        for directory in empty_dirs:
            print(directory)
    else:
        print("No empty folders found.")

while True:
    mode = input("Do you want to see detailed logs or a progress bar? (detailed/progress): ").strip().lower()
    
    if mode not in ['detailed', 'progress']:
        print("Invalid mode. Please choose 'detailed' or 'progress'.")
        continue
    
    directory = input("Please enter the directory path to scan: ")
    
    if not os.path.isdir(directory):
        print("The entered path is not valid.")
        continue
    
    total_files, total_dirs, empty_dirs, exe_files, image_files, video_files, hidden_files = count_files_in_directory(directory, mode)

    while True:
        start_time = time.time()
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        print(f"\nTotal scan time: {elapsed_time:.2f} seconds")
        print(f"Total files: {total_files}")
        print(f"Total directories: {total_dirs}")
        print(f"Empty directories: {len(empty_dirs)}")
        print(f".exe files: {len(exe_files)}")
        print(f"Image files: {len(image_files)}")
        print(f"Video files: {len(video_files)}")
        print(f"Hidden files: {len(hidden_files)}")
        
        choice = input("\nEnter the number of the category to see the file paths (1: .exe, 2: images, 3: videos, 4: hidden, 5: scan another directory, 6: empty directories, 7: rescan the directory, 0: quit): ")
        
        if choice == '1':
            print_file_paths("executable", exe_files)
        elif choice == '2':
            print_file_paths("image", image_files)
        elif choice == '3':
            print_file_paths("video", video_files)
        elif choice == '4':
            print_file_paths("hidden", hidden_files)
        elif choice == '5':
            break
        elif choice == '6':
            print_empty_dirs(empty_dirs)
        elif choice == '7':
            total_files, total_dirs, empty_dirs, exe_files, image_files, video_files, hidden_files = count_files_in_directory(directory, mode)
        elif choice == '0':
            print("Closing the program.")
            exit()
        else:
            print("Invalid choice.")
