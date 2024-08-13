import os
import shutil
import time
import argparse
import logging

def setup_logging(log_file_path):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ]
    )

def sync_folders(source_folder, replica_folder):
    if not os.path.exists(replica_folder):
        os.makedirs(replica_folder)

    for item in os.listdir(source_folder):
        source_item = os.path.join(source_folder, item)
        replica_item = os.path.join(replica_folder, item)

        if os.path.isdir(source_item):
            sync_folders(source_item, replica_item)
        else:
            if not os.path.exists(replica_item) or os.path.getmtime(source_item) > os.path.getmtime(replica_item):
                shutil.copy2(source_item, replica_item)
                logging.info(f"Copied/Updated file: {replica_item}")

    for item in os.listdir(replica_folder):
        replica_item = os.path.join(replica_folder, item)
        source_item = os.path.join(source_folder, item)

        if not os.path.exists(source_item):
            if os.path.isdir(replica_item):
                shutil.rmtree(replica_item)
                logging.info(f"Removed folder: {replica_item}")
            else:
                os.remove(replica_item)
                logging.info(f"Removed file: {replica_item}")

def main():
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument("source_folder", help="Path to the source folder")
    parser.add_argument("replica_folder", help="Path to the replica folder")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("sync_interval", type=int, help="Synchronization interval in seconds")

    args = parser.parse_args()

    setup_logging(args.log_file)

    while True:
        logging.info("Starting synchronization...")
        sync_folders(args.source_folder, args.replica_folder)
        logging.info("Synchronization completed.")
        time.sleep(args.sync_interval)

if __name__ == "__main__":
    main()