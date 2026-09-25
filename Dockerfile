# 1. Official Microsoft image with all OS dependencies and pre-installed browsers
FROM mcr.microsoft.com/playwright/python:v1.63.0-jammy

# 2. Set the working directory
WORKDIR /app

# 3. Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 4. Copy dependency requirements first to leverage caching
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy test project files
COPY . .

# 7. Run Playwright tests via pytest in headless mode
CMD ["pytest", "-v"]