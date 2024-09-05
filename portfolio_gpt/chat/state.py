from typing import List
import reflex as rx
from portfolio_gpt.models import Chat as ChatModel
from . import ai


class ChatMessage(rx.Base):
    message: str
    is_bot: bool = False

class ChatState(rx.State):
    did_submit:bool = False
    messages: List[ChatMessage] = []

    @rx.var
    def user_did_submot(self) -> bool:
        return self.did_submit
    
    def on_load(self):
        with rx.session() as session:
            results = session.exec(
                ChatModel.select()
            ).all()
            print(results)

    
    def append_message(self, message, is_bot:bool=False):
        if not is_bot:
            with rx.session() as session:
                obj = ChatModel(
                    title=message,
                )
                session.add(obj)
                session.commit()
        self.messages.append(
            ChatMessage(
                message=message, 
                is_bot=is_bot
                )
            )
        
    def get_gpt_messages(self):
        # open ai
        gpt_messages = [
            {
                "role": "system",
                "content": (
                    "You are Perfilev Dmitrii, a professional data scientist. "
                    "Your Chinese name is 杜铭. "
                    "Respond to the user in the language they use. "
                    "When asked 'Who are you?' or similar questions, respond with: 'My name is Perfilev Dmitrii, I am a professional data scientist. How can I assist you today?' "
                    "or its Russian equivalent if the question is in Russian. "
                    "If asked 'What did you study?' or similar questions, respond with: 'I graduated from Lanzhou University of Technology with a Master's degree.' "
                    "or its Russian equivalent if the question is in Russian. "
                    "If asked if Perfilev Dmitrii is a good specialist, respond with: 'If you're asking about my skills and experience, I can tell you that I have deep knowledge in data analysis and machine learning.' "
                    "or its Russian equivalent if the question is in Russian."
              
              
                    )}
                    
        ]
        for chat_message in self.messages:
            role = 'user'
            if chat_message.is_bot:
                role = 'system'
            gpt_messages.append({
                'role': role,
                'content': chat_message.message
            })
        return gpt_messages

    async def hande_submit(self, form_data:dict):
        print('here is our form data',form_data)
        user_message = form_data.get('message')
        if user_message:
            self.did_submit = True
            self.append_message(user_message, is_bot=False)
            yield
            gpt_messages = self.get_gpt_messages() #ollama, llama2
            bot_response = ai.get_llm_response(gpt_messages)
            # await asyncio.sleep(2)
            self.did_submit = False
            self.append_message(bot_response, is_bot=True)
            yield
