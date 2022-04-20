#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time

import cv2
import datetime
import os
import numpy as np
from logging import getLogger, DEBUG, NullHandler, INFO


def imwrite(filename, img, params=None):
    logger = getLogger(__name__)
    logger.addHandler(NullHandler())
    logger.propagate = True
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        logger.error(f"Image Write Error: {e}")
        return False


class Camera:
    def __init__(self, fps: int = 45):
        self.cam_threading = None
        self.capture_size = (1280, 720)
        # self.capture_size = (1920, 1080)
        self.capture_dir = "Captures"
        self.fps = int(fps)

        self.logger = getLogger(__name__)
        self.logger.addHandler(NullHandler())
        # self.logger.setLevel(INFO)
        self.logger.propagate = True

    def openCamera(self, cameraId):
        if self.cam_threading is not None and self.cam_threading.isOpened():
            self.logger.debug("Camera is already opened")
            self.destroy()
        self.cam_threading = ReadCamThreading(cameraId, self.capture_size)
        self.cam_threading.startReadingCam()

        # if os.name == 'nt':
        #     self.logger.debug("NT OS")
        #     self.camera = cv2.VideoCapture(cameraId, cv2.CAP_DSHOW)
        # # self.camera = cv2.VideoCapture(cameraId)
        # else:
        #     self.logger.debug("Not NT OS")
        #     self.camera = cv2.VideoCapture(cameraId)
        #
        # if not self.camera.isOpened():
        #     # print("Camera ID " + str(cameraId) + " can't open.")
        #     self.logger.error(f"Camera ID {cameraId} cannot open.")
        #     return
        # # print("Camera ID " + str(cameraId) + " opened successfully")
        # # print(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        # # self.camera.set(cv2.CAP_PROP_FPS, 60)
        # self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.capture_size[0])
        # self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.capture_size[1])
        # if (self.camera.get(cv2.CAP_PROP_FRAME_WIDTH) != self.capture_size[0]) or (
        #         self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT) != self.capture_size[1]):
        #     self.logger.warning("The camera's readout size is invalid.")
        #     self.logger.warning("Image recognition may be incorrect.")
        # elif self.isOpened():
        #     self.logger.warning("Camera not loaded.")
        # else:
        #     self.logger.info(f"Camera ID {cameraId} opened successfully.")

    # self.camera.set(cv2.CAP_PROP_SETTINGS, 0)

    def isOpened(self) -> bool:
        ret = self.cam_threading.camera.isOpened()
        if ret:
            self.logger.debug("Camera is opened")
        return ret

    def readFrame(self):
        _, self.image_bgr = self.cam_threading.read()
        return self.image_bgr

    def saveCapture(self, filename=None, crop=None, crop_ax=None, img=None):
        if crop_ax is None:
            crop_ax = [0, 0, 1280, 720]
        else:
            pass
            # print(crop_ax)

        dt_now = datetime.datetime.now()
        if filename is None or filename == "":
            filename = dt_now.strftime('%Y-%m-%d_%H-%M-%S') + ".png"
        else:
            filename = filename + ".png"

        if crop is None:
            image = self.image_bgr
        elif crop == 1 or crop == "1":
            image = self.image_bgr[
                    crop_ax[1]:crop_ax[3],
                    crop_ax[0]:crop_ax[2]
                    ]
        elif crop == 2 or crop == "2":
            image = self.image_bgr[
                    crop_ax[1]:crop_ax[1] + crop_ax[3],
                    crop_ax[0]:crop_ax[0] + crop_ax[2]
                    ]
        elif img is not None:
            image = img
        else:
            image = self.image_bgr

        if not os.path.exists(self.capture_dir):
            os.makedirs(self.capture_dir)
            self.logger.debug("Created Capture folder")

        save_path = os.path.join(self.capture_dir, filename)

        try:
            imwrite(save_path, image)
            self.logger.info(f"Capture succeeded: {save_path}")
            # print('capture succeeded: ' + save_path)
        except cv2.error as e:
            # print("Capture Failed")
            self.logger.error(f"Capture Failed :{e}")

    def destroy(self):
        if self.cam_threading is not None and self.cam_threading.isOpened():
            self.cam_threading.release()
            self.cam_threading = None
            self.logger.debug("Camera destroyed")


class ReadCamThreading(object):
    def __init__(self, cameraId: int, capture_size: tuple[int, int]):
        self.logger = getLogger(__name__)
        self.logger.addHandler(NullHandler())
        # self.logger.setLevel(INFO)
        self.logger.propagate = True
        self.cameraId = cameraId
        self.capture_size = capture_size
        self._frame = None
        self._frame_width = None
        self._frame_height = None
        self.camera = None
        self._ret = False

        self._is_running = False

    def startReadingCam(self):
        self._init_camera()
        self._is_running = True
        threading.Thread(target=self._update_camera, args=()).start()

    def _init_camera(self):
        if os.name == 'nt':
            self.logger.debug("NT OS")
            self.camera = cv2.VideoCapture(self.cameraId, cv2.CAP_DSHOW)
        # self.camera = cv2.VideoCapture(cameraId)
        else:
            self.logger.debug("Not NT OS")
            self.camera = cv2.VideoCapture(self.cameraId)

        if not self.camera.isOpened():
            # print("Camera ID " + str(cameraId) + " can't open.")
            self.logger.error(f"Camera ID {self.cameraId} cannot open.")
            return

        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.capture_size[0])
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.capture_size[1])
        if (self.camera.get(cv2.CAP_PROP_FRAME_WIDTH) != self.capture_size[0]) or (
                self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT) != self.capture_size[1]):
            self.logger.warning("The camera's readout size is invalid.")
            self.logger.warning("Image recognition may be incorrect.")
        elif not self.camera.isOpened():
            self.logger.warning("Camera not loaded.")
        else:
            self.logger.info(f"Camera ID {self.cameraId} opened successfully.")

    def _update_camera(self):
        while True:
            if self._is_running:
                self._ret, self._frame = self._read_from_camera()
            else:
                break

    def _read_from_camera(self) -> tuple[bool, any]:
        self._ret, self._frame = self.camera.read()
        if self._ret:
            return True, self._frame
        else:
            return False, None

    def release(self):
        self.camera.release()

    def set_cam_size(self, capture_size: list[int, int]):
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, capture_size[0])
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, capture_size[1])

    def read(self):
        return self._ret, self._frame

    def isOpened(self):
        return self.camera.isOpened()
