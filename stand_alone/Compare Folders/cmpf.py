import os
import filecmp

def compare_folders(folder1, folder2):
    with open("Differences.txt", 'w') as diff_file:
        with open("Comparison.txt", 'w') as result_file:
            for dirpath, dirnames, filenames in os.walk(folder1):
                for filename in filenames:
                    file_path1 = os.path.join(dirpath, filename)
                    rel_path = os.path.relpath(file_path1, folder1)
                    file_path2 = os.path.join(folder2, rel_path)

                    if os.path.exists(file_path2):
                        if filecmp.cmp(file_path1, file_path2) and os.path.getsize(file_path1) == os.path.getsize(file_path2):
                            result_file.write(f"{rel_path}: Same\n")
                        else:
                            result_file.write(f"{rel_path}: Different\n")
                            diff_file.write(f"{rel_path}: Different\n")
                    else:
                        result_file.write(f"{rel_path}: Not found in {folder2}\n")
                        diff_file.write(f"{rel_path}: Not found in {folder2}\n")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python cmpf.py <folder1> <folder2>")
        sys.exit(1)

    folder1 = sys.argv[1]
    folder2 = sys.argv[2]
    output_file = "differences.txt"

    if not os.path.exists(folder1) or not os.path.exists(folder2):
        print("Error: Input folders do not exist.")
        sys.exit(1)

    compare_folders(folder1, folder2)
    print(f"Comparison results written to {output_file}")
