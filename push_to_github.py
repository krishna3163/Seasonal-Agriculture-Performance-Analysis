import json
import subprocess
import os

# Read token from mcp_config.json
with open(r'C:\Users\User\.gemini\config\mcp_config.json', 'r') as f:
    config = json.load(f)

token = config['mcpServers']['github']['env']['GITHUB_PERSONAL_ACCESS_TOKEN']
repo_url = f"https://{token}@github.com/krishna3163/Seasonal-Agriculture-Performance-Analysis.git"

# Set remote URL
subprocess.run(['git', 'remote', 'set-url', 'origin', repo_url], check=True)

# Add all current files (including updated README and checklist)
subprocess.run(['git', 'add', '-A'], check=True)
subprocess.run(['git', 'commit', '-m', 'Update student details and final deliverables'], check=False)

# Push to main
result = subprocess.run(['git', 'push', '-f', '-u', 'origin', 'main'], capture_output=True, text=True)
print("Push stdout:", result.stdout)
print("Push stderr:", result.stderr)
print("Returncode:", result.returncode)

# Clean up remote url to not keep token in git config
clean_url = "https://github.com/krishna3163/Seasonal-Agriculture-Performance-Analysis.git"
subprocess.run(['git', 'remote', 'set-url', 'origin', clean_url], check=True)
print("Cleaned up git remote URL successfully!")
