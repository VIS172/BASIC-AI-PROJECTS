![images](https://github.com/VIS172/CODSOFT/assets/109724129/aa69421c-2b4d-419f-822c-fffb37a74a31)



# Image Captioning 

This project aims to predict captions for input images using a combination of Convolutional Neural Networks (CNN) and Long Short-Term Memory Networks (LSTM). The dataset consists of 8,000 images, each with 5 captions. Features are extracted from both the images and the text captions, concatenated, and used to predict the next word in the caption.

## Dataset

The dataset used is the Flickr8k dataset, which can be downloaded from Kaggle:

[Download the dataset](https://www.kaggle.com/adityajn105/flickr8k)

## Project Objective

The objective is to generate descriptive captions for images using a neural network that combines image features extracted by CNN and text features processed by LSTM.

## Environment

This project is conducted on Kaggle.

## Libraries Used

- numpy
- matplotlib
- keras
- tensorflow
- nltk

## Neural Networks

- VGG16 Network for image feature extraction
- CNN-LSTM Network for caption prediction

## Performance Metric

The BLEU Score is used to evaluate the performance of the trained model.

## Project Structure

- `data/`: Contains the dataset.
- `models/`: Contains the model definitions and trained models.
- `notebooks/`: Contains Jupyter notebooks for experimentation and model training.
- `scripts/`: Contains Python scripts for data processing, training, and evaluation.
- `results/`: Contains the results and evaluation metrics.


