import pandas as pd

# Define input and output file paths
input_file_path = "MAINDATASETS.txt"
output_csv_path = "MAINDATASETS.csv"

# Initialize a list to hold the processed data
output_data = []

# Process the text file
with open(input_file_path, "r") as file:
    chain_info = {}
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            # Save previous chain_info if it exists
            if chain_info:
                output_data.append(chain_info)

            # Parse the new entry header
            chain_info = {
                "Protein_ID": line[1:],  # Remove the '>' symbol
                "Sequence": ""  # Initialize sequence
            }
        else:
            # Append sequence data to the current chain_info
            chain_info["Sequence"] += line

    # Add the last entry if exists
    if chain_info:
        output_data.append(chain_info)

# Convert the processed data to a DataFrame
df = pd.DataFrame(output_data)

# Save the DataFrame as a CSV file
df.to_csv(output_csv_path, index=False)

print(f"CSV file saved at: {output_csv_path}")
