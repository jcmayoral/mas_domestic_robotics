FROM argenos/bitbots-base

RUN rosdep update

ADD ./ /kinetic/src/mas_domestic_robotics
WORKDIR /kinetic

RUN wstool init src && wstool merge -t src src/mas_domestic_robotics/.travis/travis.rosinstall
RUN wstool update -t src
RUN rosdep install --from-paths src --ignore-src --rosdistro=kinetic -y
