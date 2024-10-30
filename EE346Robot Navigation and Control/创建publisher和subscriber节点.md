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

查看功能包目录

```
$ rosls 功能包名字
```

编译单个功能包

```
$ rosmake 功能包1 功能包2 ...
```

安装依赖功能包

```
$ rosdep 依赖功能包
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

查看功能包的依赖，功能包的依赖定义在package.xml中

```sh
$ rospack depends1 beginner_tutorials
$ roscd beginner_tutorials
$ cat package.xml
```

查看功能包的非直接依赖

```sh
$ rospack depends beginner_tutorials
```



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

### 常用message的分类

查看所有的message目录

```
rosmsg show tab
```

常用的主要是以下目录下的message

```
sensor_msgs/
geometry_msgs/
nav_msgs/
std_msgs/
```



### 一些临时未分类的命令

查看节点信息，

```
rosnode info 节点名
```



























