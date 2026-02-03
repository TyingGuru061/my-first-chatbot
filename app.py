{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1piRqjD8mLyHqoaEY9uhPYuImoOH3EniA",
      "authorship_tag": "ABX9TyO87JOvo3ZnAW+bAO7H7zOh",
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
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kqoZnyuAKRwS",
        "outputId": "eed617ea-9605-4ce3-da8c-ef15613c3915"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2026-02-03 11:05:16.390 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.391 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.392 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.393 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.394 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.395 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.396 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.397 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.398 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.399 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.400 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.401 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.402 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.403 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.404 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.405 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.405 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.406 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.468 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.469 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.472 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.473 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.475 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.476 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.477 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2026-02-03 11:05:16.478 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "!pip install -q streamlit groq\n",
        "import streamlit as st\n",
        "from groq import Groq\n",
        "import os\n",
        "\n",
        "# 1. Setup Page Config\n",
        "st.set_page_config(page_title=\"Ibadat AI Tutor\", page_icon=\"🤖\")\n",
        "st.title(\"🤖 My First LLM Chatbot\")\n",
        "st.caption(\"Powered by Groq - Built at Ibadat International University\")\n",
        "\n",
        "# 2. Securely handle the API Key\n",
        "# When deploying, we will put this in Streamlit Secrets\n",
        "groq_api_key = st.sidebar.text_input(\"Enter Groq API Key\", type=\"password\")\n",
        "\n",
        "if not groq_api_key:\n",
        "    st.info(\"Please add your Groq API key to continue.\", icon=\"🔑\")\n",
        "    st.stop()\n",
        "\n",
        "client = Groq(api_key=groq_api_key)\n",
        "\n",
        "# 3. Initialize Chat History\n",
        "if \"messages\" not in st.session_state:\n",
        "    st.session_state.messages = [\n",
        "        {\"role\": \"system\", \"content\": \"You are a helpful assistant for students at Ibadat International University.\"}\n",
        "    ]\n",
        "\n",
        "# 4. Display Chat History\n",
        "for message in st.session_state.messages:\n",
        "    if message[\"role\"] != \"system\":\n",
        "        with st.chat_message(message[\"role\"]):\n",
        "            st.markdown(message[\"content\"])\n",
        "\n",
        "# 5. Chat Input\n",
        "if prompt := st.chat_input(\"Ask me anything...\"):\n",
        "    st.session_state.messages.append({\"role\": \"user\", \"content\": prompt})\n",
        "    with st.chat_message(\"user\"):\n",
        "        st.markdown(prompt)\n",
        "\n",
        "    # 6. Generate Response\n",
        "    with st.chat_message(\"assistant\"):\n",
        "        response_placeholder = st.empty()\n",
        "        full_response = \"\"\n",
        "\n",
        "        # Calling Groq API\n",
        "        completion = client.chat.completions.create(\n",
        "            model=\"llama-3.3-70b-versatile\",\n",
        "            messages=[\n",
        "                {\"role\": m[\"role\"], \"content\": m[\"content\"]}\n",
        "                for m in st.session_state.messages\n",
        "            ],\n",
        "            stream=True,\n",
        "        )\n",
        "\n",
        "        for chunk in completion:\n",
        "            full_response += (chunk.choices[0].delta.content or \"\")\n",
        "            response_placeholder.markdown(full_response + \"▌\")\n",
        "\n",
        "        response_placeholder.markdown(full_response)\n",
        "\n",
        "    st.session_state.messages.append({\"role\": \"assistant\", \"content\": full_response})"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "714d484e"
      },
      "source": [
        "# Task\n",
        "Build and deploy a Streamlit-based chatbot powered by the Groq API, using `localtunnel` to create a publicly accessible URL from the Colab environment."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "74091adb"
      },
      "source": [
        "## Save Streamlit App\n",
        "\n",
        "### Subtask:\n",
        "Save the chatbot code to a file named `app.py` using the `%%writefile` magic command.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "c1686a36"
      },
      "source": [
        "**Reasoning**:\n",
        "I will save the chatbot code to a file named 'app.py' using the %%writefile magic command as requested.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d5d122a6",
        "outputId": "e052f4d4-05a7-4ebe-cecb-b973b98bb04a"
      },
      "source": [
        "%%writefile app.py\n",
        "import streamlit as st\n",
        "from groq import Groq\n",
        "import os\n",
        "\n",
        "# 1. Setup Page Config\n",
        "st.set_page_config(page_title=\"Ibadat AI Tutor\", page_icon=\"ထဠ\")\n",
        "st.title(\"ထဠ My First LLM Chatbot\")\n",
        "st.caption(\"Powered by Groq - Built at Ibadat International University\")\n",
        "\n",
        "# 2. Securely handle the API Key\n",
        "groq_api_key = st.sidebar.text_input(\"Enter Groq API Key\", type=\"password\")\n",
        "\n",
        "if not groq_api_key:\n",
        "    st.info(\"Please add your Groq API key to continue.\", icon=\"အ\")\n",
        "    st.stop()\n",
        "\n",
        "client = Groq(api_key=groq_api_key)\n",
        "\n",
        "# 3. Initialize Chat History\n",
        "if \"messages\" not in st.session_state:\n",
        "    st.session_state.messages = [\n",
        "        {\"role\": \"system\", \"content\": \"You are a helpful assistant for students at Ibadat International University.\"}\n",
        "    ]\n",
        "\n",
        "# 4. Display Chat History\n",
        "for message in st.session_state.messages:\n",
        "    if message[\"role\"] != \"system\":\n",
        "        with st.chat_message(message[\"role\"]):\n",
        "            st.markdown(message[\"content\"])\n",
        "\n",
        "# 5. Chat Input\n",
        "if prompt := st.chat_input(\"Ask me anything...\"):\n",
        "    st.session_state.messages.append({\"role\": \"user\", \"content\": prompt})\n",
        "    with st.chat_message(\"user\"):\n",
        "        st.markdown(prompt)\n",
        "\n",
        "    # 6. Generate Response\n",
        "    with st.chat_message(\"assistant\"):\n",
        "        response_placeholder = st.empty()\n",
        "        full_response = \"\"\n",
        "\n",
        "        # Calling Groq API\n",
        "        completion = client.chat.completions.create(\n",
        "            model=\"llama-3.3-70b-versatile\",\n",
        "            messages=[\n",
        "                {\"role\": m[\"role\"], \"content\": m[\"content\"]}\n",
        "                for m in st.session_state.messages\n",
        "            ],\n",
        "            stream=True,\n",
        "        )\n",
        "\n",
        "        for chunk in completion:\n",
        "            full_response += (chunk.choices[0].delta.content or \"\")\n",
        "            response_placeholder.markdown(full_response + \"ဥ\")\n",
        "\n",
        "        response_placeholder.markdown(full_response)\n",
        "\n",
        "    st.session_state.messages.append({\"role\": \"assistant\", \"content\": full_response})"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing app.py\n"
          ]
        }
      ]
    }
  ]
}