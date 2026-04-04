from huggingface_hub import login, upload_folder
import os

# login using GitHub secret
login(token=os.getenv("HF_TOKEN"))

repo_id = "Harini2973/tourism_model"   # space name

# upload entire project folder
upload_folder(
    folder_path="https://github.com/HariniV2907/Tourism",   # current repo
    repo_id=repo_id,
    repo_type="space"
)

print("Deployment successful!")
