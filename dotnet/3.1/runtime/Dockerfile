ARG newrelic_agent_version=9.9.0

# Stage to download and extract the new relic agent
FROM alpine:latest AS builder

# Install curl and tar
RUN apk add --no-cache curl tar

ARG newrelic_agent_version

# Download and extract the new relic agent
RUN curl -SL --output newrelicagent.tar.gz https://download.newrelic.com/dot_net_agent/previous_releases/${newrelic_agent_version}/newrelic-netcore20-agent_${newrelic_agent_version}.0_amd64.tar.gz \
    && tar -ozxf newrelicagent.tar.gz -C /usr/local \
    && rm newrelicagent.tar.gz


# Main image
FROM mcr.microsoft.com/dotnet/core/runtime:3.1.30-buster-slim

ARG newrelic_agent_version

COPY --from=builder /usr/local /usr/local

ENV DOTNET_VERSION=3.1.30 \
    NEWRELIC_AGENT_VERSION=$newrelic_agent_version \ 
    CORECLR_PROFILER={36032161-FFC0-4B61-B559-F6C5D41BAE5A} \
    CORECLR_NEWRELIC_HOME=/usr/local/newrelic-netcore20-agent \
    CORECLR_PROFILER_PATH=/usr/local/newrelic-netcore20-agent/libNewRelicProfiler.so
