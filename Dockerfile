FROM gentoo/stage3:latest

# Set locale and environment
ENV LANG=C.UTF-8
ENV FEATURES="-sandbox -usersandbox -pid-sandbox -network-sandbox"
ENV USE="introspection"

# Sync portage tree
RUN emerge-webrsync

# Accept ~amd64 keywords for packages that may only be in testing
RUN mkdir -p /etc/portage/package.accept_keywords && \
    echo "*/*::gentoo ~amd64" > /etc/portage/package.accept_keywords/all

# Install build and runtime dependencies in two stages to handle deps
RUN emerge --quiet --noreplace --autounmask-continue \
    sys-apps/portage \
    dev-python/pip \
    dev-python/setuptools \
    dev-python/wheel \
    && rm -rf /var/tmp/portage/*

RUN emerge --quiet --noreplace --autounmask-continue \
    dev-python/pygobject:3 \
    x11-libs/gtk+:3 \
    dev-python/build \
    dev-python/pytest \
    && rm -rf /var/tmp/portage/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Default: run tests then build
CMD ["sh", "-c", "python -m pytest tests/ -v && python -m build"]
