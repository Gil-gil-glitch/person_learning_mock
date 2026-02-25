import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ASRNode(Node):
    def __init__(self):
        super().__init__('asr_node')
        self.publisher = self.create_publisher(String, 'speech_text', 10)
        self.timer = self.create_timer(10.0, self.fake_speech)

    def fake_speech(self):
        msg = String()
        msg.data = "My name is John"
        self.get_logger().info("User said: My name is John")
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = ASRNode()
    rclpy.spin(node)
    rclpy.shutdown()