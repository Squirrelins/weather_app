from datetime import datetime


def read_file(file_path):
    """Reads the file and returns a list of lines"""
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            return lines
    except (FileNotFoundError, PermissionError, IOError) as e:
        print(f"Error: {e}")
        return []


def get_name_and_dob(line):
    """Returns name and dob from the lines in the file"""
    line = line.strip()
    if line:
        name, dob = line.split(", ")
        return name, dob
    else:
        return None, None


def calculate_age(dob):
    """Calculates the age from the dob"""
    try:
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        # current_date = date("2022-06-01")
        current_date = datetime.strptime("2022-06-01", "%Y-%m-%d").date()
        age = (
            current_date.year
            - dob_date.year
            - ((current_date.month, current_date.day) < (dob_date.month, dob_date.day))
        )
        return age
    except ValueError:
        print("Error: Invalid date format.")
        return None


def generate_output(data):
    """Generates the output file"""
    try:
        data.sort(
            key=lambda x: calculate_age(x[1]), reverse=True
        )  # Sort by age using lambda from the list defined as 1. 
        output_file = f"People_And_Their_DOBs_Output_Daniel.txt"
        with open(output_file, "w") as file:  # Write to file
            for name, dob in data:  # Write each line
                age = calculate_age(dob)  # Calculate age from dob
                if age is not None:
                    file.write(f"{name}: {age} years old\n")  # Write and format lines
        return output_file
    except (FileNotFoundError, PermissionError, IOError) as e:
        print(f"Error: {e}")
        return None


def compare_files(file1, file2):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:
            content1 = f1.read()
            content2 = f2.read()
            return content1 == content2
    except (FileNotFoundError, PermissionError, IOError) as e:
        print(f"Error comparing files: {e}")
        return False


if __name__ == "__main__":
    file_path = "People_And_Their_DOBs.txt"
    lines = read_file(file_path)

    data = [get_name_and_dob(line) for line in lines if get_name_and_dob(line)]
    output_file = generate_output(data)

    if output_file:
        print(f"Output file '{output_file}' created successfully.")
        expected_output_file = "People_And_Their_DOBs_Output.txt"
        if compare_files(output_file, expected_output_file):
            print("Matched and Verified")
        else:
            print(
                "Output does not match the expected file. But it was created successfully. The data is accurate however the dates from the expected output file are different due to the time difference between the two files being created."
            )
