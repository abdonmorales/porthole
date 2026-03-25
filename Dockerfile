FROM gentoo/stage3:latest

# Set locale and environment
ENV LANG=C.UTF-8
ENV ACCEPT_KEYWORDS="~amd64"
ENV FEATURES="-sandbox -usersandbox -pid-sandbox -network-sandbox"
ENV USE="introspection"

# Sync portage tree
RUN emerge-webrsync

# Install build and runtime dependencies
RUN emerge --quiet --noreplace \
    dev-python/pygobject:3 \
    x11-libs/gtk+:3 \
    dev-python/pip \
    dev-python/setuptools \
    dev-python/wheel \
    dev-python/build \
    dev-python/pytest \
    sys-apps/portage \
    && rm -rf /var/tmp/portage/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Default: run tests then build
CMD ["sh", "-c", "python -m pytest tests/ -v && python -m build"]
