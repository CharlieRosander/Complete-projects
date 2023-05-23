# Cat vs Dog Image Classifier

## Overview
This project is an implementation of a Convolutional Neural Network (CNN) to classify images of cats and dogs. The project uses Python programming language and several machine learning libraries including TensorFlow, Keras, and OpenCV.

The network takes as input an image of size 84x84 pixels and outputs a prediction of whether the image is a cat or a dog.

## Dependencies

- Python 3
- TensorFlow
- Keras
- OpenCV
- Matplotlib
- Numpy
- os

You can install the required libraries using pip:

```
pip install tensorflow opencv-python keras numpy matplotlib
```

## Project Structure

The project is structured as a single python script which includes:

- Function to load and process the images from a given folder.
- Defining the Convolutional Neural Network model with layers including Conv2D, MaxPooling2D, Dropout, Flatten, and Dense.
- Compile and fit the model.
- Evaluate the model's accuracy on the test data.
- Predict the labels of random test images and calculate the overall accuracy.
- Write the test results to a text file.

## Usage

1. Clone the repository.
2. Make sure you have the required dependencies.
3. Add your own images in the './images/train' and './images/test' directories.
4. Run the script:
```
python script_name.py
```

## Data

Images should be placed in two folders, './images/train' and './images/test'. The image filenames should start with 'cat' for cat images and 'dog' for dog images.

## Results

The script will output the test accuracy and the overall accuracy. It also writes the results to a text file named 'test_results.txt' in the './Docs' folder. 

This includes the number of training images, number of test images, test accuracy, number of correct guesses, overall accuracy in percentage, number of epochs run, the epoch at which training was stopped (if early stopping was activated), batch size, and early stopping patience.

## Note

Please be aware that this is a simple CNN model intended for educational purposes, and its performance may not be sufficient for production-level applications. For complex tasks, consider using more advanced architectures, fine-tuning pre-trained models, and augmenting the training data.

Also, depending on your hardware, training this model can take a long time, especially if the number of training images is large. It is recommended to use a machine with a GPU for faster training.
