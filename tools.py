# tools.py
from langchain.tools import BaseTool
from typing import List
from database import search_database

class KeywordSearchTool(BaseTool):
    name = "keyword_search"
    description = "Searches the database for keywords extracted from the query, it generally have infromation about the cancer.\
        please provide the extracted keywords and search_database functions for better search option. \
        if the response is not relevant don't answer anything."

    def _run(self, query: str) -> str:
        print("Query is: ", query)
        results = search_database(query)
        print("Results from the vector database --->>> :    ", results)
        return results

class Calculator(BaseTool):
    name = "Calculator"
    description = "it help in doing the calculation only, the numbers and return the result"

    def _run(self, query: str) -> str:
        return query
