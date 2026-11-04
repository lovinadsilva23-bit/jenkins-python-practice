import os

print("Hello from Jenkins!")

branch = os.getenv("BRANCH_NAME", "Not provided")

print(f"Selected Branch: {branch}")
print("Python execution completed successfully.")
