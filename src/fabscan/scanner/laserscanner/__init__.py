__author__ = "Mario Lukas"
__copyright__ = "Copyright 2017"
__license__ = "GPL v2"
__maintainer__ = "Mario Lukas"
__email__ = "info@mariolukas.de"

from fabscan.util.FSInject import injector
from fabscan.scanner.interfaces.FSScanProcessor import FSScanProcessorInterface
from fabscan.scanner.interfaces.FSHardwareController import FSHardwareControllerInterface
from fabscan.scanner.interfaces.FSImageProcessor import ImageProcessorInterface
from fabscan.scanner.interfaces.FSCalibration import FSCalibrationInterface


from fabscan.scanner.laserscanner.FSScanProcessor import FSScanProcessorSingleton
from fabscan.scanner.laserscanner.FSHardwareController import FSHardwareControllerSingleton
from fabscan.scanner.laserscanner.FSImageProcessor import ImageProcessor
from fabscan.scanner.laserscanner.FSCalibration import FSCalibration

def create():
    # "dynamic" module classes ...

    injector.provide(ImageProcessorInterface, ImageProcessor)
    injector.provide(FSHardwareControllerInterface, FSHardwareControllerSingleton)
    injector.provide(FSCalibrationInterface, FSCalibration)
    injector.provide(FSScanProcessorInterface, FSScanProcessorSingleton)


