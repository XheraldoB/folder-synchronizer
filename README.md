# folder-synchronizer
A Python script for synchronizing two folders, ensuring the replica folder is an exact copy of the source folder. The script runs periodically, logging all actions to a specified log file.

## Usage

Run the script from the command line with the following arguments:

python sync_script.py "source_folder_path" "replica_folder_path" "log_file_path" sync_interval

'source_folder_path': Path to the source folder.
'replica_folder_path': Path to the replica folder.
'log_file_path': Path to the log file.
'sync_interval': Synchronization interval in seconds.

First example
python sync_script.py "C:\\path\\to\\source" "C:\\path\\to\\replica" "C:\\path\\to\\logfile.log" 30

Second real example in CMD.
I have a folder named sync_folders_bilo, which contains two subfolders: source and replica, along with a text logfile.

C:\Users\bigea\Downloads\sync_folders_bilo>python sync_folders.py "C:\Users\bigea\Downloads\sync_folders_bilo\source" "C:\Users\bigea\Downloads\sync_folders_bilo\replica" "C:\Users\bigea\Downloads\sync_folders_bilo\logfile.log" 30
And in order to stop it, press "CTRL + C"
