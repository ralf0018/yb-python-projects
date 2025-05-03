import tensorflow as tf
import matplotlib.pyplot as plt

(x_train, y_train), (x_test,y_test) = tf.keras.datasets.cifar10.load_data()
print("training data shape:", x_train.shape, y_train.shape)
print("test data shape:", x_test.shape, y_test.shape)

# Define the class names for CIFAR-10
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# visualize data by plotting images
fig, ax = plt.subplots(2, 2, figsize=(4, 4))
k = 10

# Plot images
for i in range(2):
    for j in range(2):
        ax[i][j].imshow(x_train[k], aspect='auto')
        ax[i][j].set_title(f"{class_names[y_train[k][0]]}") # Add a title for each pic
        ax[i][j].axis("off") # Hide the axis
        k += 1

plt.show()