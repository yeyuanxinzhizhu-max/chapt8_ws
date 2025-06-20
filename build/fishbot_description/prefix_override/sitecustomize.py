import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/xinzhizhu/xiaoyuros/chapt8_ws/install/fishbot_description'
