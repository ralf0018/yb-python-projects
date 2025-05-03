# Activity W4-2-3: - Create a Full project in Python - object oriented - File processing
# Note: You must have main function
# Write a full project to do the data file processing for csv, text and etc. file formats. .parquet image format
import pandas as pd
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

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
    
if __name__ == "__main__":
    main()