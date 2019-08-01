Catkin package containing ROS node to read from realsense camera or bagfile

ROS Nodes:
	show.py: shows images published to topic specified on command line

---

1. Dependencies

python  
	numpy: sudo apt-get install python-numpy  
	argparse: sudo apt-get install libpython2.7-stdlib  
ROS: Tested with the full version. Insatll instructions from: http://wiki.ros.org/melodic/Installation/Ubuntu  
	Source the setup.bash  
	source /opt/ros/melodic/setup.bash  

OpenCV  

librealsense: can download debian from https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md

2. Build and install

Not necessary to build to run the python script