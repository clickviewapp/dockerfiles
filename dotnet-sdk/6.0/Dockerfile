FROM mcr.microsoft.com/dotnet/sdk:6.0.408-bullseye-slim

# Add dotnet tools to path
ENV PATH="/root/.dotnet/tools:${PATH}"

# Enable cake script cache
ENV CAKE_SETTINGS_ENABLESCRIPTCACHE=true

# Install cake
RUN dotnet tool install --global Cake.Tool --version 2.3.0
