# Simple runtime image for the timescale-access package
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
        libpq-dev \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only what is needed to install the package
COPY pyproject.toml README.md ./
COPY src ./src

# Install the package (no dev/docs extras in the runtime image)
RUN pip install --upgrade pip && pip install .

# Default command (adjust to your use case)
CMD ["python", "-c", "print('timescale-access image is running')"]
