def get_suitable_prompt(keyword: str, user_message: str):
    example = get_keyword_example(keyword)
    if keyword == "objective":
        prompt = f"""
        You are an expert project documentation writer.

        Your task is to read the following variable input:

        user_requirement = "{user_message}"

        Below is an example showing the style, depth, and level of detail expected. 
        This example is ONLY for reference and should NOT be copied verbatim:

        EXAMPLE_CONTENT:
        \"\"\"
        {example}
        \"\"\"

        Now generate a structured JSON output with the format:

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
    Below is an example showing the style, depth, and level of detail expected. 
    This example is ONLY for reference and should NOT be copied verbatim:

    EXAMPLE_CONTENT:
    \"\"\"
    {example}
    \"\"\"

    Now generate a structured JSON output with the format:

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

    Below is an example showing the style, depth, and level of detail expected. 
    This example is ONLY for reference and should NOT be copied verbatim:

    EXAMPLE_CONTENT:
    \"\"\"
    {example}
    \"\"\"

    Now generate a structured JSON output with the format:

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

    Below is an example showing the style, depth, and level of detail expected. 
    This example is ONLY for reference and should NOT be copied verbatim:

    EXAMPLE_CONTENT:
    \"\"\"
    {example}
    \"\"\"

    Now generate a structured JSON output with the format:

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

    Below is an example showing the style, depth, and level of detail expected. 
    This example is ONLY for reference and should NOT be copied verbatim:

    EXAMPLE_CONTENT:
    \"\"\"
    {example}
    \"\"\"

    Now generate a structured JSON output with the format:

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


def get_keyword_example(keyword: str):
    if keyword == "objective":
        return (
"""OBJECTIVES
Develop a Modern, Lightweight Online Store:
 Build a clean, responsive WordPress-based e-commerce website optimized for both desktop and mobile devices.
Showcase 12–15 Products Effectively:
 Design an intuitive product catalog with detailed product pages including images, pricing, descriptions, and availability.
Enable Seamless Checkout & Payment:
 Integrate secure, user-friendly checkout functionality with international payment gateways such as Stripe and PayPal for multi-currency transactions.
Implement Automated Order & Email Notifications:
 Set up automatic email alerts for both the customer and the client — confirming order details, payment receipts, and purchase summaries.
Create an Informative Contact Page:
 Include a professional contact page with inquiry form, company details, and direct communication options.
Ensure Security & Data Compliance:
 Implement SSL encryption, spam protection, and GDPR-compliant privacy features for safe transactions and data handling.
Simplify Admin Management:
 Provide an easy-to-use backend for adding, editing, and tracking products, managing orders, and viewing customer purchase data.
Enhance User Experience (UX):
 Prioritize fast loading speeds, clear navigation, and minimal clicks from product selection to checkout for better conversions.
Scalability & Future Readiness:
 Keep the website flexible for future additions like coupons, product variants, or blog modules."""
        )

    if keyword == "feature_and_functionalities":
        return (
"""FEATURES AND FUNCTIONALITIES
Front-End Features
1. Home Page:
 - Elegant, mobile-friendly layout showcasing featured products (12–15 total).
 - Banner for promotions or seasonal offers.
 - Quick navigation to all product categories.
 - Prominent “Shop Now” and “Contact” buttons.

2. Product Catalog:
 - Product listings categorized (e.g., by type, size, or collection).
 - Search and filter by product name, price, or category.
 - Pagination for easy browsing.
 - “Add to Cart” and “View Details” options directly from the listing page.

3. Product Details Page:
 - High-quality product images with zoom feature.
 - Product title, short description, and full details.
 - Display of price, availability, and SKU.
 - “Add to Cart” and “Buy Now” buttons.
 - Customer reviews and star ratings (optional).

4. Shopping Cart:
 - View, update, or remove products.
 - Real-time calculation of totals, shipping, and taxes.
 - Option to apply coupon codes (future-ready).

5. Checkout Process:
 - Guest checkout and account creation options.
 - Secure input fields for billing/shipping information.
 - Order summary and tax breakdown before payment.
 - Integration with Stripe and PayPal for international payments.
 - Email confirmation sent to both customer and client.

6. Order Confirmation & Notifications:
 - Automatic emails with order details, invoice, and customer information.
 - Client receives all purchase summaries instantly.

7. Contact Page:
 - Inquiry/contact form with email notification.
 - Company address, business email, and phone number.
 - Optional Google Map integration.

8. Responsive Design:
 - Fully optimized for desktop, tablet, and mobile.
 - Tested for cross-browser compatibility.

Back-End (Admin) Features
1. Product Management:
 - Add, edit, or delete products from WordPress dashboard.
 - Manage descriptions, categories, prices, images.
 - Mark products as “featured.”

2. Order & Customer Management:
 - Dashboard with latest orders and total sales.
 - View, update, process orders.
 - Export order details.
 - Access full customer information.

3. Inventory Management:
 - Track stock and low-stock alerts.
 - Update quantities directly.

4. Payment & Shipping Settings:
 - Configure Stripe and PayPal.
 - Manage shipping options (flat rate, free, pickup).
 - Tax configuration.

5. Content Management:
 - Edit pages like Home, Contact, Policies.
 - Update banners and promotions.

6. Security & Performance:
 - SSL for transactions.
 - CAPTCHA-protected forms.
 - Backups & security updates.
 - Basic SEO optimization."""
        )

    if keyword == "technical_approach":
        return (
"""TECHNICAL APPROACH
1. Requirement Analysis:
 - Understand brand identity, product range (12–15 items), and target audience.
 - Define essential features: listings, payments, notifications.
 - Identify admin requirements like stock tracking and email alerts.

2. Design & Theme Selection:
 - Choose lightweight premium theme optimized for WooCommerce.
 - Customize colors, typography, layout per brand guidelines.
 - Create modern, minimal, user-friendly layout.
 - Ensure responsive and accessible UI.

3. WooCommerce Setup & Configuration:
 - Install and configure WooCommerce.
 - Setup categories, attributes, and variations.
 - Implement tax, currency, shipping rules.
 - Configure automatic inventory and order tracking.

4. Payment Gateway Integration:
 - Integrate Stripe & PayPal for secure multi-currency payments.
 - Enable SSL.
 - Configure sandbox testing.

5. Email & Notification System:
 - Configure email confirmations, receipts, admin alerts.
 - Include full customer + product data in admin emails.
 - Optional SMTP integration for reliability.

6. Contact & Inquiry System:
 - Create dedicated Contact page.
 - Send form data directly to client email.
 - Optional reCAPTCHA.

7. SEO & Performance Optimization:
 - Use Yoast SEO or RankMath.
 - Optimize images using Smush/Imagify.
 - Enable caching via WP Rocket/W3 Cache.
 - Use CDN for global speeds.

8. Security & Maintenance:
 - Two-factor authentication for admin.
 - Install Wordfence/Sucuri.
 - Automatic backups (UpdraftPlus).
 - Regular updates of core/theme/plugins.

9. Testing & QA:
 - Test browsing, checkout, payments.
 - Validate emails.
 - Check mobile responsiveness + browser compatibility.
 - Security & performance checks.

10. Deployment & Post-Launch Support:
 - Deploy on secure hosting (SiteGround, Bluehost, AWS Lightsail).
 - Final verification of payment gateways + SSL.
 - Provide 30 days of post-launch support."""
        )

    if keyword == "technology_stack":
        return (
"""TECHNOLOGY STACK
Platform: WordPress
E-commerce Plugin: WooCommerce
Frontend: HTML5, CSS3, JavaScript (Bootstrap for responsiveness)
Backend: PHP (WordPress Core), MySQL
Payment Gateways: Stripe & PayPal (International)
Security: SSL Certificate, reCAPTCHA, Regular Backups
SEO & Performance: Yoast SEO, WP Rocket, Cloudflare CDN
Backup & Maintenance: UpdraftPlus
Hosting: SiteGround / Bluehost (with SSL and daily backups)"""
        )

    if keyword == "time_and_budget_estimate":
        return (
"""TIME AND BUDGET ESTIMATE
The entire project will be completed in 1 phase.

Estimated Timeline:
 - 5 to 6 weeks total (Full Time)

Allocated Resources:
 - 1 WordPress + PHP Developer"""
        )

    return ""
