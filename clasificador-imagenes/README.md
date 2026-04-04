# 🧠 Image Classifier with YOLO

This project implements an image classification model using YOLO and a custom dataset from Roboflow. It allows training a model and making predictions on new images.

---

## 🚀 Features

* Train a YOLO classification model
* Download dataset automatically from Roboflow
* Run predictions on custom images
* Organized project structure for reproducibility

---

## 🛠️ Tech Stack

* Python
* Ultralytics YOLO
* Roboflow
* OpenCV

---

## 📊 Dataset

This project uses a dataset hosted on Roboflow.

To use it:

1. Create an account on Roboflow
2. Get your API key from your profile
3. Set it as an environment variable

I use this dataset: https://universe.roboflow.com/upi-awhgd/train-7-pose

---

## 🔑 Setup API Key

### Windows (PowerShell)

```
$env:ROBOFLOW_API_KEY="your_api_key"
```

### Mac/Linux

```
export ROBOFLOW_API_KEY="your_api_key"
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/your-username/Computer-Vision-projects.git
cd Computer-Vision-projects/clasificador-imagenes_YOLO
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🏋️ Training the Model

Run:

```
python train.py
```

This will:

* Download the dataset
* Train the YOLO model
* Save results in `runs/`

---

## 🔍 Inference

After training, the model will be saved in:

```
runs/classify/train/weights/best.pt
```

You can modify `train.py` to test predictions on your own images.

---

## 📈 Results

(Pendiente)

```
Pendientesresults/example.jpg
```

---

## ⚠️ Notes

* The dataset is not included in this repo (downloaded automatically)
* The API key is required but **not stored in this project**
* Large files (models, datasets) are ignored using `.gitignore`
