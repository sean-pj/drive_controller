import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class DriveManager(Node):

    def __init__(self):
        super().__init__('drive_manager')
        self.subscription = self.create_subscription(String, 'topic', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

        self.control_type = "diff"
        self.angle = 0

    '''
    Steering 
    '''
    def diff(self):
        self.get_logger().info('diff')
    
    '''
    Cartesian
    '''
    def cart(self):
        self.get_logger().info('cart')

    '''
    One point turn
    '''
    def turn(self):
        self.get_logger().info('turn')


    def listener_callback(self, msg):
        self.control_type = msg.data.split(", ")[0]
        self.angle = int(msg.data.split(", ")[1])
        self.get_logger().info(f"Control type is: {self.control_type}, Angle is: {self.angle}")

        if (self.control_type == "diff"):
            self.diff()
        elif (self.control_type == "cart"):
            self.cart()
        elif (self.control_type == "turn"):
            self.turn()
        else:
            self.get_logger().error(f"Invalid control type. Received: {self.control_type}")




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