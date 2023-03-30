"""Prompts for ChatGPT."""

from langchain.prompts.chat import (
    AIMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

from gpt_index.prompts.prompts import RefinePrompt, RefineTableContextPrompt

# Refine Prompt
CHAT_REFINE_PROMPT_TMPL_MSGS = [
    HumanMessagePromptTemplate.from_template("{query_str}"),
    AIMessagePromptTemplate.from_template("{existing_answer}"),
    HumanMessagePromptTemplate.from_template(
        "У нас есть возможность уточнить вышеуказанный ответ "
        "(только если необходимо) с помощью некоторого контекста ниже.\n"
        "------------\n"
        "{context_msg}\n"
        "------------\n"
        "Уточни первоначальный ответ на вопрос с учетом нового контекста. "
        "Если контекст бесполезен, выведи первоначальный ответ еще раз.",
    ),
]


CHAT_REFINE_PROMPT_LC = ChatPromptTemplate.from_messages(CHAT_REFINE_PROMPT_TMPL_MSGS)
CHAT_REFINE_PROMPT = RefinePrompt.from_langchain_prompt(CHAT_REFINE_PROMPT_LC)


# Table Context Refine Prompt
CHAT_REFINE_TABLE_CONTEXT_TMPL_MSGS = [
    HumanMessagePromptTemplate.from_template("{query_str}"),
    AIMessagePromptTemplate.from_template("{existing_answer}"),
    HumanMessagePromptTemplate.from_template(
        "Мы предоставляем схему таблицы ниже. "
        "---------------------\n"
        "{schema}\n"
        "---------------------\n"
        "Также мы предоставляем некоторую контекстную информацию ниже. "
        "{context_msg}\n"
        "---------------------\n"
        "Учитывая контекстную информацию и схему таблицы, "
        "уточни первоначальный ответ на вопрос. "
        "Если контекст бесполезен, верни первоначальный ответ."
    ),
]
CHAT_REFINE_TABLE_CONTEXT_PROMPT_LC = ChatPromptTemplate.from_messages(
    CHAT_REFINE_TABLE_CONTEXT_TMPL_MSGS
)
CHAT_REFINE_TABLE_CONTEXT_PROMPT = RefineTableContextPrompt.from_langchain_prompt(
    CHAT_REFINE_TABLE_CONTEXT_PROMPT_LC
)
