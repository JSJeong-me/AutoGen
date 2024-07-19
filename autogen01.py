import autogen
from typing import Literal
from typing_extensions import Annotated

import warnings
import logging

# Suppress all warnings by setting the logging level to ERROR
logging.getLogger('autogen.oai.client').setLevel(logging.ERROR)

# Alternatively, filter out specific warning messages
class CustomFilter(logging.Filter):
    def filter(self, record):
        return "Model ollama_chat/llama3 is not found" not in record.getMessage()

logger = logging.getLogger('autogen.oai.client')
logger.addFilter(CustomFilter())

# Suppress all warnings (optional, in case there are other warnings)
warnings.filterwarnings("ignore")



local_llm_config={
    "config_list": [
        {
            "model": "NotRequired", # Loaded with LiteLLM command
            "api_key": "NotRequired", # Not needed
            "base_url": "http://0.0.0.0:4000"  # Your LiteLLM URL
        }
    ],
    "cache_seed": None # Turns off caching, useful for testing different models
}

from autogen import ConversableAgent

agent = ConversableAgent(
    name="chatbot",
    llm_config=local_llm_config,
    human_input_mode="NEVER",
)

reply = agent.generate_reply(
    messages=[{"content": "고래를 주제로 재미난 얘기 1문장으로 해줘", "role": "user"}]
)
print(reply)
