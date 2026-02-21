import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class MoveTurtle(Node):

    def __init__(self):
        super().__init__('move_turtle')

        # Subscriber
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10)

        # Publisher
        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10)

        self.cmd = Twist()
        self.stopped = False

    def pose_callback(self, msg):

        # Si x o y superior a 7m, parem
        if msg.x > 7.0 or msg.y > 7.0:
            if not self.stopped:
                self.cmd.linear.x = 0.0
                self.cmd.angular.z = 0.0
                self.get_logger().info("Stopping turtle")
                self.stopped = True
        else:
            # Sino, nos movemos
            self.cmd.linear.x = 2.0
            self.cmd.angular.z = 0.0

        self.publisher.publish(self.cmd)


def main(args=None):
    rclpy.init(args=args)
    node = MoveTurtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()