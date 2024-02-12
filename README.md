## Passive Stereo Camera Distance Measurement

"The use of the passive stereo camera to reconstruct depth for a very large distance application"

**Setup** </br>
Install Python 3.10 and packages
```shell
pip install -r requirements.txt
```

### Dataset Generation
For distance measurement, there are no public datasets available. So, we have created the dataset for testing 
the model we will be using in this project.

Here are the camera settings for this dataset.
```text
f = 1.8nm
```

Two objects, a lock and cup are placed at 40 and 50cm with left and right images.


### Milestone 1
The 1st milestone contains the following points:
1. Arrange a dataset to test the model, (left-side camera, right-side camera images of the objects)
2. Data Pre-processing (remove noise, enhance images, and prepare for model)
3. Calibration code added which reads the images and gives calibration matrix
4. Buy two cameras to set for the stereo calibration (Logitech C270 Webcams) 
5. A GitHub repo is created where these data and descriptions uploaded

### Milestone 2
- Machine Learning (In-Progress)
- Deep Learning Algorithms Training (Optional)
- Stereo Rectification (Done)


### Milestone 3
- Stereo Matching
- Distance Measurement
- Model Evaluation



#### Supporting material 
- [Single Cam Distance Measurement](https://github.com/Asadullah-Dal17/Distance_measurement_using_single_camera/tree/main ) </br>
- [Stereo Calibration](https://github.com/TemugeB/python_stereo_camera_calibrate)

