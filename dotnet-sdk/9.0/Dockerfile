FROM mcr.microsoft.com/dotnet/sdk:9.0.308-bookworm-slim

# Add dotnet tools to path
ENV PATH="/root/.dotnet/tools:${PATH}"

# Enable cake script cache
ENV CAKE_SETTINGS_ENABLESCRIPTCACHE=true

# Install cake
RUN dotnet tool install --global Cake.Tool --version 6.0.0

# Intall trx2junit
RUN dotnet tool install --global trx2junit --version 2.1.0
