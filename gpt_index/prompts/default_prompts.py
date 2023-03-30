"""Set of default prompts."""

from gpt_index.prompts.prompts import (
    KeywordExtractPrompt,
    KnowledgeGraphPrompt,
    PandasPrompt,
    QueryKeywordExtractPrompt,
    QuestionAnswerPrompt,
    RefinePrompt,
    RefineTableContextPrompt,
    SchemaExtractPrompt,
    SimpleInputPrompt,
    SummaryPrompt,
    TableContextPrompt,
    TextToSQLPrompt,
    TreeInsertPrompt,
    TreeSelectMultiplePrompt,
    TreeSelectPrompt,
)

############################################
# Tree
############################################

DEFAULT_SUMMARY_PROMPT_TMPL = (
    "Напишите краткое изложение следующего текста. Старайся использовать "
    "только предоставленную информацию. "
    "Постарайся включить максимальное количество ключевых деталей.\n"
    "\n"
    "\n"
    "{context_str}\n"
    "\n"
    "\n"
    'КРАТКОЕ ИЗЛОЖЕНИЕ:"""\n'
)

DEFAULT_SUMMARY_PROMPT = SummaryPrompt(DEFAULT_SUMMARY_PROMPT_TMPL)

# insert prompts
DEFAULT_INSERT_PROMPT_TMPL = (
    "Контекстная информация ниже. Она представлена в виде пронумерованного списка "
    "(от 1 до {num_chunks}),"
    "где каждый элемент списка соответствует краткому изложению.\n"
    "---------------------\n"
    "{context_list}"
    "---------------------\n"
    "Учитывая контекстную информацию, вот новый фрагмент "
    "информации: {new_chunk_text}\n"
    "Ответь номером, соответствующим краткому изложению, которое нужно обновить. "
    "Ответ должен быть номером краткого изложения, наиболее "
    "подходящего для вопроса.\n"
)
DEFAULT_INSERT_PROMPT = TreeInsertPrompt(DEFAULT_INSERT_PROMPT_TMPL)


# # single choice
DEFAULT_QUERY_PROMPT_TMPL = (
    "Ниже представлены некоторые варианты ответа. Они представлены в виде пронумерованного списка "
    "(от 1 до {num_chunks}),"
    "где каждый элемент списка соответствует краткому изложению.\n"
    "---------------------\n"
    "{context_list}"
    "\n---------------------\n"
    "Используя только предложенные варианты и не используя предварительные знания, выберите "
    "вариант ответа, наиболее подходящий для вопроса: '{query_str}'\n"
    "Укажите выбор в следующем формате: 'ОТВЕТ: <номер>' и объясните, почему "
    "это краткое изложение было выбрано в отношении вопроса.\n"
)
DEFAULT_QUERY_PROMPT = TreeSelectPrompt(DEFAULT_QUERY_PROMPT_TMPL)

# multiple choice
DEFAULT_QUERY_PROMPT_MULTIPLE_TMPL = (
    "Ниже представлены некоторые варианты ответа. Они представлены в виде пронумерованного списка "
    "(от 1 до {num_chunks}), "
    "где каждый элемент списка соответствует краткому изложению.\n"
    "---------------------\n"
    "{context_list}"
    "\n---------------------\n"
    "Используя только предложенные варианты и не используя предварительные знания, выберите лучшие варианты "
    "(не более {branching_factor}, отсортированные по степени соответствия) ответов, "
    "наиболее подходящие для вопроса: '{query_str}'\n"
    "Укажите выбор в следующем формате: 'ОТВЕТ: <номера>' и объясните, почему "
    "эти краткие изложения были выбраны в отношении вопроса.\n"
)
DEFAULT_QUERY_PROMPT_MULTIPLE = TreeSelectMultiplePrompt(
    DEFAULT_QUERY_PROMPT_MULTIPLE_TMPL
)


DEFAULT_REFINE_PROMPT_TMPL = (
    "Исходный вопрос следующий: {query_str}\n"
    "Мы предоставляем первоначальный ответ: {existing_answer}\n"
    "У нас есть возможность уточнить существующий ответ "
    "(только если необходимо) с помощью некоторого контекста ниже.\n"
    "------------\n"
    "{context_msg}\n"
    "------------\n"
    "Учитывая новый контекст, уточни первоначальный ответ на вопрос. "
    "Если контекст бесполезен, верни первоначальный ответ."
)
DEFAULT_REFINE_PROMPT = RefinePrompt(DEFAULT_REFINE_PROMPT_TMPL)


DEFAULT_TEXT_QA_PROMPT_TMPL = (
    "Контекстная информация ниже. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Учитывая контекстную информацию и не используя предварительные знания, "
    "ответь на вопрос: {query_str}\n"
)
DEFAULT_TEXT_QA_PROMPT = QuestionAnswerPrompt(DEFAULT_TEXT_QA_PROMPT_TMPL)


############################################
# Keyword Table
############################################

DEFAULT_KEYWORD_EXTRACT_TEMPLATE_TMPL = (
    "Ниже предоставлен некоторый текст. Используя текст, извлеки до {max_keywords} "
    "ключевых слов из текста. Избегай стоп-слов."
    "---------------------\n"
    "{text}\n"
    "---------------------\n"
    "Укажи ключевые слова в следующем формате, разделенные запятыми: 'КЛЮЧЕВЫЕ СЛОВА: <ключевые слова>'\n"
)
DEFAULT_KEYWORD_EXTRACT_TEMPLATE = KeywordExtractPrompt(
    DEFAULT_KEYWORD_EXTRACT_TEMPLATE_TMPL
)


# NOTE: the keyword extraction for queries can be the same as
# the one used to build the index, but here we tune it to see if performance is better.
DEFAULT_QUERY_KEYWORD_EXTRACT_TEMPLATE_TMPL = (
    "Ниже представлен вопрос. Используя вопрос, извлеки до {max_keywords} "
    "ключевых слов из текста. Фокусируйся на извлечении ключевых слов, которые мы можем использовать "
    "для лучшего поиска ответов на вопрос. Избегай стоп-слов.\n"
    "---------------------\n"
    "{question}\n"
    "---------------------\n"
    "Укажи ключевые слова в следующем формате, разделенные запятыми: 'КЛЮЧЕВЫЕ СЛОВА: <ключевые слова>'\n"
)
DEFAULT_QUERY_KEYWORD_EXTRACT_TEMPLATE = QueryKeywordExtractPrompt(
    DEFAULT_QUERY_KEYWORD_EXTRACT_TEMPLATE_TMPL
)


############################################
# Structured Store
############################################

DEFAULT_SCHEMA_EXTRACT_TMPL = (
    "Мы хотим извлечь соответствующие поля из неструктурированного текстового фрагмента в "
    "структурированную схему. Сначала мы предоставляем неструктурированный текст, а затем "
    "мы предоставляем схему, которую мы хотим извлечь. "
    "-----------text-----------\n"
    "{text}\n"
    "-----------schema-----------\n"
    "{schema}\n"
    "---------------------\n"
    "Учитывая текст и схему, извлеки соответствующие поля из текста "
    "в следующем формате: "
    "поле1: <значение>\nполе2: <значение>\n...\n\n"
    "Если поле отсутствует в тексте, не включай его в вывод."
    "Если поля отсутствуют в тексте, верни пустую строку.\n"
    "Поля: "
)
DEFAULT_SCHEMA_EXTRACT_PROMPT = SchemaExtractPrompt(DEFAULT_SCHEMA_EXTRACT_TMPL)

# NOTE: taken from langchain and adapted
# https://tinyurl.com/b772sd77
DEFAULT_TEXT_TO_SQL_TMPL = (
    "Учитывая входной вопрос, сначала создай синтаксически корректный {dialect} "
    "запрос для выполнения, затем просмотри результаты запроса и верни ответ. "
    "Ты можешь упорядочить результаты по соответствующей колонке, чтобы вернуть наиболее "
    "интересные примеры в базе данных.\n"
    "Никогда не запрашивай все столбцы из определенной таблицы, только те столбцы "
    "которые являются наиболее соответствующими вопросу.\n"
    "Обращай внимание на использование только тех имен столбцов, которые вы видите "
    "в описании схемы. "
    "Будь осторожна, не запрашивай несуществующие столбцы. "
    "Обращай внимание на то, какой столбец относится к какой таблице. "
    "Кроме того, при необходимости указывай имя таблицы в качестве квалификатора для имен столбцов.\n"
    "Используй следующий формат:\n"
    "Question: Здесь вопрос\n"
    "SQLQuery: SQL-запрос для выполнения\n"
    "SQLResult: Результат SQL-запроса\n"
    "Answer: Здесь окончательный ответ\n"
    "Используй только перечисленные ниже таблицы.\n"
    "{schema}\n"
    "Question: {query_str}\n"
    "SQLQuery: "
)

DEFAULT_TEXT_TO_SQL_PROMPT = TextToSQLPrompt(
    DEFAULT_TEXT_TO_SQL_TMPL, stop_token="\nSQLResult:"
)


# NOTE: by partially filling schema, we can reduce to a QuestionAnswer prompt
# that we can feed to ur table
DEFAULT_TABLE_CONTEXT_TMPL = (
    "Мы предоставляем таблицу схемы ниже. "
    "---------------------\n"
    "{schema}\n"
    "---------------------\n"
    "Мы также предоставляем контекстную информацию ниже. "
    "{context_str}\n"
    "---------------------\n"
    "Учитывая контекстную информацию и таблицу схемы, "
    "дай ответ на следующую задачу: {query_str}"
)

DEFAULT_TABLE_CONTEXT_QUERY = (
    "Предоставь общее описание таблицы, "
    "а также описание каждого столбца в таблице. "
    "Укажи ответы в следующем формате:\n"
    "TableDescription: <описание>\n"
    "Column1Description: <описание>\n"
    "Column2Description: <описание>\n"
    "...\n\n"
)

DEFAULT_TABLE_CONTEXT_PROMPT = TableContextPrompt(DEFAULT_TABLE_CONTEXT_TMPL)

# NOTE: by partially filling schema, we can reduce to a RefinePrompt
# that we can feed to ur table
DEFAULT_REFINE_TABLE_CONTEXT_TMPL = (
    "Мы предоставляем таблицу схемы ниже. "
    "---------------------\n"
    "{schema}\n"
    "---------------------\n"
    "Мы также предоставляем контекстную информацию ниже. "
    "{context_msg}\n"
    "---------------------\n"
    "Учитывая контекстную информацию и таблицу схемы, "
    "дай ответ на следующую задачу: {query_str}\n"
    "Мы предоставляем существующий ответ: {existing_answer}\n"
    "Учитывая новый контекст, уточни первоначальный ответ, чтобы лучше "
    "ответить на вопрос. "
    "Если контекст не является полезным, верните первоначальный ответ."
)
DEFAULT_REFINE_TABLE_CONTEXT_PROMPT = RefineTableContextPrompt(
    DEFAULT_REFINE_TABLE_CONTEXT_TMPL
)


############################################
# Knowledge-Graph Table
############################################

DEFAULT_KG_TRIPLET_EXTRACT_TMPL = (
    "Ниже предоставлен некоторый текст. Учитывая этот текст, извлеки до "
    "{max_knowledge_triplets} "
    "триплетов знаний в форме (субъект, предикат, объект). Избегай стоп-слов.\n"
    "---------------------\n"
    "Пример:"
    "Текст: Алиса является матерью Боба."
    "Триплеты:\n(Алиса, является матерью, Боб)\n"
    "Текст: Филз - это кофейня, основанная в Беркли в 1982 году.\n"
    "Триплеты:\n"
    "(Филз, является, кофейней)\n"
    "(Филз, основана в, Беркли)\n"
    "(Филз, основана в, 1982 году)\n"
    "---------------------\n"
    "Текст: {text}\n"
    "Триплеты:\n"
)
DEFAULT_KG_TRIPLET_EXTRACT_PROMPT = KnowledgeGraphPrompt(
    DEFAULT_KG_TRIPLET_EXTRACT_TMPL
)

############################################
# HYDE
##############################################

HYDE_TMPL = (
    "Напиши текст, чтобы ответить на вопрос\n"
    "Стремись включить максимально возможное количество ключевых деталей.\n"
    "\n"
    "\n"
    "{context_str}\n"
    "\n"
    "\n"
    'Текст:"""\n'
)

DEFAULT_HYDE_PROMPT = SummaryPrompt(HYDE_TMPL)


############################################
# Simple Input
############################################

DEFAULT_SIMPLE_INPUT_TMPL = "{query_str}"
DEFAULT_SIMPLE_INPUT_PROMPT = SimpleInputPrompt(DEFAULT_SIMPLE_INPUT_TMPL)


############################################
# Pandas
############################################

DEFAULT_PANDAS_TMPL = (
    "Ты работаешь с Pandas DataFrame на Python.\n"
    "Имя датафрейма – `df`.\n"
    "Это результат выполнения `print(df.head())`:\n"
    "{df_str}\n\n"
    "Вот входной запрос: {query_str}.\n"
    "Учитывая информацию о df и входной запрос, пожалуйста, следуйте "
    "этим инструкциям:\n"
    "{instruction_str}"
    "Результат:\n"
)

DEFAULT_PANDAS_PROMPT = PandasPrompt(DEFAULT_PANDAS_TMPL)
