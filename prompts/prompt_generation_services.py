def get_suitable_prompt(keyword: str, user_message: str):
    if keyword == "objective":
        prompt = f"""
    You are an expert project documentation writer.
    
    Your task is to read the following variable input:
    
    user_requirement = "{user_message}"
    
    Based on this requirement, generate a structured JSON output with the key:
    
    {{
      "keyname": "OBJECTIVES",
      "bullet_points": [
        {{
          "pointNumber": "1",
          "headline": "Write a clear, short objective headline based on the requirement",
          "description": "Write a concise description that explains the objective in 1–2 sentences."
        }},
        {{
          "pointNumber": "2",
          "headline": "...",
          "description": "..."
        }}
      ]
    }}
    
    Guidelines:
    - Generate **3–9 objectives** depending on the complexity of the user requirement.
    - Each **headline** should be short, action-oriented, and professional.
    - Each **description** must expand logically on the headline.
    - All objectives must be **specifically tailored to the content of user_requirement**.
    - No extra text outside the JSON.
    - Maintain the exact field names: keyname, bullet_points, pointNumber, headline, description.
    """
        return prompt
    elif keyword == "feature_and_functionalities":
        prompt = f"""
    You are an expert project documentation writer.

    Your task is to read the following variable input:

    user_requirement = "{user_message}"

    Based on this requirement, generate a structured JSON output with the following format:

    {{
      "keyname": "FEATURES AND FUNCTIONALITIES",
      "features": [
        {{
          "feature_name": "frontend",
          "bullet_points": [
            {{
              "pointNumber": "1",
              "headline": "Write a clear, short frontend feature headline",
              "description": "Write a meaningful, detailed explanation of the frontend functionality based on the requirement."
            }}
          ]
        }},
        {{
          "feature_name": "backend",
          "bullet_points": [
            {{
              "pointNumber": "1",
              "headline": "Write a clear, short backend feature headline",
              "description": "Write a meaningful, detailed explanation of the backend functionality based on the requirement."
            }}
          ]
        }}
      ]
    }}

    Guidelines:
    - Generate 5–12 bullet points under each feature_name section if the requirement is moderately complex.
    - Each headline must be short, action-oriented, and directly related to the user's requirement.
    - Each description should be meaningful, covering expected behavior, purpose, and benefit.
    - The JSON should include ONLY sections relevant to the given requirement.
      For example, if the requirement is NOT about websites, adjust features accordingly.
    - Tailor the content dynamically:
      - If it's an app, use App UI Features instead of frontend/back-end.
      - If it's a SaaS product, use Dashboard/API/Admin features.
      - If it's eCommerce, include pages, cart, checkout, admin functions, etc.
    - Do NOT add any explanatory text outside the JSON output.
    - Maintain the exact field names: keyname, features, feature_name, bullet_points, pointNumber, headline, description.
    """
        return prompt
    elif keyword == "technical_approach":
        prompt = f"""
        You are an expert technical documentation writer.

        Your task is to read the following requirement:

        user_requirement = "{user_message}"

        Based on this requirement, generate a structured JSON response for the section titled "TECHNICAL APPROACH" (keep the key in uppercase exactly).

        The JSON structure must follow this exact format:

        {{
          "keyname": "TECHNICAL APPROACH",
          "bullet_points": [
            {{
              "pointNumber": "1",
              "headline": "Write a short headline summarizing the technical step",
              "description": "Write a concise, requirement-specific description (2–4 sentences maximum)."
            }},
            {{
              "pointNumber": "2",
              "headline": "...",
              "description": "..."
            }}
          ]
        }}

        STRICT RULES:
        1. The number of bullet points should be between 8 and 12, depending on the complexity of the user_requirement.
        2. All content must be customized to the given requirement – nothing generic or irrelevant.
        3. Each headline must be a short technical process step (e.g., “Requirement Analysis”, “System Architecture Design”, “API Integration”).
        4. Each description must meaningfully expand the step with requirement-specific details.
        5. Use a professional, structured, action-oriented tone.

        OBJECTIVE:
        Produce a polished, well-structured TECHNICAL APPROACH section that fully adapts to any given user requirement.
        """
        return prompt
    elif keyword == "technology_stack":
        prompt = f"""
            You are an expert technical documentation writer.

            Your task is to read the following requirement:

            user_requirement = "{user_message}"

            Based on this requirement, generate a structured JSON response for the section titled "TECHNOLOGY STACK" (keep the key in uppercase exactly).

            The JSON must follow this exact structure:

            {{
              "keyname": "TECHNOLOGY STACK",
              "tech_items": [
                {{
                  "category": "Platform / Framework / Tool category",
                  "value": "Specific technology selected based on the requirement"
                }},
                {{
                  "category": "Another category",
                  "value": "..."
                }}
              ]
            }}

            ### RULES:
            1. Categories must be meaningful and relevant to the user_requirement. Examples include:
               - Platform
               - Frontend
               - Backend
               - Database
               - Deployment / Hosting
               - Payment Gateways
               - Security
               - Analytics
               - Integrations
               - DevOps / CI-CD (only if requirement needs it)
               - Mobile / Web Framework (if applicable)
            2. Each category should appear only if relevant — no filler.
            3. The value must be requirement-specific (e.g., if ecommerce → WooCommerce, Shopify, Stripe, etc. based on context).
            4. Produce 6–12 items depending on complexity.
            5. Use clear, professional, technical language.
            6. Do NOT add explanations outside the JSON response.

            ### OBJECTIVE:
            Produce a clean, concise, requirement-adapted TECHNOLOGY STACK section in JSON format with well-structured categories and accurate technology choices.
            """
        return prompt
    elif keyword == "time_and_budget_estimate":
        prompt = f"""
        You are an expert project planner and documentation writer.

        Your task is to read the following requirement:

        user_requirement = "{user_message}"

        Based on this requirement, generate a structured JSON response for the section titled "TIME AND BUDGET ESTIMATE" (keep the key in uppercase exactly).

        The JSON must follow this exact structure:

        {{
          "keyname": "TIME AND BUDGET ESTIMATE",
          "estimation_details": {{
            "project_phases": "Describe number of phases and why",
            "timeline": "Provide ballpark timeline based on requirement",
            "resources": "Specify type and count of resources needed",
            "budget_range": "Give a reasonable budget range based on complexity and industry standards (no currency symbol required unless obvious)",
            "notes": "Any additional assumptions or constraints"
          }}
        }}

        ### RULES:
        1. Timeline must be realistic and directly connected to the user_requirement (e.g., ecommerce, mobile app, CRM system, API development).
        2. Budget range should reflect typical market pricing and complexity (low/medium/high), not random values.
        3. Resources must be meaningful: specify roles such as:
           - Backend Developer
           - Frontend Developer
           - Full-stack Developer
           - UI/UX Designer
           - QA Engineer
           - DevOps
           …only if required by the project.
        4. Keep descriptions short, clear, and professional.
        5. Do NOT add explanation outside the JSON.

        ### OBJECTIVE:
        Produce a clean, requirement-specific TIME AND BUDGET ESTIMATE section in JSON format with realistic phase planning, timeline, resource count, and budget range.
        """
        return prompt
    else:
        return None