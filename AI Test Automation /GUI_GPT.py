import openai
import os
import time
from difflib import SequenceMatcher
import tkinter as tk
from tkinter import messagebox
from queue import Queue
import threading

# Securely load API key
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OpenAI API Key not set. Please set it in environment variables.")

# Similarity check
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Read questions or outputs
def read_lines_from_file(filename, num_lines):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    if len(lines) < num_lines:
        raise ValueError(f"File {filename} does not contain enough entries.")
    return lines[:num_lines]

# Process question
def process_question(queue, question_label, response_label, status_label, log_file):
    while not queue.empty():
        i, question, expected_output = queue.get()
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ]
            )
            message = response.choices[0].message['content']
            similarity_score = similar(message, expected_output)

            # Update GUI
            question_label.config(text=f"Question {i + 1}: {question}")
            response_label.config(text=f"Response: {message}")
            if similarity_score >= 0.6:  # Adjustable threshold
                status = "Pass"
                status_label.config(text="Pass", fg="green")
            else:
                status = "Fail"
                status_label.config(text=f"Fail (Expected: {expected_output})", fg="red")
            
            # Log result
            with open(log_file, "a") as log:
                log.write(f"Q{i+1}: {question}\nResponse: {message}\nExpected: {expected_output}\nStatus: {status}\n\n")
            
            root.update()
        except openai.error.RateLimitError:
            messagebox.showerror("Rate Limit Exceeded", "Rate limit exceeded. Retrying in 60 seconds...")
            time.sleep(60)
        except openai.error.OpenAIError as e:
            messagebox.showerror("API Error", str(e))
        finally:
            queue.task_done()

# Main GUI logic
def start_testing():
    try:
        questions = read_lines_from_file("questions.txt", 40)
        expected_outputs = read_lines_from_file("expected_outputs.txt", 40)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return
    
    queue = Queue()
    for i, (question, expected_output) in enumerate(zip(questions, expected_outputs)):
        queue.put((i, question, expected_output))
    
    log_file = "test_results.log"
    threading.Thread(target=process_question, args=(queue, question_label, response_label, status_label, log_file)).start()

# GUI Setup
root = tk.Tk()
root.title("OpenAI Tester")
root.geometry("800x600")

question_label = tk.Label(root, text="Question: ", wraplength=700)
question_label.pack(pady=10)

response_label = tk.Label(root, text="Response: ", wraplength=700)
response_label.pack(pady=10)

status_label = tk.Label(root, text="Status: ")
status_label.pack(pady=10)

start_button = tk.Button(root, text="Start Testing", command=start_testing)
start_button.pack(pady=20)

root.mainloop()
