import os

DIRS = [
    'gpt3_logs',
    'internal_notes',
    'nexus'
]

def empty_dir(dir):
    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete {filename}. Reason: {e}")
    print(f"Cleared dir: {dir}")

if __name__ == '__main__':
    for dir in DIRS:
        empty_dir(dir)
        