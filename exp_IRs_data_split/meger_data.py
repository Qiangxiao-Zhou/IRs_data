import os
import glob


def merge_files(output_file, part_files):

    with open(output_file, "wb") as outfile:
        for part_file in part_files:
            if not os.path.exists(part_file):
                print(f"file {part_file} does not exist")
                continue
            with open(part_file, "rb") as infile:
                outfile.write(infile.read())
    print(f"Merged file saved as {output_file}")


file_path = "exp_IRs_data.mat"  #file path

# merge files
output_file = "exp_IRs_data.mat"  # file name after merge
split_dir = os.path.splitext(file_path)[0] + "_split"  # content of split files
part_files = sorted(glob.glob(os.path.join(split_dir, "exp_IRs_data.mat.part*")))  
merge_files(output_file, part_files)
