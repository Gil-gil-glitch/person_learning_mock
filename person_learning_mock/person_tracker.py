import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PersonTracker(Node):
    def __init__(self):
        super().__init__('person_tracker')
        self.subscription = self.create_subscription(
            String,
            'person_detections',
            self.callback,
            10)

        self.publisher = self.create_publisher(String, 'tracked_person', 10)

    def callback(self, msg):
        self.get_logger().info("Tracking person")
        tracked_msg = String()
        tracked_msg.data = "person_position_xyz"
        self.publisher.publish(tracked_msg)

def main():
    rclpy.init()
    node = PersonTracker()
    rclpy.spin(node)
    rclpy.shutdown()