# Activity W4-2-3: - Create a Full project in Python - object oriented - File processing
# Note: You must have main function
# Write a full project to do the data file processing for csv, text and etc. file formats. .parquet image format
import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import math

# A class for processing files, 
# supported formats: csv, parquet, text, and some image format(.jpg, .png, .bmp)
class fileFormatProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    
    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
        elif self.file_path.endswith('.txt'):
            self.data = pd.read_csv(self.file_path, header=None)
        elif self.file_path.endswith(('.bmp','.png','.jpg')):
            self.data = mpimg.imread(self.file_path)
        else:
            raise ValueError("Unsupported file format. Please try again")
        print(f"Data loaded successfully from {self.file_path}")
    

    def initial_processing(self):
        if self.data is None: # 
            raise ValueError("File is Empty.")
        # Plot the image if it is a image
        elif self.file_path.endswith(('.bmp','.png','.jpg')):
            plt.imshow(self.data)
            plt.axis("off")
            plt.show()
        # Output the results of other types of file
        else:
            print("Initial Data Summary:")
            print(self.data.info())
            print("\nMissing Values:")
            print(self.data.isnull().sum())
            print("\nDescriptive Statistics:")
            print(self.data.describe())

def main():
    filePath1 = "./week4/inclass_activities/sample_junk_mail.csv"
    filePath2 = "./week4/inclass_activities/img.png"

    processor = fileFormatProcessor(filePath1)
    processor.load_data()
    processor.initial_processing()

def sin_cos(degree):
    sin = math.sin(math.radians(degree))
    cos = math.cos(math.radians(degree))
    print(f"The sin value of the angle is {sin:.2f}")
    print(f"The cos value of the angle is {cos:.2f}")
    
def circleArea(diameter):
    if diameter < 0:
        raise ValueError("The diameter of a circle can't be negative")
    else:
        area = math.pi * (diameter * 0.5) ** 2
        print(f"The area of the circle is {area:.2f}")
        
def union_symmetricDiff():
    set1 = {10,20,30,40}
    set2 = {10,15,20,25}
    
    print(f"Here are 2 sets: {set1} and {set2}")
    union = set1.union(set2)
    print(f"The union of the 2 sets is {union}")
    symmetricDiff = set1.symmetric_difference(set2)
    print(f"The symmetric difference of the 2 sets is {symmetricDiff}")

if __name__ == "__main__":
    # main()
    
    # degree = float(input("Enter an angle in degrees: "))
    # sin_cos(degree)
    
    # diameter = float(input("Enter a diameter of a circle: "))
    # circleArea(diameter)
    
    # union_symmetricDiff()