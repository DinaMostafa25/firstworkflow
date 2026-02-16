
# Build Stage
FROM python:3.11-alpine AS builder

WORKDIR /install

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt



# Production Stage

FROM python:3.11-alpine

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application file
COPY hellopython.py .

ENTRYPOINT ["python3", "hellopython.py"]
