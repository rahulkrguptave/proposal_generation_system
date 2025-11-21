from open_ai_services.chat_completion_api import call_gpt_4o
from prompts.prompt_generation_services import get_suitable_prompt


def generate_proposal_content_with_ai(user_requirement: str):
   document_content = []
   keys = ["objective","feature_and_functionalities","technical_approach","technology_stack","time_and_budget_estimate"]
   for key in keys:
      prompt = get_suitable_prompt(key, user_requirement)
      response = call_gpt_4o(prompt)
      document_content.append(response)
   return document_content