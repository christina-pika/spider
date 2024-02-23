## Instructions for Running the Youtube Video Download Script From CSV file

To run the video download script, please follow these steps:

1. **Pull this repository** to your local machine using the command:
   ```
   git pull <repository-url>
   ```
   
2. **Navigate to the 'spider' folder** within the pulled repository by running:
   ```
   cd spider
   ```
   
3. **Change directory to the 'video' folder** to locate the video files by executing:
   ```
   cd video
   ```
   
4. **Modify the `csv_file_path` in the `set.json` file** to point to your CSV file containing the video links. This step is crucial for the script to know where to fetch the video links from.

5. **Run the `run.py` script** located in the `src` folder to start the video download process. You can do this by navigating to the `src` folder and executing the command:
   ```
   python path/to/run.py
   ```

Please ensure you have Python installed on your machine and have the necessary permissions to execute these commands.
