from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from src.helpers.prompts import Prompts
from dotenv import load_dotenv

class AiService:
    def __init__(self, model_name: str):
        load_dotenv() 
        self.llm = ChatGoogleGenerativeAI(model=model_name,temperature=0.3)
        self.math_prompt_template = Prompts.MATH_TUTOR_PROMPT_TEMPLATE
        self.speech_therapy_prompt_template = Prompts.SPEECH_THERAPY_PROMPT_TEMPLATE

    def text_generation(self, text: str, tutor: str, verbose: bool):
        PROMPT = PromptTemplate(input_variables=["history", "input"], 
                                template= self.math_prompt_template if tutor == 'math' else self.speech_therapy_prompt_template)
        conversation = ConversationChain(
            llm=self.llm,
            verbose=verbose,
            prompt=PROMPT,
            memory=ConversationBufferMemory(ai_prefix="AI Assistant")
            )
        result = conversation.predict(input = text)
        return result
    
    def image_generation(self, text: str, verbose:bool):
        pass



    


