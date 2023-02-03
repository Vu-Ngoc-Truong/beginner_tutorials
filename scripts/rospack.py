import rospkg

# ros_root = rospkg.get_ros_root()

r = rospkg.RosPack()
depends = r.get_depends('roscpp')
path = r.get_path('agf_common')
print(depends)
print(path)