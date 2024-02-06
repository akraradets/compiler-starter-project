FROM python:3.9.18-bookworm

ARG WORKDIR=/src/app
ARG VENDORDIR=/src/vendor
WORKDIR ${WORKDIR}

ENV DEBIAN_FRONTEND=noninteractive
# Remove printing buffer to stdout, stderr
# https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=${WORKDIR}:${VENDORDIR}
ENV PIPENV_VENV_IN_PROJECT=1
# Timezone
ENV TZ="Asia/Bangkok"

# https://github.com/pyenv/pyenv/wiki#suggested-build-environment
RUN apt update && apt upgrade -y
RUN apt install -y build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
# Set timezone
RUN apt install -y tzdata
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone
# Set locales
# https://leimao.github.io/blog/Docker-Locale/
RUN apt install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LC_ALL en_US.UTF-8 
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  


# Here we install dependencies of our project
# Install tkiner for GUI
# RUN apt install -y python3-tk
RUN apt -y install designer-qt6
# We use pipenv to manage dependencies
RUN pip install pipenv

RUN --mount=type=bind,source=./src/Pipfile,target=/root/src/Pipfile \
    --mount=type=bind,source=./src/Pipfile.lock,target=/root/src/Pipfile.lock \
    pipenv install

# COPY SLY project to container
COPY ./sly/src/sly ${VENDORDIR}/sly
COPY ./src ${WORKDIR}
# Clear apt for optimizing image size
RUN apt clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD tail -f /dev/null