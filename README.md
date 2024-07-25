# SwachhMukh

# Spit Detection and Recognition System

## Overview

The Spit Detection and Recognition System is a project aimed at detecting instances of people spitting in public spaces and recognizing them either by their facial features or vehicle number plates. This system utilizes advanced image processing, object detection, facial recognition, and license plate recognition techniques to identify and track individuals who engage in spitting behavior.

you can also view this project at roboflow: https://universe.roboflow.com/vibhore/swachmukhh

<img width="434" alt="image" src="https://github.com/user-attachments/assets/9b30e0d5-c47c-4f54-8a0b-daa0ee7c7b0e">


## Results

![P_curve](https://github.com/user-attachments/assets/2d4bcdb1-c1c2-4c24-87a8-bdf2d5987ec1)
![F1_curve](https://github.com/user-attachments/assets/f3109540-38f0-4f1d-b14f-c4eff9e2e99f)
![confusion_matrix_normalized](https://github.com/user-attachments/assets/c229bfbf-2e0c-4c39-9560-b45bea2c8fa6)




## Features

- **Spit Detection**: Utilizes object detection algorithms to identify instances of people spitting within images or video streams.
- **Facial Recognition**: Implements deep learning techniques to recognize individuals by their facial features.
- **License Plate Recognition (Optional)**: Provides the capability to recognize individuals by their vehicle number plates using optical character recognition (OCR).
- **Real-Time Processing**: Supports real-time processing of live video feeds from cameras for prompt detection and recognition.
- **User Interface**: Offers a user-friendly interface for system configuration, monitoring, and feedback on detected instances.
- **Scalability**: Designed to be scalable and adaptable to different environments and deployment scenarios.

## Getting Started

To get started with the Spit Detection and Recognition System, follow these steps:

1. **Installation**: Clone this repository to your local machine and install the required dependencies as specified in the `requirements.txt` file.

2. **Configuration**: Modify the configuration settings in the `config.yaml` file to match your specific environment and preferences.

3. **Data Collection**: Collect a diverse dataset of images and videos containing instances of people spitting, as well as data for vehicle number plates if utilizing license plate recognition.

4. **Training (Optional)**: If necessary, train the facial recognition and license plate recognition models on your custom dataset using the provided training scripts.

5. **Run the System**: Execute the main application script (`main.py`) to launch the Spit Detection and Recognition System. Monitor the system output for detected instances and recognized individuals.

## Usage

The Spit Detection and Recognition System can be used in various scenarios, including:

- Public spaces such as parks, streets, and transportation hubs to enforce hygiene regulations.
- Corporate environments to enhance security and monitor employee behavior.
- Law enforcement operations for identifying individuals engaged in antisocial activities.

## Contributing

Contributions to the Spit Detection and Recognition System are welcome! If you encounter any bugs, have suggestions for improvements, or would like to contribute new features, please open an issue or submit a pull request on GitHub.


## Acknowledgements

We would like to thank the developers and contributors of the following open-source projects, which were instrumental in the development of this system:

- [TensorFlow](https://github.com/tensorflow/tensorflow)
- [OpenCV](https://github.com/opencv/opencv)


## Contact

For questions, inquiries, or collaborations, please contact vjmj4005@gmail.com.
