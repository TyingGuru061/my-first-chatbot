{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1piRqjD8mLyHqoaEY9uhPYuImoOH3EniA",
      "authorship_tag": "ABX9TyPtGILQSKp7QZ8RYBgaZI9G",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/TyingGuru061/my-first-chatbot/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Install streamlit and the groq library\n",
        "!pip install -q streamlit groq\n",
        "\n",
        "# Install localtunnel to expose the port\n",
        "!npm install -g localtunnel"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1HZOhVSVP975",
        "outputId": "0bfaec84-d068-4f14-f58b-37bdb483079b"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K\n",
            "changed 22 packages in 3s\n",
            "\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K\n",
            "\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K3 packages are looking for funding\n",
            "\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K  run `npm fund` for details\n",
            "\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "from groq import Groq\n",
        "\n",
        "st.set_page_config(page_title=\"Ibadat AI Tutor\", page_icon=\"🤖\")\n",
        "st.title(\"🤖 My First LLM Chatbot\")\n",
        "\n",
        "# Sidebar for API Key\n",
        "groq_api_key = st.sidebar.text_input(\"Enter Groq API Key\", type=\"password\")\n",
        "\n",
        "if not groq_api_key:\n",
        "    st.info(\"Please add your Groq API key to continue.\")\n",
        "    st.stop()\n",
        "\n",
        "client = Groq(api_key=groq_api_key)\n",
        "\n",
        "if \"messages\" not in st.session_state:\n",
        "    st.session_state.messages = []\n",
        "\n",
        "for message in st.session_state.messages:\n",
        "    with st.chat_message(message[\"role\"]):\n",
        "        st.markdown(message[\"content\"])\n",
        "\n",
        "if prompt := st.chat_input(\"Ask me anything...\"):\n",
        "    st.session_state.messages.append({\"role\": \"user\", \"content\": prompt})\n",
        "    with st.chat_message(\"user\"):\n",
        "        st.markdown(prompt)\n",
        "\n",
        "    with st.chat_message(\"assistant\"):\n",
        "        completion = client.chat.completions.create(\n",
        "            model=\"llama-3.3-70b-versatile\",\n",
        "            messages=[{\"role\": m[\"role\"], \"content\": m[\"content\"]} for m in st.session_state.messages],\n",
        "        )\n",
        "        response = completion.choices[0].message.content\n",
        "        st.markdown(response)\n",
        "\n",
        "    st.session_state.messages.append({\"role\": \"assistant\", \"content\": response})"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KiEbdHd5P-JH",
        "outputId": "046fb19d-731c-427f-aeda-cd06dc69c3b3"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# This gets your public IP (needed for the tunnel password)\n",
        "import urllib\n",
        "print(\"Password/Enpoint IP for localtunnel is:\", urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip(\"\\n\"))\n",
        "\n",
        "# Run streamlit in the background and expose it via localtunnel\n",
        "!streamlit run app.py & npx localtunnel --port 8501"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MK0mgQY6P-QV",
        "outputId": "6b0d250e-80ff-47e1-aabe-70986c574425"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Password/Enpoint IP for localtunnel is: 34.126.100.18\n",
            "\u001b[1G\u001b[0K⠙\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[1G\u001b[0K\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.126.100.18:8501\u001b[0m\n",
            "\u001b[0m\n",
            "your url is: https://strong-worms-bathe.loca.lt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "dosRvtpDP-VS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "8nwt7taJP-av"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}