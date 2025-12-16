# -------- Stage 1: Build Dependencies --------
FROM python:3.12-slim AS builder

WORKDIR /build

COPY app/requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt


# -------- Stage 2: Runtime Image --------
FROM python:3.12-slim

# Create non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*

# Copy application code
COPY app/ .

# Set permissions
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
