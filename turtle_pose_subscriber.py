import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import Float32
import math

class TurtlePoseSubscriber(Node):
    def __init__(self):
        super().__init__('turtle_pose_subscriber')

        # Subscribe to /turtle1/pose
        self.pose_subscriber = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

        # Publisher to /turtle1/distance_from_origin
        self.distance_publisher = self.create_publisher(Float32, '/turtle1/distance_from_origin', 10)

    def pose_callback(self, msg):
        # Compute distance from origin (0,0)
        distance = math.sqrt(msg.x**2 + msg.y**2)

        # Publish distance
        distance_msg = Float32()
        distance_msg.data = distance
        self.distance_publisher.publish(distance_msg)

        self.get_logger().info(f'Published Distance: {distance:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = TurtlePoseSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
