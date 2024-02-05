import os

def split_file_by_size(file_content, target_size):
    part_count = -(-len(file_content) // target_size)  # Equivalent to math.ceil
    for i in range(part_count):
        start = i * target_size
        length = min(target_size, len(file_content) - start)
        content_part = file_content[start:start + length]

        output_file_name = os.path.join(output_folder, f"part{i + 1:03d}.txt")
        with open(output_file_name, 'w', encoding='utf-8') as output_file:
            output_file.write(content_part)

    print('\nProcessing complete.')

# Welcome message centered without color or formatting
welcome_message = "{:^80}".format("WELCOME TO SPLIT | ELITE KAMRUL")
print(welcome_message)

# Main loop
while True:
    # Get user input for target size in megabytes
    target_size_mb = input("Enter the target size in megabytes: ")
    
    if target_size_mb:
        target_size = int(float(target_size_mb) * 1024 * 1024)  # Convert to bytes
    else:
        print("Please provide a valid target size.")
        continue

    # Get user input for file path and output folder
    file_path = input("Enter the file path: ").strip('\'\"')  # Remove quotes from the file path
    output_folder = input("Enter the output folder: ").strip('\'\"')  # Remove quotes from the folder path

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Display message before starting the file splitting process
    print("{:^80}".format("Commencement of splitting in progress - please await."))

    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # Split the file based on the target size
    split_file_by_size(file_content, target_size)

    # Ask the user whether to run the script again or exit
    run_again = input("Do you want to run the script again? (yes/no): ").lower()
    if run_again in ['yes', 'y']:
        continue
    elif run_again in ['no', 'n']:
        break
    else:
        print("Invalid response. Exiting the script.")
        break
