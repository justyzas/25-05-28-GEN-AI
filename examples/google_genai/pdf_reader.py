from google import genai
from google.genai import types
from pydantic import BaseModel

from dotenv import load_dotenv
import os
from rich import print
load_dotenv()

class AdministrativeCostStatement(BaseModel):
    staff: float
    early_departures: float
    other_operating_costs: float
    deprecation_costs: float

class ProgrammeCostStatement(BaseModel):
    impairment_loss: float

class IncomeStatement(BaseModel):
    general_income: float
    increase_in_value: float
    subtotal: float




class AccountingStatement(BaseModel):
    year: int
    balance: float
    costs_subtotal: float

    income: IncomeStatement
    administrative_costs: AdministrativeCostStatement
    programme_costs: ProgrammeCostStatement




with open('resources/sample-tables.pdf', 'rb') as f:
    pdf_bytes = f.read()

GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL="gemini-2.5-flash"

client = genai.Client(api_key=GOOGLE_AI_KEY)

response = client.models.generate_content(
    model=MODEL,
    contents=["Tell me what's in the 17 table? give me structured output", types.Part.from_bytes(
        data=pdf_bytes,
        mime_type='application/pdf'
      )],
    config={
        "response_mime_type": "application/json",
        "response_schema": list[AccountingStatement],
    }
)

#Strukturizuotas atsakymas
accounting_statements:list[AccountingStatement] = response.parsed
print(accounting_statements[0].administrative_costs)