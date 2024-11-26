# File Scanner and Categorizer

This Python script scans a specified directory and categorizes files into various types. It provides options for detailed logs or a progress bar to visualize the scanning process. The categorized files are then displayed based on user selections (e.g., executable files, image files, video files, hidden files). It also identifies empty directories within the scanned path.

## Features

- **Scan directories**: Scan any directory to analyze its contents.
- **Categorize files**: Categorize files into `.exe` files, image files (e.g., `.png`, `.jpg`), video files (e.g., `.mp4`, `.avi`), and hidden files.
- **Track empty directories**: Identify and list empty directories.
- **Progress bar or detailed log**: Choose between a progress bar for a quick overview or detailed logs to track the scanning process.
- **Re-scan or switch directories**: You can re-scan the same directory or switch to a new directory at any time.

## Prerequisites

Before running the script, ensure that you have the following:

- **Python 3.x**: You need Python 3.x installed. You can download it from [here](https://www.python.org/downloads/).
- **Required Python packages**:
  - `tqdm` (for the progress bar): Install it using pip by running the following command:

    ```bash
    pip install tqdm
    ```

- **Windows Batch File**: A `.bat` file is included for easy execution of the Python script in Windows.

## Installation

1. **Clone this repository**:

    ```bash
    git clone https://github.com/Mifu999/Super-Files-Scanner
    ```

2. **Install dependencies**:
   
   Open a terminal (or command prompt) and navigate to the repository folder. Then, install the required Python package:

    ```bash
    pip install tqdm
    ```

3. **Using the Batch File**:
   
   For Windows users, simply double-click the `start.bat` file to run the script. This will execute the `main.py` script.

4. **Manual execution**:

    If you prefer to run the script manually, use the following command from your terminal:

    ```bash
    python main.py
    ```

## Usage

### 1. Select Scan Mode

When you run the script, you will be prompted to choose the scanning mode:

- **Detailed Logs**: Displays detailed logs of the scan process, showing folder names and the number of files found.
- **Progress Bar**: Displays a progress bar for the scan, showing the overall progress as the files are analyzed.

### 2. Specify Directory to Scan

After choosing the scan mode, you will be asked to enter the directory path you want to scan. Ensure that the directory path is correct and accessible.

### 3. View Scan Results

Once the scan is completed, you can view the following results:

- Total files found in the directory.
- Total directories.
- Number of empty directories.
- Number of `.exe` files, image files, video files, and hidden files.

### 4. File Categories

You will be able to choose the following options to display file paths:

1. `.exe` files
2. Image files (e.g., `.png`, `.jpg`)
3. Video files (e.g., `.mp4`, `.avi`)
4. Hidden files
5. Scan another directory
6. Empty directories
7. Re-scan the same directory
8. Quit the program

### 5. Re-scan or Switch Directories

At any time, you can opt to re-scan the current directory or switch to another directory to scan by selecting the appropriate option.

## Example Usage

1. Start the script by running the `.bat` file or `python main.py` from the terminal.
2. Choose **detailed** mode or **progress** mode.
3. Enter the path to the directory you want to scan, e.g., `C:\Users\YourName\Documents`.
4. The script will scan the directory and categorize the files.
5. After the scan, you can view the categorized file paths and perform additional actions as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this repository and submit pull requests. If you find any bugs or have suggestions for improvements, please open an issue.
