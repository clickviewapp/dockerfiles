FROM mcr.microsoft.com/dotnet/core/runtime:2.1.23-stretch-slim

ENV DOTNET_VERSION=2.1.23 \
    NEWRELIC_AGENT_VERSION=8.36.0 \ 
    CORECLR_PROFILER={36032161-FFC0-4B61-B559-F6C5D41BAE5A} \
    CORECLR_NEWRELIC_HOME=/usr/local/newrelic-netcore20-agent \
    CORECLR_PROFILER_PATH=/usr/local/newrelic-netcore20-agent/libNewRelicProfiler.so

RUN curl -SL --output newrelicagent.tar.gz https://download.newrelic.com/dot_net_agent/previous_releases/$NEWRELIC_AGENT_VERSION/newrelic-netcore20-agent_${NEWRELIC_AGENT_VERSION}.0_amd64.tar.gz \
    && tar -ozxf newrelicagent.tar.gz -C /usr/local \
    && rm newrelicagent.tar.gz
