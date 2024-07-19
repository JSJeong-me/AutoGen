import autogen
from typing import Literal
from typing_extensions import Annotated

import warnings
import logging

# Suppress all warnings by setting the logging level to ERROR
#logging.getLogger('autogen.oai.client').setLevel(logging.ERROR)

# Alternatively, filter out specific warning messages
#class CustomFilter(logging.Filter):
#    def filter(self, record):
#        return "Model ollama_chat/llama3 is not found" not in record.getMessage()

#logger = logging.getLogger('autogen.oai.client')
#logger.addFilter(CustomFilter())

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

from autogen.coding import LocalCommandLineCodeExecutor

executor = LocalCommandLineCodeExecutor(
    timeout=60,
    work_dir="coding",
)


from autogen import ConversableAgent, AssistantAgent

code_executor_agent = ConversableAgent(
    name="code_executor_agent",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="ALWAYS",
    default_auto_reply=
    "Please continue. If everything is done, reply 'TERMINATE'.",
)

code_writer_agent = AssistantAgent(
    name="code_writer_agent",
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
)

code_writer_agent_system_message = code_writer_agent.system_message

#print(code_writer_agent_system_message)

#The task!

import datetime

today = datetime.datetime.now().date()
message = f"Today is {today}. "\
"Create a plot showing stock gain YTD for NVDA and TLSA. "\
"Make sure the code is in markdown code block and save the figure"\
" to a file ytd_stock_gains.png."""

chat_result = code_executor_agent.initiate_chat(
    code_writer_agent,
    message=message,
)
