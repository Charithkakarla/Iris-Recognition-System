# Iris Recognition System

A Python desktop application that compares a selected iris image with the
images in the training dataset. The application uses OpenCV to detect the
pupil and iris, unwraps the iris into a normalized representation, generates
an iris code with Gabor filters, and selects the image with the lowest code
similarity score.

## Features

- Pupil and iris detection with the Hough Circle Transform
- Gamma correction, grayscale conversion, and median filtering
- Polar iris normalization
- Gabor-filter-based iris-code generation
- Similarity comparison against the dataset
- Visual display of segmentation, normalization, and matching results

## Requirements

- Windows, macOS, or Linux
- Python 3.10 or newer
- A desktop session with Tkinter support
- The Python packages listed below:
  - `opencv-python`
  - `matplotlib`
  - `numpy`
  - `scikit-image`

## Project structure

```text
.
├── app.py              # Application entry point
├── util.py             # Iris processing and comparison functions
├── train/
│   ├── eye/            # Iris images searched by the application
│   └── noeye/          # Additional dataset images
└── output/             # Existing generated image artifacts
```

The application searches `train/eye` by default.

## Setup on Windows

Open PowerShell in the project directory and create a virtual environment:

```powershell
py -3 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation for the current user, run PowerShell as your
normal user and execute:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate the environment again and install the dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install opencv-python matplotlib numpy scikit-image
```

## Run the application

From the project directory, with the virtual environment activated:

```powershell
python app.py
```

The application opens a file picker rooted at `train/eye`. Select an image to
start the comparison. It then displays the selected image, the best match,
the similarity score, the execution time, and the segmentation/normalization
steps.

If the environment is not activated, use the virtual-environment interpreter
directly:

```powershell
.\.venv\Scripts\python.exe app.py
```

## Dataset filename format

The query-image validation in `app.py` expects a filename with three
underscore-separated parts, for example:

```text
001_1_001.jpg
```

The first part is treated as the individual ID. The bundled dataset currently
contains files such as `1-543.JPG`, which do not satisfy this validation. Rename
or copy a query image to the expected format before running the application, or
update the filename validation in `app.py` if the existing dataset naming
scheme should be supported directly.

## Processing pipeline

1. Load the selected image.
2. Apply gamma correction and preprocessing.
3. Detect the pupil and iris boundaries.
4. Unwrap the annular iris region into polar coordinates.
5. Encode the normalized iris using Gabor filters.
6. Compare the query code with each image in `train/eye`.
7. Display the lowest-distance match and processing details.

## Troubleshooting

### `ModuleNotFoundError`

Make sure the virtual environment is active and install the dependencies:

```powershell
python -m pip install opencv-python matplotlib numpy scikit-image
```

### No file picker or image windows appear

Run the application in a local desktop session. Tkinter and OpenCV display
windows may not work in a headless terminal, remote shell, or some notebook
environments.

### No suitable match is found

Confirm that the query image is readable, that the iris is visible, and that
the dataset is present in `train/eye`. The application compares against all
supported `.jpg`, `.jpeg`, and `.png` files in that folder.

## License

No license file is currently included in this repository.
