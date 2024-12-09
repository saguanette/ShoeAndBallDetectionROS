# Import the necessary libraries
import rclpy  # Python Client Library for ROS 2
from rclpy.node import Node  # Handles the creation of nodes
from sensor_msgs.msg import Image  # Image is the message type
from cv_bridge import CvBridge  # Package to convert between ROS and OpenCV Images
import cv2  # OpenCV library
from ament_index_python.packages import get_package_share_directory

class VideoPublisher(Node):
    """
    Create a VideoPublisher class, which is a subclass of the Node class.
    """
    def __init__(self):
        """
        Class constructor to set up the node
        """
        # Initiate the Node class's constructor and give it a name
        super().__init__('video_publisher')

        # Create the publisher. This publisher will publish an Image
        # to the video_frames topic. The queue size is 10 messages.
        self.publisher_ = self.create_publisher(Image, 'video_frames', 10)

        # We will publish a message every 0.1 seconds
        timer_period = 0.1  # seconds

        # Use the default camera (usually 0 for the first camera)
        self.cap = cv2.VideoCapture(0)

        # Check if the camera opened successfully
        if not self.cap.isOpened():
            self.get_logger().error('Failed to open camera. Please check if the camera is connected.')

        # Used to convert between ROS and OpenCV images
        self.br = CvBridge()

        # Create the timer
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        """
        Callback function.
        This function gets called every 0.1 seconds.
        """
        # Capture frame-by-frame
        ret, frame = self.cap.read()

        if ret:
            # Publish the frame to the ROS topic
            self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
            self.get_logger().info('Publishing video frame')
        else:
            self.get_logger().error('Failed to capture frame from camera.')

def main(args=None):
    # Initialize the rclpy library
    rclpy.init(args=args)

    # Create the node
    video_publisher = VideoPublisher()

    # Spin the node so the callback function is called.
    rclpy.spin(video_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    video_publisher.destroy_node()

    # Shutdown the ROS client library for Python
    rclpy.shutdown()

if __name__ == '__main__':
    main()

