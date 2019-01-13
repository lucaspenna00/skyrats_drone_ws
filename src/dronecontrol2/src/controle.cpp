#include <math.h>
#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <mavros_msgs/CommandBool.h>
#include <mavros_msgs/SetMode.h>
#include <mavros_msgs/State.h>
#include <geometry_msgs/TwistStamped.h>
#include <geometry_msgs/PoseStamped.h>
#include <dronecontrol2/Vector3D.h>
#include <sensor_msgs/BatteryState.h>


/* O pacote "mavros_msgS" contém todas as mensagens necessárias para o funcionamento dos "services" e dos "topics" oriundos do pacote MAVROS. Todos os serviços e tópicos, assim como seus respectivos tipos de mensagens, estão documentados na MAVROS wiki. */

mavros_msgs::State current_state;
/*Criamos uma simples função que salva o estado momentâneo do vôo. Ela nos permite checar parâmetros como: connection, arming e offboard flags. */

//sensor_msgs::BatteryState battery_state;

float position[2];
float velocity[2];
float positionAtual[2];

void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
}

/*void battery_cb(const sensor_msgs::BatteryState::ConstPtr& msg){

  battery_state = *msg;

}
*/

void callbackPosition(const dronecontrol2::Vector3D::ConstPtr& msg)
{
   position[0] = msg->x;
   position[1] = msg->y;
   position[2] = msg->z;
}

void callbackVelocity(const dronecontrol2::Vector3D::ConstPtr& msg)
{
   velocity[0] = msg->x;
   velocity[1] = msg->y;
   velocity[2] = msg->z;
}

void callbackPositionAtual(const geometry_msgs::PoseStamped::ConstPtr& msg){

   positionAtual[2] = msg->pose.position.x;
   positionAtual[2] = msg->pose.position.y;
   positionAtual[2] = msg->pose.position.z;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "integracao_controle");

    ros::NodeHandle nh;

    ros::Subscriber velExt = nh.subscribe<dronecontrol2::Vector3D>
            ("controle/velocity", 10, callbackVelocity);

    ros::Subscriber posExt = nh.subscribe<dronecontrol2::Vector3D>
            ("controle/position", 10,  callbackPosition);

    ros::Subscriber posAtual = nh.subscribe<geometry_msgs::PoseStamped>
            ("mavros/local_position/pose", 10,  callbackPositionAtual);

    ros::Subscriber state_sub = nh.subscribe<mavros_msgs::State>
            ("mavros/state", 10, state_cb);

    ros::Publisher pos = nh.advertise<geometry_msgs::PoseStamped>
            ("mavros/setpoint_position/local", 10);

    ros::Publisher vel_pos_pub = nh.advertise<geometry_msgs::TwistStamped>
            ("mavros/setpoint_velocity/cmd_vel", 10);

    ros::ServiceClient arming_client = nh.serviceClient<mavros_msgs::CommandBool>
            ("mavros/cmd/arming");

    ros::Publisher local_pos_pub = nh.advertise<geometry_msgs::PoseStamped>
            ("mavros/setpoint_position/local", 10);

    ros::ServiceClient set_mode_client = nh.serviceClient<mavros_msgs::SetMode>
            ("mavros/set_mode");

  /*  ros::Subscriber battery = nh.subscribe<sensor_msgs::BatteryState>
            ("sensor_msgs/BatteryState",10, battery_cb);
*/

    /*Acima, instanciamos um "publisher" a fim de publicar a posição da aeronave, bem como "clients" apropriedades, de forma a dar o comando "arm".*/
    //the setpoint publishing rate MUST be faster than 2Hz

    ros::Rate rate(20.0);

    /* A pilha de vôo do PX4 possui um intervalo de 500ms entre dois comandos offboard. Se esse intervalo for excedido, o programa de comando irá voltar para o último estado da aeronave antes de entrar no modo offboard! */


    while(ros::ok() && !current_state.connected){

        ros::spinOnce();
        rate.sleep();
    }

    //printf("Hello everyone! Crystal Fissure here. %f", battery_state.percentage );

    geometry_msgs::TwistStamped vel;

    geometry_msgs::PoseStamped pose;

    pose.pose.position.x = 0;
    pose.pose.position.y = 0;
    pose.pose.position.z = 2;

    for(int i = 100; ros::ok() && i > 0; --i){
        local_pos_pub.publish(pose);
        ros::spinOnce();
        rate.sleep();
    }

  /* Antes de entrarmos no modo offboard, você tem que ter iniciado os setpoints de transmissão. Caso contrário, a escolha do modo de vôo será rejeitada (próx. passo). Aqui, o número 100 foi uma escolha arbitrária */

    mavros_msgs::SetMode offb_set_mode;
    offb_set_mode.request.custom_mode = "OFFBOARD";

    mavros_msgs::CommandBool arm_cmd;
    arm_cmd.request.value = true;

    ros::Time last_request = ros::Time::now();

while(ros::ok()){

	if( current_state.mode != "OFFBOARD" &&
            (ros::Time::now() - last_request > ros::Duration(5.0))){
            if( set_mode_client.call(offb_set_mode) &&
                offb_set_mode.response.mode_sent){
                ROS_INFO("Takeoff enabled");
            }
            last_request = ros::Time::now();
        }

	else {
            if( !current_state.armed &&
                (ros::Time::now() - last_request > ros::Duration(5.0))){
                if( arming_client.call(arm_cmd) &&
                    arm_cmd.response.success){
                    ROS_INFO("Vehicle armed");
                }
                last_request = ros::Time::now();
            }
        }


    if(positionAtual[2] >= fabs(2-0.05) || positionAtual[2] <= fabs(2-0.05)){
	     vel.twist.linear.x = velocity[0];
	     vel.twist.linear.y = velocity[1];
	     vel.twist.linear.z = velocity[2];

	     pose.pose.position.x = position[0];
	     pose.pose.position.y = position[1];
	     pose.pose.position.z = position[2];

	     local_pos_pub.publish(pose);
	     vel_pos_pub.publish(vel);

	     ros::spinOnce();
	     rate.sleep();

     }

     local_pos_pub.publish(pose);
     vel_pos_pub.publish(vel);

     ros::spinOnce();
     rate.sleep();

    }

    return 0;
}
