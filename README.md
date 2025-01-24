# BotQA
Software Quality Assurance on AI Chatbots

# Overview
This project involved creating python scripts to automate the testing process of AI chatbots, focusing on their Natural Language Processing (NLP) capabilitites in the domain of Formula 1. The testing process included identifying test cases, executing tests, analyzing results, and automating the testing pipeline.

# Key Features
1. Test Case Creation:
   - Test cases were designed based on equivalence partitioning, decision tables, boundary value analysis, and scenario testing to cover various aspects of Formula 1 knowledge and chatbot functionality. 
2. Automation Framework:
   - Python scrips were developed to automate test execution, utilizing libraries such as openai, google.generativeai, requests, and Selenium
   - Automated comparison of chatbot responses were exepected outputs using similarity scoring algorithms (e.g., difflib.SequenceMatcher)
3. Test Coverage
   - Inputs tested included 26 general questsions and 14 contextual questions.
   - Focused on validating chatbot response accuracy, coherence, and adherence to expected outputs. 
4. Bug Detection and Analysis:
   - Identified bugs in chatbot responses, analyzed their impact, and provided detailed reports on issues.
5. Test Results
   - Automated testing covered all major areas, detecting bugs efficiently and offering insights into chatbot performance. 

# Prerequisites
   - Python 3.8 or higher
   - Required Python Libraries: openai, requests, difflib, selenium, webdriver_manager
   - API keys for OpenAI and relevant chatbot APIs

# Test Details
   - Equivalence Partitioning: Divided Formula 1 knowledge into manageable segments for thorough covereage.
   - Decision Tables: Validated responses based on specific input conditions.
   - Boundary Values: Tested chatbot accuracy with edge casees in inputs.
   - Scenario Testing: Evaluated chatbots responces in predefined interactive scenarios. 

# Results Summary
   - Total Questions: 200
   - Pass Rates: ~81.50%
   - Bugs Detected: 78 (from both conventional and automated testing)

# Link to Video Demonstration
https://www.youtube.com/watch?v=6rGZPV0Q29g
