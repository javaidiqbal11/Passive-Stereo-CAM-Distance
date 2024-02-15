# Package importation
import numpy as np
import cv2

# ***** Parameters for Distortion Calibration *****
SQUARE_SIZE = 30
BOARD_SIZE = (9, 6)

# Termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, SQUARE_SIZE, 0.001)
criteria_stereo = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, SQUARE_SIZE, 0.001)

# Prepare object points
objp = np.zeros((BOARD_SIZE[0] * BOARD_SIZE[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:BOARD_SIZE[0], 0:BOARD_SIZE[1]].T.reshape(-1, 2)

# Arrays to store object points and image points from all images
objpoints = []  # 3d points in real world space
imgpointsR = []  # 2d points in image plane
imgpointsL = []

# Start calibration from the camera
print('Starting calibration for the 2 cameras... ')

# Call all saved images
for i in range(1, 21):
    t = str(i)
    ChessImaR = cv2.imread("data/chessboard/leftcamera/chessboard-L" + t + '.png', 0)  # Right side
    ChessImaL = cv2.imread("data/chessboard/rightcamera/chessboard-R" + t + '.png', 0)  # Left side
    retR, cornersR = cv2.findChessboardCorners(ChessImaR, BOARD_SIZE, None)  # Define the number of chees corners we are looking for
    retL, cornersL = cv2.findChessboardCorners(ChessImaL, BOARD_SIZE, None)  # Left side
    if retR:
        cv2.cornerSubPix(ChessImaR, cornersR, (11, 11), (-1, -1), criteria)
        imgpointsR.append(cornersR)
    if retL:
        cv2.cornerSubPix(ChessImaL, cornersL, (11, 11), (-1, -1), criteria)
        imgpointsL.append(cornersL)
    objpoints.append(objp)

# Determine the new values for different parameters
#   Right Side
retR, mtxR, distR, rvecsR, tvecsR = cv2.calibrateCamera(objpoints, imgpointsR, ChessImaR.shape[::-1], None, None)
hR, wR = ChessImaR.shape[:2]
OmtxR, roiR = cv2.getOptimalNewCameraMatrix(mtxR, distR,(wR, hR), 1, (wR, hR))

#   Left Side
retL, mtxL, distL, rvecsL, tvecsL = cv2.calibrateCamera(objpoints, imgpointsL, ChessImaL.shape[::-1], None, None)
hL, wL = ChessImaL.shape[:2]
OmtxL, roiL = cv2.getOptimalNewCameraMatrix(mtxL, distL, (wL, hL), 1, (wL, hL))

retS, MLS, dLS, MRS, dRS, R, T, E, F = cv2.stereoCalibrate(objpoints,
                                                           imgpointsL,
                                                           imgpointsR,
                                                           mtxL,
                                                           distL,
                                                           mtxR,
                                                           distR,
                                                           ChessImaR.shape[::-1],
                                                           criteria=criteria_stereo,
                                                           flags=cv2.CALIB_FIX_INTRINSIC)

# StereoRectify function
rectify_scale = 0  # if 0 image croped, if 1 image nor croped
RL, RR, PL, PR, Q, roiL, roiR = cv2.stereoRectify(MLS, dLS, MRS, dRS, ChessImaR.shape[::-1], R, T, rectify_scale,(0, 0))
# initUndistortRectifyMap function
Left_Stereo_Map = cv2.initUndistortRectifyMap(MLS, dLS, RL, PL, ChessImaR.shape[::-1], cv2.CV_16SC2)
Right_Stereo_Map = cv2.initUndistortRectifyMap(MRS, dRS, RR, PR, ChessImaR.shape[::-1], cv2.CV_16SC2)

print(Left_Stereo_Map)
print(Right_Stereo_Map)