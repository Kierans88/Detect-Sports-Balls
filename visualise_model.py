from ultralytics import YOLO

# Load and predict with the best.pt model
model_best = YOLO('yolov8m.pt')
results_best = model_best.predict(
    'Testing data/v2/resized_VID-20241129-WA0006.mp4', 
    save=True, 
    classes=[32]
)
 
print("Results from best.pt model:")
print(results_best[0])
print('===================================')
for box in results_best[0].boxes:
    print(box)