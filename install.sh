#!/bin/bash

# Install mlc-ai and mlc-chat
pip install --pre --force-reinstall mlc-ai-nightly-cu118 mlc-chat-nightly-cu118 -f https://mlc.ai/wheels

# Install git-lfs
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
apt-get install git-lfs
git lfs install

# Install Flask and Flask-CORS
pip install --ignore-installed flask
pip install Flask-CORS

# Create directory and clone repositories
mkdir -p dist/prebuilt
git clone https://github.com/mlc-ai/binary-mlc-llm-libs.git dist/prebuilt/lib
cd dist/prebuilt && git clone https://huggingface.co/mlc-ai/mlc-chat-WizardCoder-15B-V1.0-q4f16_1/
