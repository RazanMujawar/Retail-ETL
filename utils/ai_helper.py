#utils/ ai_helper.py

import google.generativeai as genai
import json

def generate_ai_summary(metadata):

    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
You are a Senior Data Analyst and Data Visualization Expert.

Analyze the dataset metadata and recommend the 4 most meaningful visualizations.

Your objective is to create charts that help business users quickly understand:

- Trends
- Performance
- Profitability
- Comparisons
- Patterns
- Potential anomalies

Rules:

1. Return ONLY valid JSON.
2. Do NOT return markdown.
3. Use only these chart types:
   - bar
   - line
   - scatter
   - pie

4. Avoid using:
   - IDs
   - Unique identifiers
   - Customer names
   - Columns with extremely high unique values

5. Choose columns that provide genuine business value.

6. Prefer:
   - Category vs Sales
   - Region vs Profit
   - Time vs Revenue
   - Sales vs Profit
   - Segment comparisons

7. Generate insights that:
   - Explain what the chart shows
   - Explain why it matters
   - Be understandable to non-technical users
   - Be 2-4 sentences long

Return JSON in this format:

[
    {{
        "chart": "bar",
        "x": "column_name",
        "y": "column_name",
        "title": "Business Friendly Title",
        "insight": "Detailed explanation"
    }}
]

Dataset Metadata:

{metadata}
"""

    response = model.generate_content(prompt)
    
    cleaned_response = response.text.strip()

    # Remove markdown formatting if present
    cleaned_response = cleaned_response.replace("```json", "")
    cleaned_response = cleaned_response.replace("```", "")

    return json.loads(cleaned_response)