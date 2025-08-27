def file_read_write():
    # Ask the user for the input file
    input_file = input("Enter the name of the file to read: ")

    try:
        # Try opening the file for reading
        with open(input_file, "r") as f:
            content = f.read()

        # Modify the content (example: make it uppercase)
        modified_content = content.upper()

        # Create a new filename
        output_file = "modified_" + input_file

        # Write modified content to a new file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ Successfully created '{output_file}' with modified content!")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# Run the function
file_read_write()
