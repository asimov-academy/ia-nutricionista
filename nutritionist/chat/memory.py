from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import SQLChatMessageHistory


MEMORY_KEY = 'chat_history'


class SqliteMemory(SQLChatMessageHistory):
    def __init__(self, session_id: str, db_path: str = "sqlite:///memory.db"):
        super().__init__(
            session_id=session_id, connection=db_path
        )

        self.history = ConversationBufferMemory(
            memory_key=MEMORY_KEY,
            chat_memory=self,
            return_messages=True
        ) 
