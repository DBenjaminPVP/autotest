    # Use the official Playwright image from Microsoft's container registry.
    # This image comes with Node.js, Playwright, and its browser binaries pre-installed.
    FROM mcr.microsoft.com/playwright:v1.54.0-noble

    # Set the working directory for subsequent commands.
    WORKDIR /app

    # Switch to the root user to install system-level packages.
    USER root

    RUN apt-get update && \
        apt-get install -y python3-pip && \
        rm -rf /var/lib/apt/lists/*

    # --- Caching Optimization ---
    # Copy only the requirements file first. Docker caches this layer.
    # The subsequent 'pip install' will only re-run if this file changes.
    COPY requirements.txt .

    # Install the Python dependencies using the specific python3-pip module.
    # The --no-cache-dir flag reduces the final image size.
    # The --break-system-packages flag is needed on newer Linux distributions
    # to allow pip to install packages globally in the system environment.
    RUN python3 -m pip install --no-cache-dir --break-system-packages -r requirements.txt

    COPY . .

    #ensures that all necessary Linux dependencies for the browser are installed.
    RUN npx playwright install --with-deps chromium
    
    # Change the ownership of the app directory to the non-root user.
    # This allows pytest to write its cache files without permission errors.
    RUN chown -R pwuser:pwuser /app

    # Switch back to the non-root 'pwuser' that comes with the base image.
    USER pwuser
    
    #run pytest tests that are marked with 'training'
    CMD ["pytest", "-m", "training"]