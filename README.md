# MaskWatchCV

## Overview

MaskWatchCV is a computer vision project designed to detect face masks using deep learning techniques. This repository contains code for training and evaluating the model, as well as for deploying the model through a Flask-based web application.

## Project Structure

```
MaskWatchCV/
├── model/
│   └── saved_model.h5
├── scripts/
│   └── train_model.py
│   └── evaluate_model.py
├── app/
│   └── app.py
├── .gitignore
├── .gitattributes
├── requirements.txt
├── README.md
└── LICENSE
```

## Setup

### Prerequisites

- Python 3.x
- Git
- Git LFS (Large File Storage)

### Clone the Repository

```bash
git clone https://github.com/Vardhani30/MaskWatchCV.git
cd MaskWatchCV
```

### Install Dependencies

Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Configure Git LFS

Ensure Git LFS is installed and configured:

```bash
git lfs install
git lfs track "*.h5"
```

This will set up Git LFS to handle large files like `.h5` files.

### Ignore Large Files

Add `saved_model.h5` to `.gitignore` to prevent it from being tracked by Git:

1. Open `.gitignore`:

   ```bash
   notepad .gitignore
   ```

2. Add the following line:

   ```
   # Ignore the saved_model.h5 file
   model/saved_model.h5
   ```

3. Save the file.

4. Remove the file from Git tracking:

   ```bash
   git rm --cached model/saved_model.h5
   ```

5. Commit the changes:

   ```bash
   git add .gitignore
   git commit -m "Ignore saved_model.h5 and remove it from tracking"
   ```

### Running the Project

#### Training the Model

To train the model, run the training script:

```bash
python scripts/train_model.py
```

#### Evaluating the Model

To evaluate the model, run the evaluation script:

```bash
python scripts/evaluate_model.py
```

#### Running the Flask App

To start the Flask application, run:

```bash
python app/app.py
```

The application will be available at `http://localhost:5000`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

