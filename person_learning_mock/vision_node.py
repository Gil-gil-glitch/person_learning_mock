import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class VisionNode(Node):
    def __init__(self):
        super().__init__('vision_node')
        self.publisher = self.create_publisher(String, 'person_detections', 10)
        self.timer = self.create_timer(5.0, self.detect_person)

    def detect_person(self):
        msg = String()
        msg.data = "person_detected"
        self.get_logger().info("Person detected")
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = VisionNode()
    rclpy.spin(node)
    rclpy.shutdown()