# Wine_Predictor


Wine Predictor Using KNN Algorithm

This repository contains a Python script that implements a Wine Predictor using the K-Nearest Neighbors (KNN) algorithm. The script leverages the sklearn library to classify different types of wine based on their chemical properties.

Key Features:
- Dataset: Utilizes the Wine dataset from sklearn, which includes 13 chemical features for different wine samples.
- KNN Classifier: Implements the KNN algorithm to classify wine samples into three classes.
- Model Training and Testing: Splits the dataset into training (70%) and testing (30%) sets to evaluate the model's accuracy.
-Accuracy: Achieves an accuracy of approximately 83% in predicting wine classes.

 Script Highlights:
- Feature and Target Names: Prints the feature names and target names (class labels) of the Wine dataset.
- Data Preview: Displays the first five records of the wine data and corresponding labels.
- Model Training: Trains the KNN model with the training data.
- Prediction and Evaluation: Predicts the wine classes for the test data and evaluates the model's accuracy.

 Usage:
1. Clone the Repository: 
   
   git clone https://github.com/yourusername/wine-predictor.git
   
2. Navigate to the Directory:
  
   cd wine-predictor
   
3. Run the Script:
   
   python wine_predictor.py
   

Output:
- Feature names and target names of the Wine dataset.
- First five records of the wine data.
- Wine labels (0: Class_0, 1: Class_1, 2: Class_2).
- Model accuracy.

Author:
Vaishnavi Pravin Talekar

 Sample Output:

---Vaishnavi_Pravin_Talekar---

Wine Predictor Application using KNN Algorithm

['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']
['class_0' 'class_1' 'class_2']
[[1.423e+01 1.710e+00 2.430e+00 1.560e+01 1.270e+02 2.800e+00 3.060e+00
  2.800e-01 2.290e+00 5.640e+00 1.040e+00 3.920e+00 1.065e+03]
 [1.320e+01 1.780e+00 2.140e+00 1.120e+01 1.000e+02 2.650e+00 2.760e+00
  2.600e-01 1.280e+00 4.380e+00 1.050e+00 3.400e+00 1.050e+03]
 [1.316e+01 2.360e+00 2.670e+00 1.860e+01 1.010e+02 2.800e+00 3.240e+00
  3.000e-01 2.810e+00 5.680e+00 1.030e+00 3.170e+00 1.185e+03]
 [1.437e+01 1.950e+00 2.500e+00 1.680e+01 1.130e+02 3.850e+00 3.490e+00
  2.400e-01 2.180e+00 7.800e+00 8.600e-01 3.450e+00 1.480e+03]
 [1.324e+01 2.590e+00 2.870e+00 2.100e+01 1.180e+02 2.800e+00 2.690e+00
  3.900e-01 1.820e+00 4.320e+00 1.040e+00 2.930e+00 7.350e+02]]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2]
Accuracy :  0.8333333333333334




Feel free to customize this description to better match your preferences and any additional details you want to highlight about your case study.
