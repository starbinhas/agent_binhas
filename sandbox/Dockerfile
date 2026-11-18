FROM kalilinux/kali-rolling:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        bash \
        curl \
        python3 \
        sqlmap \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash pentester && \
    install -d -o pentester -g pentester /workspace

USER pentester

WORKDIR /workspace

CMD ["sleep", "infinity"]