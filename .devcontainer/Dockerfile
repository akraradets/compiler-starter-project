FROM ubuntu:24.04
ARG BUILD_VERSION
ENV BUILD_VERSION=$BUILD_VERSION

ARG WORKDIR
WORKDIR $WORKDIR
# Ubuntu already have `ubuntu` user
ARG USERNAME=ubuntu
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
# RUN groupadd --gid $USER_GID $USERNAME \
#     && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
#
# [Optional] Add sudo support. Omit if you don't need to install software after connecting.
RUN apt update \
&& apt install -y sudo \
&& echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
&& chmod 0440 /etc/sudoers.d/$USERNAME

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

# Python 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Essential 
RUN apt install -y --no-install-recommends ca-certificates
# Common tools
RUN apt install -y --no-install-recommends iputils-ping vim
# PySide6
# RUN apt install -y ffmpeg libsm6 libxext6
RUN apt install -y libgl1 libegl1 libfontconfig1 libglib2.0-0 libdbus-1-3
RUN apt install -y libxkbcommon-x11-0


RUN apt clean
RUN rm -rf /var/lib/apt/lists/*

COPY --chown=${USER_UID}:${USER_GID} start.sh /start.sh

# uv setup 
COPY --from=ghcr.io/astral-sh/uv:0.10.4 /uv /uvx /bin/
# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy
# UV will instapp python in the ~/.local/uv/python by default which won't be cached when container is destroyed.
# Change the path to project folder so it easier to cache.
ENV UV_PYTHON_INSTALL_DIR=${WORKDIR}/.python
# Add uv tools path
ENV PATH="/home/${USERNAME}/.local/bin:$PATH"
# Place executables in the environment at the front of the path
ENV PATH="${WORKDIR}/.venv/bin:$PATH"


# [Optional] Set the default user. Omit if you want to keep the default as root.
USER $USERNAME
WORKDIR ${WORKDIR}
# # Install the project's dependencies using the lockfile and settings
# RUN --mount=type=bind,source=uv.lock,target=uv.lock \
#     --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
#     uv sync --locked --no-install-project --no-dev
# COPY ./data data
# COPY ./src  src
# COPY ./README.md README.md
# Reset the entrypoint, don't invoke `uv`
EXPOSE 8000
ENTRYPOINT []
CMD ["sleep", "infinity"]
# CMD [ "uv", "run", "uvicorn", "src:app", "--host=0.0.0.0", "--port=8000", "--workers=2"]