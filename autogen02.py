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



llm_config={
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

cathy = ConversableAgent(
    name="야옹님",
    system_message=
    "당신의 이름은 야옹님이고 당신은 재미난 이야기를 잘 만드는 코미디언입니다. \    You must answer in Korean.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

joe = ConversableAgent(
    name="멍멍님",
    system_message=
    "당신의 이름은 멍멍님이고 당신은 재미난 이야기를 잘 만드는 코미디언입니다"
    "이전 대화의 내용을 이어서 다음 재미난 이야기를 시작하세요. \
    You must answer in Korean.",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

chat_result = joe.initiate_chat(
    recipient=cathy,
    message="나는 야옹님이야, 우리 재미난 이야기를 이어서 나가 볼까?",
    max_turns=5
)
