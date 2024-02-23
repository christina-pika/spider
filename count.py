import os

def count_files(directory):
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

directory_path = '/Users/christina/Desktop/spider/youtube/video'
file_count = count_files(directory_path)
print(f"Number of files in {directory_path}: {file_count}")
