# Genre Classification Project

This project focuses on classifying music genres using various machine learning techniques.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2. **Create a new Conda environment:**
    ```sh
    conda create --name genre_classification python=3.9
    conda activate genre_classification
    ```

3. **Install necessary packages:**
    ```sh
    conda install numpy matplotlib pandas scikit-learn jupyter
    ```

4. **Verify the installation:**
    Open the Python interpreter or a Jupyter notebook and try importing the installed packages:
    ```python
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    from sklearn.model_selection import train_test_split
    ```

5. **Run the project:**
    Open your project in Visual Studio Code:
    ```sh
    code .
    ```
    Make sure your Python interpreter is set to the Conda environment you just created. You can do this by opening the Command Palette (Ctrl+Shift+P) and selecting `Python: Select Interpreter`, then choosing `genre_classification`.

## Usage

To use the genre classification model, follow these steps:

1. **Prepare your dataset** and ensure it is in the correct format.
2. **Run the preprocessing script** to clean and prepare the data.
3. **Train the model** using the training script provided.
4. **Evaluate the model** using the evaluation script to check its performance.
5. **Classify new data** by running the prediction script.

Detailed instructions for each step can be found in the corresponding script files.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
