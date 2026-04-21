import os
import openai
from openai import OpenAI
from anthropic import Anthropic


class LLMTool(object):
    def __init__(
        self,
        model_name="gpt-4o",
        reasoning_effort=None,
        web_search=None,
        temperature=0,
        top_p=1,
    ):
        self.api_key = os.environ.get("LLM_API_KEY", "YOUR_API_KEY")
        self.base_url = os.environ.get("LLM_BASE_URL", "https://api.openai.com/")

        # for single request (openai sdk)
        openai.api_key = self.api_key
        openai.base_url = self.base_url
        openai.default_headers = {"x-foo": "true"}

        # for batch processing
        self.openai_client = OpenAI(
            api_key=self.api_key,
            base_url=f"{self.base_url}/v1",
        )

        self.anthropic_client = Anthropic(
            auth_token=self.api_key,
            base_url=f"{self.base_url}/anthropic/",
            max_retries=0,  # 将最大重试次数设置为0，完全禁用重试
        )

        # Configure the model parameters
        self.model_name = model_name
        if "gpt5" in model_name:
            assert reasoning_effort in [None, "minimum", "low", "medium", "high"], (
                f"Error reasoning_effort {reasoning_effort} for {model_name}"
            )
        elif "claude" in model_name:
            assert reasoning_effort in [None, "enabled", "disabled"], (
                f"Error reasoning_effort {reasoning_effort} for {model_name}"
            )
        elif "gemini" in model_name:
            assert reasoning_effort in [None, "-1", "128"], (
                f"Error reasoning_effort {reasoning_effort} for {model_name}"
            )
        self.reasoning_effort = reasoning_effort
        self.web_search = web_search
        self.temperature = temperature
        self.top_p = top_p

    def generate_response(self, content):
        while True:
            try:
                if "gpt-5" in self.model_name:
                    if self.web_search:
                        tools = [{"type": "web_search"}]
                    else:
                        tools = []
                    extra_body = {}
                    if self.reasoning_effort:
                        extra_body["reasoning_effort"] = self.reasoning_effort
                    completion = openai.chat.completions.create(
                        model=self.model_name,
                        messages=[
                            {
                                "role": "user",
                                "content": content,
                            },
                        ],
                        extra_body=extra_body,
                        tools=tools,
                        temperature=1,  # only temperature=1 is supported
                        top_p=self.top_p,
                    )
                    # completion = openai.responses.create(
                    #     model=self.model_name,
                    #     input=content,
                    #     # text={"verbosity": "low"},
                    #     # reasoning={"effort": "minimal"},
                    #     # tools=tools,
                    #     # temperature=self.temperature,
                    #     # top_p=self.top_p,
                    # )
                elif "gpt" in self.model_name:
                    if self.web_search:
                        tools = [{"type": "web_search"}]
                    else:
                        tools = []
                    extra_body = {}
                    if self.reasoning_effort:
                        extra_body["reasoning_effort"] = self.reasoning_effort
                    completion = openai.chat.completions.create(
                        model=self.model_name,
                        messages=[
                            {
                                "role": "user",
                                "content": content,
                            },
                        ],
                        extra_body=extra_body,
                        tools=tools,
                        temperature=0,
                        top_p=self.top_p,
                    )
                elif "claude" in self.model_name:
                    if self.web_search:
                        tools = [
                            {
                                "type": "web_search_20250305",
                                "name": "web_search",
                                "max_uses": 5,
                            }
                        ]
                        extra_headers = {"anthropic-beta": "web-search-2025-03-05"}
                    else:
                        tools = []
                        extra_headers = {}
                    completion = self.anthropic_client.beta.messages.create(
                        betas=["context-management-2025-06-27"],
                        model=self.model_name,
                        messages=[{"role": "user", "content": content}],
                        tools=tools,
                        extra_headers=extra_headers,
                        extra_body={
                            "thinking": {"type": "enabled", "budget_tokens": 1024},
                        },
                        max_tokens=2048,
                        temperature=1,  # temperature` may only be set to 1 when thinking is enabled
                        top_p=self.top_p,
                    )
                elif "gemini" in self.model_name:
                    if self.web_search:
                        tools = [
                            {
                                "type": "function",
                                "function": {
                                    "name": "googleSearch",
                                    "description": "Search the web using Google",
                                    "parameters": {
                                        "type": "object",
                                        "properties": {
                                            "query": {
                                                "type": "string",
                                                "description": "The search query",
                                            }
                                        },
                                        "required": ["query"],
                                    },
                                },
                            }
                        ]
                    else:
                        tools = []
                    completion = openai.chat.completions.create(
                        model=self.model_name,
                        messages=[
                            {
                                "role": "user",
                                "content": content,
                            },
                        ],
                        extra_body={
                            "google": {
                                "thinkingConfig": {
                                    "includeThoughts": True,
                                    "thinkingBudget": self.reasoning_effort,
                                }
                            }
                        },
                        tools=tools,
                        temperature=self.temperature,
                        top_p=self.top_p,
                    )
                # elif "qwen" in self.model_name:
                else:
                    extra_body = {}
                    extra_body["enable_thinking"] = False
                    if self.web_search:
                        extra_body["enable_search"] = True
                    if (
                        self.reasoning_effort
                        and self.reasoning_effort == "-1"
                        and self.model_name != "qwen-max"
                        and self.model_name != "qwen3-235b-a22b"
                        and self.model_name != "qwen3-30b-a3b"
                    ):
                        extra_body["enable_thinking"] = True
                    completion = openai.chat.completions.create(
                        model=self.model_name,
                        messages=[
                            {
                                "role": "user",
                                "content": content,
                            },
                        ],
                        extra_body=extra_body,
                        temperature=self.temperature,
                        top_p=self.top_p,
                    )
                if "claude" in self.model_name:
                    ret = completion.content[-1].text
                else:
                    ret = completion.choices[0].message.content
                    ret = ret.split("</think>")[-1].strip()
                break
            except Exception as e:
                print(f"Error occurred: {e} in model {self.model_name}")
        return ret, completion
