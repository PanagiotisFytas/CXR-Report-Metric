# Model checkpoints
CHEXBERT_PATH = "/mnt/nas_home/pf376/Documents/CXR-Report-Metric/chexbert/chexbert.pth"
RADGRAPH_PATH = "/mnt/nas_home/pf376/Documents/CXR-Report-Metric/radgraph/model_checkpoint/model.tar.gz"

# Report paths
GT_REPORTS_FILES = [
    "/mnt/nas_home/pf376/Documents/llama-rec/mimic_impression_model_Llama-3.2-1B-Instruct_peft_3.2-1B_mimic_impression_background_quantization_no_quantization_mode_test_outputs.csv",
    "/mnt/nas_home/pf376/Documents/llama-rec/mimic_impression_model_Llama-3.2-1B-Instruct_peft_3.2-1B_mimic_impression_background_quantization_no_quantization_mode_val_outputs.csv",
    "/mnt/nas_home/pf376/Documents/llama-rec/mimic_impression_model_Llama-3.2-1B-Instruct_peft_3.2-1B_mimic_impression_quantization_no_quantization_mode_test_outputs.csv",
    "/mnt/nas_home/pf376/Documents/llama-rec/mimic_impression_model_Llama-3.2-1B-Instruct_peft_3.2-1B_mimic_impression_quantization_no_quantization_mode_val_outputs.csv",
]
PREDICTED_REPORTS_FILES = [
    "/mnt/nas_home/pf376/Documents/llama-rec/mimic_impression_peft_3.2-1B_mimic_impression_background_mode_test_gold_outputs.csv",
    "/mnt/nas_home/pf376/Documents/llama-rec/mimic_impression_peft_3.2-1B_mimic_impression_background_mode_val_gold_outputs.csv",
    "/mnt/nas_home/pf376/Documents/llama-rec/mimic_impression_peft_3.2-1B_mimic_impression_mode_test_gold_outputs.csv",
    "/mnt/nas_home/pf376/Documents/llama-rec/mimic_impression_peft_3.2-1B_mimic_impression_mode_val_gold_outputs.csv",
]
OUT_FILE_FILES = [
    "/mnt/nas_home/pf376/Documents/CXR-Report-Metric/scores/mimic_impression_model_Llama-3.2-1B-Instruct_peft_3.2-1B_mimic_impression_background_quantization_no_quantization_mode_test_scores.csv",
    "/mnt/nas_home/pf376/Documents/CXR-Report-Metric/scores/mimic_impression_model_Llama-3.2-1B-Instruct_peft_3.2-1B_mimic_impression_background_quantization_no_quantization_mode_val_scores.csv",
    "/mnt/nas_home/pf376/Documents/CXR-Report-Metric/scores/mimic_impression_model_Llama-3.2-1B-Instruct_peft_3.2-1B_mimic_impression_quantization_no_quantization_mode_test_scores.csv",
    "/mnt/nas_home/pf376/Documents/CXR-Report-Metric/scores/mimic_impression_model_Llama-3.2-1B-Instruct_peft_3.2-1B_mimic_impression_quantization_no_quantization_mode_val_scores.csv",
]

# Whether to use inverse document frequency (idf) for BERTScore
USE_IDF = False
