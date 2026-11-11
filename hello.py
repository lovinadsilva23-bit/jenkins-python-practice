
import os

environment = os.getenv("ENVIRONMENT", "QA")
branch = os.getenv("BRANCH_NAME", "main")

print("================================")
print("JENKINS BUILD DETAILS")
print("================================")
print(f"Environment: {environment}")
print(f"Branch: {branch}")
print("Build execution successful!")
