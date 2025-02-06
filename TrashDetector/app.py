import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO

def detect_objects(image, column):
    # Load in the model
    model = YOLO("best.pt")

    # Perform object detection
    prediction = model.predict(image)

    # Visualize the results
    for i, r in enumerate(prediction):
        # Plot results image
        im_bgr = r.plot()  # BGR-order numpy array
        im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image

    # Show predicted image next to the input image
    column.image(im_rgb, caption="Predicted Image", use_container_width=True)

# Main Streamlit app code
def main():
    # st.title("Trash Detector")
    st.markdown("<h1 style='text-align: center;'>Trash Detector</h1>", unsafe_allow_html=True)

    # Upload image
    uploaded_image = st.file_uploader("Please upload an image", type=["jpg", "jpeg", "png"])
    
    # Set up columns for predicted and original images
    col1, col2 = st.columns(2)

    if uploaded_image is not None:
        # Display uploaded image
        image = Image.open(uploaded_image)
        col1.image(image, caption="Uploaded Image", use_container_width=True)

        # Perform object detection when button is clicked
        if st.button("Detect Objects"):
            # Convert image to numpy array
            image_np = np.array(image)

            # Perform object detection
            detect_objects(image_np, col2)

if __name__ == "__main__":
    main()
