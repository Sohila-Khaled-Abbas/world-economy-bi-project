# 1️⃣ Use lightweight Python image
FROM python:3.10-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4️⃣ Copy project files (main app + data)
COPY src/data_ingestion.py ./src/data_ingestion.py
COPY data/processed_data.csv ./data/processed_data.csv
COPY main.py .

# 5️⃣ Expose port
EXPOSE 8000

# 6️⃣ Start API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
