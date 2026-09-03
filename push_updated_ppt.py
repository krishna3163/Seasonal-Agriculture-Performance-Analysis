import json
import subprocess

with open(r'C:\Users\User\.gemini\config\mcp_config.json', 'r') as f:
    config = json.load(f)

token = config['mcpServers']['github']['env']['GITHUB_PERSONAL_ACCESS_TOKEN']
repo_url = f"https://{token}@github.com/krishna3163/Seasonal-Agriculture-Performance-Analysis.git"

subprocess.run(['git', 'remote', 'set-url', 'origin', repo_url], check=True)
subprocess.run(['git', 'add', '-A'], check=True)
subprocess.run(['git', 'commit', '-m', 'Embed charts directly into PPT presentation'], check=True)

result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
print("Push stdout:", result.stdout)
print("Push stderr:", result.stderr)

clean_url = "https://github.com/krishna3163/Seasonal-Agriculture-Performance-Analysis.git"
subprocess.run(['git', 'remote', 'set-url', 'origin', clean_url], check=True)
print("Git remote cleaned.")
