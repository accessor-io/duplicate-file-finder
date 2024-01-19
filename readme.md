##Duplicate File Finder (DFF)
###Description

Duplicate File Finder (DFF) is a Python-based command-line utility designed to efficiently identify and manage duplicate files within a specified set of directories. Utilizing the SHA-1 hashing algorithm, DFF ensures accurate detection by comparing file contents rather than just file sizes, which provides a more reliable identification of duplicates.

The utility offers a user-friendly interactive prompt, allowing users to review and manage detected duplicates. Users can delete duplicates individually or in bulk, examine the content of the files, or open files using a specified command. With customizable command-line arguments, DFF provides flexibility to cater to different user needs, including minimum file size consideration and symlink following.
Features

    Efficient Duplicate Detection: Uses SHA-1 hashing to ensure that files with identical contents are flagged as duplicates.
    Interactive Management: Offers an interactive prompt for users to manage duplicates – delete, view, or open files.
    Customizable File Size Filter: Users can define a minimum file size for files to be considered, optimizing performance for large datasets.
    Symlink Support: Provides an option to follow or ignore symlinks during the scanning process.
    User-Friendly Commands: Customizable command to open files and simple commands within the interactive prompt for easy management.

###Usage

    Clone the Repository:

    sh

```
git clone https://github.com/accessor-io/duplicate-file-finder.git

cd DuplicateFileFinder
```
```
Run the Script:

sh
```
    python duplicate_file_finder.py [-s minsize] [-c command] [-S] <directories>

   ### Arguments:
        -s or --minsize: Specify the minimal file size in bytes.
        -c or --command: Command to use to open files in the prompt.
        -S or --symlinks: Follow symlinks.
        <directories>: Directories to scan for duplicate files.

    Interact with the Prompt: Follow the instructions in the prompt to manage duplicate files.

### Download and Installation

#### To download and use DFF, follow these steps:

    #### Download:
        Navigate to the GitHub repository: Duplicate File Finder
        Click on the 'Code' button and select 'Download ZIP', or use the command line to clone the repo.

    Unzip (if downloaded as ZIP):
        Unzip the downloaded file in your preferred directory.

    Installation:
        DFF requires Python to run. Ensure you have Python installed on your system.
        No additional libraries are required for the basic functionality.

    Execution:
        Open a terminal or command prompt.
        Navigate to the directory where you placed DFF.
        Run the script with appropriate arguments as mentioned in the Usage section.

