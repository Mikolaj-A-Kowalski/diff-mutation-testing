FROM python:3.11-slim

# Install git
RUN apt-get update && apt-get install -y git


# Set working directory
WORKDIR /app

# Copy everything... EVERYTHING!!!! (TODO: figure out a smarter way)
COPY . .

# Make entrypoint executable
RUN ls -la
RUN chmod +x entrypoint.sh
RUN chmod +x run_all_patches.sh

# Create a non-root user (same UID/GID as GitHub Actions runner user 1001)
RUN adduser --disabled-password -u 1001 --gecos "" action
USER action

# Set entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
