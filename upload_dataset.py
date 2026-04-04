from huggingface_hub import login, create_repo, upload_file
import os

# Login using GitHub secret
login(token=os.environ["HF_TOKEN"])

repo_id = "Harini2973/Data"  

# Create repo if not exists
create_repo(repo_id=repo_id, repo_type="dataset", exist_ok=True)

# Upload file
upload_file(
    path_or_fileobj="train.csv",   
    path_in_repo="train.csv",
    repo_id=repo_id,
    repo_type="dataset"
)

print("Dataset uploaded successfully!")
