import pandas as pd

OUT_FILE_FILES = [
    "/mnt/nas_home/pf376/Documents/CXR-Report-Metric/scores/mimic_impression_model_Llama-3.2-1B-Instruct_peft_3.2-1B_mimic_impression_background_quantization_no_quantization_mode_test_scores.csv",
    "/mnt/nas_home/pf376/Documents/CXR-Report-Metric/scores/mimic_impression_model_Llama-3.2-1B-Instruct_peft_3.2-1B_mimic_impression_background_quantization_no_quantization_mode_val_scores.csv",
    "/mnt/nas_home/pf376/Documents/CXR-Report-Metric/scores/mimic_impression_model_Llama-3.2-1B-Instruct_peft_3.2-1B_mimic_impression_quantization_no_quantization_mode_test_scores.csv",
    "/mnt/nas_home/pf376/Documents/CXR-Report-Metric/scores/mimic_impression_model_Llama-3.2-1B-Instruct_peft_3.2-1B_mimic_impression_quantization_no_quantization_mode_val_scores.csv",
]

OUT_FILE_NAMES = [
    "background_test_scores",
    "background_val_scores",
    "test_scores",
    "val_scores",
]

# Load the CSV files into DataFrames
df_list = [pd.read_csv(file) for file in OUT_FILE_FILES]

avg_scores = []
# print the average of each column for each DataFrame
for i, df in enumerate(df_list):
    avg_scores.append(df.mean())
    print("\n")

# create a new DataFrame to store the average scores indexed by out file names
avg_df = pd.DataFrame(avg_scores, index=OUT_FILE_NAMES)
print(avg_df)