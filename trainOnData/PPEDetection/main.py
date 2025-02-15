if __name__ == '__main__':
    from ultralytics import YOLO

    # Load model weights (relative path from PPEDetection)
    model = YOLO("../../Yolo-Weights/yolov8l.pt")

    # Train the model using the dataset YAML file (absolute or relative path)
    model.train(
        data=r"C:\Users\Rafael Jabbour\OneDrive\Documents\GitHub\datasets\Construction-Site-Safety_roboflow\data.yaml",
        epochs=50,
        imgsz=640
    )
