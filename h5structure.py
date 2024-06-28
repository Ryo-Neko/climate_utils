import sys
import h5py

def print_h5_keys(file_path):
    def print_keys(name, obj):
        indent = "  " * (name.count("/"))
        if name.count("/") == 0:
            print("-" * 36)
        if isinstance(obj, h5py.Group):
            print(f"{indent}Group: {name.split('/')[-1]}")
        elif isinstance(obj, h5py.Dataset):
            print(f"{indent}Dataset: {name.split('/')[-1]}")

    with h5py.File(file_path, "r") as file:
        file.visititems(print_keys)

if __name__ == "__main__":
    args = sys.argv
    print_h5_keys(args[1])
