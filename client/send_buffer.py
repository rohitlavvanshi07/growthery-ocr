import requests
from io import BytesIO

# Load PDF into memory
with open("sample.pdf", "rb") as f:
    pdf_bytes = f.read()

buffer = BytesIO(pdf_bytes)
buffer.name = "buffered_file.pdf"

# POST request to FastAPI server
response = requests.post(
    "http://localhost:8000/extract",
    files={"file": ("buffered_file.pdf", buffer, "application/pdf")}
)

print("Status Code:", response.status_code)
print("Response:", response.json())
