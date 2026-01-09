import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class DriveManager(Node):

    def __init__(self):
        super().__init__('drive_manager')
        self.subscription = self.create_subscription(String, 'topic', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

        self.control_type = ["diff", 0]

    def listener_callback(self, msg):
        self.control_type = msg.data.split(", ")
        self.get_logger().info('Control type is: %s, Angle is: %s' % (self.control_type[0], self.control_type[1]))

    '''
    Steering 
    '''
    def diff():
        self.get_logger().info('')
    '''
    Cartesian
    '''

    def cart():



def main(args=None):
    rclpy.init(args=args)

    drive_manager = DriveManager()

    rclpy.spin(drive_manager)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    drive_manager.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()