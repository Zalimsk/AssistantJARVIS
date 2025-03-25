import os

def load_qa_data(file_path):
    qa_dict = {}
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":")
                if len(parts) != 2:
                    print(f"Skipping malformed line: {line}")
                    continue
                q, a = parts
                qa_dict[q.strip()] = a.strip()  # Strip whitespace from both sides
    except FileNotFoundError:
        print("File not found! Please check the file path.")
    except Exception as e:
        print("An error occurred while loading the data:", e)
    return qa_dict

qa_file_path = r"J:\\Assistant JARVIS\\qna.txt"
qa_dict = load_qa_data(qa_file_path)

# Print the loaded QA dictionary for verification
