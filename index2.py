# Load the content of the text file and convert it to CSV format
input_file_path = "G-protein.txt"
output_csv_path = "G-protein.csv"

# Process the data: Each entry starts with a ">" and is followed by sequences with "|" as field separators
output_data = []

with open(input_file_path, "r") as file:
    for line in file:
        if line.startswith(">"):
            parts = line.strip(">").strip().split("|")
            chain_info = {
                "Protein_ID": parts[0],
                "Chains": parts[1],
                "Description": parts[2],
                "Organism": parts[3]
            }
        else:
            chain_info["Sequence"] = line.strip()
            output_data.append(chain_info)

# Convert the processed data to a DataFrame and save it as CSV
import pandas as pd

df = pd.DataFrame(output_data)
df.to_csv(output_csv_path, index=False)

output_csv_path
