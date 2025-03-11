import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class TurtleDistancePublisher(Node):
    def __init__(self):
        super().__init__('turtle_distance_publisher')

        # Subscribe to /turtle1/distance_from_origin
        self.distance_subscriber = self.create_subscription(
            Float32,
            '/turtle1/distance_from_origin',
            self.distance_callback,
            10
        )

    def distance_callback(self, msg):
        self.get_logger().info(f'Received Distance: {msg.data:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = TurtleDistancePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
