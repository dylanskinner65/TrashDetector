from ultralytics import YOLO

# Load the model
model = YOLO('yolov8n.pt')

# Use the model
results = model.train(data='config.yaml', 
                      epochs=1, 
                      batch=2,
                      imgsz=640,
                      device='mps')