from ultralytics import YOLO

# Load the model
model = YOLO('yolov8n.pt')

# Use the model
results = model.train(data='config.yaml', 
                      epochs=100, 
                      imgsz=640,
                      device=[0,1,2,3])
