import os
from roboflow import Roboflow
from ultralytics import YOLO

def download_dataset():
    api_key = os.getenv("ROBOFLOW_API_KEY")
    if not api_key:
        raise ValueError("Please set the ROBOFLOW_API_KEY environment variable")

    rf = Roboflow(api_key=api_key)
    project = rf.workspace("upi-awhgd").project("train-7-pose")
    version = project.version(1)

    dataset = version.download("folder")  
    return dataset.location


def train_model(data_path):
    model = YOLO("yolo11m-cls.pt")

    results = model.train(
        data=data_path,
        epochs=20 # Puedes usar 5 para probar 
    )

    return results


def predict(model_path, image_path):
    model = YOLO(model_path)
    results = model(image_path)

    for r in results:
        r.show()


if __name__ == "__main__":
    # Descargar dataset
    data_path = download_dataset()

    # Entrenar modelo
    train_model(data_path)

    # Ruta del mejor modelo entrenado
    model_path = "runs/classify/train/weights/best.pt" # Esta ruta se genera al ejecutar el código

    # Hacer predicción (cambia esta ruta a una imagen tuya)
    image_path = os.path.join(data_path, "test")

    predict(model_path, image_path)