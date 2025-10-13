# !pip install huggingface_hub hf_transfer
import os
# os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download

print("Starting download...")

snapshot_download(
    repo_id = "moxin-org/DeepSeek-V3-0324-Moxin-GGUF",
    local_dir = "DeepSeek-V3-0324-Moxin-GGUF",
    allow_patterns = ["*IQ1_M*"], #IQ1_S
)

print("Download finished.")
