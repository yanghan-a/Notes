# 创建publisher和subscriber节点

## python

## 基本命令

创建工作空间

```sh
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
```

创建功能包

```sh
$ catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
```

source ros源setup.bash以及功能包setup.bash

```sh
$ source /opt/ros/<distro>/setup.bash
source /opt/ros/kinetic/setup.bash

$ source devel/setup.bash
```

查看环境内功能包

```sh
$ echo $ROS_PACKAGE_PATH
/home/youruser/catkin_ws/src:/opt/ros/kinetic/share
```

查找功能包位置

```sh
$ rospack find [package_name]
```

## ros包的目录结构

- ```
  workspace_folder/        -- WORKSPACE
    src/                   -- SOURCE SPACE
      CMakeLists.txt       -- 'Toplevel' CMake file, provided by catkin
      package_1/
        CMakeLists.txt     -- CMakeLists.txt file for package_1
        package.xml        -- Package manifest for package_1
      ...
      package_n/
        CMakeLists.txt     -- CMakeLists.txt file for package_n
        package.xml        -- Package manifest for package_n
  ```

每个目录下基本都有相应的CMakeists.txt文件

## 常用的关于话题的命令

### 话题相关

```sh
rostopic list
```

查看现有话题

```sh
rostopic echo
```

查看话题发布的内容

```sh
rostopic info 话题名
```

查看哪话题对应的基本信息

```sh
rostopic pub /topic_name message_type message_content
```

使用命令行发布一个话题，以及话题的内容

示例

```sh
rostopic pub /number std_msgs/Int32 "data: 42"
```



### messeage相关

```sh
rosmsg info msg名称
```

查看msg具体的数据结构



































