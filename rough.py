from utils.mcp_helper import build_mcp_prompt
from utils.llm_client import GeminiClient

client = GeminiClient()

topic = "Docker"
level = "Easy"

prompt = build_mcp_prompt(topic, level)

output = client.ask(prompt)
print(output)