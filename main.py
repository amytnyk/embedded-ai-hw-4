import os

from roboflow import Roboflow
from roboflow.core.dataset import Dataset
from ultralytics import YOLO


def download_dataset():
    return (Roboflow(api_key=os.environ.get('ROBOFLOW_API_KEY')).workspace("hubert-ang-usedk")
            .project("vehicle-detection-using-drone").version(2).download("yolov8", "datasets"))


def train(dataset: Dataset, **kwargs):
    model = YOLO("yolov8n.yaml")  # "runs/detect/train9/weights/last.pt"

    results = model.train(data=f"{dataset.location}/{dataset.name}-{dataset.version}/data.yaml", **kwargs)
    print(results)


def main():
    train(download_dataset(), epochs=100, imgsz=640, resume=True)


if __name__ == "__main__":
    main()
