{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO65xqDqtaEVMZ+nXu5tE+O",
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
        "<a href=\"https://colab.research.google.com/github/Sushmitha07b/codsoft/blob/main/task3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Task 3: Iris flower classification using machine learning"
      ],
      "metadata": {
        "id": "cmSNXeP4tgyT"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 73
        },
        "id": "_it1fnobmGsW",
        "outputId": "9332f6a7-e35e-4dde-c03b-514e56abbff3"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-66dd82ff-1467-4b0c-ae46-0ba0ea6995e9\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-66dd82ff-1467-4b0c-ae46-0ba0ea6995e9\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving IRIS.csv to IRIS.csv\n"
          ]
        }
      ],
      "source": [
        "from google.colab import files\n",
        "uploaded=files.upload()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "lpLVT3nInRbr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "iris = pd.read_csv(r\"IRIS.csv\")"
      ],
      "metadata": {
        "id": "E3f-EouCnVDX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "iris.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "nxIbFEfknbJt",
        "outputId": "b15425e7-0f11-4775-f2fa-4bf37d56ceef"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   sepal_length  sepal_width  petal_length  petal_width      species\n",
              "0           5.1          3.5           1.4          0.2  Iris-setosa\n",
              "1           4.9          3.0           1.4          0.2  Iris-setosa\n",
              "2           4.7          3.2           1.3          0.2  Iris-setosa\n",
              "3           4.6          3.1           1.5          0.2  Iris-setosa\n",
              "4           5.0          3.6           1.4          0.2  Iris-setosa"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e92165f4-6520-4dd6-bfc9-f4b18339230b\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sepal_length</th>\n",
              "      <th>sepal_width</th>\n",
              "      <th>petal_length</th>\n",
              "      <th>petal_width</th>\n",
              "      <th>species</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5.1</td>\n",
              "      <td>3.5</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>4.7</td>\n",
              "      <td>3.2</td>\n",
              "      <td>1.3</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4.6</td>\n",
              "      <td>3.1</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5.0</td>\n",
              "      <td>3.6</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>Iris-setosa</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e92165f4-6520-4dd6-bfc9-f4b18339230b')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-e92165f4-6520-4dd6-bfc9-f4b18339230b button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-e92165f4-6520-4dd6-bfc9-f4b18339230b');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-dcf87f3e-99a4-4fde-9d21-9865f73ceda5\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-dcf87f3e-99a4-4fde-9d21-9865f73ceda5')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-dcf87f3e-99a4-4fde-9d21-9865f73ceda5 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "iris.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DwZ1dLRwnefV",
        "outputId": "598a32e2-bfe6-46ae-92db-1ffffa0dbc68"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 150 entries, 0 to 149\n",
            "Data columns (total 5 columns):\n",
            " #   Column        Non-Null Count  Dtype  \n",
            "---  ------        --------------  -----  \n",
            " 0   sepal_length  150 non-null    float64\n",
            " 1   sepal_width   150 non-null    float64\n",
            " 2   petal_length  150 non-null    float64\n",
            " 3   petal_width   150 non-null    float64\n",
            " 4   species       150 non-null    object \n",
            "dtypes: float64(4), object(1)\n",
            "memory usage: 6.0+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "iris.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        },
        "id": "FMk8A9AUniAA",
        "outputId": "b0e93974-c39f-4547-fca2-a6539ae3e36f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       sepal_length  sepal_width  petal_length  petal_width\n",
              "count    150.000000   150.000000    150.000000   150.000000\n",
              "mean       5.843333     3.054000      3.758667     1.198667\n",
              "std        0.828066     0.433594      1.764420     0.763161\n",
              "min        4.300000     2.000000      1.000000     0.100000\n",
              "25%        5.100000     2.800000      1.600000     0.300000\n",
              "50%        5.800000     3.000000      4.350000     1.300000\n",
              "75%        6.400000     3.300000      5.100000     1.800000\n",
              "max        7.900000     4.400000      6.900000     2.500000"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-4201d8c5-0f30-47fb-86f4-47ba455a24ae\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sepal_length</th>\n",
              "      <th>sepal_width</th>\n",
              "      <th>petal_length</th>\n",
              "      <th>petal_width</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>150.000000</td>\n",
              "      <td>150.000000</td>\n",
              "      <td>150.000000</td>\n",
              "      <td>150.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>5.843333</td>\n",
              "      <td>3.054000</td>\n",
              "      <td>3.758667</td>\n",
              "      <td>1.198667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>0.828066</td>\n",
              "      <td>0.433594</td>\n",
              "      <td>1.764420</td>\n",
              "      <td>0.763161</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>4.300000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.100000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>5.100000</td>\n",
              "      <td>2.800000</td>\n",
              "      <td>1.600000</td>\n",
              "      <td>0.300000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>5.800000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>4.350000</td>\n",
              "      <td>1.300000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>6.400000</td>\n",
              "      <td>3.300000</td>\n",
              "      <td>5.100000</td>\n",
              "      <td>1.800000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>7.900000</td>\n",
              "      <td>4.400000</td>\n",
              "      <td>6.900000</td>\n",
              "      <td>2.500000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-4201d8c5-0f30-47fb-86f4-47ba455a24ae')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-4201d8c5-0f30-47fb-86f4-47ba455a24ae button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-4201d8c5-0f30-47fb-86f4-47ba455a24ae');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-8390f907-d270-4daf-8eae-ada1c4af18ec\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-8390f907-d270-4daf-8eae-ada1c4af18ec')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-8390f907-d270-4daf-8eae-ada1c4af18ec button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "iris.value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S2EwOufRnly5",
        "outputId": "c49470ac-8ae4-44cd-f0bf-b352b3193574"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "sepal_length  sepal_width  petal_length  petal_width  species        \n",
              "4.9           3.1          1.5           0.1          Iris-setosa        3\n",
              "5.8           2.7          5.1           1.9          Iris-virginica     2\n",
              "              4.0          1.2           0.2          Iris-setosa        1\n",
              "5.9           3.0          4.2           1.5          Iris-versicolor    1\n",
              "6.2           3.4          5.4           2.3          Iris-virginica     1\n",
              "                                                                        ..\n",
              "5.5           2.3          4.0           1.3          Iris-versicolor    1\n",
              "              2.4          3.7           1.0          Iris-versicolor    1\n",
              "                           3.8           1.1          Iris-versicolor    1\n",
              "              2.5          4.0           1.3          Iris-versicolor    1\n",
              "7.9           3.8          6.4           2.0          Iris-virginica     1\n",
              "Length: 147, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "iris.count()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s0eZfEuQnpA-",
        "outputId": "90fb7e27-ef5c-49ab-c7d4-ffa374581f94"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "sepal_length    150\n",
              "sepal_width     150\n",
              "petal_length    150\n",
              "petal_width     150\n",
              "species         150\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "iris['species'].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A9Xyz_QNnuWx",
        "outputId": "f345dfaf-6dfe-4e6b-d0e3-021aa560a4e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Iris-setosa        50\n",
              "Iris-versicolor    50\n",
              "Iris-virginica     50\n",
              "Name: species, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ],
      "metadata": {
        "id": "fHCrDs-Rny51"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sns.set()"
      ],
      "metadata": {
        "id": "guHBaJgAn2vX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sns.countplot(x = 'species', data = iris,  )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 475
        },
        "id": "Qa6epuTpn59D",
        "outputId": "a25080e6-204d-45c0-e59e-fb8727ee5b73"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='species', ylabel='count'>"
            ]
          },
          "metadata": {},
          "execution_count": 12
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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QKVz+RqeUaNGqaioSA8//LCefPJJNWrUSDabc37y8vLSv//97wsuEgAA4EK4HHjq1aunevXq6YorrqjMegAAACqdy4Fn0aJFlVkHAABAlXH5Gh4AAICawuUjPJ9//nmF5l1//fWu7gIAAKBSuBx4+vfvLy8vrz+d991337m6CwAAgEpxQU9a/qPi4mLt379fy5YtU0lJiR588MELKg4AAKAyVMlvS7/tttvUp08f/fe//1V8fLyruwAAAKgUVXLRss1mU48ePbR8+fKq2DwAAMB5qbK7tHJycpSXl1dVmwcAAKgwl09p/fLLL+Uuz83N1ZYtWzRv3jxdd911LhcGAABQWVwOPAkJCWe9S8uyLEVHR2vixIkuFwYAAFBZXA48zzzzTJnA4+XlJbvdriZNmujKK6+84OIAAAAqg8uB57bbbqvMOgAAAKqMy4HnTD/88IP2798vSbr88ss5ugMAADzKBQWetWvXavLkyY6wU6px48YaO3asOnfufEHFAQAAVAaXA89HH32kBx54QJdddplGjx6t0NBQSdKePXu0bNkyjRgxQq+88orat29facUCAAC4wuXAM2vWLIWHh+v1119XnTp1HMs7d+6sfv36qU+fPkpNTSXwAAAAt3P5wYPff/+9brnlFqewU6pOnTq69dZb9f33319QcQAAAJXB5cBTq1Yt5eTknHU8JydHtWrVcnXzAAAAlcblwBMbG6uFCxfqyy+/LDO2bds2LVq0iF8cCgAAPILL1/A89NBD6tWrl/r06aOoqCiFhIRIkn788Udt375dgYGBGjNmTKUVCgAA4CqXj/AEBwfr3//+t/r376+cnBxlZGQoIyNDOTk5GjBggFauXKnGjRtXZq0AAAAucfkIT1FRkWrVqqVHH31Ujz76aJnxY8eOqaioSD4+lfJsQwAAAJe5fIRn0qRJ6tWr11nHe/furcmTJ7u6eQAAgErjcuDZsGGDEhMTzzqemJiojz/+2NXNAwAAVBqXA8+hQ4fUsGHDs44HBQXp4MGDrm4eAACg0rgceOrVq6cff/zxrON79uxR3bp1Xd08AABApXE58LRr105Lly7Vt99+W2bsm2++0bJly/i1EgAAwCO4fAvVyJEjtWHDBqWkpCghIUFXXnmlJGn37t1av369AgICNHLkyEorFAAAwFUuB56GDRvqzTff1NSpU7Vu3Tp98MEH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v/7arXXUdD7uLgBV74knnpDN5hnZ9r///a/mz5+voUOHursUVCJP6rELkZKSog4dOri7DFSR6urTjh07Kj09XXa7vVK2FxERofT0dIWGhrq1jpqOwGOwkydP6qKLLtKVV17p7lJgqJrSYwUFBfLx8fnT/9k1atRIjRo1qqaqzl9xcbFKSkrk6+vr7lJqlOru04CAAAUEBFSopoqoW7euoqOjq6SOv5Ka/5UMkqSff/5Z4eHheuuttzR+/HjFxsYqJSVFUtnDuAcOHNDIkSPVpk0bRUZGKiEhQc8888yf7mPFihXq0aOHoqKiFBsbq969e2v79u2OccuyNG/ePCUmJqpFixbq3LmzXnvtNcf4jBkzNHPmTJ04cULh4eEKDw9X//79HeOff/65evXq5dj+uHHjlJ2d7VTDnDlz1LVrV0VGRiouLk533323srKyHOMvvPCCbrrpJsXExKhdu3b6+9//rkOHDp3v24lyVGWPlW57zZo1ZcZuu+02/f3vf3fa9pgxYxQbG6uoqCj17dtXO3bscFonISFBTz31lNLS0tSpUydFRUUpOzv7T+sq79RIbm6unn76abVv314tWrRQQkKCpk6d6jRn6dKljr5PSEjQrFmzVFJScs73Mzs7W+PGjXP8HL169dLnn3/uNKf0ff3Xv/6lxMRERUZGaufOnefc7l+dJ/TpH08lnaumvLw8jRkzRjExMYqPj9eLL76o+fPnKzw83LHt8k5phYeHKy0tTTNmzFCbNm0cn5knTpxwzCnvlFZBQYFeeuklde7cWS1atFD79u01duxYx/iXX36poUOH6oYbblB0dLSSk5P19ttvV+i993Qc4THMiy++qA4dOmjq1Kln/cB9+OGHdejQIY0fP16BgYH69ddfy/wP448+//xzPfbYY7r33nvVoUMHnTx5Utu3b1deXp5jzj/+8Q8tX75cQ4cOVcuWLfXFF1/ohRdeUK1atdS7d2+lpKTowIEDevfdd7VgwQJJp7+5SNKOHTt0zz33KDY2Vi+//LJ+//13TZ06VT/88IOWLl0qb29vvf3223r55Zf1wAMPKDo6Wnl5edq6dauOHz/uqOHw4cMaMmSIgoKCdOTIEb366qvq37+/Vq1aJR8f2r0yVEWPNW7cWNHR0crIyNCNN97oWL5371598803Gj58uKTTvzy4T58+qlOnjiZMmKBLLrlEixYt0sCBA/X+++8rMDDQse7777+vK664Qo899phsNpvq1KmjUaNGnVddBQUFGjhwoPbv369hw4YpLCxMBw4c0NatWx1zFi1apEmTJql///7q2LGjvvzyS82cOVN5eXl65JFHyt1ucXGx/va3vykrK0tjxozRpZdeqkWLFumee+7R0qVL1aJFC8fcHTt2aP/+/Ro5cqTsdrv+53/+56z14v+4s0/Pp6Zx48bps88+00MPPaTLL79cy5Yt0zfffFOhn/H1119Xq1atNHnyZO3du1dTpkxRYGCgxowZc9Z1RowYoc8++0xDhgxRdHS0jhw5ovfff98x/ssvv+jaa69V79695efnpy+++ELjx4+XZVm69dZbK1SXx7JQY02fPt2Kjo62LMuysrKyrLCwMGvQoEFl5vXr188aPHiw43V0dLS1cOHC89rX3LlzrdatW591fN++fVZ4eLi1dOlSp+XPP/+81bZtW6u4uLhMzWcaNmyY1bFjR6ugoMCxbMOGDVZYWJi1bt06y7Isa+LEidatt95a4ZqLioqsAwcOWGFhYdaGDRsqvB7+T3X22IIFC6zIyEgrLy/PsWzGjBnW9ddfb506dcqyLMt6+eWXrVatWlm///67Y86pU6esjh07Ws8995xjWadOnazWrVtbx48fd9rHn9X1x/5MT0+3wsLCrC+++KLc+UVFRVZsbKw1evRop+VTp061IiIirCNHjliWZVlvvvmmFRYWZh0+fNiyLMtau3atFRYWZn388ceOdQoKCqyOHTtaw4cPdyzr16+fFRERYf3yyy9nrRme16d//Ps+W027d++2wsLCrH/961+OZcXFxVa3bt2ssLAwx7LPPvvMCgsLs7Zv3+5YFhYWZt1xxx1O23vkkUesLl26OF7/sY5PPvnECgsLs955550K/awlJSVWYWGhNWHCBOuuu+6q0DqejFNahunYseOfzmnevLnmz5+vJUuWaN++fWXGi4qKHH+Ki4sd62RnZ2vs2LHauHGj8vPzndb59NNPJUndunVzWr9Nmzb67bff9Ouvv56zpi1btqhz585O1ybccMMNstvtjm/TzZs317fffqtnn31WW7ZsUWFhYZntfPTRR+rVq5datWql5s2bq3379pJOfwND5aiqHktKSlJhYaHWrl3rmJeRkaFu3brJz89PkrRx40bFxsbK39/fsb7NZtP1119f5g6W2NhY1alT57zq+qNNmzYpNDT0rHcAZWZm6ujRo07f9iWpe/fuKiwsdDrle6YtW7aobt26ateunWOZr6+vunbt6nT0SJLCwsI4quMCd/ZpRWsq7dnOnTs7ltlsNnXq1OlPa5ekNm3aOL0ODQ3VgQMHzjp/06ZNql27tnr06HHWOTk5OZo0aZI6deqkiIgIxwXTP/74Y4Vq8mQEHsOceUj/bF566SXFxcVp2rRp6tatm2688UbHIc2ff/7Z0eQRERHq2rWrJCk+Pl5TpkzR7t27NWjQIMXFxenhhx92XGNz9OhRWZaluLg4p/XvueceSfrTwJObm1tu7YGBgcrJyZF0+hz5uHHj9Mknn6hv376Kj4/XpEmTdPLkSUnS9u3bdf/99ysoKEhTpkxRenq6li1bJkk6depUBd49VERV9ViDBg0UGxurVatWSZJ27typPXv2qGfPno7tHj16VGvXrnVaPyIiQitXrizzQV9eneeqqzzZ2dkKCgo663hpb/5xX6WvS8f/6Gz9fumll5ZZ59JLLz3r/nF27uzTitb022+/ydfXV5dcconT8opeaPzHu698fX1VUFBw1vnZ2dlq0KCBvLy8zjpn7Nixevfdd3Xvvfdq3rx5WrFihW6//fZzbrem4KIGw5yrkUsFBQXp2WefVUlJiXbs2KHZs2dr9OjRWrNmjRo2bKgVK1Y45p75jSU5OVnJyck6cuSI1q1bp2effVY+Pj565pln5O/vLy8vLy1ZsqTcO0hCQkLOWZO/v78OHz5cZvnhw4fl7+8v6fQ3n4EDB2rgwIE6ePCgVq1apalTp6p+/foaNmyY1q5dq7p162ratGmOu3H279//p+8Hzk9V9liPHj00ceJEHT16VKtWrVKDBg3UunVrx7i/v7/atWunkSNHltnnH79dl1fnueoKDg4uM79evXr6/vvvz/pz1qtXT5LKPOektJdLe/ePztbvv//+e5l1KvJ+oyx39mlFa2rQoIEKCwuVl5fnFHqq6rk59erV02+//SbLssp9f06dOqX//Oc/Gjt2rNMNJUuWLKmSeqobR3j+wmw2m6KiojRq1CgVFRVp37598vPzU2RkpOPPmXcKlAoICFBKSoratm2rzMxMSaePAEmnv0GcuX7pn9KLk8/2DaRVq1Zat26dioqKHMs2btyo3NxctWrVqsz8hg0b6t5771V4eLijhpMnT8rX19fpP+R33nnnAt4hXKjz7bFu3bpJkt577z2tWrVK3bt3d7qVvE2bNtqzZ49CQ0PL9Fh5vXo+dZWndH/btm0rdzwkJEQBAQFl7tpZvXq1fH19FRUVVe56rVq10rFjx/TJJ584lhUVFWnt2rXl9juqVmX3aUWVXpy+bt06x7KSkhKtX7/+An+i8rVp00b5+flavXp1ueMFBQVlHntw7Ngxffjhh1VST3XjCM9fTF5engYNGqTk5GSFhISosLBQixYtkt1uV/Pmzc+63vTp05Wdna3WrVsrMDBQu3bt0oYNG3T33XdLOv3B37dvXz388MMaNGiQWrZsqcLCQu3du1ebN2/WrFmzJJ0+x1xUVKQFCxYoJiZGdevWVbNmzTR06FD16tVLQ4YMUf/+/R13aUVFRTkeBPf444/LbrcrOjpadrtdX3zxhXbu3KnevXtLktq2basFCxbo6aefVteuXfXll19q5cqVVfuGogxXe0z6vyM4qampOnToUJnTBHfffbfeeecd9evXTwMGDNBll12mI0eOaNu2bWrYsKGjHyurruTkZC1ZskSDBw/W8OHDddVVV+ngwYPasmWLnn76aXl7e+v+++/XpEmTFBAQoA4dOuirr75SWlqaBg4cqPr165e73Y4dOyoqKkoPPfSQHnzwQcddWocOHdL06dPP/QajUlRln1bUVVddpa5du2rSpEnKz8/XZZddpmXLlunkyZNVcmSvTZs26tChgx599FH99NNPatmypbKzs/Xee+9p2rRpuuSSSxQZGam0tDQFBATIx8dHc+bMUd26dY14WjOB5y+mVq1aCgsL06JFi/Trr7/qoosuUosWLTRv3rxznjeOjIzUggULtHr1ah07dkyNGjXSoEGDdN999znmjB8/XiEhIUpPT1dqaqouvvhihYSEOF3Q2alTJ/Xp00dz5szR4cOHdf3112vRokVq0aKF5s+frxdffFEjRoxQnTp1lJCQoEceeUTe3t6SpJiYGC1btkzLly9Xfn6+goODNW7cOMfzLDp06KAxY8Zo8eLFeuutt3Tttdfqn//8pxITE6vo3UR5XO2xUj179tSHH36oJk2alDlCUr9+faWnp2vatGl64YUXlJ2drcDAQLVs2dJxjUVl1uXn56fXXntNL730kv75z38qOztbjRo1crros3///vLx8dFrr72mN954Qw0aNNDw4cPP+TRxb29vzZkzR1OmTNHzzz+vEydOKCIiQvPnz3e6JR1Vpyr79Hw888wzeuqppzRlyhT5+fnp1ltv1VVXXaXXX3/d5W2eS+nz0NLT0zVz5kwFBgaqbdu2jvGpU6fq8ccf19ixY1WvXj31799fJ06c0Pz586uknurkZVmW5e4iAADAaX379pXNZtOiRYvcXYpROMIDAICbvPfee/r1118VFham/Px8vfvuu9qyZYtSU1PdXZpxCDwAALhJnTp1tHLlSu3du1eFhYVq1qyZnn/+eXXp0sXdpRmHU1oAAMB43JYOAACMR+ABAADGI/AAAADjEXgAAIDxCDwAoNMPEDzz9wcBMAuBBwAAGI/b0gFAcvxS2z/+1nUAZiDwAAAA43FKC0C1OnbsmP7xj38oISFBLVq0UHx8vO655x598803kk5fS9OzZ0/t2LFDvXr1UlRUlBISEvTGG2+U2VZBQYGmT5+url27qkWLFurQoYOmTJniOFpzppUrV+qOO+5Qy5Ytdf3116tv37765JNPHOPlXcNT0e1v3LhRvXv31nXXXaeYmBglJibqxRdfrIy3C0Al4VdLAKhWTzzxhN577z3169dPoaGhys7O1tatW7Vnzx5FRERIknJycjR48GAlJSWpR48eWr16tZ588kn5+vrqjjvukCSVlJTovvvu09atW3XnnXcqNDRUu3bt0oIFC7R3717NmjXLsc+ZM2dqxowZiomJ0QMPPCBfX19t27ZNn332mW644YZy66zo9nfv3q0hQ4YoPDxcDzzwgPz8/LRv3z598cUXVfxOAjgvFgBUo1atWlkTJ04863i/fv2ssLAwa/78+Y5lp06dspKTk634+HiroKDAsizLevvtt62rr77a+vzzz53Wf+ONN6ywsDBr69atlmVZ1t69e62rr77aGjZsmFVcXOw0t6SkxGm//fr1c7yu6PZfffVVKywszDp8+PD5vA0AqhmntABUK7vdrm3btungwYNnnePj46O77rrL8drPz0933XWXDh8+7Dj1tWbNGoWGhqpZs2Y6cuSI409cXJwkafPmzZKktWvXqqSkRMOGDZPN5vyR5+XlddYaKrp9u90uSVq3bp1KSkrO9+0AUE04pQWgWo0ZM0Zjx45Vx44dFRERoQ4dOuiWW25RcHCwY05QUJDq1KnjtF7Tpk0lSfv371d0dLT27dunPXv2KD4+vtz9HD58WJL0008/yWazKTQ09LzqrOj2u3fvruXLl2v8+PGaOnWq4uPj1bVrV914441lAhYA9yHwAKhW3bt313XXXacPPvhAGzdu1Lx585SWlqYZM2aoQ4cOFd5OSUmJwsLCNG7cuHLHGzVqdEF1VnT7F110kV5//XVt3rxZ//nPf7RhwwZlZGQoPT1d8+fPl7e39wXVAaByEHgAVLugoCD17dtXffv21eHDh3XrrbfqlVdecQSeQ4cO6cSJE05Hefbu3StJuvzyyyVJTZo00c6dOxUfH3/OU1NNmjRRSUmJ9uzZo2uuuabCNVZ0+5Jks9kUHx+v+Ph4jRs3Tq+88opeeuklbd68WW3atKnwPgFUHY63Aqg2xcXFysvLc1oWGBiooKAgp1u9i4qKlJ6e7nhdUFCg9PR0BQQEOO7kSkpK0sGDB7Vs2bIy+zl58qROnDghSerSpYtsNptSU1PLXGNjneMxZBXdfnZ2dpnx0mBV3u3xANyDIzwAqs3x48fVoUMHJSYm6uqrr1adOnX06aef6uuvv9bYsWMd84KCgpSWlqb9+/eradOmysjI0Hfffaenn35avr6+kqTk5GStXr1aTzzxhDZv3qxrr71WxcXFyszM1Jo1azR37lxFRkbqiiuu0NChQzVr1iz16dNH3bp1k5+fn77++msFBQXpwQcfLLfWim4/NTVVW7ZsUYcOHXT55Zfr8OHDWrJkiRo1aqRWrVpVy/sK4M/xpGUA1aagoEDTpk3Txo0blZWVJcuy1KRJE911113q06ePpNMPADx69KgmT56sSZMm6dtvv9Wll16qQYMGqW/fvk7bKyws1GuvvaaVK1dq3759ql27tho3bqyEhATdfffdqlu3rmPum2++qcWLF+uHH35Q7dq1FR4ervvuu89xyqn0oYOLFi06r+1v2rRJixYt0tdff62jR4+qfv36at26tUaMGOG40BqA+xF4AHiU0sDz7rvvursUAAbhGh4AAGA8Ag8AADAegQcAABiPa3gAAIDxOMIDAACMR+ABAADGI/AAAADjEXgAAIDxCDwAAMB4BB4AAGA8Ag8AADAegQcAABiPwAMAAIz3/wCXFMn+P5yLUQAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "iris['species'].value_counts().plot(kind='barh', color=['red','green','yellow'], title='species count')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 474
        },
        "id": "5fWyBj-Yn_M5",
        "outputId": "942bbe02-5357-4440-ca1d-260656aea668"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: title={'center': 'species count'}>"
            ]
          },
          "metadata": {},
          "execution_count": 13
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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AwAAMAwBDwAAwDDXHfBSU1MVHR19zXHJyckaOHDgDRVVnpT0+V6v1atXKywsTGfOnCn1uQEAQMXmdbMmHjdunDw8bv0Fwh49eig+Pt7uMgAAAEqs1APexYsXVblyZd11112lPXWpysvLk5eX1zVDaJ06dVSnTp0yqur6OZ1OuVwueXt7210KAAAoJ/6rJbZjx44pLCxMq1ev1pgxYxQTE6MePXpIKnqK9uTJkxo2bJji4uIUERGhhIQETZw48Zpzr1+/vsi+hx9+WCkpKYXmHjFihGJiYhQZGak+ffpo7969hY5JSEjQX/7yF82fP1/t27dXZGSksrKyrllXcados7Oz9corr6ht27YKDw9XQkKCpk6dWmjMO++8o86dO7v3z549Wy6X66r9zMrK0ujRo93Po1evXvryyy8Ljbnc1//93/9V586dFRERof379191XgAAULGUygretGnTFB8fr6lTp14xxLzwwgs6ffq0xowZo8DAQJ04caJICPu1evXqKSoqShkZGXrggQfc2w8fPqxvvvlGQ4YMkSSdO3dOjz32mKpWraqXX35Z1atXV3p6uvr166cPP/xQgYGB7mM//PBD3XHHHXrppZfk4eGhqlWr6vnnn7+uuvLy8tSvXz8dP35cgwcPVmhoqE6ePKkdO3a4x6Snp2vChAlKTk5Wu3bttHPnTs2cOVM5OTkaOXJksfM6nU4988wz+uGHHzRixAjddtttSk9P15NPPql33nlH4eHh7rF79+7V8ePHNWzYMPn5+el3v/vdFesFAAAVT6kEvEaNGunVV1+96pg9e/YoJSVFXbp0cW/r3r37VY/p2rWrpkyZotzcXPn6+kqS1qxZI39/f7Vu3VqStGjRImVnZ2vlypXuMBcbG6vOnTtrwYIFeuGFF9zz5efna/78+apateoN1/Xee+/pX//6l955551CK3sPPfSQpF+C2qxZs9S1a1eNGTNGktS6dWvl5+crLS1NAwYMUM2aNYvM++mnn2r37t1688031aZNG/dxnTp10htvvKHU1FT32HPnzmnVqlUEOwAAyikPD4e8vOy7FqFUHrldu3bXHNOkSROlpaVp6dKlOnLkSJH9BQUF7g+n0ylJSkxMVH5+vj7++GP3uIyMDHXq1Ek+Pj6SpC1btigmJkb+/v7u4z08PNSyZUvt2bOn0GPExMQUCnclqeu3vvji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gGHKXcBLTU1VdHT0NcclJydr4MCBZVDRtW3btk1z5861uwwAAABJkpfdBdyocePGycOjfOTT//u//1NaWpoGDRpkdykAAAC3XsC7ePGiKleurLvuusvuUgAAAMql8rEEdgXHjh1TWFiYVq9erTFjxigmJkY9evSQVPQU7cmTJzVs2DDFxcUpIiJCCQkJmjhx4jUfY9WqVeratasiIyMVExOj3r17a/fu3e79lmVpwYIF6ty5s8LDw9WhQwctXLjQvT81NVUzZ87U+fPnFRYWprCwMCUnJ7v3f/nll+rVq5d7/tGjRysrK6tQDfPmzVPHjh0VERGh++67T0888YR++OEH9/4pU6bo97//vaKjo9WmTRulpKTo9OnT19tOAABQQdwSK3jTpk1TfHy8pk6dKpfLVeyYF154QadPn9aYMWMUGBioEydOaO/evVed98svv9RLL72kp556SvHx8bp48aJ2796tnJwc95hXX31VK1eu1KBBg9SsWTN99dVXmjJliipVqqTevXurR48eOnnypNasWaNFixZJknx9fSVJe/fu1ZNPPqmYmBj9/e9/13/+8x9NnTpV3333nd555x15enrqvffe09///nc999xzioqKUk5Ojnbs2KGff/7ZXUNmZqYGDhyoWrVq6cyZM3rrrbeUnJystWvXysvrlngJAQBAGbol0kGjRo306quvXnXMnj17lJKSoi5duri3de/e/arH7N69WzVq1NDIkSPd29q1a+f+/OjRo1q8eLHGjx+vnj17SpLi4uJ08eJFzZo1Sz179lSdOnVUp04deXh4KCoqqtD8c+fOVVBQkObOnStvb29J0u9+9zv1799fmzdvVkJCgnbv3q2wsLBCq5H3339/oXkmTZrk/tzpdCo6Olpt27bV1q1b1bp166s+RwAAUPY8PBzy8rLvROktEfB+HbqupEmTJkpLS5Onp6datWqlO+64o9D+goIC9+cOh0Oenp5q0qSJsrKyNGrUKP3+979X8+bNVaVKFfe4zz//XJLUqVOnQsfHxcVp/vz5OnHihOrWrXvFmrZv365u3bq5w50ktW7dWn5+ftqxY4cSEhLUpEkTLV26VJMmTVLHjh3VrFmzQuMlafPmzZozZ44OHDig3Nxc9/bDhw8T8AAAKId8fSvb+vi3RMALDAy85pjp06dr+vTpmjFjhsaPH6/g4GClpKSo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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.swarmplot(x= 'species', y='petal_length', data = iris)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 530
        },
        "id": "FXoAVI4yoBno",
        "outputId": "795e5345-e010-4b2e-b44d-3bbc034f36aa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='species', ylabel='petal_length'>"
            ]
          },
          "metadata": {},
          "execution_count": 14
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/seaborn/categorical.py:3398: UserWarning: 10.0% of the points cannot be placed; you may want to decrease the size of the markers or use stripplot.\n",
            "  warnings.warn(msg, UserWarning)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjIAAAG5CAYAAACUU97fAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABBZ0lEQVR4nO3deXgUVdbH8V8nJAjEkAQSEGQTTZQQVgWCyqq4gIOiKLKIyrzCCG4jKjig44C7uAHqoKKIoiCiKJsIDA4yiCyOgrKqRGSXJCQhQJau9w8mbZJe0unqTnelv5/n4dHUrbp10hRwUnVPHZthGIYAAAAsKCLYAQAAAPiKRAYAAFgWiQwAALAsEhkAAGBZJDIAAMCySGQAAIBlkcgAAADLIpEBAACWRSIDAAAsq0awA6gKhmHIbucFxgAAWEVEhE02m63C/cIikbHbDWVmHg92GAAAwEsJCXUUGVlxIsOjJQAAYFkkMgAAwLJIZAAAgGWF1BqZYcOG6ZtvvnE59vzzz6tv375VHBEAAAhlNsMwQqacZ/fu3crLyyuzbdasWVq+fLnWrFmjhIQEn+YtLraz2BcAAAs5vdi34gdHIXVH5txzz3Xadv/99+viiy/2OYkBAADVV0ivkdm8ebN+++03XXPNNcEOBQAAhKCQTmQWLVqk2rVrq3fv3sEOBQAAhKCQerRUWlFRkZYuXapevXqpdu3apuerUSOkczYAAOCDkE1k1q5dq8zMTPXr18/0XBERNsXH1/FDVAAAIJSEbCKzaNEixcXF6ZJLLjE9l91uKCcn3w9RAQCAqhAbW8t6VUslTp48qRUrVuhPf/qToqKi/DJnUZHdL/MAAODK5p1HtHjdHu37/bga16+jvunN1SE5MdhhVXshuXBk1apVys/Pp1oJAGAJm3ce0bQFW/TLgVwVFNr1y4FcTV+wRZt3Hgl2aNVeSCYyn332mRo1aqSOHTsGOxQAACq0eN0ep22GpMXrMqo8lnATconMsWPHtGbNGl199dWy2Spu3w0AQLDt+9312+P3u9kO/wm5NTJ169bV1q1bgx0GAABea1y/jn45kOu0vVF9KmYDLeTuyAAAYDV905ur/DMEm6R+6c2CEU5YCammkYFC00gAQKCdrlrK0P7fj6tR/Trql95M7ala8pm3TSNJZAAAQMjxNpHh0RIAALAsEhkAAGBZJDIAAMCySGQAAIBlhdx7ZAAAsIKKeivRe6lqULUEAEAllfRWKs0mafSANHVITqxwHBWjagkAgACpqLcSvZeqDokMAACVVFFvJXovVR0SGQAAKqmxmx5KJb2VKhqH/5DIAABQSRX1VqL3UtVhsS8AAD4o31vpgmbx2paR6ahSOv11Nr2XfESvpVJIZAAAgUSVkv9RtQQAQBWhSil4SGQAADCJKqXgIZEBAMAkqpSCh0QGAACTqFIKHhb7AgDgB+WrmKhSMoeqpVJIZAAAsBaqlgAAQLVHIgMAACyLRAYAAFhWjWAHAACAFZ1e3LvH0ZKgb3pz3uIbBCz2BQCgkmhJEHgs9gUAIEBoSRA6SGQAAKgkWhKEDhIZAAAqiZYEoYNEBgCASqIlQehgsS8AAD4o35Lggmbx2paRSRWTn9CioBQSGQBAIFHF5H9ULQEAUEWoYgoeEhkAAEyiiil4SGQAADCJKqbgIZEBAMAkqpiCh8W+AAD4Qfkqpn7pzdSehb4+o2qpFBIZAACshaolAABQ7ZHIAAAAyyKRAQAAllUj2AEAABCqTi/g3eNT24GKjjUzN/7AYl8AAFww03agomNpaVAxFvsCAGCCmbYDFR1LSwP/CclE5uOPP9a1116rtLQ0de7cWX/+85918uTJYIcFAAgjZtoOVHQsLQ38J+TWyLz66qt6/fXXNWrUKLVr105ZWVlat26diouLgx0aACCMNK5fR78cyHXa7k3bgYqONTM3ygqpRObnn3/WtGnT9Morr6h79+6O7VdccUUQowIAhKO+6c01fcEWlV5I6m3bgYqONTM3ygqpxb7PPfecvvjiC33++ed+nZfFvgAAX5RvO3BBs3hty8h0WWlUvgrp9L7ZblsW0NLAM0u2KBg2bJji4uJ0wQUXaPbs2crNzVXr1q01fvx4tW3b1ud5SWQAAGZ5qjSSRBWSn3mbyITUo6UjR45o69at2rlzpx599FHVqlVLr732mm6//XYtX75c9erV83nuGjVCcl0zAMAilnztXFFkuNleeqxTqwaBDSzMhVQiYxiG8vPz9dJLL+n888+XJLVt21a9evXSu+++q3vuuceneSMibIqPZwEVAMB3niqN3D3a2P/7cf79CbCQSmRiY2MVFxfnSGIkKS4uTq1atdLu3bt9ntduN5STk++PEAEAYapx/Tr6eX+O0/aSSiN3Y1lZLG3wRWxsLes9Wjr33HP166+/uhw7deqUqbmLiuymjgcAhJ/SC3jjYmo6jdsk9e3STIbkVIUkSXknCvXnp1fRgiCAQmrhSM+ePZWdna1t27Y5tmVlZemHH35QampqECMDAISbksW9vxzIVUGhXYezTkiSkuJrqWZUpFqcFasxA9LUPjlRHZITNXpAmlqcFauaUZFKiq8lSTqcdUIFhXb9ciBX0xds0eadR4L5LVVLIVW1ZLfbdeONN+rYsWO67777VLNmTc2YMUN79uzRokWLlJjoWyZL1RIAoLImzdrg8qV1Lc6K1cThFwbsWJxmyV5LERERmjFjhtq1a6dHHnlEf/3rXxUTE6P33nvP5yQGAABfBLJFAfwnpNbISFJCQoKeffbZYIcBAAhzgWxRAP8JqTsyAACEir7pzWUrt60yLQp8PRaVE1JrZAKFNTIAgIqUbzHQN725JAWsRQE8s2SLgkAhkQEAeOKp/UDpRIUWBVXHkot9AQAIhsXr9jhtM3T6bow3+3hzPAIj5Bb7AgBQ1bypMvLcosD1ww2qlAKPOzIAgLDX2E01UekqI0/7eHM8AoNEBgAQ9rypMvK0D1VKwcNiXwAAVFJ1lFGmyuj0OhfvKpHKH39Bszhty8hyWeH0x/573I6HO6qWSiGRAQBUljeVTL4ea2bucEHVEgAAJpipRKroWKqc/IdEBgAAFwLZa4leTP5DIgMAgAtmKpEqOpYqJ/9hjQwAIGx4WmDrqsXA0q9/dXpDTFJ8LWXnnfJ4fFxMtA5nnSxznE3SmAFpav+/NTLTF2zxae5wWRjMYt9SSGQAAL60GLiqS1NHlVLdmGgdzjrh9fGS1CC+lrLzClz2Wipd5VTZucNhYbC3iQxv9gUAhAXPC2ydf6Y3JG3LyNbE4RdKkibN2lCp4yWp9hlRenJkusuxDsmJjkSksnOXjFXnRMZbJDIAgLBgtsVAIFsU0P7Adyz2BQCEBbMtBgLZooD2B74jkQEAhAWzLQYC2aKA9ge+Y7EvACBsuGpD4K7FgPkWBfHalpHpdYuCysxdfuFwdUTVUikkMgCAyqJFQXDRogAAABNoUWANJDIAALhAiwJrIJEBAMAFWhRYA4kMAAAumKkWquhYKpH8h8W+AAC44VyJFKdtGVle92pyV4Xkau5wqESqDKqWSiGRAQCY5UuvJqqQfEevJQAA/MiXXk30Qwo8EhkAALxAP6TQxGJfAAC8QD+k0EQiAwCAF+iHFJpY7AsAgBtm+iFV1GsJnlG1VAqJDACgsgLZawkVo9cSAAAmBLLXEvyHRAYAABcC2WsJ/kMiAwCAC4HstQT/4T0yAAC40De9uaYv2OL0hpjjJws1aspqjy0K4mJqOs1HFVNgsNgXAAA3Slci1Y2J1uGsE2XGPbUokKSk+Fo6lldALyUfULVUCokMAMCsSbM26JcDuU7bW5wVK8lwOzZx+IVVEF31Q68lAAD8iBYFoYnFvgAAeIEWBaGJRAYAAC/QoiA0sUYGgCWVf3U8r3+HK56uE2+uoUC2KPA1tnC59lnsWwqJDFC98Pp3eMPTdSI5VxmVv4YC2aLA19i8ibu6oEUBgGqL17/DG56uE2+uoUC2KPA1Nq59ZyFVtbRgwQKNHz/eafv//d//aezYsUGICEAo4vXv8IbZKqNAtijwNTaqo5yFVCJT4o033tCZZ57p+LpBgwZBjAZAqGlcv47Ld3ZQIYLSPF8nrt/7UvoaMnOdVXSs77FVHHe4CclHS6mpqWrXrp3j11lnnRXskACEECpE4A2zVUZmrrOKjvU1Nq59ZyG12Lfk0dK6deuUkJDgt3lZ7AtYX2WqR4AS5SuJPFcZxWlbRlaZaiBJFe7jrpqoomu0MrF5O1adWLJqqSSRqVevnrKystSoUSPdeOON+vOf/6zIyEif5yWRAayNKiUEmjfXmNkqKFSOJVsUJCYm6q677lLbtm1ls9m0atUqvfjiizp06JAeeeQRU3PXqBGST9EAeGHJ184VGcb/tndqxRo6mOfNNeZpH1e4RqtGSCUyl156qS699FLH15dccolq1qypWbNmadSoUUpKSvJp3ogIm+Ljw3chFGB1nio8+LMNf/DmGvNcaeQa12jghVQi48pVV12lmTNnatu2bT4nMna7oZycfD9HBqCqNK5fRz/vz3Ha3qh+HWVl8dgY5nlzjXnaRxLXqJ/Fxtay3qOlQCoqsgc7BAA+urpLM01fsMXpp968EwX689OrwvYV7vAfV9eYTdL5TeP06Jvrte/344qLiXY6ziapb5dmMiQ312ihy2tU4jr1l5Ba7OvKU089pXfeeUdffvmlEhN9+w1msS9gfaUrNeJionUo60SZcRZdwixXVUxLvv7Vab8G8bWUnVfgsZqobky0Dru5RitqUcB1epolF/uOGDFCnTt3VkpKiiRp5cqVmjdvnm655RafkxgA1UOH5ETHX/CTZm1wGv/jNe3OP5uVjPEPBDwpfY1Jrq8zSap9RpSeHJnu8XhP12iH5ESPrQa4TisnpBKZFi1a6KOPPtLBgwdlt9vVvHlzPfzwwxo2bFiwQwMQQsy+eh7wRrBaFKByQiqRmTBhQrBDAGABZl89D3gjeC0KUBm8XAWA5fAKd1SFYLUoQOWE/GJff2CxL2B9lXn9uzevnmcdArxRmWvJny0KYNEWBYFCIgNYm5kKD6pD4C+0KKha3iYyPFoCEPI8VXgE8ligNE/XEtdZ8ITUYl8AcCWQ1SOAt6iWC02mE5k1a9Zo/vz52rt3r3JyclT+SZXNZtOKFSvMngZAGAtk9QjgLarlQpOpROaNN97QlClTVK9ePbVp08bxIjsA8Ke+6c1dvj7e2+oRX48FSvN0LblqUcB1VjVMLfbt1q2bWrZsqRkzZigqKsqfcfkVi32B0FPZPjPO1SPx2paR6VP1iKdjfYkN4cNTpRFVSP5VJVVL7dq107hx4zRo0CBfp6gSJDJAaDFbSWSmeqSic1PlBISGKqlaSktL0y+//GJmCgBhyGyFh5nqEbPjAEKLqUTm73//u7744gt99tln/ooHQBgwW0nk6XizPW6ocgKspVKLfa+55hqnbUVFRXrwwQf197//XQ0bNlRERNncyGaz6dNPPzUXJYBqxWwlkZnqEXrgANVLpRKZuLg4l9uaNWNVNgDvuar+kKTjJws1asrqChfgxsVEO83pqXqk9NxxMTXdHusuNqpPgNBFiwIAQVG6wqNuTLQOZ50oM17RAlxJahBfS9l5BR6rR1zNLUlJ8bV0zMWx5Y+n+gQIjiqpWvrkk0904YUX6uyzz3Y5vm/fPm3YsEHXXnutr6fwCxIZILRNmrXB5eOcFmfFauLwCyscNzM3gNBUJVVL48eP17fffut2/LvvvtP48ePNnAJAGAjkAlwW7wLVm6lEpqKbOfn5+YqMjDRzCgBhoLGbhbSlF+B6GjczNwBrq3SLgu3bt2v79u2Orzdu3Kji4mKn/XJycvTBBx+oRYsW5iIEUO1VtMCWFgUA3Kn0Gplp06Zp2rRppw+22TzelYmNjdXTTz+tnj17movSJNbIAIHj6XX+lRkr30agogW4ZloUVLR419fvCeGNa8O/ArbY9/Dhwzp8+LAMw9DAgQN19913q1u3bmUntdlUq1YtNW3aVDVqmG6wbRqJDBAYvrYK8DQW6BYFwZwb1RetLfzP20Sm0llGUlKSkpKSJEnvvPOOWrZsqXr16lU+QgCW5/l1/s4/I3kz5s1f+r6eN9hzo/rydN1wbQSWqdslnTp18lccACzIU0WQ4eIffW/GAnneYM+N6ovquOAxlcjccsstHsdtNptq1qyphg0bqnPnzrriiitC4lETAP/wvVWA5zYCgTtvcOdG9UVri+AxXX598OBBffPNN9qxY4fy8vKUl5enHTt26JtvvtHBgwd19OhRff7557r//vt1/fXXKzMz01+xAwiyvunNZSu3raQiyNexQJ432HOj+uLaCB5Tb/bduHGjRo8erfHjx+uaa65xvDOmuLhYn376qZ5++mm99tpratu2rT7++GNNnDhR1113nSZPnuy3b8AbLPYFAsfT6/wrM+apCumP/b2rRHKeO07bMrICMjftC1CCa8O/qqRFwY033qiOHTvqoYcecjn+9NNPa/PmzZo7d64k6ZFHHtGqVav01Vdf+XpKn5DIAKGtoooPMxUhgZwbQOBUSYuCHTt2uO2zJElnn312mZfnpaam6tixY2ZOCaAa8lwpVPF4sOYGEHymEpnExEQtW7ZMdrvdacxut2vp0qWqX7++Y1t2drbq1q1r5pQAqqFg9lqi2gSwNlOJzG233aYNGzbo5ptv1vz58/XNN9/om2++0YcffqhBgwZp06ZNuv322x37L1u2TG3atDEdNIDqJZi9lujFBFibqVroIUOGyGaz6eWXX9aECRNks51es20YhuLi4jRhwgQNGTJEklRQUKDx48ercePG5qMGUK0Es9cSvZgAazO12LdEYWGhtm7dqv3790uSGjVqpNatWysqKsp0gP7AYl8g9FVU8VGZSiSzfZyoNgGCr0qqlqyCRAaoXuiHBFR/Aeu15Mru3bu1d+9etxVJ1157rT9OAwCS6IcE4A+mEplff/1VDzzwgL7//nu5u7Fjs9lIZAD4Ff2QAJQwlcg88sgj2rlzpx5++GFdeOGFio2N9VdcAOAW/ZAAlDCVyGzevFkjR47UsGHD/BUPgDBUfnFu+RYC5feJi4l2mqOk0siQnKqQJOn4yUKNmrLaqxYFrs4PIDSZeo9MfHy8zjzzTH/FAiAMlSzc/eVArgoK7frlQK6mL9iizTuPuN3ncNZJSVKD+FqqGRWpFmfFasyANLVPTlSH5ESNHpCmFmfFqmZUpJLia0mSDmedcDm/N+cHELpMJTKDBg3Sp59+quLiYn/FAyDMeNMiwNU+klT7jCi9en93TRx+YZly6Q7JiZo4/EK9en931TnD+cYzLQqA6sPUo6XmzZvLbrerf//+uv7669WwYUNHB+zS+vTpY+Y0AKoxb1oE0KIAgDumEpn77rvP8f9PP/20y31sNpu2bdtm5jQAqjHPC3e938fX+c3MDSD4TCUy77zzjr/iABCmvGkRQIsCAO7wZl8AQefcfiBe2zIyy1QRSapwH1oUANVHlbYoKCgo0A8//KCjR4+qQ4cOSkhIMDulX5HIANbhqf1A6USFFgVA9eZtImOqakk6/Xjpkksu0eDBg3XXXXdpx44dkqTMzEx17txZ8+fPN3sKAGHE1yqmkn2oQgLCi6lE5qOPPtITTzyhSy+9VI8//niZNgUJCQnq0qWLlixZ4vP8x48fV7du3ZSSkqItW7ZUfAAAyzNbxUQVEhBeTCUyb731lnr37q0pU6aoZ8+eTuOpqanatWuXz/O/8sorvKMGCDON3VQLla9icrePN8cDqD5MJTIZGRnq1q2b2/G4uDhlZ2f7NPdPP/2kOXPm6K677vIxOgBW1De9uWzltrmqYnK3jzfHA6g+TJVfx8bGKisry+347t27lZjo2+K6yZMna9CgQWrRooWv4QEIIZ76GZUfu6pLU6cqI0PSpFkbPO5TUmk0ekCaU4XTonV79M/PfqDXElDNmEpkunXrpnnz5mnw4MFOY7t27dKHH36o66+/vtLzLlu2TDt37tTUqVP1ww8/mAkRQAgoX2VU0s/IVZXRLwdytedArscqJVf7lNbhfz2XKjp3h+TECscBhDZTicy9996rG2+8Uf369VPPnj1ls9n0ySef6KOPPtLy5cuVmJioO++8s1JznjhxQk899ZTuu+8+xcTEmAmvjBo1TBdoAfDRkq+dK4YMN9tLj3Vq1aDC40v28eXcnVo1MDU3gOAzlcg0aNBACxYs0PPPP6+lS5fKMAwtXLhQderUUd++fTV27NhKv1Pm1VdfVb169Xy6k+NORIRN8fEs9AOCxVMlkbsXWe3//bjjz62n4yv6s13RsWbmBhB8phIZSapXr54ef/xxPf7448rMzJTdbldCQoIiIip/B2Tfvn2aOXOmpk+frtzc071P8vPzHf89fvy46tSp/F8sdruhnJz8Sh8HwD8a16+jn/fnOG0vqSRyN5aVdbzC40v28eXcWVnHTc0NIHBiY2tV3Zt9/WX9+vW65ZZb3I63bdtW8+bNq/S8vNkXCK7NO4+47Gc0ZkCaDMlpTJKS4s9Qdl6Bo8XA0q9/dbFPLWXnnfK4eDgupqYOZ50oc1zJudv/b42Mu9hoUwAET0BaFEybNq3SgdhsNo0ePdqrfXNycpw6ZW/btk1PPvmkHnvsMaWlpSk1NbXSMZDIAMHnqZ9R6bG4mGgdcpF4lK5SqhsT7TI5cdeiQDqd9BzLK6DXEmARAUlkzj///EoHYrPZnJKTyii5SzN//nylpaX5NAeJDGAdk2Zt0C8Hcp22tzgrVhOHX1jhPpJR4fEAQp+3iUyl1shs377d54AAwBtmWxQYbpYP06IAqJ6qtCY5Pz9f06ZN02+//eb1MZ07d9aOHTt8vhsDwFpoUQCgMqo8kZk+fbr27t1blacFYCG0KABQGabLrysrhIqkAISgDsmJTi0GzLYoYPEuUH1VeSIDABUp3WJAMteiAED1xnv7AYS8xev2OG0zJC1e57rFAYDwQSIDIOR5U8kEIDyRyAAIeVQiAXCHRAZAyKMSCYA7LPYFEPJcVTJd0CxOi9bt0T8/+8Gp1xKA8FGlTSPtdrsOHDigxMRERUdHV9VpaVEAVDPlq5ikP3otkcwA1UNAWhSYbRoZERGhxo0bV3oOACjNUxUTiQwQXqo0kQEAf6CKCUAJmkYCsJzG9eu47HBNFRMQfqhaAmA5rqqYJOn4yQKNmrJak2Zt0OadR6o8LgBVr0oX+wYLi32B6mfzziOOKqa4mGgdyjpRZpzFv4C1BWSxryvbt2/Xu+++qx9//FG5ubmy2+1lxm02m1asWGH2NABQRul+SpNmbXAaZ/EvEB5MPVpav369Bg4cqNWrVyspKUl79+5VkyZNlJSUpP3796t27dq66KKL/BUrALjE4l8gfJlKZF5++WU1adJEy5Yt0xNPPCFJGjlypN5//3198MEHOnTokK688kq/BAoA7tDCAAhfphKZH3/8UTfccINiYmIUGRkpSY5HS23bttVNN92kl156yXyUAOABLQyA8GVqjUxkZKTq1Dn9E09sbKxq1Kiho0ePOsabNGmin376yVyEAMLS6cW8e7Tv9+MuWxCUH7+qS1Nty8h2tDDol95M7VkfA1R7phKZpk2bas+ePZJOL+o955xztGLFCv3pT3+SJK1evVr169c3HSSA8FK+BcEvB3I1fcEWRxWSq/E9B3KpUgLCkKlHS927d9fixYtVVFQkSbrtttu0fPly9enTR3369NGqVat00003+SVQAOHDUwsCb8YBhA9Td2TuvPNO3XLLLY71Mdddd50iIiK0fPlyRUZGatSoURowYIBfAgUQPiqqQqJKCUAJU4lMVFSU4uPjy2zr37+/+vfvbyooAOGtohYEtCgAUMLUo6XevXtr5cqVbsf/9a9/qXfv3mZOASAMVVSFRJUSgBKmEpl9+/YpPz/f7Xh+fr72799v5hQAwlCH5ESNHpCmFmfFqmZUpFqcFasxA9IcVUgVjQMIH6ZbFNhsrlq3nbZlyxbFxsaaPQWAMFS6BYEv4wDCQ6WbRs6aNUvvvPOOJGn//v2Kj49XrVq1nPbLy8tTTk6O+vXrp2effdY/0fqIppEAAFhLwJpG1qtXT+edd56k04+WGjRooAYNGjjtV7t2baWmpmrw4MGVPQUAAIBXKn1HprRhw4bpzjvvVHp6uj9j8jvuyAAAYC3e3pExlchYBYkMYD2VbVFQfhyAtVVZIpOXl6c5c+Zo/fr1Onr0qP7xj3+oTZs2ys7O1scff6xevXqpWbPglkSSyADWUr4FgXS6vNpdi4Ly4wCsz9tExlT59cGDB3Xttdfq5Zdf1sGDB7Vjxw4dP346YYiLi9MHH3yg2bNnmzkFgDBEiwIA3jJVfv3MM8/o+PHj+uSTT5SQkKCuXbuWGb/sssu0evVqM6cAEIZoUQDAW6buyKxdu1bDhg3Tueee6/J9Mk2aNNGBAwfMnAJAGGrsptVA6RYFnsYBhA9TiczJkyeVkJDgdrzkMRMAVAYtCgB4y1Qi07JlS23YsMHt+IoVK9SqVSszpwAQhmhRAMBbptbIDB8+XOPGjVNKSoquuuoqSZJhGMrIyNC0adP03//+V1OnTvVLoADCCy0KAHjDdPn1q6++qmnTpskwDNntdkVERMgwDEVEROiee+7RHXfc4a9YfUb5NQAA1lKlL8Tbv3+/li9froyMDNntdjVt2lR9+vRRkyZNzE7tFyQyAABYS5W8R6ZEXl6eCgsLZRiGbDab7Ha7Tpw44Y+pAQAA3DJ1R6agoECPPPKIFi5c6HicJEl2u102m03XXHONJk+erOjoaL8F7AvuyAAAYC0B635d2rPPPqtPPvlEgwcP1tChQ9W0aVPZbDZlZGRo9uzZev/991W3bl397W9/M3MaAAAAl0zdkencubN69Oihp59+2uX4Aw88oH//+99av369zwH6A3dkAACwlipZI1NUVKS2bdu6HW/fvr2Ki4vNnAIAAMAtU4nMJZdcoq+++srt+Jo1a3TxxRd7Pd+XX36poUOHqkuXLmrdurV69+6tJ598Urm5uWbCBAAA1ZSpR0s///yz7r33XjVt2lRDhgxR06ZNJUkZGRl677339Ntvv+mFF15wamMQFxfncr6FCxdqx44datu2reLi4rRr1y5NnTpVqampmjlzpq9h8mgJAACLqZL3yJx//vl/TFSuaWTJtK6aSW7bts3rc8ybN08TJ07Uv//9bzVo0MCnOElkAACwliqpWho9erTLRMWfSu7eFBYWBvQ8AKxl884jWrxuj/b9flyN69dR3/TmtCwAwpBf3uzrb8XFxSoqKtLu3bv18MMPq1GjRnr11VdNzMcdGaA62bzziKYt2FJmm03S6AFpJDNANVEld2QCpWfPnjp06JAk6dJLL9WUKVNMz1mjhl9eYgwgBCz5OsNpm/G/7Z1a+fYIGoA1heQdme3bt+vEiRPavXu3Xn31VZ199tl66623FBkZ6dN8Ja0TAFQPN4xfpFMFzq92OCM6Uh8+2S8IEQEIlpC8I1OyiLh9+/ZKS0tT//799cUXX+jKK6/0aT673VBOTr4/QwQQRI3r19HP+3OctjeqX0dZWTxGBqqD2Nha1n20VFpKSoqioqL066+/mpqnqMjup4gABNvVXZpp+oItKn072Sapb5dm/FkHwkzILxz57rvvVFhYqLPPPjvYoQAIER2SEzV6QJpanBWrmlGRanFWrMYMSFN7FvoCYSek1siMGTNGrVu3VkpKis444wxt375db775phISEjR//nyfu2hTtQQAgLVYsmqpTZs2WrJkiWbMmCHDMNS4cWMNHDhQI0aM8DmJAQAA1VdI3ZEJFO7IAABgLVXS/RoAACCYSGQAAIBlkcgAAADLIpEBAACWRSIDAAAsi0QGAABYFokMAACwLBIZAABgWSQyAADAskhkAACAZZHIAAAAyyKRAQAAlkUiAwAALItEBgAAWBaJDAAAsCwSGQAAYFkkMgAAwLJI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oCTnW6kHDx7UPffco65duyotLU29evXSE088UeE55s+fr759+6pNmzbq3Lmzbr75Zn3//feOccMw9Oabb+qKK65Q69at1bt3b7399tuO8alTp2ratGnKz89XSkqKUlJSNGzYMMf4hg0bNGjQIMf848ePV3Z2dpkYZsyYocsvv1xpaWnq0qWLbr31Vu3du9cx/txzz+maa65R+/btdemll+qvf/2rDh8+XNmPE24E8jormXvZsmVOYwMGDNBf//rXMnOPHTtWnTt3Vps2bTRkyBBt3bq1zDG9evXSP/7xD73++uvq2bOn2rRpo+zs7ArjcvWIIicnR5MmTVK3bt3UunVr9erVS1OmTCmzzwcffOC49nv16qVXXnlFdrvd4+eZnZ2t8ePHO76PQYMGacOGDWX2KflcP/74Y11xxRVKS0vT9u3bPc4b7kLhOi3/SMdTTLm5uRo7dqzat2+v9PR0Pf/885o5c6ZSUlIcc7t6tJSSkqLXX39dU6dOVdeuXR1/b+bn5zv2cfVoqaCgQC+88IJ69+6t1q1bq1u3bho3bpxj/Ntvv9WoUaN0ySWXqF27durfv78++eQTrz77UMYdGYt4/vnn1b17d02ZMsXtX6IPPvigDh8+rAkTJqhevXo6cOCA0z8C5W3YsEF/+9vfdPvtt6t79+46efKkvv/+e+Xm5jr2efzxx/Xhhx9q1KhRatu2rTZv3qznnntONWvW1M0336yBAwfq4MGDWrRokWbNmiXp9E8ZkrR161bddttt6ty5s1566SX9/vvvmjJlinbv3q0PPvhAkZGR+uSTT/TSSy/p7rvvVrt27ZSbm6tNmzbp+PHjjhiOHj2qkSNHKikpSZmZmXrrrbc0bNgwLV68WDVqcBn7SyCus7PPPlvt2rXTkiVLdOWVVzq279mzRz/88IPGjBkjSTp27JgGDx6s2rVra+LEiTrzzDM1e/ZsDR8+XMuXL1e9evUcxy5fvlzNmjXT3/72N0VERKh27dq69957KxVXQUGBhg8frn379mn06NFKTk7WwYMHtWnTJsc+s2fP1uTJkzVs2DD16NFD3377raZNm6bc3Fw99NBDLuctLi7W//3f/2nv3r0aO3as6tevr9mzZ+u2227TBx98oNatWzv23bp1q/bt26d77rlHsbGxOuuss9zGiz8E8zqtTEzjx4/X119/rQceeECNGzfW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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.scatterplot(x ='sepal_length', y = 'sepal_width', hue ='species', data = iris)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 478
        },
        "id": "1pomZhJ_oJt2",
        "outputId": "f08a4921-6faf-4717-e707-3b30f575ad49"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='sepal_length', ylabel='sepal_width'>"
            ]
          },
          "metadata": {},
          "execution_count": 15
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkMAAAG8CAYAAADdFaHKAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAACvsElEQVR4nOzdd5xcVfn48c+5Zdr2zab33nsgFUIJvYN06YqoAUH9qj8VFb8oqCDyBaQXqdKUGnqHhJBCCiE9pPdk+9Rbfn8su8lkZraX2Z3n/XpF3Htm7j1n5s6dZ8495zzKdV0XIYQQQogMpbV1BYQQQggh2pIEQ0IIIYTIaBIMCSGEECKjSTAkhBBCiIwmwZAQQgghMpoEQ0IIIYTIaBIMCSGEECKjSTAkhBBCiIwmwZAQQgghMprR1hWoTWVlJSeddBK7du3ihRdeYPTo0Skfe8wxx7Bt27aE7cuWLcPr9bZkNYUQQgjRjqV1MPTPf/4T27br/fgTTjiBK6+8Mm6bx+Np7moJIYQQogNJ22Bo/fr1PP300/zyl7/k97//fb2eU1RUxLhx45qtDq7r4jjtN3Wbpql2Xf/GytR2g7Q9E9ueqe0GaXsmtr0+7dY0hVKqQftN22Do5ptv5oILLqB///5tVgfHcdm/v7LNjt8UhqFRUJBFWVkQy3LaujqtJlPbDdL2TGx7prYbpO2Z2Pb6truwMAtd7wDB0JtvvsmaNWu46667WLFiRb2f9+qrr/Lcc89hmiaTJk3i5z//OUOHDm1SXQyjfY4x13Ut7r+ZIlPbDdL2g/+bKTK13SBtP/i/maIl2512wVAoFOLWW2/lhhtuIDs7u97PO+aYYxgzZgw9evRgy5Yt3HfffVx00UW89NJL9O7du1F10TRFQUFWo56bLnJz/W1dhTaRqe0GaXsmytR2g7Q9E7VEu9MuGLr33nvp1KkT55xzToOe99vf/rbm/0+aNInp06dz0kkn8fDDD/OHP/yhUXVxHJeysmCjntvWdF0jN9dPWVkI286cbtRMbTdI2zOx7ZnabpC2Z2Lb69vu3Fx/g3uP0ioY2rZtG4888gj33HMP5eXlAASDwZr/VlZWkpVVv56aLl26MHHixAbdZkumvd+PtW2n3behMTK13SBtz8S2Z2q7QdqeiW1viXanVTC0detWYrEYV199dULZpZdeytixY3nuuefaoGZCCCGE6KjSKhgaPnw4jz/+eNy2lStXcsstt3DTTTfVuujioXbt2sWiRYs444wzmruaQgghhOhA0ioYys3NZfLkyUnLRo4cyciRIwG47LLL2L59O++88w4Ar732Gh988AEzZ86kS5cubNmyhQceeABd17niiitarf5CCCGEaH/SKhiqL8dx4lam7tWrF7t37+bPf/4z5eXl5OTkMGXKFK677rpGzyQTQgghRGZI+2Bo8uTJrF69Om7bE088Eff3uHHjErYJIYQQQtRHZq3YJIQQQghxiLTvGRJCpA/T1FGqasmJTMyLJITomCQYEkLUyVWK8rDFJ/M3UxmKMWVUd3oWZWEoF1diIiFEOyfBkBCiVo5SfPDlNp56c1XNtjc/38SgXnn88pJJ6Eg0JIRo32TMkBCiVhVhKy4QqrZuaynvLdyC3k6TGQshRDW5igkhUjJNnQ8XbU1ZPmfuRiIZmA5ACNGxSDAkhEhJKUVZMJqyPBi2WrE2QgjRMiQYEkKkZFk200Z3T1k+YWhnDE21Yo2EEKL5STAkhEjJcVz6ds2hb7echDLT0PjuicNQMp1MCNHOSTAkhKiVoVx+e8XhnDVzIAGfgaYpJg7rwm3XHkGuz5Cp9UKIdk+m1gshauW6oONy5oz+nDS1HwC6BprrysKLQogOQYIhIUS92LZz4ILhIKsLCSE6DLlNJoQQQoiMJsGQEEIIITKaBENCCCGEyGgSDAkhhBAio0kwJIQQQoiMJsGQEEIIITKaBENCCCGEyGgSDAkhhBAio0kwJIQQQoiMJsGQEEIIITKaBENCCCGEyGgSDAkhhBAio0kwJIQQQoiMJsGQEEIIITKaBENCCCGEyGgSDAkhhBAio0kwJIQQQoiMJsGQEB2EYVR9nJVq44oIIUQ7Y7R1BYQQTeMoRVkwxiefbyYcsZg2pjvdCgLouG1dNSGEaBckGBKiHXOUYs68jfznw/U1296Yt5GRAzpxw/nj0FwJiIQQoi5ym0yIdkop2F8eiQuEqq3YsI/PV+ysuXUmhBAiNblSCtFOGabOW/M3pyx/9dNvCFvSMySEEHWRYEiIdsp1oSIYTVkeili4cptMCCHqJMGQEO2U67hMH9MjZfmEYV3wGDK1TAgh6iLBkBDtlG07DOtbQPeirIQyr0fn3GMG49rSMySEEHWRYEiIdsxUcNP3p3DajP74vQa6ppgyqhu3XXsEAVM+3kIIUR8ytV6Idsx1XQzgnJkDOf2IAeiGju66OLaN60ivkBBC1If8dBSiA3BsB6+u6JzvR+Ei46aFEKL+JBgSQgghREaTYEgIIYQQGU2CISGEEEJkNBlALUQD6bqGriscx8WynLaujhBCiCaSYEiIetJ0Rdhy+Wr1HtZsLqZfjzzGD+mMz1Ayc0sIIdoxCYaEqAdNUxRXxvjtfXOpDFs1272mzk1XT6Fbng9HAiIhhGiXZMyQEPUQc+FvTy6KC4QAIjGbWx9fSFQCISGEaLckGBKiHirDFtv3ViYtKymPUBaMtXKNhBBCNBcJhoSoB8uufaB0NGa3Uk2EEEI0NwmGhKiHHL+Jz6MnLdM1RWGOr5VrJIQQorlIMCREPXgNxSUnDU9advbRg/AYqpVrJIQQornIbDIh6sGxXaaM6EpRvp8n31zF1t3ldC0McMFxQxnVvxBkALUQQrRbEgwJUU/KdRnWK4/fXXE4VaGPi1fXsOsYTySEECK9STAkRAPYtoN+yN9CCCHaNxkzJIQQQoiMJsGQEEIIITKaBENCCCGEyGhpHQxVVlZy5JFHMnToUJYvX17rY13X5YEHHuCoo45izJgxnH/++SxZsqR1KiqESErTFB6PjmEkX6NJCCHSQVoHQ//85z+x7fqt7Pvggw/yf//3f1x++eXcf//9dO7cmSuvvJItW7a0cC2FEIfSNIWFYuWWUh5/czVvL9xCyHJBk/WYhBDpJ22DofXr1/P0009z7bXX1vnYSCTC/fffz5VXXsnll1/O1KlT+fvf/05+fj4PP/xwK9RWCFFNKQjbLr+5fy5/eWIhb3+xmSffXMW1t3/Aqi0lEhAJIdJO2gZDN998MxdccAH9+/ev87GLFy+moqKCk046qWabx+PhuOOO4+OPP27JagohDuEqjcde/5o9xaG47Y4Ltz+1mKgtC1QKIdJLWq4z9Oabb7JmzRruuusuVqxYUefjN2zYAMCAAQPitg8cOJB//etfhMNhfL7G5Y4yjLSNF2ul61rcfzNFprYb0qftwZjDFyt2Ji2zHZe1W0oYP6gTTjOu2p0ubW9tmdpukLYf/N9M0ZLtTrtgKBQKceutt3LDDTeQnZ1dr+eUlZXh8Xjwer1x23Nzc3Fdl9LS0kYFQ5qmKCjIavDz0klurr+tq9AmMrXd0PZtr9xdUWt2kmDEIi8v0CLHbuu2t5VMbTdI2zNRS7Q77YKhe++9l06dOnHOOee0dVVwHJeysmBbV6NRdF0jN9dPWVkoo1ZJztR2Q/q03dSgR1EW2/dWJi0f0juf4uLkZY2VLm1vbZnabpC2Z2Lb69vu3Fx/g3uP0ioY2rZtG4888gj33HMP5eXlAASDwZr/VlZWkpWV2FOTm5tLNBolEonE9Q6VlZWhlCIvL6/RdbKs9n2i2bbT7tvQGJnabmj7tpu6xtVnjuamhz/HPaSHaPLIbuT4zRarX1u3va1kartB2p6JbW+JdqdVMLR161ZisRhXX311Qtmll17K2LFjee655xLKqscKffPNNwwbNqxm+4YNG+jRo0ejxwsJIRrOth36dMnizz+czr9e+5rVW4rJy/Zy5pEDmTG2B5qTeRdvIUR6S6tgaPjw4Tz++ONx21auXMktt9zCTTfdxOjRo5M+b8KECWRnZ/PGG2/UBEOxWIy3336bI488ssXrLYQ4hOPSPd/H/1w8gerJY15DYWfgr1ghRPpLq2AoNzeXyZMnJy0bOXIkI0eOBOCyyy5j+/btvPPOOwB4vV5+8IMfcNddd1FYWMiQIUN45plnKCkp4aqrrmq1+gshDnAcF8WBi4xtyZR6IUR6SqtgqL4cx0lYmfr73/8+ruvyyCOPsH//foYPH87DDz9M796926iWQgghhGgPlOseOsRRVLNth/37m3fWS2sxDI2CgiyKiyszaoBdprYbpO2Z2PZMbTdI2zOx7fVtd2FhVoNnk2XWik1CCCGEEIdol7fJhOjoTFPHNHVs2yESsdq6OkII0aFJMCREGjFNncqozeJVu1m5sZienbOZMqobAVPDyaDF1YQQojVJMCREmtB1jeLKGL+9fy5lldGa7U+/tYobrzycfl2zZWq6EEK0ABkzJESaiDoudz77ZVwgBGDZDn99YiEhCYSEEKJFSDAkRJoIRmzWbytNWlYZtthTHGrlGgkhRGaQYEiINGFZdq3lwbCFJp9YIYRodnJpFSJNZPlNcgJm0jKloFeXbCStlxBCND8JhoRIE1lejctOGZG07PjJffGbeivXSAghMoMEQ0KkiVjUYdzgIn5zxeH0656LUtC5wM8PzhrNuccMRrqFhBCiZcjUeiHSiOa4DO2Zy28uO4zq0Cfbq8vCi0II0YIkGBIizViWgw5U3xSTQEgIIVqW3CYTQgghREaTYEgIIYQQGU2CISGEEEJkNBkzJDKaroPf70UpCAYj2LWve5jxTFNHqapxTY7jtnV1hBAtQNMUhqHhOHUvBtvUY7guxGJtf+GVYEhkLEspdhWH+fiDDQAcMbYnnfN96K58yR/KVYrysMUn8zdTGYoxZVR3ehZlYSgXebmE6Bg0TREzwqwp3sjy3avoklXE4T3H4nUCYDfPjSSlFJYZZn3pFpbsXEGnQAGTe47H7wbAbru11CQYEhnJVorH56zk06Xba7a9MXcjU0Z248rTR2LIN3wNRyk++HIbT725qmbbm59vYlCvPH55ySR05LUSor1TCsJGJf/70T/YHyqp2f7silf46ZTvMzB7IK6tmnycmBnkz5/cxa7KvTXbXljxOj8+/DKG5w8Dq21G78iYIZFxPB6dDdvL4gKhap+v2MmazSV4PLLac7WKsBUXCFVbt7WU9xZuQTfkMiJEe+caNv9a8nxcIATgui53zn+EqB5u8jGU6fLcitfiAiEAF5d7FvyLqGr6MRpLrmIi48QceH3uNynL58z9hoglvR1QNUbow0VbU5bPmbuRiCUrYwvR3kWJsHTn10nLLMdiY8kWNK1pPUNRwny+dVHSMtd1Wbl3LbouPUNCtIqY7RAKp17IMBi2sCX1BVB1f78sGE1ZHqzldRRCtB+WY+HWcss7GAuhmniXzHYdbDf1tbUyGmzyMRpLgiGRcbK9BhOHdUlZPnFYFwJeGU4HVTNJpo3unrJ8wtDOGE38tSiEaHtezUeXrKKU5QML+2HbTesx9ygPvfN6pCwf0XkIVhv1NEswJDJOOBzjqIm9yc/xJpTlZnk47vA+RCUFBgCO49K3aw59u+UklJmGxndPHIaSweZCtHsex8cV489LWjal53iytKwmH8OwPVwx7jwUiT+gxnQdTp6Z2+RjNJYEQyIjZXs0bvnRdI6e0AvT0DANjSPH9+TWH88gxyeDpw9mKJffXnE4Z80cSMBnoGmKicO6cNu1R5DrM2RqvRAdgG079An05vdH3cDAwr4oFAW+PC4Zcw7fHfMdVKzpveWO49LV240/HvNzhhUNRKHI9eZwwagzuHrCxaiY2QwtaRzlunIpS8W2Hfbvr2zrajSKYWgUFGRRXFzZZt2ObaGh7TY8BqFo1YJfXlPDSYPFvxqrpd9zXdeIfNtNrmuguemzxpCc75nVbpC2t1TbNU1h61Ec5YALHteH3cwTSqqOEcNRNrjgdX1Y9ThGfdtdWJjV4IHYMjBCZDQralH9W6Q9B0KtwbadAxeMquukEKKDcRwX5ZhU94/bLfBJrzqGgf7tFcVKg6uJ3CYTQgghREaTYEgIIYQQGU2CISGEEEJkNBkzJDKaUmAYVZnYYzG7xQYEV2d7r+8xdF1D1xWO42bc4FAhhGhtEgyJjOUoxf7yCB8v2QbAEWN70CnXh9aMEZGjFCWVUT5dspGo5TBjbA865/vRUxxD1zXClsOy9Xv5esN+enfNYdLwrvgMheu0/SBDIYToiCQYEhnJUYon3lrNR4sP5N167dNvmDamO1eeMqJZAiJHKV74YB1vfr6pZtucuRuZMLQLPzp7dMIxNE1RFrb4zX1zKas8kALjX3NW8vvvTaZ3pwCOBERCCNHsZMyQyDiapti4szwuEKo2d9kO1m0rbXJCQqUUO/cH4wKhaotX72bZ+n0J62BYLvzj31/GBUIAlu1w678WEJFASAghWoQEQyLjuChe+XRDyvJXPtlAE1PwoOkar3+2sdZjRA85SChqs35badLHV4Yt9paEm1YpIYQQSUkwJDKO7bp1Zq13mnibzHEcKsOxlOWhSGKGaMuufaB0OGq1WUZnIYToyCQYEhnH1BSTR3VLWT55VDc8DVzK/VC6ppg2JnW298NGdE04RsBrkBNInptHKejeKStt0l8IIURHIsGQyDi27XDE2J4ps9YfPaEXdh29NHWxLIcJQ7rQOd+fUJblMzhlWn+cQ47hMxRXnjYy6f5OntYPnyEfVyGEaAlydRUZyavBrT+azrGTetdkrT9qYi/+8uMZ+I3muRfl0eDma6Zx4tS+eE0dQ1fMGNuDv157RNJj2LbLmAGd+N1Vk+nXPReloHOBnx9/ZwxnzRyIdAsJIUTLkKz1tZCs9e1PQ9ut6VrNQGZTB7epI6eTHkMR/TYHrKkr3Dp6nTRNYTngAArwGqpebcnU9xwyt+2Z2m6Qtmdi2yVrvRAtxDkoE7vbQknrHds96Bh1B1uO46JxoNvWsuT3ihBCtCS5TSaEEEKIjCbBkBBCCCEymgRDQgghhMhoEgwJoGpgmsejN3jQWbqprn97b4cQom0pBaap4/HosthpBpAB1BlOaYpQzGHBV9vZtruCkQM7MaxvIT69aqp3e6FpirDtsmD5TtZtLWFw73zGDCrCZyicdtQOIUTbc80YxbFS5m5YiO3YTO09kU7eTmix5IuiivZPgqEMpjTFpt2V3PzofKxvA4a3v9hMfraXm6+ZSpap0x5WXtA0xZ7yCDfeP4/wt3PY3/liM36vwc0/mEpRjqddBXZCiLbjmjFeXP0aH2ycV7PtrfUfMbH7GK4Yez4qKgFRRyT3EjJY1Hb5yxMLawKhaiUVEe5+fintZfWKqAO3Pr6wJhCqFopY/PXJRUQkEBJC1IOmKbYHd8YFQtUW7VjGqv1r5RZ8ByXvaoZSCnbuDxKKJE9YumpTMaFYCy2808wqQjH2lSbP6L5rf5DKWpKyCiFEDd3hzXUfpiyes/Z9Ylq09eojWo0EQxlL1Zq5HUjoMUpXsTpWYG0v7RBCtC0Hh2AslLI8FAvjuu2lz1w0hARDGcp1XXp3zUlZnp/jJeDVW7FGjZeX7cFI0XXtNfWUmeCFEOJgumNyeM9xKcsn9hiDRyUmeBbtnwRDGcxnahw/uW/SsqtOG4m3ndwb9+qK82cNTlp24fFD8Eq2dyFEPdi2w6TuYyjw5yWUZXkCzBpwBHZMepo7IplNlsGU63LesYMY0DOXF99fx97SEP175HHZycPpVZSFXUdC0XThOi7HTOhFt05ZPP32anbuq6Rn52wuOn4oQ3vn15kYVQghqpmWnz/M/Ckvr36bTzd/geO6TO45nnNGnIzXCuAgwVBHJFnra5EpWet1XauZcaUpMFRVstD2Rtc1Yq6Lpms4toOpVLsJ6JpDpmayhsxte6a2G1q+7ZrpElNVg6VN14MTS5+VFzP1fZes9aJF2QdlbseFdhgHAVXt8BgaBfmBjLtICCGalxNT6FSND5IrSccngymEEEIIkdEkGBJCCCFERpNgSAghhBAZLa3GDH300Uc8+OCDrFu3joqKCrp27cqsWbOYPXs2OTmp18S55JJL+OKLLxK2z5kzh4EDB7ZklUWaMU295r/1GTOkaeD1migF4XAMpx6DA3RdQ9cVjuOm1bgk49slBCTDthBCNExaBUMlJSWMGTOGSy65hPz8fNauXctdd93F2rVreeSRR2p97oQJE/jlL38Zt61Xr14tWV2RRgxDozLqMHfxNr7ZVsqAXnlMGNqFLI+GFUsesNhKsaskzMdLNgBwxLiedM7zoaeYYKnpirDl8tXqPazZXEy/HnmMH9IZn6Fw23DUuaMUZcEYn3y+mXDEYtqY7nQrCKDLFGAhhKiXRgdDruvy7LPP8sILL7BlyxbKysoSHqOU4uuvv673Ps8444y4vydPnozH4+HGG29k165ddO3aNeVzc3NzGTduXL2PJToOw9DYURLm9w8cyFr/3sIt+L0Gf7x6Kt3yvcQOCYhspfjXnJV8unR7zbY35m5kyshuXHX6yISASNMUxZUxfnvf3LhcZ15T56arp9Atz9cmyxE4SjFn3kb+8+H6mm1vzNvIyAGduOH8cWiycoYQQtSp0cHQX//6Vx577DGGDx/O6aefTl5e4oqdzSE/Px+AWCzWIvsX7V/IcvnrE8mz1t/21CL+ePUUDk7IYRgaa7eUxgVC1T5fsZMjxvVkdP+CuFtgMRf+9uSihKSvkZjNrY8v5K8/nt7q3axKwf7ySFwgVG3Fhn18vmInR47pnla38oQQIh01+vr90ksvcfzxx3PnnXc2Z30AsG0by7JYt24d99xzD8ccc0ydt7y++OILxo0bh23bjB07lp/85CccdthhTa6L0U5TOVQvONXQhafao/1lkdqz1ocsinI8NdscpXh97jcp9/f63G8Y3r8g7r0vr4yxfW/yBThLyiOUB2N0zm3dnEWGofH2u+tSlr/66TdMHtktI9KRZNL5frBMbTdI2w/+b6ZoyXY3OhgKh8NMmzatOetS4+ijj2bXrl0AHHHEEdx+++21Pv6www7jjDPOoF+/fuzevZuHH36YK664gieeeILx48c3uh6apigoyGr089NBbq6/ravQ4rbtT51lGiBmO3Hv477SEKFDengOFgxbgKKgIHDgORUldRzDbfVzxbIdyoPRlOWhiIVp6hTkdfxzoFomnO/JZGq7QdqeiVqi3Y0OhqZOncry5cs5//zzm7M+ADzwwAOEQiHWrVvHvffeyzXXXMOjjz6KrifPon7dddfF/X3UUUdx6qmn8s9//pMHH3yw0fVwHJeysmCjn9+WdF0jN9dPWVmow6ekyM/xYugaVpJ2ek2d3CwPxcUHenU8hs7EYV1Yu6Uk6f4mDuuCx1Bxz8nyGfg8esKtOABdU+Rnxx+jNWiaYsbYHsxfsTNp+YRhXVCu2+r1aguZdL4fLFPbDdL2TGx7fdudm+tvvXQcv//97/ne977Hfffdx/nnn09BQUFjd5Vg2LBhAIwfP57Ro0dzxhln8M4773DiiSfW6/mBQICZM2fy1ltvNbku7X28hW077b4NdfGbGuccPYhn312TUHbusYPxe3Ss2IEgxrIcjprYmzc/30RJeSTu8blZHo47vA/RQ3qOPLrikpOG8+DLXyUc4+yjB+HRVZu8zkP7FNC9KIsdh9zC83p0zj1mMHYsMXjryDLhfE8mU9sN0vZMbHtLtLvewdD48eNRhyxgYts2d955J3feeSderxdNi4/ElFIsWrSoSRUcOnQopmmyefPmJu1HdFyO5XDc4X3oXpTFs++uqclaf96sIYzoV4iTJCAIGIpbfjSd595Zw6fLqgZSTx3dnQuOG0qWR0uYfebYLlNGdKUo38+Tb65i6+5yuhYGuOC4oYzqX9hmCd1MBTd9fwqvfrKBdxdsIRqzOWxEVy4+YRgBU2vTKf9CCNFe1DsYOuGEExKCodawdOlSYrFYg9YMCgaDfPjhh4wePboFaybSieY4TBpSxIj+hTXbAqZGNMltLajqHfIquPyU4Vxw/FAAvIbCsZyEQKiacl2G9crjd1cc/u0KPi5eXWvTbmrXdTGAc2YO5PQjBqAbOrrr4ti2BEJCCFFP9Q6Gbr311pasBwCzZ89m1KhRDB06FJ/Px6pVq3j44YcZOnQos2bNAuDXv/41L730Us36RQsXLuShhx7iuOOOo2fPnuzevZtHH32UPXv2tMhMN5G+olEbn6FRUJBFcXFlykDoYHbMrpl271h1Bw+27aAf8nc6cGwHr6FRkO+nuLgSWV5ICCHqr9Fjhu6++26OP/54hgwZkrR87dq1vPXWW8yePbve+xwzZgxz5szhgQcewHVdevbsybnnnstVV12Fx1M1NdpxHGz7wJdc586dicVi3HHHHZSUlOD3+xk/fjw33XQTY8aMaWzzhBBCCJEhlOs27jfksGHD+Nvf/sZpp52WtHzOnDn87Gc/Y+XKlU2qYFuybYf9+9vnTBzjoB6STBpgl6ntBml7JrY9U9sN0vZMbHt9211YmNXg2WQttmJTSUkJpmnW/UAhhBBCiDbUoNtkCxYsYP78+TV/v/POO2zatCnhceXl5cyZMyflLTSRfgxDQ9MUtu222DgYr9dA1zUsy67XeJ7GaGjWeqXAMHSUgljMrtdYm9bIWm+aOqapY9sOkUjqBSJF1XpL1e97Sx7DMDRct+o8qQ/D0NG0qsH6bZG3TghRfw0KhubPn8/dd98NVE2bf/vtt3n77beTPnbQoEHceOONTa+haFFKU4RiDgu+2s623RWMHNiJYX0L8elg281zAde/zSj/8cKtbNldwZA++YwdXETA0JotmGhM1npHKfaXR/h4yTYAjhjbg065vpTJTVsja71p6lRGbRav2s3KjcX07JzNlFHdCJgaTpoM1k4XSimyVBBrz0aC6xcRzelEYNhUInoOUad5giOlwDajbC7fwcLtS8j15TC11yQCKgtlpTiG4RAmyILtS9hduY8xXYczIL8vptU2yXyFEHVr0JihcDhMKBTCdV2mTZvGTTfdxPHHHx+/Q6Xw+/14va2bp6kldPQxQ0pTbNpdyc2Pzsc6KPDJz/Zy8zVTyTJ1GjmkLK4em/cGuemhz4kdVI9sv8nN10yjMMtsckCULGs9UGvWekcpnnhrNR8t3hq3fdqY7lx5yoiEgEjTFMXBls1ar+sapSGL394/l7LKA2k2DF3jxisPp1/XbOxaXqtMG0eQo1Wy+9mbsYp3xG3vdMqPofeEZgmIHG+Ev829l82l8Ul9Lx93Lod1mQCHBETKcFlTvpY7P3847rPTKVDAjUdejyfmb9aZfpn2nh9M2p55bU+bMUM+n4+CggIKCwt57733OP300ykoKIj7l5+f3yECoUwQtV3+8sTCuEAIoKQiwt3PL6U5PmLBWFVG+dghJ25FKMYdzywmXI/p7HWpK2t98JBASNMUG3eWJwRCAHOX7WDdtlI0LX5Nrbqy1keb4Rd/1HG589kv4wIhqMpB9tcnFhLKoIteXbyGQ+lnzycEQgD7Xv8nXqfpP2I0A95Y90FCIATw2JLnCZJ4jKgW5q75jyb8iNgXLObJZS+CIe+hEOmo0QOoe/bsid+fmUniOgKlYOf+IKEU41FWbSom1AypHIrLwwlf7tU27Swn2AzjYcqD0Tqz1h/MRfHKpxtS7u+VTzZw6B3CyrBVa9b6smCsYZVOIhixWb+tNGlZZdhiT3HtCWkziWmHqFzxaYpSl/DGZU3ObB3TIrz3zWcpyxdsW4phHOgZ0jTFhuJN2E7yz82iHcuJkPw8FUK0rXqPGTrmmGMavAK1Uop33323wZUSrUHVmrkdqOoxavRKVFVSBVvVYpYD3qbdzojW0WNyaK+U7bp1Zq13XDduccVkSWDj6hCzgabNnrSs2oPPYNhC08CRzgVwHXBSv4d2uAKtiQvmu7hErEjK8opoJQdfEpVSVEZTJ3Z2XTdloCSEaFv1/qo7/PDDE4Khr776irVr1zJo0CD69+8PwDfffMO6desYPHgwo0aNat7aimbjui69u+akLM/P8RJoYpAC0K1TFppKnrory2eQE2j68gsFdWWtz/bEbTM1xeRR3VJmrZ88qhueQ9Js5PjNWrPWF+b4mtYIIMtvkhMwKU/Sy6QU9OqSLYHQt2zNi6dbf6I7v0la7u83hmATB5wbrsGIzoP5es/apOUTu4+OG7dg2w6DO/VPub9u2Z3xaF6QeEiItFPvfuRbb72VW265pebfsccey86dO3n00Ud57bXXuOuuu7jrrrt47bXXePjhh9m5cyfHHntsS9ZdNJHP1Dh+ct+kZVedNhJvE28zAHgNjVOmJ/+CuPjEYQQ8TQ+4qrPWJ1Odtf5gtu1wxNie5Ockjm3LzfJw9IReCcsLeI2qrPXJnH30IDxG0/P2ZXk1LjtlRNKy4yf3xd/C08fbkwheCmZdCSrxHPX1HYUb6NTkgcrKMvnumHPQkxxjUGE/ugQ6J4wNytZzmNRjbNL9XTHufDxO04NmIUTza/QK1KeddhqzZs3iJz/5SdLyf/zjH7z33nu8+uqrTapgW+ros8kAHE2xcNVuXnx/HXtLQ/TvkcdlJw+nV1EWqpmmvTiaxuLVu3nxg3XsLg7Su2sOF50wjEE98tDc5unqcDSNrzbsS5q1XkvSnaJpirDt8vx7a2um1k8f24Pzjx1CwFRJlxVwlWLd9rKkWetTTcdveDsU3+wo56k3V7FpZxlF+X7OPmoQhw3vmrQdB8u0GSamZuMJ7qbkwycIb16JFsghd9LJ+EceRYXdPEGH0l1K3RKeWf4Sy3evImD6OX7gkRzTbwZ61JM04HK9MT7ftojX1rxLabicQYX9uHjMWXT2dAGrede5zbT3/GDS9sxre0vOJmt0MDRmzBh+9rOfcdlllyUtf+yxx7jjjjtYunRpY3afFjIhGIKqKd2Rb7/8NQWGotnXQ/F6DSoiVfcHFOA3Vcrs8I3l8ehxM8dqy1pfTdM1ot+23dTBrWNtJf3bx7dk1nrD0IhYbs1svmyvXq+FFzPxAqmUwqeiGCqGYRoEXR+RSPO2XSmFa1hYykK54HF92HXMgtQNRVSFQYHm6ui22SJrDGXie15N2p55bU+bqfUH69OnD//5z3+orEwMFioqKnjxxRfp3bt3Y3cvWpFtOxi4GLhortsiF+1IxMLExfz2OM0dCMG3Wet1RfeibHy6qtcq185Bba8rEILqrPXut89pmaz1llV1jOrXS1agTs11XUKOSUhlY+R0wm6B8Tiu60JMx4h60WPeOgMhANty0WNe9KgXFTNksUUh0lyj5wpdf/31XHfddZx00kmcddZZ9O1bNfZk06ZN/Pe//2Xfvn3ceeedzVZRIYQQQoiW0OhgaNasWTzwwAPcdttt3H///XFlw4cP509/+hNHHHFEkysohBBCCNGSmrSKzIwZM5gxYwZ79uxh+/aqVVp79OhB586dm6VyQgghhBAtrYlL6lXp3LmzBEAiLVQPmtP1+iWBbUzWeiHqw+s10XVFNGq160GuXq+BrmvEYjaxZliVXoh0VO9g6KWXXgLgjDPOQClV83ddzjzzzEZUS4iGqZ4qv2D5TtZtLWFw73zGDCrCZyicFAOjG5q1Xoj6MEyboFvJJ5sWszu4n7FdhjGwsB+mk92ugiLNAyEq+GzrMraX72JIUX9GdB5CwMmRoEh0OPWeWj9s2DCUUixduhSPx8OwYcPq3rlSrFy5ssmVbCuZMrW+vdM0xZ7yCDfen5i1/uYfTKUox5OwblBDs9a3B5n0nh8qXdpumA6rilfzjwWPJWSt//2R12FaWc26inhLtVs3YEt4C3/59F6sg9Ke5HiyuPGon5BHYZufY+nynreFTG17S06tr3fP0HvvvQeAx+OJ+1uIthZ14NbHk2et/+uTi/jfq6fEneiaptiwI3XW+iPH9WRYrzyZDi0aLKJC/N/Cx5NmrX986Yt8f+xFONFmGZ3QosJ6kH/MezguEAIoj1byzy8e5+dTf4CyEldwF6K9qvensmfPnrX+LURbqQjFas9aH7bI8x041euTtX7wBeNpeoINkUkMQ2PNvg2ps9bvXMGlY8LoZLdyzRpub7CYyljypLMbS7YStENkIcGQ6Dgavejiv//9b9avX9+cdRGiUQ7NSn8o65BbZPXNWi9EQyilqKgja73VDrLWaxqEreQ/LqrFHFkIVHQsje6v/cMf/oBSiry8PCZOnMikSZOYOHEio0aNQtOaN/+OELXJy/bUmrU+J2DGbWtM1noh6hKL2QwpGpiyvFt2Z3y6BzfN4yHHge45XVAoqhPPHCzbk0W2mQWRNqicEC2k0cHQZ599xoIFC1i0aBGLFi3ib3/7G67r4vf7GTduXE2ANHny5OasrxAJvLri/FmDeeqt1QllFx4/BK+h4R4U2FRnrX/t028oKY+/oqfKWi9EfeSZOUzqPoqFO75KKLty7DmYZBMlzaMhwKf8zBo4g3fWf5JQduHoM/C7AWJJAiUh2qtGJ2o9VEVFBV9++SULFy7krbfeYtOmTSil+Prrr5tj921CZpO1H65SfL2pmKffXl2Ttf6i44cytHc+Kskp3pis9eku097zg6VT2zVvhM82f8Fr6z+qylpf0JfvjjmDbr4uWDGz7h00QEu22/VFWbxzOa+ueoe9wWJ65/XgvFGn0i+nDyravO1ojHR6z1tbprY9LbPWH2zz5s0sXLiw5t/mzZvx+/2MHz+eRx55pKm7bzMSDLUvuq4Rc100XcOxHUyl6uzhaWjW+nSWie95tXRru8erEXUrARcdHeX4W6ReLd1ur9egkgqqph1oeO2WaUdjpNt73poyte1pMbX+UE8++WRN8LN3796asUMXXnghEydOZOTIkei63tjdC9Fgtu3gMTQK8gP1vkhUZa2vku5jOUT7EY04gB/g25ti7fMLKxKxMPDV/G2103YIUZdGB0M333wzuq5z/PHHc9VVVzFq1KjmrJcQQgghRKtodDB08cUXs2jRIt566y3effddRo0axaRJk5g0aRITJkwgJyenOesphBBCCNEiGh0M3XjjjUDVwOnqGWULFy7ksccew7ZtBg8ezKRJk2oeJ4QQQgiRjpq8Lnx2djYzZ85k5syZbNmyhblz5/LYY4+xevVq1qxZI8FQMzAMHU2rGhPTUrOcDEND06pmUdVnWrmmKXw+A9eFUCjWInVqjIZmrRfpxzR1lALLcjIqJYqua3i9eoM+U9Xnu6alz3rpSlW9h65LvRO6NvT6o1TVdbElVR9Dqap2yDqsHVuTgqF169axcOHCmvWGdu3aBUCXLl045ZRTmDhxYrNUMmNpilDMYf7SLezcF2Ts4M4M7p2PR6PZviTUt8dY8NV2tu2uYOTATgzrW4hPJ2XgZSnFzr1BPlu6HdPUmDm+F/nZJnobXiwak7VepBePZuGJlRH86jPsYCn+wYehd+pD0PV36C8iTQPXCLGlfCfz1y0ly/Axve/h5OjZODFP0uco3SWsBZm7dSk7K/cwovMQBhX0x2P52zSAdMwYeyP7+HzjInRNZ1rvSeSZeWgplhTQdIjoIRbu+ppNJVsZVNiPkZ2H4LH9pFqs269FUJV7CS76jIhSBIZPxwwUEXKSv1aN4ZoximOlzN2wENuxmdp7Ip28nVK2Q7R/jZ5aP3nyZMrKynBdlwEDBtSMFZo0aRK9evVq7nq2ibacWq80xZptZfzl8QUcfG3rlOfj5h9Mw6dT6xdEfaYgKk2xaXclNz86Py5lRX62l5uvmUqWqScknLSVxv89/yXL1+2L237S1H6cfdRA9Db41mpM1vqOqD1Pt/VoFs76uRS/E78Uh1nUm87n/ppy21/r89tz25UvzN/nPsS6ks1x288bdiLH9J2OHYvPAaZ02BTayG2f3YftHmhrni+X3828Hr+Vk/C5bQ2OJ8rDS55hyc4VcdtnDZjBmYNPQh0SSGiaYo+9i5s/vpOofaAnzG/6+N3MG8inMCGwC+hhyj94nOCqufHbR8wgZ+YlBO2m50tzzRgvrn6NDzbOi9s+sfsYrhh7vqyx1IZacmp9o/NmnHXWWdx1113MnTuXOXPm8Mc//pEzzzyzwwRCbS1iu/ztyUUc+iNvX2mYh175Clc1PeVJ1Hb5yxMLE3J3lVREuPv5pQmTaL1eg/lf70wIhADemLeR3SUh2iITS11Z6yMZEAi1dx6rIiEQAojt3UL5gtfwpH+i90bxejXe3/BZQiAE8NyqNym1yhO2x/Qwd8x7MC4QAigNl/Hw4mdwjda/ba3rGl/vW5MQCAG8u+FTdoV2o1T8rbyoHubv8x6IC4QAQrEwd37+EJYevzq8pimcXRsSAiGA4Nef4uz5psm3CzVNsT24MyEQAli0Yxmr9q9t8JesaB8a/a7+6le/YtasWRQWFtbr8aWlpVx66aXtekXq1qJpio07ypLm2gJYvHo34Xrei09FKdi5P0gokjzh4qpNxYQOOUZlxOLNeRtT7vONuRsxzNb/1VSfrPUifRmGTmjtFynLK5a+i+mkToDankXcSt75JvHLvdpHm+bj9x/4TCml2F6+MyGAqPb1nrVE3NZPGmZpEd5Y+37K8jfWfYBmxP8oqbAqKAmXJX38zoo9BO3499yjYpQveC3lMcoXvIapmvhZ1x3eXPdhyuI5a98npkWbdgyRllotxI3FYnzxxReUlpa21iHbLaWgspYBlK4LdpPHBahaM7dDYrZ3x63K6J5KMGxhO63fZdvQrPUivSgFdiixB6SaG4ugOmgeLBeXYC0Z4sujwbgeFaUgGAvVuk/Lbf3g33FdQrHU7QjGQjiH9DXHUgR01axDBg0p18GJpg6KnUgQ1cSVUx2cWl/fUCyM62bObalMIv19aci2XQb1zk9Z3rUwgNds2lvnui69u6ZeCyo/x0vAGz9bw+/RGT+kc8rnTBnVDb0NJrVUZ61PJlnWepFeLMshMCj1ZAtfnxHYNN/g2HRi4mFsl6Epy6f2HEc0eiC4cRyXvvmphyIU+PPw6b6U5S3FxMOE7qNTlk/pNQHNib+e5Htz0VPc7vcaXrI9gbhtlubFP/jwlMcIDJmMpTVtzJDumBzec1zK8ok9xuBRTR+XJNKPBENpKstrMGNsj6Rl3z9jFN5muG/tMzWOn9w3adlVp41MOIYdszn76EH4vYkDOLoWBhg7uDPRaOvntKjOWp9MddZ6kb5c14Xcbnh7JHkPNZ38Yy4j7HbMYMixDC4YdTqmlviZ6pPbg755vRIGivqUn5l9pyTd3+XjzsVjt34w5Fhw/KCZBMzEge6d/AWM7ToyYRKDx/VxxrATku7vgpGn4XHi9xWzXLJGHokWyE14vJ6VR2DEDCyraT2Itu0wqfsYCvx5CWVZngCzBhyBHeuYvZSZrtmy1tdl7969zJgxg0cffZSpU6e2xiGbrK0TtbqaxmfLd/DSR+spLg8zqFc+l58ygm4F/qSZ2A9W31H3jqZYuGo3L76/jr2lIfr3yOOyk4fTqygr6TEMQ6M0bPHUm6tY8PUuTENj5vienH30YHx63YlRW0pDs9Z3RO15holSkKWFCS59l/LFb+JEgvj6jqLg6O8S8RYRc2oPaNtz200TSp1inl72Mkt3r8JreJjVdyonDjkaLeoj2Z1n1xtj4Y6lvLL6bYpDpfQr6M3Fo8+im68bymqbnJCaBiG9khe+fo3525agK40j+07htCGz8FiBpFP+XTPGyuI1vPD1HHZX7KVHTlfOH3U6A3L7oWKJAaKuKwJ2GaXzXiD4ddVYq8CIGeRNO5tKldssywpomiJqBHl59dt8uvkLHNdlcs/xnDPiZPx2dlqsfdWez/emSPus9fUhwVDj6IZGxHIAhabAUPVbY6ghHxZd12pmXNXnGJpWFahFv62Xz9Swmziguzk0Jmt9R9IRLpCmAR4nhMLFUiYRx1OvaeLtve2aBpoZI+bGUCg8KkA0Unu7dV0jZoTRDYUbU2iWmRZf1Mp0sVTVIGPT8eLUMYRJ1zWiWhiUi3IVpuOr83PrNRxMN4Jp6IRdD6EWGNOsmS6x6na4HpxY+ixs2d7P98ZKy6z1onXYVnVWdRdcEqbaN8sxDsrcXp9jOE7V/5jfPiEdAiFoXNZ6kV5iFsQ4+PZI23+5twbHASdior79VEXr0W7bdvAoHwW53345tMHkhWTcmEKnalxNfWpk2w66feA2qF2PZ0UsDdvIwp+bRay4sp5Hahinge0Q7ZsMphBCCCFERmu1YEjTNHr06IHP1/qD+4QQQgghUmm122SFhYW8/37qRbmEEEIIIdpCvYOhSy+9tME7V0rxr3/9q8HPE62voVmjW+MYug6BgBfXhWAwknRWjRAdhaYpDENrULb31uD3mxiGTjRqEUmxYn1zHSMWswjLivGiDdQ7GGrMpLO2SBYoGqYxWesbStMUIctl7rIdbN5ZzrB+hYwcUIhXUylnv1gotu8L8en769GUxpHje1KY68WQc0p0MEqBbUbZVrmLLzYsIcv0M633JLK0bJTVdnNcPF6HoFPJh5uWsbViF8MK+zOiyxB8Kq/ZgiLTC5VuJZ9vXc6W0h0MKOzDmK7DCJBFrPWziogM1mpT69ujdJha31gtlbW+oTRNsb04zO8fnBeXNiPbb/KnH04jz2ckBES20rj/pWUsXLk7bvtRE3px8QlD0WupU6ZOOQVpe3ttu+ONcuf8h1i3f2Pc9vNGnsaRPafWGhC1VLs9HthSuZk/f3Yf1kFz43M8Wfx+5nXkakVN7r3yeHS2Rbby54/vTshaf+PMn9DZ6FLrIq7t+T1vqkxte1pmrRftX0Oz1jdGxIZbH1+QkD+sIhTj708vJnbIQbxeg6827EsIhAA+XLyVzbsrMIy2WVROiOamG4qPNs1LCIQAnlvxKhVO6pxtLSlCJbd//khcIARQHq3k7gVP4Kqm/0gMqnL+Me/hpFnr/+/zRwiriiYfQ4j6apZgqKKigp07d7J9+/aEfyI9NSZrfWOUVEQoq0y+ItqmneWEovHHD0Ud5sz9JuX+5nz2Da5Kn8XPhGiKqArzzvqPU5Z/vGk+ptn6wf/eYDGVseRJUTeWbKXCTp2Utb7KorVnra+0ak9IK0RzatIN6aeffprHHnuMLVu2pHzMypUrm3II0WLqmbW+iUMWInUEVJbtAAcu9pbrpAzQAIJhC8txkHBIdAiKOrLWV8RlrW8Nug7hcO3BjuXUnnG+Pg7tETpUzJaB1KL1NLpn6JlnnuGPf/wjffr04frrr8d1XS677DKuvvpqioqKGDZsGH/605+as66iGTUma31jdM73o6W4lmf5DLJ88Rnls70m44d0Trm/w0Z0JeCRu7uiYzBck7Fdh6csn9JrApbVujPLbBu65XRFpfjJke3JItvMavJxCv35tWatz/E2/RhC1Fejv1WefPJJZsyYwUMPPcR5550HwMyZM7nhhhuYM2cOlZWVlJSUNFc9RQtoaNb6xvAYitOPHJi07LKTRyRklI9GYpw8vT/ZfjPh8YW5PqaN6UEoJL8YRQdhaZw3MkXW+rwe9M7p2Sb5xgKalxMHTE9adsmo0/FpTQ9U/MrHqUNnJS37zoiTyVaBJh9DiPpq9Lfd5s2bOfroowEwzaovrlisqtszJyeH73znOzz99NPNUEXRUpTrct6xg7jm7NF0zvejFAzomcdN35/CiL4FzbLekHJcTp3Wj+vOG0fXwgBKQZ9uOfzmisOZOLQzTpJjZHs0/jJ7BjPG9sDQNbymzrGTevOnH04jW3qFRAfiupBNLn869peM7z4KTWn4TR+nDT2O/5n2I4yYt03qFYt4OHPo8Vw97jw6BwpRKPrk9eRX037A+C7DCYebHqDZYZ3jBxzBNZO+S9fszigUPXO68ZMpVzKt1wQiYbkZLlpPo0eE5OTkYNtV3bfZ2dn4/X527txZU56VlcXevXubXkPRojTHZerwrkwY0qXq73pkrW/wMVyXSUOKGDWgEwAK8NSyjlEs5uDXFd87fSTfPWk4Chefx8COWrVOtRWiPXJtyFZ5fH/Md7HGVv2g9Lg+7IjbpmlqrYiPKT2nMr7bCKpG9il0spv3Mxj2cliXiYzsPBgHFx0NH9lEZOFF0coaHQwNHjyYVatW1fw9duxYnnnmGWbOnInjODz77LP069evOeooWlhDs9Y3hmU5cSebXY/rqROzqc5lbUfl4ig6LtcFYlpNlnS7TcOgA0KhGFB1u8oGbJr/x0g4HEPDX3ObIoJ81kXra/Q9h9NPP521a9cSjVZNm7722mtZv349Rx11FMcccwzffPMN119/fXPVUwghhBCiRTS6Z+icc87hnHPOqfl74sSJvP7667z33nsYhsH06dPp379/s1RSCCGEEKKlNGvim969e3P55Zc35y6FEEIIIVpUk4OhNWvW8NFHH7Ft2zYAevXqxRFHHMHQoUMbvK+PPvqIBx98kHXr1lFRUUHXrl2ZNWsWs2fPJicn9Zo4AM8//zwPPfQQ27dvp3///txwww01s93SSWMyUxuGjqZVje1pruSpbcHrNdB1Dcuy6zUIUykwTR3XBcuyqU+atOp8NFXHab85e3RdQ9erEtm2VDtMU8M0DWzbqXfiTdPUUapqDFhLTfn2+02UgmjUrlfbNU01eJVmn89E0xTRqNWuzxPft+t0maZer3YopTDNhl1/qj+3sZhdr+cc/Lltav6y5tTQz5RSVddepara0Z6zeFZ/bmMxp175Jqu/pxyHVl/nqq00OhiKRqP87ne/4+WXX8Z1XTSt6kvIcRxuv/12TjvtNG6++WY8Hk8dezqgpKSEMWPGcMkll5Cfn8/atWu56667WLt2LY888kjK573++uvceOONXHPNNUyZMoU5c+Ywe/ZsnnrqKcaNG9fYJjYrpSDmKrbtquDzFTvJDXiYMa4H2V4Dlerk/Daj/PylW9i5L8jYwZ0Z3Dsfj9a8s71amm5oVEYdPl64lS27KxjSJ5+xg4sIGKkDFhvF3tIwny7djqYpjhzbk4IcD1qK10rTFGHbZcHynazbWsLg3vmMGVSEz1A47SiA1HUNv1NOdMsqIltWYhb1InvgRMJ6NpbdPFONDUMj4JQS3bSays0rMPO7kjtsClE9h7CdPKjwajHMaCnB5Z9hhysJDJmMVtCToOtrti8J3YxR4VTw3rqFlEYqmNR9NH3ye6LF/DhJThOlFJYZ5puybSxev5xOWQVM7jEenxFAWcnbYZgxKtxKPtiwiP3hUiZ0G0n//D5oVhZOsoOkKd3nUOlU8tGGj9ldsY9hnQcxrGggWW5Oyh8aWVoYt2wnwVXzUKaXrBEzsL35hJ3k12jD4xJ2K5m/ZWlN1vrhXYbgdXNTBjmOGWNvZB+fb1yErulM6z2JPDMPLZa4blhr0XSI6CGW7F7N+uKN9Mvvw5guw/DagaTnFYBrxiiOlTJ3w0Jsx2Zq74l08nZq03Y0hmtYVDjlzNu4iEorxOSe4+kW6IIWTf6ea5oiZoRZU7yR5btX0SWriMN7jsXrBMDu2MuaNDpr/Z/+9CeeeOIJLrroIr773e/Sp08flFJs2rSJJ554gmeeeYZLLrmE3/zmN02q4HPPPceNN97Ixx9/TNeuXZM+5oQTTmDUqFHcfvvtNdsuuOACcnJyePDBBxt97ObMWm8rxZ8fW8A3O+Jz8Vxx6ghmjO6eEBApTbFmWxl/eXxB3OyuTnk+bv7BNHw6tX4JpUtWY8PQ2Lw3yE0PfZ6Qtf7ma6ZRmGUm1M9RigdfWcH8FTvjts86rDcXzBqSEBBpmmJPeYQb759H+KAvAr/X4OYfTKUox9MuetQ0TRGw9rPrqd/hhA5K0KkbdD3vN0Ty+lPb0k/1ec81TZHtFLPz6T9gV5QcVKDT9eyfYXceRuSQi55Xi2F9/T4lHz8Tt93TfSCdzvwfKmxfQ5uaQDdjfL5jIY8t+2/c9t453fnVjB9CJPEYlifMLZ/exc6KPXHbr5l0CaMLRsAhgZ1hWizZ+xX3Lopf/6xrdmduPGI2KuJvcjtag+6D9aXr+fvcB7HdA+9zni+XG2deR7aTl3C+Z+th9r/+f0Q2fx23PXfy6fjGn0rokIDIMGBbKFXW+p+QowoTP7eeKA8veYYlO1fEbZ81YAZnDj4J1cyBRH3Od11X7Hf28b8f/YPQQWlPvIaX3x55HUVal4Qflq4Z48XVr/HBxnlx2yd2H8MVY89HRds+IKpP213T4oPNn/Liyjlx2wd36s91h1+FFol/z5WCiBnkfz/6B/tDJQdtV/x0yvcZmD0Qt5l+kDVWWmatf+WVVzjjjDP43e9+x4ABAzAMA13XGTBgAL///e857bTTeOWVVxq7+xr5+fnAgQUdD7VlyxY2btzISSedFLf95JNPZt68eTWz3dqSrmu8MW9TQiAE8OhrX1OZ5BZFxHb525OLEqa57ysN89ArX+GmWMY+3QRjLn99YmHSrPV3PLOYsBXfQF3XWLmpOCEQAnh3wRa27a1EOyS/R9SBWx9fGBcIAYQiFn99chGRdhAIAXiJsO+1/4sPhABsiz3/+Rt+kifObIgsLcy+Nx+ID4QAHJvdL/0Dn5MY/JvR0oRACCC6Yz3B5e9jGk2/QAbdYEIgBLClfAevrXkHzyFrD2qmy39WzUkIhADuX/gkES0xt1aIEPctSmzHroo9PPfVq3i87aNnKOwGufPzR+ICIYDScBkPL/43ticSt13XNcJrv0gIhADK5r+CFtzLoenPYlptWesfx9Hik6jqusbX+9YkBEIA7274lF2h3a2eYw0gqkf4x+cPxQVCABErwh3zHiRmxG/XNMX24M6EQAhg0Y5lrNq/tsFfsm2l3CpLCIQA1u77hs+2fIF+yOfWNWz+teT5uEAIqlI33Tn/EaJ605PzprNG3yazLIuxY8emLB8/fjwffPBBo/Zt2zaWZbFu3TruuecejjnmGHr16pX0sRs2bABImLk2cOBAYrEYW7ZsYeDA5Okg6sMwmn7iR2yXNz/fmLL802U7OHNGv5pIVynFmk3F3yYxTbR49W4ilkNWLasxHzx2pi3t2h+qNWt9MGJRmHXgl5blwiufbEi5v1c+2cBPzh2Lph0IcEoqouwrTf5B3bU/SDBixx0jXenRSqI7v0la5kSCOOV7MfL6pX5+Pd5zFQsSTvKlCOBaUaJ7t+DpPqrm9oFh6FTO/yjl/soXv0nX0UfjGo1Pz+DxGHyy4cuU5e9vnM8pg4/FNLJrtoVVkE83L0j6eBeXr3avYlq3w2t6SExTY/HWlaRaxvCzbV9y7shT8Bi1j01sa7oOG0q3p0xyunLPOkJWhBzjQE+a1w2yd1Hil2K1ii/fxn/09+J+ae+oI2t90A6RbRzoSbP0KG+sfT/lMd5Y9wFXj7sE12q+61F9zvdyK8juyuSL/+4PlVBpVVJ4UDvQXd5c8WHK/c1Z+z7DpwzFUG17Pamr7aap88rqxICu2lvrP2J6r8PwHNT2oAqydGfya4PlWGwq3cLw3OH1GnPUUlrye63RwdCMGTP49NNPueiii5KWf/LJJ0yfnjy3TV2OPvpodu3aBcARRxwRd/vrUKWlpQDk5ubGba/+u7q8MTRNUVDQ9Bw8e0qChGsZoFoRjJKTE99FH1qTevVu1wUX6lW33Ny27fpfv7O81nLLduLaUVIerjNrvcdrkOU/0MW7qyyS8vFQNb6qOd7HlhbZldjLcTBlRZr8nkd27qr1uU64kry8+GOEgqnfQycSxDR0/LlNe33Lo6lvR0fsKErFn++7KoLYTuqBncFYiNzc+NxWldHUPWu2Y+O67eM8Ce4N1Voec2IUFB5oh1UexomkbrsTriArYKLpB74OvtlSV9Z6i4Kigz63IYtQLPVzgrEQXp+B32z6LdVD1Xa+79tf+2fKdu2497wyGiIYS/36hmJhTFMjv4nne3NJ1XbXdSmPpP5MhWJhDFOnIHCgHcGy8pQ/FgBCVpj8/PTIF9cS32uNDoZ+8pOfcP311zN79mwuvvhi+vTpA8CmTZt46qmn2L59O3fccUdCstbq2161eeCBBwiFQqxbt457772Xa665hkcffRRdb3oW9YZwHJeysqbfmtCAMYM6s2Rt8g/m5JHdKCkJxkXcA3vmpdxf18IApq4oLk59suu6Rm6un7KyULPkGGusroVZaCr5qtZZPoNsvxnXDqVpHDaiK1t3VyTd37Qx3bFjFsXhA7+McwMmhq4l7UnzmjpZhxwjXfkMP5o/GyeUrO0KLa9rk9/zgOlHzynELt+ftNzbfUD8+6EUgWFTqVj+YdLH+weMI+LolDfh9dU0mNh9NK+vS94DNaJoEAZGXL003aB/QW++Kd6S9DkjuwxNeK1GdR0GSW4bAPTL74VHtY/zpH9Bn5RlBf48AqY/rh2mZuIfOIHK5R8mfU5g+HTKK6I4zoEfFdVZ65N9OWZ7ssgyA/HniW4wofto3liX/G7AlF4TiAYdwkluwzZWfc73LD0Lj24m7UkzNIMcMzuuHbqumNxzHKv2rku6v4k9xkBMpzjctudJXW3XNMXUXhOYu2Vh0ueP6zYSZcV/pgzdpEtWUcqetAH5fdv881Hf77XcXH+De48aHQydfPLJQNXU+vfeey+urPpL/ZRTTkl43sqVK+vc97Bhw4CqW22jR4/mjDPO4J133uHEE09MeGxeXlXQUF5eTufOnWu2l5WVxZU3VnMMPlZKcdkpw/nqrr1Yh4xfGdgzjx6dshJmZwS8OjPG9uDTpdsT9vf9M0bh0VS96mbbTpsOoPYaGqdM78+rnybe/rn4xGEEPDpWXNsdTpjcl3fmb6YiFH8BK8z1cfiIbkQi8a+VR1OcP2swT721OuEYFx4/BI9ev9eqrYX1LAqOuZx9r9+dUJYz8USieqDJ73nIzKXTsZex+6U7EsqyRkzHMbMSnuvp1Aezcx9iezbHbVe6Sf6RF1Fp6bhu017fblldGFTQl3XFm+K260rjkjFn4cR8cbO9NMfksrHncdNHf0/oth/ZeQj5Zj5WLL5Onfz5jCoazFd718a3QymuGHsOyvG3i/Mk4PMxvc8kPtuc+EV3ydizyXKziRw0HdpCkTf1LIKrPsc9pPfGKOiG2WMoFYeMt/ObPk4cMJ03NnyaeIxRp+Mli+jBr5UFxw+ayUebPk/oWenkL2Bs15EtllewtvPdY/g4b+RpPLnsPwllZw0/EdPxxT3XsqoGSr+y5h2KQ/F3FbI8AWYNOIJYJH3Okdra3jevN71yurO1fEfcdlM3OWfEyThR4j63puvjivHn8ZdP/5mwryk9xxPQshI+U22lJb7XGj2b7K677mrUgLjZs2c36PGu6zJ69Giuu+46rr766oTyLVu2MGvWLO655x5mzZpVs/2JJ57gL3/5C4sXL27Q9P6DNedsMqUpSoIxHp+ziqVrd+P3mZw0pS8nTOmLgZt0ZpiraXy2fAcvfbSe4vIwg3rlc/kpI+hW4E89Hf9b6TKbDMDRNBav3s2LH6xjd3GQ3l1zuOiEYQzqkYeW5EtU0xRBy+HZd9bw2bId6Jpi5oSenH3UIHzfrhNyKFcpvt5UzNNvr2bnvkp6ds7mouOHMrR3fp2vVTrxahba/m8o+fBJors3Y+QWkTf9HIx+EwjatZ/H9X3Ps/QoFG9m/4dPE935DXpOAXmHn4p/6FTKrMTuZ6UgWwtRsfhNype8gxsN4+8/jvyjLyZsdqI5Ti9NA9cT5t31n/DWN58RjIUYVTSEi8ecQYFRgBVL0iusOxTb+3hq2X9ZtXc92d4sThp0NEf2mYKKJB/TofkifPjNXOZs+ISKSCXDigby3dFnUOQpSn6MNOX6o3y+dTFz1rxPcaiUfgW9uWD06fTM6oaKJJ4nugZ+q5jSj58huG4RSjfJHnM0OYedRoWblXQciOaN8uWOZfx3zbvsDRbTO68HF408lX45vbFjicfQNAjplbzw9WvM37YEXWkc2XcKpw2ZhccKNPtyIPU9313TYl3pBp5b8So7ynfTNbuIc0eeytD8wahYYn+ApimiRpCXV7/Np5u/wHFdJvcczzkjTsZvZ6fFsib1abtSYHkivLX+Q97f8BkRO8q4biO5YNTp5JBH0rvMhs3u6G6eXPYfNuzfTL4vl1OHzGJyzwkpP1OtqSVnkzU6GGotS5Ys4fzzz+eOO+6o6Y061AknnMDo0aO57bbbarZdeOGFZGdnp83Ueqg6OR0U1Z1DXkNh1/FNohsaEcsBVIMyyqdTMARVC7dVfNujowC/qYjV8StD6Rox2wVcTF3DreN2n65rxFwXTddwbAdTqTa9RdhYmqbwEkbHxkER1RJ7a5JpyHtuGBp+txLl2oAibOTW+cvdNMDjhFC4WMpDxDGafSE6j1cRdYO4uBgYuJa31vNdKYVjxHA0G49hoFsm0Tp+uccfQ8e1/O1qjaFqPp9BhVsOCjQ0fE6g1vdQKfBoNqYboSovbIC68h97vQYRt2osiYaG7tTdO6lMF0tVTZowHS9OC+Vdbcj5rusaMS2Mq1yUqzAdX53XBs10iVW3w/XgxNp2WvnBGtR2A6IqAgp010RZWq2fW01T2HoURznggsf1YVvpESa0ZDDUbOk4ysvLCQQCTRrXM3v2bEaNGsXQoUPx+XysWrWKhx9+mKFDh9b0+vz617/mpZde4uuvD4x6v/baa/n5z39Onz59mDx5MnPmzGHZsmU8+eSTTW5Xc3JdULg1L3p9TjC7Jtu722IZ5VtDJGJx8O+KWKzuhrj2gUz3dQVCUBW8egyNgvxA2gSBjeE4LiG8B29o9mNYlkM5B/UC1eMWRsyCGC07ID8acQE/Cr7Nj177eeK6Lipm4DU8FORm1WtMQ+Ix2ud5Eg5b+Iysmi+HaB0rBbsuRGydyLdZ6OvT7KqVyateKxew6vEkN6bQvz1/0+WVtW0H7aCeVbseNXPSsB2NYVvUtAPq+kRVXX+UY1L9TW7X+YyOoUnB0PLly/nHP/7BwoULicViPPzww0ydOpX9+/fzm9/8hssvv5zJkyfXe39jxoxhzpw5PPDAA7iuS8+ePTn33HO56qqram51OY6Dbcd/6E899VRCoRAPPvggDzzwAP379+fuu+9m/PjxTWmeEEIIITJAo2+TLV68mMsuu4yuXbsydepUnn/+eR599FGmTp0KwCWXXELnzp35+9//3qwVbk3NfZusNaXbbbLWkqntBml7JrY9U9sN0vZMbHtarkB9xx13MHDgQObMmcMNN9yQUD558mSWLl3a2N0LIYQQQrSKRgdDy5cv5+yzz8bj8SSdVda1a1f27k29cKCoP8PQ8Xh0dD19BvCJ9k/XFR6P3qBV1k2z6lw8NCVKW2pM1vqGtkPTql6rhhyn+nPbksdoKKVa/hiZTNe1Bn+mRHpo9JghwzBqnYGxa9cuAoH0WK2y3eogWetFetE0RYBKYtvWEN70FUZhd7IHH0ZEyybmJL+It0bW+oZSSpGlglh7NhJcv4hoTicCw6YS0XOIOsm/7D2ahccqJ7h0Hnb5fvyDJmB07k+lG0g6vVwpCKgQzr4tBNd+gR7II3v4dGJmLhEnxeXTcAgTZMH2Jeyu3MeYrsMZkN8X0/Il/dzWHKN4O8E189F9WVXH8OQRcZpvOnNDs9aL+quejr987zrW7NtA79wejOs+Ep8dSD6FXaSdRgdDY8eO5a233uLyyy9PKAsGg/znP//hsMMOa0rdMlqyrPVvf7G53lnrhUhGKUWWU8qup38Xl6y15KOn6XLOL3A7DcY6JCCqzlq/96BkrRVfvt2sWesbI1tVsPvZm7GKDywqV/LJs3Q65cd4ek9ICIg8mg1bvmTH6/fUbKtY+i5GQTe6nP87yt3EH2/ZWog9L9wSt+Bk6dwXKZh1JZ5B04geEhApw2VN+Tru/PzhmuDq/W8+o1OggBuPvB5PzJ/wuc3Swux76XaiOw6selw677/kH3kBvhHHEm6GgChZ1vqy+a+QO/l0/Emy1ov60zRFuSrhpvfviEv58vTy//LrI66lm6e7BETtQKP78q677jq++uorrr76aj7++GMAVq9ezfPPP8/ZZ5/N/v37+dGPftRsFc00HSVrvUgvPi3K/rfuT5q1fs9/b8fnJuZlao2s9Q3lNRxKP3s+LhCqtu/1f+JNkvbB61Sy7/XE1XWt4p2UfvYsXuOQlbcNKF/4WsLK2wDF7z6Cx0rM2RbVwtw1/9GEXqZ9wWKeXPYiHHIM01AEl78fFwhVK/n43xiRkoTtDdWYrPWi/iw9yl1fPJqQ+y7mWNw+7wFiHTzbe0fR6G/UsWPH8sADD7Bp0yZ++ctfAnDrrbdy44034jgODzzwQE1aDdEwmqbYuKOs1qz14Zj81BANp1tBwptWJC1zrSjW/q1xYwBNU6fyq9qz1nucpufvayjTDlG5IjFVRBWX8MZlcbNJdF0jvGk5qVZZqVzxGaYdHwh6nBAVS95L+niA0Jr5GMaB3idNU2wo3pQygeyiHcuJEP/F6HGCVHz5VspjVHz1YZPH93jdIOV1ZK03ZYxLo4WcEFtKE9MmAVREKymOlLVyjURjNGmdoalTp/LWW2+xcuVKNm7ciOu69O7dm9GjRzdX/TKSUlAZSkwsWM11wXZckAHVooHcOvrrnUgQpQ7cglVK4YRqz1rfJmeh61Db0sZ2uIKDxy0rBU5tyTUdq2qf8RsTcnnFHSNUgRl3DJXQOxBXZddNEii5OJHUWdKdYHmj0h7FH8KpM2u9ypCF9VqCVccS2xErAm2fyULUodE/B1auXMlrr70GwPDhwznppJPIycnh1ltv5dxzz+Vf//pXs1Uy09i2y6De+SnLuxYG8JryS040wrdZ61PxdOkXN8jXsmz8Q6emfLx/wDhiqvWv9LbmxdOtf8pyf78xcekWbNvB13dUysd7uvbH1uLHzdjKg6/PiNTHGDQpbq0T23YY3Cl1nbpld8ajeeO2WcqLr/+YlM8JDJ+GVcfK0nWxdR/+gRNqOcZ0LEd+WDVWlhkgYCZfmV0pRedAp1aukWiMRn+j/u1vf2POnANdr1u2bGH27Nls3boVqLpl9uyzzza9hhkqy2swY2yPpGXfP2MU3gYuKCUEQFgFKDzuyqRlWaOOxDKy47Y5joteVJW1/lDVWesPHUTcGiJ4KZh1JSQZO+frOwo30CluoLLrgpvVCV/fJL3WSqPguCuJED8QPOx4KDjmMtASb1N5ug9Cy+uWMDYoW89hUo+xSet8xbjz8Tjxx4g6OvlHXoTSEwNKs3Mf9KK+TZ45GrE08qaehTITB7pXZ61vjzn80oXX8XPxmLOSlp0y+Fg8bttMMBAN0+gVqKdNm8ZVV13FVVddBcDdd9/Nww8/zHvvvUdhYSHXX389mzZt4r///W+zVrg1tfUK1B0la31rytR2Q/3b7tUs9NItFH/wRE3W+twpZ+IdNJlK25vw+NbIWt8YpmbjCe6m5MMnCG9eiRbIIXfSyfhHHpVyhlu2Hia04iPKFr6OEyzH12c4+UddQjTQhViS6fim5uKN7KH4wycJb/wKzRsgZ8IJBMYeR6WTfFkB1xvj822LeG3Nu5SGyxlU2I+Lx5xFZ08XsBKDN0MDX2wfJR8+RWjDEpTHR86448iecCIVTuLss7jn1vM9b0zW+nSXTp9117TYXLGFZ756ma2lOyjKKuTs4ScxumgEKtr8PxbSqe2tKS2z1o8ePZo//OEPnHPOOQCce+65dO3albvvvhuA559/nltuuYXFixc3Zvdpoa2DIeg4WetbS6a2GxrWdk1TeImgY+GgiKisOnsHWiNrfUMppfCpKIaKYZgGQddHpI6s9Yah8DpBFC42BmHXW2swoJTCq0Ux3BguiqjmJ1ZHJnbdUERVuCqjvKuj22atn1ulqoJUw43W+xhVban/e96YrPXpLN0+67quiGlRXOWAq/C6vharV7q1vbWkZdb6zp07s379egB2797NihUrOPvss2vKKysr0TS5ldNUHSVrvUgvjuMSwgNUj5Op+4LaGlnrG8p1XUKuiWF4KcjJwq5H1nrLcrHi2lH7h8p1XcK2Sc0o2Hp899iWG5cp3KnzGBC2DWouyS3w/daYrPWi/mzbRbMP3O605AVuVxodDB177LE8+eSTRKNRli5disfj4bjjjqspX716Nb17926WSgohhBBCtJRGB0PXX389+/fv5+WXXyYnJ4dbbrmFoqIiACoqKnjzzTe5+OKLm62iQgghhBAtodHBUFZWFrfffnvSskAgwMcff4zPJ6PohRBCCJHeWmROrKZp5OTktMSuhRDNRNcVuq7hOG69B2H6/SZKQSRi12s6tqYpDEPDcWjyejnNyeczq5JrRq16tb26Ha4LsXqu/m4YOpoGluXUa9KDrmt4vTquC6FaFl099DnV9UsXSlWtXN6Q1yqTmaaOUhCLOWkzqy9dP7ctqfUXCBFCtKmqDNshVu3fyIo9q+me3ZmJPcbicwK4dvIv1Sw9jBYpo3LeJ9iRIFlDDsco6kWFm4WTJJbQNEXMCLOuZBNLd62kc6ATh/cch49A0unlrSWgRzFi5VQs/Ay7opjAwPFkdRtAuZuLk6QhSoFtRtlcvoOF25eQ68thaq9JBFQWykqRJqOBWes1DWJmmM3lO1mwbgl+08+MvoeRrWejRZMnUDV1B69dQfirBewp3oG3z0iyewwlSFaT1yVqioAWgfLdBFd9BppB1ogZOP5CSQSbhGtalFllzP1mIVE7yuSeE+jiL0KLtd1rVf25XVO8keW7V9Elq4jDe47F6wTA7tgToho9tT4TpMPU+saSqZeZ1W6oX9uVUoSNCv740R2UhA/kTNKVxs+nX0Nff9+EgChLDxNe/h4lnz4ft93TbQBdzv45pVZ8tnelIGqGuPnjO9kb3B937J9MvorBOYOa/cJan7b79RjOxoXsfeP++OcWdKPbBb+l1M5OeI7jjfC3ufey+ZDcU5ePO5fDukyAQwKiqqz1a+Oy1gO1Zq13fBHumPcgG4rjE8KePeIkjukzHXVIQGToLubetex+8S8cnA5dz8qn60U3UaHlt0kPQ5YepvTt+wmt/zJue/b44whM/g4hJ3ENq6Zoz591x4zxxob3mLP2/bjto7oM5ZqJl6AitQdELdF2pSBiBvnfj/7B/lDJQdsVP53yfQZmD0z5Y6m1tOTU+o4d6gkh4rhGjIcWPxMXCAHYrsMd8x5MmmFbC5cmBEIA0Z0bKF/yDj7vIZcRw+GpZf+JC4Sgaor6XfMfIaZHmt6QRvDYlex944GE7VbxToo//jdZnvjbAZoBb6z7ICEQAnhsyfMESfyh1OCs9V6N9775NCEQAvjP129QZiXmhfM5Qfb897a4QAjArixh/1v349OiCc9pabquEdu8PCEQAqj48h0o3dH0HGsdhFKwP7I/IRAC+Gr3ahbv/AqjDRLnuobNv5Y8HxcIQdXn9s75jxBNcm3oSCQYEiKDhN0IX+9Zk7QsasfYVr4r7kvL7zepWF5L1vol7+GJxQdWEcIs3LEs6eNt12Hd/o2tPsbF49EJbVhKyqz1Kz9Hj8UHNzEtwnvffJZynwu2LW1y1voQlXywYW7KY3y08XP8/gNr1yilsPZvw7WSBzzhzV+jW6kTv7YUjxumfOGclOUVi17Ho7ev3puWopuKdzZ8krL8zXUfEFGtH3hEibB059dJyyzHYmPJlrQam9bcJBgSIoPYbu1LDodiIdQhmdidcEXKxyfLhm67dq23aYKxYKv3EiilsGtpR7Ks9S5uVcbxFCqilQmvVUOz1rtA0Er9xVcZjX+tlEr+msft06nf4Otm5Tq11ssJBxNe30zlui6VsdTDL0KxMG4di3S2BMuxaj1u8JBrQ0cjwZAQGcSn+Sj056cs75PfM24AbjRqERgyOeXj/f3GYOvx4xu8ykv37C4pnzOk04BWTwwai1n4a8kO7+naH1ePH9NiuAYjOg9O+ZyJ3Uc3OWu9Bw+juwxL+ZzDe40jelDODMdx8XTpm/Lxek4hmIGU5S3F1n34B01KWR4YNhVL5utUcTSm9JqYsnh891F4aP1B1F7NR5esopTlAwv7Ydsdd4ixBENCZBCP4+PycecmLTuiz+H4VfwXqWU5mF37YXZOXE1e6SaFR11IyI6/cJuOjyvGn48i8WfkpB5jyNYTByq3NMcBLbsIX5+RiYVKo3DWZYRUVvxmy+S7Y85BV4mXyUGF/egS6NzkrPUqpnP+6NMwtcRAoXdeD/rl9UoYKGoZWWSNPirpMQpnXUFYtX4wFLUgZ+KJaN7EY+s5nfAOmNChv0gbwrYdhncanDTw8BleTh0yCyfW+l0wHsfHFePPS1o2ped4srSspGUdhcwmq4XMJmt/MrXd0IC2GzY7wjt5avl/2Vi8hQJ/HqcPPZ5J3caiombCwzUNcrRKyhbMoXzZB99mrR9DwVEXEfV1IZLszpvhsCe6h6eX/4e1+zaS68vh1CHHMrXnJFQk8RhNVd+25xlBKpa9T9nit6uy1vceRsHRF2NndSVkJ9ZL6S6lbgnPLH+J5btXETD9HD/wSI7pNwM96mmWrPWaCWVOMU8vf5nlu1bhNTwc3W8qJw4+GjPqS7p0QZYeIbLuC8o+/y92eTGebv0pOPoS7LzeRJy26YHRNMhyyij99FkqV81HaRpZo44id8oZVJLd7FP+2/NnXdMUUTPEnLXv8+HGeVh2jEk9x3LuiFPJcnMOHRufoMXabtjsju7myWX/YcP+zeT7cjl1yCwm95zQIp/bBlcvHbPWZwIJhtqfTG03NDxrva1HcZQDLngcf523rvxeMGMVoMBRHoKOJ+kXdfwxYjjKrjqG68O2WuZy05C2e70Kb6xqlparGVQ6gaRrDFVTSuEaFpayUPVsR0Oz1msauB6LmFs13sevAsTCdRxD1/ARxDQUMVsRcrxtusZQNa/uYLhhFIqo5iNqtUwvR0f4rOsmRFXVuDTDNcHSkgbYh2rJtidcG1rwc9tQaZm1XgjRfjmOi3JMqudC2fXIsB2KQIj63+KqOoaB/u1lxm6DQaHJRCIukep2ODX/k5LruhDTMb59terTjoZmrXccIGxgfPtaxepzDNshYgQI5GZRUVxZa0DXmiK2RoRvb5elR5XSlh2j5jxJj09HsmtDutSsZcmYISGEEEJkNAmGhBBCCJHRJBgSQgghREaTMUNCNJCua+i6alC293TUmKz1DeXzGXi9JrbtUFHRMmk4NE1hmimSprahhmatr84ULtnehWh9EgwJUU+6Dn6ngujGFUS2r8XTpS85A8YR1LKx2ziBYUNomiJAJbFtawhv+gqjsDvZgw8jomUTc5qns9jjMQipMpbs28TyXavoFChgau8J5OgBrHDzXHaUUmSpINaejQTXLyKa04nAsKlE9ByiThsGRw3MWq8U2GaUbZW7+GLDErJMP9N6TyJLy0ZZcokWojXIJ02IetA0hT+8m11P/z4u7YAyPHS98HeEsnrVOs08XSilyHJK2fX077ArSmq2l3z0NF3O+QVup8FYTQyIdB0qVSk3f3RXXLLW/6x8g2sPv5yRhYOxIk2/9GSrCnY/ezNW8Y6abSWfPEunU36Mp/eENgmIqrLWr4vLWv/+N5/VmrXe9kS5c/5DrNu/sWbby6vf5ryRp3Fkz6kSEAnRCmTMkBD14CPE3pf/npB/ybWi7PnPbfhp/eSYjeHToux/6/64QAgAx2bPf2/H5za9HcoT44klybPW3/PFvwjS9NtlXsOh9LPn4wKhavte/ydep23WB2to1nrdUHy0aV5cIFTtuRWvUuEkZq0XQjQ/CYaEqAcVrSC2P/GLF8CuLIFQaetWqJF0K0h404qkZa4Vxdq/tclJVIN2hMU7v0paZrsOa/aux+ttWm+HaYeoXPFpilKX8MZlDV50rakak7U+qsK8s/7jlPv8eNP8tBwPJURHI8GQEPVh157t3bWirVSRpnHrWOffiQSbnJnacqxas9ZXREPoehMP4jpVmeZTsMMVrZ5huzFZ61G1Z60vj1Y0OTgVQtRNgiEh6kH5clCmL3mhpqNnF7ZuhRrL9FdlNk/B06Vfk1M6+HRPrVnrh3ceSDAYa9IxbM2Lp1vqDPH+fmPqTC/S3BqTtd5wTcZ2HZ7yOVN6TcCyZGaZEC1NgiEh6iGiBcg/6qKkZXlTziSq+Vu5Ro0TVgEKj7syaVnWqCOxjKZnlM/S8rh03HeSZq2f0G0keZ6mHyOCl4JZV0KSjPK+vqNwA53qleOpuTU0az2WxnkjT0+atb5PXg965/RMi3xjQnR0kqi1FpKotf1pyXb7tRju7jWUfPwMsb3bMPK7kDfjPIzeownanmY9VmPUt+1ezUIv3ULxB08Q3fkNek4BuVPOxDtoMpW2N+XzGlQXb4xtoT08s/xl1n2btf7EQTM5su/hEGqeY5iajSe4m5IPnyC8eSVaIIfcSSfjH3kUFXaKXrxW0NCs9UqHCkp55quXWbrza7yGh1kDjuD4ATPRo55ag7pM/ZyDtD0T2y5Z69uIBEPtT0u3W9c1vG4IDRsHjYgKtPrtmFQamrXeSwQdCwdFRGU1ezs8HoOYVonlVt3myTZyCFU27y0fpRQ+FcVQMQzTIOj6iETa/v1oaNZ6pQDDwVJVtw89rg87VvelOVM/5yBtz8S2S9Z6IdKEbTsEObhno31eiBzHJYQHqO7Rav52RKMW4K3Jfh2KNP/YF9d1CbkmhuGlICcLuzg9frw0NGu96wIxreY5mZIpXIh0IWOGhBBCCJHRJBgSQgghREaT22RCCCGazHEc7DrW42re4ynCYZ1oNIJtZ9ZtxUxte3W7HceGJLNVm0KCISE6CMOo6uhtyTX6TFNHqYZnYncc0mq9nIa2Q6Tmui5lZfsJhSpa/dh792o47SEpYAvI1LZXt9vvzyY3t7DZFiWVYEiIds6nRdEjJQSXfko4FiEwbCqe3G5UHrqmTRN4tRhmtJTg8s+ww5UEhkxGK+hJ0PUlnfqtaYoAlcR2rSe8YSlGXmeyh04hqucQbWIi2CYxHEJU8sGWxewPlTC++yj65vbCiPlqXTVbpFYdCGVnF+DxeFt1xWxdVxnVM3Kwlmq7qxyiVoywHcHQdPymD83VaO6emMbSdQgGw1RUFAOQl9epWfYrwZAQ7ZhfixJe8jpln79cs6188Vt4e4+g8NTrmmW9Ha8Ww/r6ffZ+/EzNtoov38bTfSCdzvyfhGMoBVluObufuQmrbE/N9pJPnqXzGTdgdhtJrC0CIt3hq+KvuXfB4zWb3v/mM7pmd+Y3M65Fj7bd2kTtlePYNYFQdnZuqx/fMLSMmlp+sJZou6NsdpTvw6pOG2NDWaySrtlFeDUP6RAQGYaGplXNgq2oKCYnpwBNa/r1RAZQC9FOKQVacF9cIFQtsuVrwmvn19w6awozWkrJQYFQteiO9QSXv49pxF8gPZpNyQePxwVCALgOe175Bz43df6ulhTVQty34ImE7bsq9vDCytfRzMzsYWgK26760vR4mmchTdGGlMu+YPGBQOhbLrCrci+OSq/PR/U511zj1CQYEqKdMk2NiiVvpywvXzgHj920wMM0dSq/+ij1MRa/iceJP4ZpBwmuXZj8CY5NZMdaNK11f2HqusZXe9bgpli/57MtCxMyyov6k2Sy7Z+DQyiW/DPguhBNs2TUzX3OSTAkRDulXBcnnHrQqhMJQhMX71NK4YTKaz1GwiXJsauyyqfghitb/ctTKaiIpF6Q0XbslIGSEJnAdWu/Wji1fKY7AgmGhGinLEcRGDYtZbl/4HhsrWm3LyzLxj90aupjDBhHTJlx2xzDh1nYPeVzvD2HtklG+VFdhqYs75ffCxMzZbkQHZ2mVNKEwdW8RtvnX2xJEgwJ0U7ZtoPZYyhGQWLgoUwveVPPIWI37SPuOC56UR/Mzn0Sj6Gb5B95EVEn/gIaUQEKjruKZIMt/YMPw/a2/kBb14V8b37SgEgpxeXjzkNPg2S7Qhxq9uyrmT376hY/jnI1OgUKkpZle/xoSk9a1lFIMCREO1bpZtHlghvJmXQKyuMDTScw5HC6XXYrQT2vWY4RdP10/s7/I3fyGShvAJSGf8AEul1+K2GzMGFqvW072AX96frdP+LtMQRQ6Fn55B99CfmzvkfIaZvBtlrU5JqJl3D+yNPI8WajUAwvGsQfj/45Xcwust6QyHhezUOPnC54DQ8KMDSdTv58Cv0FKLdjjwuTrPW1kKz17U+mtttjgNcNoRsaUcckZGlJ1/9pCtMAjxNC4WIpDxHHqPUYmqbwqgi6a+GiiGgBLKtlLjcNed+rM8q7CnRXR7PMdrvGUFuf77FYlH37dtCpU3dMs/V71jJhan0sFgPANONv47Zk2111YL/KTa8+k+p213buSdZ6ITJU1ALHyKIgN4uK4krcFhjsGLMghr/ej3cclxAe4NsLVZr0vByaUV4GTot0dmgQ1BrSLQBqDRIMCSGEyHjBYCUPPngfn3zyIfv27SUrK5tBgwbzwx9ex9Chw5g9+2pKS0v4zW9u4h//+Btr1qymU6dOXHzxpZx55nfi9hWNRnniiUd5++032L17FwUFhcyadTzf+94P8XjiezHeemsOL7zwbzZsWI9pehg4cBCXXXYVhx8+BaBmvNDddz8Qt/9HH32UN9+sff8LFnzOI488yDffrMe2bYqKOnPUUcfygx/8uGVexHZMgiEhhBAZ729/u4UPP3yPs88+j/79+1NaWsqyZUvYtOkbhg4dBkB5eTn/8z8/4ZhjZjFr1vG8//673HbbrRiGyamnngFUJaz91a9+yrJlSzj99LPo27c/Gzas49lnn2bLls3ccsvtNcd85JEHeOSRBxg9egxXXXUNpmny9ddfsWjRgppg6FD13f+GDev5xS9uYODAwTX73rZtK8uXL23hV7J9kmBICCFExps371NOO+1Mrr32hpptF198Wdxj9u7dw+zZ13PBBd8F4IwzzuHqqy/j/vvv4cQTT8EwDN55500WLvyCu+56gLFjx9U8t3//gdx22y0sX76U0aPHsnXrFh577CGOPPJobr75L3EpJWobw1a9/3/+80FGjRqbcv8LF84nFotx223/R35+fhNfnY4vrW4MvvHGG/zwhz/kyCOPZNy4cZxxxhm88MILdQ5uPOaYYxg6dGjCv0gk0ko1Fy1BKfB49JoM4y11DNPU8Xha7hitpaFZ63Vd4fHoDUrZUf1atfYK0u2R12sSCHiaJSVKWzIMDY9Hb/CA1PYmOzuHr79ewd69e1I+Rtd1zjjjnJq/TdPkjDPOprh4P6tWrQTggw/epW/ffvTt24+SkpKafxMnHgbA4sVVq7N//PGHOI7DFVd8LyG3Vm2Lklbvv1+/2vefnZ0DwKeffpiR2e0bKq16hh577DF69uzJr371KwoKCpg7dy433ngjO3fuZPbs2bU+94QTTuDKK6+M23bovVnRfjhmjH2RfXy+aRFKaUzvPYk8Mx8t1nyDCf1aBC24j8qvPwUgMHw6blZRm039bqyGZq2vySi/bQ3hTV9hFHYne/BhRLTslAlUXcOi0qlg7saFVMZCHN5zHN2zuqLHPM0+a629M0yboFvJJ5sWszu4n7FdhjGwsB+mk92uZj4pHSJakM93fsW2sh0MLRrIsE6D8NqBVl80szX88IfX8ac//YGzzz6FoUOHMWXKdE488RR69uxV85iios74/fGTCHr37gvAzp3bGTVqNFu3bmHjxm849dRZSY9TXFyVbX379q1omka/fgMaVM/q/Z944rG17v/YY4/j1Vdf4tZbb+a+++5m4sTDOPLIYzj66GObJbFpR5NWwdC9995LYWFhzd9Tp06lpKSERx99lB/96Ee1voFFRUWMGzeuFWopWprjifGvZc+ycPuymm1vrP2Ao/pN5TtDT0U1Q0AU0CJUfPIUlSs+rtlWvnAOgWFTyT3qspSBRLppaNZ6pRRZTim7nv4ddkVJzfaSj56myzm/wO00GOuQgMg1LD7ZNo9nV7xas+3dDZ8woKAPN0y5Gi0iPzqqGabDquI1/GPBYzU92u9v/JxOgQJ+f+R1mFoW7eFHuqbB9sg2bvn0HiynKhHm+998Ro4ni9/NvIFsLa/Drct07LHHMXbseD7++AMWLPicZ555gqeeepw//emvTJ06vd77cRyHgQMHMXv2DUnLu3bt2qR6Vu//Jz/5WdKgtHr/Xq+Pe+55kMWLFzJv3qfMnz+P9957h1deOYy///1udL1jL6LYUGkVHh4cCFUbPnw4FRUVBINtk+latC5d11izf11cIFTtw43z2B7c2eRbNJqmcPZtjAuEqgVXzcPevb5d3AZqTNZ6nxZl/1v3xwVCADg2e/57Oz43lLCvCqciLhCqtqF4Mx9tmotupP9r1VoiKsT/LXw84db+vmAxjy99Ec1ongzbLS1qhPn7vAdrAqFq5dFK7lnwGLaeXkk7m0tRURFnn30ut9xyO88//wp5eXk8/vgjNeV79+4hFIr/jGzZsgmAbt16ANCzZy/KysqYNOlwDjtscsK/Pn36AdCjRy8cx2Hjxg0NqmP1/g87rPb9A2iaxqRJh3PttT/lySef5+qrf8SiRQtqbqWJA9IqGEpm0aJFdO3alezs7Fof9+qrrzJq1CjGjx/P97//fVavXt0sxzcMrV3+q76/r+ttX5eG/HP0GHPWvZ/y/Xhj7ftoptukdvt0m/IFr6U8RtkXr+LTrTZ/Ler65/UaVCx5J2U7yhfOwesG459nhwhvWpH08a4Vxd6/FdM86LXymXy6eX7KY7y1/mNiWqTNX4t0ON+9XoP1+zZgO3bS12rRzhVE3HC7aPf+cDGVseQ/QDeWbCX8bTt0ve0C4ephNc0x1s+2bSoq4pMeFxQUUlRUVLPoYfXjXn75xZq/Y7EYL7/8H/LzCxg2bDgAxxxzHHv27OaVV/6bcJxIJFwTTB155FFomsajjz6UMKantnGy1ft/+eX/JLT94P2XlZUmPHfw4CE19W6Pkr3nuq4Szt/GSKvbZIdauHAhc+bM4Ze//GWtjzvmmGMYM2YMPXr0YMuWLdx3331cdNFFvPTSS/Tu3bvRx9c0RUFBVqOfnw5yc+u/SF46KA2XEYqFU5YHrRAen0GWp/Z21dZuO1ROSSR1T6MbDeH1aGQF0vu9d22LynDtGeU9pkYg50A7onv2177TWJj8/Ph2l0dTr8IeioUxTI2CNHmt2vp8r9hey3nlutiu3SLXlOZu98YdtX9ZOjgUFGQRDuvs3avVfCG1heYY2B0KVXLWWSdx9NGzGDx4MH5/gAUL5rNy5ddcd91PMQwNpRSdO3fmqaceZ9eunfTp04d3332btWvX8Ktf/Rafr+p28SmnnMoHH7zLbbfdwpIlixgzZuy3PUAbee+9d7jzznsYPnwE/fr15fLLr+KRRx7kxz/+PkcddQwej8nKlV9TVNSZH/3oWuDAYOrq17d6/3/5y59ZtGhhyv3/618P8eWXXzJ9+gy6detOcfF+Xnzxebp06cqECePb7P1qDrpedc5pmkZeXgCfr+nDGtI2GNq5cyc33HADkydP5tJLL631sb/97W9r/v+kSZOYPn06J510Eg8//DB/+MMfGl0Hx3EpK2uft+d0XSM3109ZWahdDXZUus7EHmPYvjp5j8fknhOwwy7Flcm/oOvTbl3T8Q+ZTGTH+qTl/sGHE4rpWMXpnYpF06qy1gfXLEha7h84nrBjEjuoHT7di55TiF2ePCgyOveh+KDHK6WY3HM8H238POnjx3YdDpYW95y2kC7n+5CiQSnLumV3xqd5mvW1aql2dwl0QqGSrs6d7cnCp/soLq4kGo3gOA627bb64HClqtpv206TB/EbhoezzvoOX3wxnw8/fB/XdejZszc/+9mvOOus72BZDq7rkp2dU7Po4ssv/5fCwkJuuOEXnHrqmXHt//Ofb+PZZ5/izTdf56OPPsDr9dGjR0/OPfcCevToVfPYK6/8AV27dufFF5/l/vvvwev1MXDgII477qSax1T3Eh28/1tuuY3nnnuaOXNeS7n/adOOZPv27bz66suUlpaQl5fPuHETuOqqH+DzZbWrwfzVDn7PbdvFcRxKS4OEQvG9sbm5/gYHyWmZm6ysrIyLL74YgKeffpqcnJwG7+Pqq6+muLiY559/vtH1kNxkbSPmCfGb9/9CZTQ+EC3w53HTzJ+hR1P/Cqhvu3O0SnY98RvsypK47Vogl26X/plyp/bbsukiWwuy59n/xSreEbddmV66X/5XylV8slZdV5i7lrPnP7cl7Ctr1JEEZlxC2IkfoG57Itw27142l26P225qBn869pdkO3ltPqMsXc533RPhoaXPsnDHVwllv55+Df1zBhONJr+N1hgt1m7D5rUNb/PGug8Siq6ZdAnjCsZg225G5SarXoH6iSeea5Xj1aU1255Oqtvd3LnJ0q6fLBwO84Mf/IDy8nIeeuihRgVCon3zWgH+9+j/YXqfwzA0A49uckz/6fx+5k8xrea5HVBJNl2/ezNZo49G6SZKN8kadSTdLvkTQdV+zrmGZq23bRe3yzC6Xvh7PN0GAAo9p5CC464k54iLEwIhACPm5X+m/YjThh6H3/ShKY1x3UZy87G/JIe2D4TSiR31ctW48/nuyNPI9+WiUAwu6MdNM39C3+zezRoItShL55RBs/j+xIvpHChEoeiT15NfzvgRowqHY9vypouOJa16hizLYvbs2Xz55Zc89dRTDBqUusu5Nrt27eLkk0/mjDPO4He/+12j6yM9Q21LM11iqmrWiul6cGJ1j5RsaLu9hovhVA04tJSPiJ12vw/qpaFZ6zVN4SWCjoWDIqKy6rzNoptV2d4BdNdAWXraBELpdr57vBpRtxJw0dFRjr9F6tXS7TYMjYgKg3JRroZhe+Km1EvPUNuRnqEOnLX+pptu4oMPPuBXv/oVFRUVLFmypKZsxIgReDweLrvsMrZv384771SNKXnttdf44IMPmDlzJl26dGHLli088MAD6LrOFVdc0UYtEc3Biama7OIt9ZGPWIoIgRbae+tpaNb6hIzy9XiF7dih2d5FKtGIA1T1Ylb1BbXPLy3LctA58EXjyLsuOqi0CoY+++wzAG699daEsvfee49evXp9O1jvQFdzr1692L17N3/+858pLy8nJyeHKVOmcN111zVpJpkQQghR7eCs8aLjSatg6P33U68vU+2JJ56I+3vcuHEJ24QQQggh6qt9DpAQQgghhGgmadUzJMTBqjPKuy5Ylp02g3XTlddb9XGWHIxCCNEwEgyJtBTQIlCxm+DKuaBpZA2fgRMobHcZ5VtDth5GhYqp+PJTKmMRAsOm4CvoQZnd/geGCyFEa5BgSKSdLD1C6bsPEVp7YGXl8gWvkzXmGLKnn0/QloCoWrYeonLha5QteL1mW/mSd/H2Gkrn039CqSUBkRBC1EU61EVa0XUNa9vKuECoWuWy93GLt7aLjPKtQdOAin1xgVC1yNbVVK6ci9ert37FhBCinZFgSKQVjxumfGHqjPLlC17H1NrJKr4tzOczKF/ybsry8i/fwRMra8UaCSFE+yTBkEgvroMTCaUsdiKVqDoWFMwUynFwIqlXSHciQZSMOhei3h5++H6OO+6IOh83e/bV/OIX17d8heph8eKFPP74I21djXZPgiGRVizdh3/QpJTlgaFTsVTrL/ufjqK2IjDk8JTl/v5jsY3myeUmhDjgZz/7FbNnX9/W1QDgyy8X8cQTj7Z1Ndo9CYZEWolZkD3uODRfYtZ4PacQ/+DDMzIfTzKxmI2393CMgu4JZcr0kj/9HCpjMmZItC+uUgQth70VUYKWg6vSZ4xgJFKVm69//wH06dOvbSsjmpXMJhNpp1Ll0O3SP1P66fNUrp6HUhpZI48kd8qZVJKFZMU6oMLNpdsFv6F0/qtUfPURrhUjMHA8BTMvJGQWgNXWNRSi/myl+OeLy/hyzZ6abeOHduZHZ49Bb+Vbvjt2bOfcc0/n17/+PcuXL+Wjjz6gqKiIxx9/ltmzryYQCPDXv/4DgN27d3HXXXewZMliKisr6NSpiCOOmMl11/2s1mO89trL/PvfT7F9+zZ8Ph99+/bjuut+yvDhIwFwXZdnnnmSV175L7t27aCoqAvf+c55nH/+xUDVbb1HH30QgBkzqnrUx42bUJM6ZMmSxdx3392sWbMav9/H9OlHMnv29eTm5tXU4YknHuO1115iz57dBAIBBg4cwi9/+Rt69OgJwL333sW8eZ+yY8d2srKyGTt2PNde+1OKioqa78VOAxIMibTjOC7l5OKfeQU5R16IQhFVXsptDVl5MZ7jOJSSTWDaheRNPq1qm+6jwjJwJBAS7YibJBAC+HL1Hv75n2XMPntMm4yBu//+u5k6dQZ/+MOfcJzkvdI33/x79u7dw/XX/5yCgkJ27drJ6tUra93vkiWLufXW/+XCCy9h6tTphMNhVq5cQUVFec1j7rzzNl599SUuvfRKRowYxVdfLePee+/C6/Xyne+cx2mnncmePbt55503ufPO+wDIysoCYNWqldxww48ZP34i//u/t1JcvI/77rubb77ZwH33PYKu67zxxms89NC9fO971zBy5GgqKytYunQJlZUHxiIWF+/nkkuuoKioMyUlxfz7308xe/bVPPnkcxhGxwkhOk5LRIcTsbUOkVG+NQSjYBi5FBRkUVxcmfKiLUS6CsXshECo2per9xCK2QSM1h/ZMWjQUH71qxtrfczKlSv4wQ9+zLHHHl+z7aSTTq31OV9/vYLc3Dx+/OOf1GybNm1Gzf/ftm0rL774HD//+f/jjDPOBuCwwyYTDod59NEHOfvs79ClS1c6d+6CpmmMGjU6bv+PP/4IhYWd+Otf/1ETtHTp0o2f/nQ28+Z9xowZR7Jy5QoGDhzMJZdcUfO8I444Km4/v/7172v+v23bjBo1hrPOOpnFixdy+OFTam1jeyJjhoQQQrS5YLj2rsy6ylvKtGnT63zMkCHDeOaZJ/nvf19g69YtCeWWZdX8s+2qpUGGDh1GWVkpf/rTH1iw4HPC4XDccxYsmA/AUUcdE/f8SZMOZ9++fezatbPWOi1b9iVHHDEzrvfm8MOnkJ2dw7JlS2rqvXbtau666+8sXboEy0p8jefN+4xrrrmSE06YycyZkznrrJMB2LJlU52vS3siPUNCCCHaXMBX+9dRXeUtpaCgU52PuemmW3jggXt44IF/cvvtt9KnT19+8IMfM3PmMTVjj6p169adF154lYkTD+PGG//I88//m5/+9Fo8Hg9HHXUsP/nJz8jNzaO0tATXdTnllFlJj7lr1y46d+6Wsk7l5eUUFBQmbC8sLKS8vGr9sZNPPo1gMMgrr/yXZ599muzsbE488VR++MPZeL0+Vq5cwa9+9VOOOGIm3/3uZeTnF6KU4gc/uJxIJFrn69KeSDAkhBCizflNnfFDO/Pl6sRbZeOHdsZv6m0yZrA+k9mKior49a9/j+M4rF69kn/962F+97v/x9NPv0iXLl156KHHax5rmgeWBjnhhJM54YSTKSkp4dNPP+T//u8ODMPg//2/35Gbm4dSin/+8yFM00w4Zv/+/WutU05OLsXFxQnb9+/fT05OLgCapnHeeRdy3nkXsmfPbt59923uu+8u8vPzufzy7/Hxxx+SnZ3NH/94K9q3GaB37txR9wvSDsltsg5IKYVhZOaUal3X4v6bSYxvx1Ok0UzkjGYYOh6PLulj6km5Lj86ewzjh3aO2149m6w9LCCqaRrDh4/k+9//EbZts23bVkzTZNiwETX/Bg4clPC8/Px8Tj31TA477HA2bdoIwMSJhwFQWloa9/zqf9UDpU3TJBpN7KUZM2Ycn3zyYdytrwULPqeiopwxY8YlPL5z5y5ceOF3GThwMBs3fgNULSVgGAbqoIvK22+/0chXJ71Jz1AHYyvFjn1B5i3fQcBncMTYHmT7TbR2cCFpCl1TBNxywmuWsmfnBszug8juO5qQlo3dwbN3+LQoeqSE4NJPCcciBIZNxZPbjUrH19ZVy0gezcFjlxNaMZ9IyW58/cdidhtIkCwcp2N/DptKd11mnz2GUMwmGLYI+Az8pp7WgVBFRQU//elsTjjhZPr06YtlxXjhhefIzs5hyJBhKZ/38MP3U1pawvjxEykoKGT9+nXMnz+vZtp8nz59Ofvsc7n55t9x4YWXMGLEKCzLYsuWzXz55UL+9rc7AOjbtz+2bfPcc88wevQYsrKy6NOnH5deeiU//OGV/OIXN/Cd75zP/v1Vs8mGDx/J1KlV46D++tc/kZOTy8iRo8nJyWH58qWsX7+Ws8/+DlA1YPu5557hjjv+ypFHHs1XXy3jrbfmtPAr2jYkGOpAbKVx+9OLWLXpQNfoix+s47xZQzj+sN4dNiDSNIUvuJ0dz9yEG/t2EOLS91AeP10v+gNhfzdsu2O23a9FCS95nbLPX67ZVr74Lby9R1B46nVU2BIQtSZTc9B2rWDHS3fAt2ljKpa+i55bRNcL/0CFypbVIeqgXJeAoRHI/vZ2Upq/YB6Ph4EDB/Hii8+ya9dOvF4fw4YN54477iY/Pz/l84YNG8Fzzz3D+++/SzBY+W3PzCVcdtlVNY+5/vr/oU+fvrz88n947LGH8PsD9OnTl6OPPrbmMdOnH8FZZ53Lk08+RnHxfsaOHc/ddz/AsGHD+fvf7+b+++/ht7/9BT6fnxkzqtYZ0vWqOwejR4/llVf+y6uvvkQ4HKZHj55ce+0NnHrqmQBMnTqDH/7wWl588TnmzHmV0aPH8te//oMLLzy7RV7LtqRcN83PtDZk2w7796fO/ZROdF3jvcVbefyNVUnLb//JERT4E+87dwRZWog9T/0Gu3x/QpmR14VOF95E0Ol4aSmUgkBoBzsf/39JywtmXQFDjs6IFbsNQ6tZVqAt25ujKtj+4PUkW+TJP3gSWbN+SMRuvlvYbd3uWCzKvn076NSpe9xYmNZiGFpGnN/JZGrbq9td27lXWJjV4KESmTewooOK2A6vz92YsvzdL7bg8XTQcUTh8qSBEIBVuhst2j4C2oYyTY2KJW+nLC9fOAePHWzFGmU2TVNEd65LGggBhNYtxpT3Q4i0JMFQB+G6ta/DUV4Z7bhJLOxYrcWuVXt5e6VcFydckbLciQSR1CWtRymFE64l8HYdcDr4ADYh2ikJhjoIU1eMH9olZfmMcT2wO2iXqgrkgZ58+JsyPCh/bivXqHVYjiIwbFrKcv/A8diatxVrlNls28HbY0jKcqOgO44hY7iESEcSDHUQynW58LgheM3EW2G9umQzoEdeh53JEtUC5E//TtKy/CPOJ6p3zJQetu1g9hiaMmt93tRziNjyEW9Nti8P/+DDk5YVHn8lEdUxz0Uh2jsZQF2L9jSAGkBpivKwxZNvrmLhqt14TZ0TJvfllOn9MKjKgNxR+fUozravKfnkWazinZidepB3xAVo3YcSslt/YGdrUUqRrVVSvuB1Kpa9V5W1ftBE8o68kJBRgN0xOwMTtPVA4oNl6xHCqz+j7ItXsCtK8fYYTP4xl2BldyfqNO8E3rZutwygbjuZ2vaWGkAtwVAt2lswBFUzjFylsN2qRd8M5RKLZsY4BV3X8BHCNCBmQRg/doZEAx4DvG4I3dCIOiYhS0v3GcnNqq2DgsT6KLxOEIWLrQwirrdFembbut0SDLWdTG27zCYT9eK6gOPi1RVF+X7cDnprLBnbdogoP2ZuERGVOYEQQNSCkMrCzC0i6hoZFQilI8tyqXT8VDgBQranw96iFqKjkGBICCGEEBlNgiEhhBBCZDQJhoQQQgiq8oUdd9wRdT5u9uyr+cUvrm/5CrWw+ra3oebMeZUZMyZRUlLS7PtuKZKbTAjRrhmGhs/XsqlmNE1hGFWD0mOxzJiQIFL72c9+1eABuunotNPOZNq0GW1djbQgwZAQol3SNA3HqGRdyRYWrfmKQl8eU/tMIssMYMeaJzhSCgIqhLNvC8G1X6AH8sgePp2YmUukmafJiyp+LYZuVeJGgyhvAFvPIuSkR17FSCSM1+ujf/8BbV2VWkWjUQzDQNNqD9i6dOlKly5dW6lWDWfbNq7rYhgt/1mTT7MQol2yzAr+9Mk97KzYU7PthVVv8cMJFzK282jsWNMvb9laiD0v3EJsz+aabaVzX6Rg1pV4Bk1r9nWDMl2OHqL4zfsIfbO0Zpu//zgKTvwB5XbrJlvesWM75557Or/+9e9ZvnwpH330AUVFRTz++LPMnn01gUCAv/71HwDs3r2Lu+66gyVLFlNZWUGnTkUcccRMrrvuZ7Xu+3//91aOPnpWXNlVV11Cr169uemmP9fs+7777mb+/LmEQmGGDx/Btdf+lFGjRtY85zvfOY1p02bQtWs3/vOf59m9exevvvoO0Wik1no9/PD9/PvfT/LOO5/U7Ku8vJyHHrqXjz/+kJKSYoqKOnPsscdzzTWzax7z0ksv8uyzT7Fz5w46dSri1FPP4NJLr6w1+CorK+Xuu//BZ599TCgUZsiQoVxzzWzGjZtQ85jq1/Xoo2fx+OOPsH37Nu6//1GGDRtRz3et8eSTLIRodzxehydXvB4XCFW7b/G/ueOEQZjkNO0YBpQveC0uEKpW/O4jdO83mqhW0KRjiAP8WiwhEAL4/+3deVxU9frA8c8M+76pqCGp2AiIiIgi5oqaWvZruZVoLrmQVmZa3kIr0a6Z1591VdzBLbdKzayuGop711uGP7WU9CZpuOHCvsPM+f3BZXJkEXBY53m/Xrxeznc58zxzOMzj95w5k/v7Kdi7CodBr9XJCtGqVUsJCenJ7NkfotOVfbuOuXMjuX37FlOnTsfFxZXk5BucP59Q7jZbtGhJhw4diYuLNSiGkpL+4Pz5BMaODQcgIyODV1+dgI2NDVOn/hV7e3u2b/+CN96YxLZtu3B0dNbPPXz4AB4enrzxxnTUajU2NtbMmhVRpbgKCgp4441JXL9+nbFjw/HyasfNm8mcOXNKP2b79s9YtGghzz03jB49evHzz6dZty6arKwsJk+eWuZ2tVotb701hevXr/LKK6/j4uLG9u2fMW3aa6xYsRZvbx/92F9/TeD69WtMmDAJBwfHWlu5kmJICNHg5Cm5HLtyssw+BYUz188S0vJRCh7ghqOWulxSTsWV25974QfM/Z6gqEiuITIGs6LsUoVQidzfT+FclA1q59oNCmjXrj0REe9XOCYh4SwTJ75G//6P6duGDBla4ZwBAwaxYkUUOTnZ2NraAbB//3c4ODgSHBwCwLZtW8nKyiQ6egMuLq4AdOnSjeHDn2Xz5k955ZUp+u0VFRWxcOESbGz+XEGralx79/6TCxfOs3LlWvz8/EvN0Wq1rF8fQ//+jzF16l8B6NatO0VFRXz22SZGjXoJJyfnUts9fvwYCQln+fjjKH1uwcEhDBv2NBs3ruXDD/9XPzYjI53o6A24uzev8PUztoZ/BZgQwuToFB3aCr4BPrswB5VK9aDPglKYV26vNjeLB34KoacU5DxQf03p0ePR+47RaLzZunUTO3du58qVpFL9RUVF+h+ttvj3NjR0AEVFhRw5ckg/Li4ulr59Q7GwKF4B+/HHf9O5cxAODo76+Wq1moCAQBISzhk8R+fOXQwKocrEda/4+B9p3bqNQSF0t8uXL5GWlkZoqOGpvdDQgRQWFnLu3Nky550+fQo7Ozt9IQRgbm5Onz79OHPGsAD28nqk1gshkGJICNEAWaosaePSqtz+ju4+FBYWPdBzaFWWWHuWf62CTbsgk/w6hJqisqz4S2zv119TXFzc7jtmzpyP6NKlK6tXLycs7BlGjPgLhw8fAIqvD+rbt7v+Z9iwpwFwc2tC585B7N//HQD/+c8FLl36nYEDB+u3m56extGjhwzm9+3bne++283NmzfuG2dFcZUlPT0dN7em5fZnZmb+97lcDdpdXV3/259RzryMUnNKYs7ISC9zW7VNTpMJIRoctc6Gl/z/wuwji0t9AXGHJu1ws3ZBV/Bgz5Gns8QldAzXP50J96xCWbZoh9qpuUl93U1N05rbYdMmoPgaoXvYtAlAa24HdVB7Vmb1r0mTJsycGYlOp+P8+QQ2bFjDrFkz2LJlB82auRMT86l+7N3fozVw4GMsXDif9PQ04uJicXNrYnBBcfEpsx6Eh08q9ZzW1lb3jbOiuB56yKPUeCcnJy5e/K3cPB0dHQFITU01aE9JSdHHW9681NSUUu2pqXdwdHS6J4+6WW6VlSEhRINTVKSjubU7c/u+iU+TdqhQ4WBlzwveg5ncbQy6AusHfg5FUci3bkaLMR9h3cYfVGrU1vY49fgLbk9PJ0d58OcQf8rVWeAyeCI2bQIM2ks+TVZfPl5fEbVajY9PB8LDX0Wr1XL16hUsLCzw9vbV/3h5tdOP7907FJVKxcGDccTFxdK//0CDT2QFBXXj0qVEHn64jcE2vL19adfukQeKqyxBQcFcuvQ7Z8/+Uma/p+fDODu7cPDgfoP2Awf2YWFhga9vhzLn+fsHkJ2dzY8//lvfVlRUxJEjh/D371TpPGqSrAwJIRqkokIzXM1a8EbQSxSpijBTqbBU2ZGXa7zlg0KdiiJLdxwGv46LUoiCigK1DVkPdgZOlCNTa4PDoNdwLrnPkKUtWnM7MrX1txDKysrizTcnM2jQ43h6PkxRUSHbt3+Bvb0DGo13hXMdHYsvll6/Pobbt28ZnCIDCAt7kX379jJ58ss8/3wY7u7NSUtL5dy5szRr1pTnnx9h1LgGDXqcnTu38fbbbzB2bDht27bj1q2bnDr1f7zzzruYmZnx0kvjWbRoIS4uroSEPMrZsz+zZcunPP/88DIvngYICemJj08HPvjgfSZNmoyrqxvbt3/OnTu3GTVqXMUvcC2RYkgI0WDpdDoosMTC3BoXFztSU7ON/hyKopCntQD++4YslwnVqFydRfGnxqydixvq+ettaWmJl1c7duz4nOTkG1hZWePt7cM//rEUZ2fn+84fMGAQx44d4aGHPPDxMVxZcXJyZtWqdURHr2DFiigyMtJxcXHF19ePfv1CjR6XpaUlixatYPXq5WzcuI6MjAyaNm3GgAGD9GOeey4Mc3NzPvtsCzt3bsPNrQljx4YzenT5RY2ZmRkLFy5m2bLFLF++hLy8XDQabz75ZKnBx+rrkkq594S70NNqdaSkGP+Pa20wN1fr3xxM6SJPU80bJHdTzL2u8y4sLODOneu4ubUwuBamtpibq01qf9/NVHMvybui3z1XV7sqf12KXDMkhBBCCJMmxZAQQgghTJoUQ0IIIYQwaVIMCSGEEMKkSTEkhBBCCJMmxZAQQgghTJoUQ0IIIYQwaVIMCSGEEMKkSTEkhBBCCJMmxZAQQgghTJoUQ0IIIQSwZs0qBg7sdd9xkye/zNtvT63xeHbv/oaePYNIS0szyvZOnvyJnj2D+PXXc3UaR30kX9QqhBBCVMFbb0VU+buvqiMkpCcrV67D3t7eKNtr396blSvX8fDDbeo0jvpIiiEhhBD1hmKhJU/JIbcwF1sLW6xUNqgKzeo6LADy8/OwsrKmTZu2tfJ8Li4uuLi4VCqmyrCzs8fPr2ONxNHQSTEkhBCiXtBa5RNzcgtnkhP0bf7uPkwIHIFZvlWtxnL9+jWef/5/mDkzkp9/Ps3hwwdp0qQJn376OZMnv4ytrS0LFiwC4ObNZKKi/sGpUyfJzs7Cza0JvXr1YcqUtyrc9t/+Np9+/QYY9I0fPwoPj1bMmTOP3bu/Yd68OXz77X6cnZ0NYvrllzMcOnRAH1NWVhaffPJ3jh49jJWVFU8++TSOjk4sW7aIY8d+AopPk02ZMomYmE/x9vYFoGfPIF555XXy8vL46qsd6HRaHn20N9OmvY2NjQ1AqTgACgoKWL8+hn37vuP27Zs4O7sQFNSNd9+dDcAvv5xh48Z1/PprAtnZWXh4eBIW9iKDBz9h5D1lHFIMCSGEqHOKhbZUIQRwJjmBmJNbeDlgdJ2sEK1atZSQkJ7Mnv0hOp2uzDFz50Zy+/Ytpk6djouLK8nJNzh/PqHMsQAtWrSkQ4eOxMXFGhRDSUl/cP58AmPHht83ph49ehnENG/eHE6ePMGrr06hefPmfP31VxXGcLcdO76gU6fOvPvubJKS/mD58sW4uLjyyiuvlzvnvffeJj7+BKNGjaVDh46kpaVy+PBBff+NG9fp2LETTz/9Fywtrfj559PMn/83FEVhyJChlYqrNkkxJIQQos7lKTmlCqESZ5ITyFNysMGhlqOCdu3aExHxfoVjEhLOMnHia/Tv/5i+7X5v+AMGDGLFiihycrKxtbUDYP/+73BwcCQ4OOS+Mb377iyKiooLod9/T+TIkYO8994c/cpLcHAPRox47r75Abi5NSEyci4A3bv34MKFXzl0KK7cYujEiX/zr38dIzJyLgMHDta33/3vAQMG6f+tKAqdOnXm5s1kdu36sl4WQ/Xq02R79uzhlVdeoXfv3gQEBPDUU0+xfft2FEWpcJ6iKKxevZq+ffvi7+/PsGHDOHXqVO0ELeqVkosaa+PiRiGE8eQW5lbcX5RXS5EY6tHj0fuO0Wi82bp1Ezt3bufKlaRS/UVFRfofrVYLQGjoAIqKCjly5JB+XFxcLH37hmJhYVGlmEo+HdazZx99m1qt5tFH7//JOICuXYMNHrdu3YZbt26WO/6nn05gbW1tUPDcKyMjg0WL/pe//GUofft2p2/f7nz99U6Ski5XKqbaVq/eMdavX4+NjQ0RERGsWLGC3r178/7777Ns2bIK50VHR7NkyRJeeuklVq1aRdOmTRk3bhxJSaV/KUXjZKZW4aDKQnfhMLe+XY7uP0exV2VhVj+uuxRC3IeNhU3F/eaVu0jY2Fxc3O47Zs6cj+jSpSurVy8nLOwZRoz4C4cPHwCKrw8qKQb69u3OsGFPA8WrMZ07B7F//3cA/Oc/F7h06XeD1ZXKxnT79m3Mzc1Lfdqrshc929sbrrhZWFhQUFBQ7viMjHTc3JqgUqnKHTNv3mz27/+O4cNH8sknS4mJ+ZQnnvifCrdbl+rVabIVK1bg6uqqfxwSEkJaWhrr1q3j1VdfRa0uXbvl5+ezatUqxo0bx0svvQRAly5dGDx4MGvWrGH27Nm1FL2oK2q1Cuuca1zfOgel8L//ezwdh8rSBvcRs8mzaY5WW/HqohCiblmrbPF39ynzVJm/uw/WKts6iAoqeL/Xa9KkCTNnRqLT6Th/PoENG9Ywa9YMtmzZQbNm7sTEfKofa2Fhqf/3wIGPsXDhfNLT04iLi8XNrQkBAYFVjqlJkyYUFRWRlZVlUBClpqbeP/hqcHR04s6d2yiKUmZBlJ+fz7/+dYzJk6fx3HNh+vb7neWpS/VqZejuQqiEj48PWVlZ5OTklDnn5MmTZGVlMWTIEH2bpaUlAwcO5MiRIzUWq6g/bMjh1s7//bMQ+i+lIJfbOz/GSin7d0cIUX+oCs2YEDgCf3cfg3Z/dx/CA0fUm4/XV0StVuPj04Hw8FfRarVcvXoFCwsLvL199T9eXu3043v3DkWlUnHwYBxxcbH07z+wzP/030/79sWv2dGjh/RtOp2O778/+oAZlS0oqBt5eXkcOLCvzP7CwkJ0Op3B6b6cnGyOHau/78n1amWoLPHx8bi7u5d7s6fExEQA2rY1vO+Dl5cXGzZsIC8vD2vr6i+vmpvXq3qx0kzp2hlVbibazJQy+4rSb6IuyMbc2q6Wo6p9prTP72Wqudd13jpdJZZNqsAs34qXA0YX32eoKA8bc2usVbao8ksXQiULEioV1OWCQ1ZWFm++OZlBgx7H0/NhiooK2b79C+ztHdBovCuc6+hYfLH0+vUx3L59q1KnyKB07m3betG7dz8WL15Ifn4e7u4t+PrrnRQU5Fd4Kqu6unYNJiTkUT766AOuXr2Cr68fGRkZHDoUxwcffIS9vT0+Pr5s2rQeZ2dnzMzM2bRpPXZ29qSllf23ujLuzruEmZnKKO/T9boY+umnn9i9ezfvvPNOuWMyMjKwtLTEysrwHhSOjo4oikJ6enq1iyG1WoWLS8N+E3V0rPg8fGOQl6OtsF+laBv8fqwKU9jn5THV3Osq77w8M27fVhvtDQkARY0FTjiYO/33MRW+UxmzEFSri99lzc3VBoXmvbmpVCpUquJxtrbWtGv3CF9++QU3btzAysoKHx8flixZTpMmpc923GvQoCEcO3YEDw8POnY0vCHin/GoDGIqWT26O/f335/NwoXzWbZsMZaWVjz++FDatWvH9u2f6+MvL6d799/dr0NZcQDMn7+QNWtW8/XXX7J27WpcXd0IDu6u7//gg3n8/e8f8uGHs3FycuaFF8LIyclhy5aND/y7YmZW/DunVqtxcrJ9oAWPEiqlnp7Eu3HjBs8//zxeXl6sXbu23KXDFStWsHz5cn7++WeD9r179/LGG29w5MgR3N3dqxWDVqsjI6PiTzjUV2ZmahwdbcjIyEWrLfveGI2FjS6Da9FTQVtUqk9lbkmLCf8gV137H8mtbaa0z+9lqrnXdd4FBfncvHkNN7cWBtfC1AaVqjh/rVZXpytDdaGyub/2WjhqtZqoqFW1F1wNujvvgoIC7ty5TrNmLbG0vHcxxKbKRXK9XBnKyMggPDwcZ2dnoqKiKjyH6ujoSEFBAfn5+QarQxkZGahUKpycnB4olpL7ODRUWq2uwedwP/lmtjg/+hxpRz4r1efcaxj5attG/xrczRT2eXlMNfe6yrsuP5hQUgSYWiEEZed+6FAcyck3aNu2Hfn5eezbt5fTp/+PefMW1k2QNaCsvLVaxSi/+/WuGMrLy2PixIlkZmby+eef4+BQ8f/oS64V+v333/H2/vP8bGJiIi1btjTK8pmo3wq0amw6hNLEuTlpRz+nKPUGFm4tceoVhrpFe3KLjH/OXAgh6hMbG1u++243SUlJFBUV4unZmlmz/kbv3n3rOrQGoV4VQ0VFRUydOpXExEQ2b95cqdNbgYGB2Nvbs2fPHn0xVFhYSGxsLL17967pkEU9kau1xOyhQJqE+WBhDoVFkIeNSZ0yEUKYruDgkPveuVqUr14VQ3PmzOHgwYNERESQlZVlcBdpX19fLC0tGTNmDNeuXWPfvuKP9FlZWTFx4kSioqJwdXVFo9GwdetW0tLSGD9+fB1lIuqCVqsj39wGW0c7slKz0Zrg6RIhhBBVV6+Koe+//x6A+fPnl+qLi4vDw8MDnU6nv515ifDwcBRFYe3ataSkpODj48OaNWto1apVrcQthBCmrJ5+Dkc0Ysb+nau3nyarD7RaHSkp2XUdRrWYm6txcbEjNTXbpC4oNdW8QXI3xdzrOm+dTsvNm1ewt3fB3t6x1p/f3FxtUvv7bqaae0neWVkZZGWl0qxZq1IfsnJ1tWscnyYTQghR/6nVZtjY2JOVVfy1D5aWVjVyk7/y6HQqk/2qHVPNXaeDnJw8srJSsbGxr9Ydu8sixZAQQohqc3QsvrFgSUFUm9RqNTqd6a2OgOnmXpK3jY29/nfPGKQYEkIIUW3F93Nzw8HBBW0ZNz6tKWZmKpycbElPzzG5FRJTzb0k7+zsAqN/FYwUQ0IIIR6YWq1Gra69u1Cbm6uxtrYmN1drctfOmGrud+dt7FUx0/pWQyGEEEKIe0gxJIQQQgiTJsWQEEIIIUyaFENCCCGEMGly08UKKIqCTtdwXx4zM7VJfjeXqeYNkrsp5m6qeYPkboq5VyZvtVpV5ftdSTEkhBBCCJMmp8mEEEIIYdKkGBJCCCGESZNiSAghhBAmTYohIYQQQpg0KYaEEEIIYdKkGBJCCCGESZNiSAghhBAmTYohIYQQQpg0KYaEEEIIYdKkGBJCCCGESZNiSAghhBAmTYohIYQQQpg0KYaEEEIIYdLM6zoA8WCys7MZMmQIycnJbN++nY4dO5Y7NjQ0lKtXr5ZqP3PmDFZWVjUZplF8+eWXzJgxo1R7eHg406dPL3eeoihER0ezZcsWUlJS8PHxYcaMGQQEBNRgtMZT3bwb+v6+286dO9mwYQMXL17E1taWjh07snTpUqytrcuds23bNmJiYrh27Rpt2rRh2rRp9OvXrxajfnBVzXvUqFH8+OOPpdp3796Nl5dXTYdrFOXlAPDJJ5/wxBNPlNnX0I9zqH7ujeFYj4uLY+XKlfz222/Y2dnRpUsXpk+fTqtWrSqcZ6z9LsVQA7d8+XK0Wm2lxw8aNIhx48YZtFlaWho7rBoVExODg4OD/rG7u3uF46Ojo1myZAnTp0+nffv2bN68mXHjxrFr1677Hmj1SVXzhsaxv1esWEF0dDSTJk0iICCA1NRUjh8/XuHv/T//+U/ef/99Jk2aRPfu3dm9ezeTJ09m8+bNDebNsTp5AwQGBvLOO+8YtHl4eNRkqEYVGRlJVlaWQduGDRuIjY0lJCSk3HmN4Tivbu7QsI/1H374gcmTJ/P0008zbdo00tLSWLx4MePGjeObb76p8D89RtvvimiwfvvtNyUgIEDZunWrotFolDNnzlQ4vl+/fsqcOXNqKTrj27Fjh6LRaJQ7d+5Uek5eXp4SGBiofPzxx/q2/Px8pV+/fkpkZGQNRGl81clbURr+/lYURbl48aLi6+urHDp0qErzHnvsMeXNN980aBs2bJgyYcIEY4ZXY6qb98iRI5WXX365hqKqO6GhoUp4eHi5/Y3hOC/P/XJXlIZ/rL///vtKaGiootPp9G3Hjx9XNBqNcuLEiXLnGXO/yzVDDdjcuXMJCwujTZs2dR1KvXXy5EmysrIYMmSIvs3S0pKBAwdy5MiROoxMVMaXX36Jh4cHffr0qfScpKQkLl26ZLDPAR5//HGOHz9OQUGBscM0uurk3VidPHmSK1eu8OSTT1Y4pjEe55XJvTEoKirCzs4OlUqlbytZBVcUpdx5xtzvUgw1UHv37uXChQu89tprVZr3zTff4OfnR+fOnQkPD+f8+fM1FGHNGTp0KD4+PvTv359Vq1ZVeNogMTERgLZt2xq0e3l5ce3aNfLy8mo0VmOqSt4lGvr+Pn36NBqNhuXLlxMSEoKfnx9hYWGcPn263Dkl+/ze/yR4eXlRWFhIUlJSjcZsDNXJu8SPP/5IQEAAHTt2ZOTIkZw4caIWIq453377Lba2tvTv37/cMY3pOL9bZXIv0ZCP9WeffZaLFy+yefNmMjMzSUpK4pNPPsHX15fAwMBy5xlzv8s1Qw1Qbm4u8+fPZ9q0adjb21d6XmhoKP7+/rRs2ZKkpCRWrlzJiBEj+OqrrxrEOfWmTZvy+uuv06lTJ1QqFQcOHGDRokUkJycza9asMudkZGRgaWlZ6iJCR0dHFEUhPT29wvPR9UF18oaGv78Bbt26xS+//MKFCxeIjIzExsaGlStXMm7cOGJjY3Fzcys1Jz09HSjex3creVzSX59VJ2+Arl278tRTT9G6dWtu3rzJmjVrGDt2LBs3bqRz5861nMWDKyoqYs+ePYSGhmJra1vuuMZwnN+rsrlDwz/Wg4KCWLp0KW+99RYffPABAD4+PsTExGBmZlbuPKPu9yqdVBP1wscff6w8++yz+vOr//73vyt1zdC9kpOTlcDAwAZ9Tn3+/PmKj4+PkpycXGb/8uXLFT8/v1Lte/bsUTQajXLjxo2aDrFG3C/vsjTE/f3YY48pGo1GSUhI0LelpqYqnTt3VhYtWlTmnF27dikajUa5efOmQfuZM2cUjUajxMfH12jMxlCdvMuSnZ2t9OvXr8FcK3WvQ4cOKRqNRjlw4ECF4xrjcV7Z3MvS0I71+Ph4JSgoSPnoo4+U48ePK3v27FGefPJJ5ZlnnlFyc3PLnWfM/S6nyRqYq1evsnbtWqZMmUJmZiYZGRnk5OQAkJOTQ3Z2dqW31axZM7p06cLZs2drKtwaN2TIELRaLQkJCWX2Ozo6UlBQQH5+vkF7RkYGKpUKJyen2gjT6O6Xd1ka4v52dHTE2dkZb29vfZuzszO+vr789ttvZc4p2aeZmZkG7RkZGQb99Vl18i6Lra0tffr0aVD7/G7ffvstzs7O9OzZs8JxjfE4r2zuZWlox/rcuXPp3r07ERERdO/encGDB7N69WrOnTvHrl27yp1nzP0uxVADc+XKFQoLC3n55Zfp2rUrXbt2ZdKkSQCMHj2asWPH1nGE9UvJueTff//doD0xMZGWLVs2uKVzU9OuXbty++79A1iiZJ+XXE9QIjExEQsLiwZx2qA6eTc2eXl57N+/n8GDB2NhYVHh2MZ2nFcl98bg4sWLBoU/QPPmzXFxceGPP/4od54x97sUQw2Mj48Pn376qcFPyQ355syZQ2RkZKW3lZycTHx8fIU3aqzvdu/ejZmZGb6+vmX2BwYGYm9vz549e/RthYWFxMbG0rt379oK0+jul3dZGuL+7tevH2lpaQYrYKmpqZw9e5YOHTqUOadVq1a0bt2avXv3GrTv3r2bkJCQBnHvlerkXZacnBwOHTrUoPZ5iQMHDpCTk1OpT1I1tuO8KrmXpaEd6y1btuTcuXMGbVevXiU1NZWHHnqo3HnG3O9yAXUD4+joSHBwcJl9HTp00P+hHDNmDNeuXWPfvn1A8ZLrwYMH6dOnD82aNSMpKYnVq1djZmbWYFaTxo8fT3BwMO3btweK71j6xRdfMHr0aJo2bQqUztvKyoqJEycSFRWFq6srGo2GrVu3kpaWxvjx4+ssl6qoTt6NYX8DDBgwgI4dOzJlyhSmTZuGlZUVq1evxtLSkhEjRgAwc+ZMvvrqK4M/pq+//jrTp0/H09OT4OBgdu/ezZkzZ9i0aVNdpVIl1cn7p59+IiYmhoEDB/LQQw9x8+ZN1q1bx61bt1i8eHFdplMt33zzDS1btqRLly6l+hrjcX63quTeGI71sLAw5s2bx9y5cwkNDSUtLY0VK1bg5uZm8LH5mtzvUgw1UjqdzuCj1x4eHty8eZN58+aRmZmJg4MD3bt3Z8qUKQ3itAEUf1R6x44d3LhxA51OR+vWrZk5cyajRo3Sj7k3byj+2gpFUVi7dq3+du1r1qxp1Hk3hv0NoFarWb16NR999BGzZs2isLCQoKAgNm/erC8Ey9rnQ4cOJTc3l+joaFavXk2bNm1YunRpg/lEVXXybtq0KYWFhfzjH/8gLS0NGxsbOnfuzJw5c/D396+rVKolPT2do0ePMmbMGIN7z5RojMd5iarm3hiO9dGjR2NpacnWrVvZsWMHdnZ2BAQEsGjRIlxcXPTjanK/qxSlgjsaCSGEEEI0cnLNkBBCCCFMmhRDQgghhDBpUgwJIYQQwqRJMSSEEEIIkybFkBBCCCFMmhRDQgghhDBpUgwJIYQQwqRJMSSEEEIIkybFkBCiURg1apTBXblrak5diIqKon379qSkpNR1KEI0SlIMCSFEPbFy5Ur2799f12EIYXKkGBJCiHpi1apVUgwJUQekGBJCCCGESZNiSAhRaVlZWXz44YeEhobi5+dHSEgIY8eO5ezZs/oxp0+fZvz48XTp0oVOnToxcuRI4uPjDbZTcg3MxYsXeeONNwgMDCQ4OJi5c+eSn59vMHbHjh2MHj2akJAQ/Pz8ePzxx9myZUuN5VhQUMCSJUsYOHAgfn5+9OnThwULFlBQUGAwrn379nzwwQfs37+foUOH4ufnxxNPPMGRI0dKbfOHH37g2WefpWPHjgwYMIDPPvtM/xrcvb2cnBx27txJ+/btad++PREREQbbyczMJCIigqCgILp06cKMGTPIzc2tmRdCCBNiXtcBCCEajsjISL777jtGjhyJl5cXaWlpxMfHc/HiRTp06MDx48cJDw/Hz8+PyZMno1Kp+PLLLxkzZgxbtmzB39/fYHtTp07loYce4q233uLUqVNs3LiRjIwMFixYoB+zdetWHnnkEUJDQzE3N+fgwYPMmTMHRVF48cUXjZqfTqfjlVdeIT4+nhdeeAEvLy8uXLjAhg0buHTpEsuXLzcYHx8fT2xsLCNGjMDOzo6NGzcyZcoUDh48iIuLCwDnzp1jwoQJNG3alNdffx2dTseyZctwdXU12NaCBQt477338Pf354UXXgDA09Oz1Ovl4eHBm2++yblz59i2bRuurq789a9/NerrIITJUYQQopK6dOmizJkzp8w+nU6nPPbYY8q4ceMUnU6nb8/NzVVCQ0OVsWPH6tuWLFmiaDQaZdKkSQbbmD17tqLRaJSEhASD+fcaN26c0r9/f4O2kSNHKiNHjqxSPvfO+eqrrxRvb2/lxIkTBuO2bt2qaDQaJT4+Xt+m0WiUDh06KJcvX9a3JSQkKBqNRtm4caO+beLEiUqnTp2UGzdu6NsuXbqk+Pr6KhqNxuB5AgIClHfeeadUnCWv14wZMwzaX3vtNaVbt25VylkIUZqcJhNCVJqjoyOnT58mOTm5VF9CQgKXLl3iySefJDU1lZSUFFJSUsjJySEkJIQTJ06g0+kM5ty7sjNy5EgAg1NN1tbW+n9nZmaSkpJCt27dSEpKIjMz05jpsXfvXry8vGjbtq0+/pSUFLp37w4Un+66W48ePQxWb7y9vbG3tycpKQkArVbL8ePH6d+/P+7u7vpxDz/8ML169apyfGFhYQaPg4KCSEtLIysrq8rbEkL8SU6TCSEqbfr06URERNC3b186dOhAnz59ePrpp2nVqhWXLl0C4J133il3fmZmJk5OTvrHDz/8sEG/p6cnarWaK1eu6Nvi4+OJiori1KlTpa6PyczMxMHBwQiZFbt8+TIXL14kJCSkzP47d+4YPG7RokWpMU5OTmRkZOjH5+XllcoTSudeGS1btjR47OjoCEB6ejr29vZV3p4QopgUQ0KISnv88ccJCgpi3759fP/996xZs4bo6GiioqJQFAWAt99+Gx8fnzLn29raVrh9lUpl8PiPP/7gpZdeom3btkRERNCiRQssLCw4fPgw69evL7XS9KB0Oh0ajYYZM2aU2d+8eXODx2ZmZmWOK3ktjE2tLnsxv6aeTwhTIcWQEKJKmjVrxosvvsiLL77InTt3eOaZZ1i5cqW+gLC3t6dHjx6V2tbly5dp1aqVwWOdToeHhwcABw4coKCggBUrVhisitx7uspYPD09+fXXXwkJCSlVmFWHm5sbVlZWXL58uVRfWW1CiLoh1wwJISpFq9WWukbHzc2NZs2aUVBQgJ+fH56enqxdu5bs7OxS88v6KonNmzcbPN60aRMAvXv3Bv5cebl75SMzM5MdO3Y8WDLlGDJkCMnJyXzxxRel+vLy8sjJyanS9szMzOjRowdxcXEG11ldvnyZo0ePlhpva2urP8UmhKg9sjIkhKiU7Oxs+vTpw6BBg/D29sbW1pZ//etf/Pzzz0RERKBWq5k7dy7h4eEMHTqUZ599Fnd3d5KTk/nhhx+wt7dn5cqVBtu8cuUKkyZNolevXpw6dYqvv/6aoUOH4u3tDcCjjz6KhYUFkyZNIiwsjOzsbLZt24abmxu3bt0yeo5PPfUUe/bsITIykh9++IHAwEC0Wi2JiYns3buXmJgYOnbsWKVtTp48mWPHjjF8+HCGDx+OTqdj06ZNPPLIIyQkJBiMLbk9wbp162jWrBkeHh506tTJmCkKIcogxZAQolKsra0ZPnw433//PbGxsSiKgqenJ5GRkYwYMQKA4OBgPv/8c5YvX86mTZvIycmhadOm+Pv7M2zYsFLbXLRoEYsXL+bjjz/G3NyckSNH8vbbb+v727Zty5IlS1i0aBF///vfadKkCcOHD8fV1ZWZM2caPUe1Ws2yZctYv349u3btYt++fdjY2ODh4cGoUaNo06ZNlbfp5+dHdHQ0CxYsYPHixbRo0YIpU6aQmJhIYmKiwdiIiAhmzZrFokWLyMvL45lnnpFiSIhaoFLkyjshRC2Liopi6dKlHD9+vNTNB03Fq6++ym+//UZsbGxdhyKEyZNrhoQQoobl5eUZPL506RJHjhyhW7dudRSREOJucppMCNHopKSkoNVqy+23sLDA2dm51uIZMGAAzzzzDK1ateLq1at89tlnWFhYMGHChFqLQQhRPimGhBCNznPPPcfVq1fL7e/WrRsbN26stXh69erFP//5T27duoWlpSUBAQG8+eabtG7dutZiEEKUT64ZEkI0OvHx8eTn55fb7+joiJ+fXy1GJISoz6QYEkIIIYRJkwuohRBCCGHSpBgSQgghhEmTYkgIIYQQJk2KISGEEEKYNCmGhBBCCGHSpBgSQgghhEmTYkgIIYQQJu3/AWXPVxMJMNArAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "iris.replace({'species':{'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2}}, inplace = True)"
      ],
      "metadata": {
        "id": "kDXEiFtbokRH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split"
      ],
      "metadata": {
        "id": "dpeN4nCEo0Dn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x = iris.drop(columns='species', axis= 1 )"
      ],
      "metadata": {
        "id": "GMIjUgXgo3lC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "y = iris['species']"
      ],
      "metadata": {
        "id": "fWzsXRluqawY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25, random_state=4)"
      ],
      "metadata": {
        "id": "IxClKRsCqcNB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LogisticRegression\n",
        "LR = LogisticRegression()"
      ],
      "metadata": {
        "id": "BAJu--6zq2UX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "LR.fit(x_train,y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 214
        },
        "id": "LjMqZN3Ark0d",
        "outputId": "a71aa634-fa39-4c65-b1cb-7de74dedd7db"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/linear_model/_logistic.py:458: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
            "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
            "\n",
            "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
            "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
            "Please also refer to the documentation for alternative solver options:\n",
            "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
            "  n_iter_i = _check_optimize_result(\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LogisticRegression()"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report"
      ],
      "metadata": {
        "id": "q9Qp3aB2rqKi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = LR.predict(x_test)\n",
        "acc_LR = accuracy_score(y_pred, y_test)\n",
        "print(acc_LR)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i8ivws74sPwh",
        "outputId": "63f4a4df-6c42-440a-88da-e15abd20a67b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.9736842105263158\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn import metrics"
      ],
      "metadata": {
        "id": "avmq-vv8sStH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "score = round(LR.score(x_test, y_test)*100,2)\n",
        "score"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S4WXin8CsjDw",
        "outputId": "59bcaf84-f565-4885-992a-6144181062e8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "97.37"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cls_report = classification_report(y_pred, y_test)"
      ],
      "metadata": {
        "id": "MFCiw3PBsnS2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('accuracy score for the logistic regression model is:', score)\n",
        "\n",
        "print('classification report for our model is:', cls_report)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NwEP-Pxwsove",
        "outputId": "7b42abfb-72e7-4b3a-b326-acddda59be9a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "accuracy score for the logistic regression model is: 97.37\n",
            "classification report for our model is:               precision    recall  f1-score   support\n",
            "\n",
            "           0       1.00      1.00      1.00        18\n",
            "           1       0.88      1.00      0.93         7\n",
            "           2       1.00      0.92      0.96        13\n",
            "\n",
            "    accuracy                           0.97        38\n",
            "   macro avg       0.96      0.97      0.96        38\n",
            "weighted avg       0.98      0.97      0.97        38\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.svm import SVC"
      ],
      "metadata": {
        "id": "PVINDsb9stEC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "svc = SVC()\n",
        "svc.fit(x_train,y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 75
        },
        "id": "kp6NTPyYsz71",
        "outputId": "01090cf3-08ef-4fb6-8317-6e5f7d92ce90"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "SVC()"
            ],
            "text/html": [
              "<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>SVC()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">SVC</label><div class=\"sk-toggleable__content\"><pre>SVC()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred_svc = svc.predict(x_test)\n",
        "acc_svc = accuracy_score(y_pred_svc,y_test)\n",
        "score_svc = round(svc.score(x_test, y_test)*100,2)\n",
        "score_svc"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E15vXS6ds9Ki",
        "outputId": "d445ebe6-9d3e-486e-e8d1-c6cba9477144"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "97.37"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cls_svc = classification_report(y_pred_svc, y_test)"
      ],
      "metadata": {
        "id": "CN6EUI3mtOz_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('accuracy score of svc model is :', acc_svc)\n",
        "print('classification report of svc model is:', cls_svc)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Mn3qMsLNtSdX",
        "outputId": "80e688fd-6bfb-4151-c8f8-1d71ce5fb540"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "accuracy score of svc model is : 0.9736842105263158\n",
            "classification report of svc model is:               precision    recall  f1-score   support\n",
            "\n",
            "           0       1.00      1.00      1.00        18\n",
            "           1       0.88      1.00      0.93         7\n",
            "           2       1.00      0.92      0.96        13\n",
            "\n",
            "    accuracy                           0.97        38\n",
            "   macro avg       0.96      0.97      0.96        38\n",
            "weighted avg       0.98      0.97      0.97        38\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(x)\n",
        "print(y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AGewZAY5tU9Y",
        "outputId": "2991c5ae-d47e-43d8-8df2-5e1fb5a74d3f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     sepal_length  sepal_width  petal_length  petal_width\n",
            "0             5.1          3.5           1.4          0.2\n",
            "1             4.9          3.0           1.4          0.2\n",
            "2             4.7          3.2           1.3          0.2\n",
            "3             4.6          3.1           1.5          0.2\n",
            "4             5.0          3.6           1.4          0.2\n",
            "..            ...          ...           ...          ...\n",
            "145           6.7          3.0           5.2          2.3\n",
            "146           6.3          2.5           5.0          1.9\n",
            "147           6.5          3.0           5.2          2.0\n",
            "148           6.2          3.4           5.4          2.3\n",
            "149           5.9          3.0           5.1          1.8\n",
            "\n",
            "[150 rows x 4 columns]\n",
            "0      0\n",
            "1      0\n",
            "2      0\n",
            "3      0\n",
            "4      0\n",
            "      ..\n",
            "145    2\n",
            "146    2\n",
            "147    2\n",
            "148    2\n",
            "149    2\n",
            "Name: species, Length: 150, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "LR.predict([[6.7, 3.0, 5.2, 2.3]])\n",
        "svc.predict([[6.7, 3.0, 5.2, 2.3]])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oFb0rDJgtYTW",
        "outputId": "d1aa9c90-2dd2-4aad-bf2e-f71cf9af10c0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names\n",
            "  warnings.warn(\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but SVC was fitted with feature names\n",
            "  warnings.warn(\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([2])"
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ]
    }
  ]
}