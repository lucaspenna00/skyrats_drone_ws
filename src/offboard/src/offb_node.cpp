/**
 * @file offb_node.cpp
 * @brief Offboard control example node, written with MAVROS version 0.19.x, PX4 Pro Flight
 * Stack and tested in Gazebo SITL
 */

#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <mavros_msgs/CommandBool.h>
#include <mavros_msgs/SetMode.h>
#include <mavros_msgs/State.h>
#include <std_msgs/String.h>
#include <string.h>

std::string qrcode;

/* O pacote "mavros_msgS" contém todas as mensagens necessárias para o funcionamento dos "services" e dos "topics" oriundos do pacote MAVROS. Todos os serviços e tópicos, assim como seus respectivos tipos de mensagens, estão documentados na MAVROS wiki. */

mavros_msgs::State current_state;
void state_cb(const mavros_msgs::State::ConstPtr& msg){
    current_state = *msg;
}

void callback(const std_msgs::String data){
	qrcode = data.data;
}

/*Criamos uma simples função que salva o estado momentâneo do vôo. Ela nos permite checar parâmetros como: connection, arming e offboard flags. */

int main(int argc, char **argv)
{
    ros::init(argc, argv, "offb_node");

    ros::NodeHandle nh;


    ros::Subscriber state_sub = nh.subscribe<mavros_msgs::State>
            ("mavros/state", 10, state_cb);

    ros::Publisher local_pos_pub = nh.advertise<geometry_msgs::PoseStamped>
            ("mavros/setpoint_position/local", 10);

    ros::ServiceClient arming_client = nh.serviceClient<mavros_msgs::CommandBool>
            ("mavros/cmd/arming");

    ros::ServiceClient set_mode_client = nh.serviceClient<mavros_msgs::SetMode>
            ("mavros/set_mode");

    ros::Subscriber qr_sub = nh.subscribe<std_msgs::String>
            ("qrcode", 10, callback);

    /*Acima, instanciamos um "publisher" a fim de publicar a posição da aeronave, bem como "clients" apropriedades, de forma a dar o comando "arm".*/

    //the setpoint publishing rate MUST be faster than 2Hz
    ros::Rate rate(20.0);

    /* A pilha de vôo do PX4 possui um intervalo de 500ms entre dois comandos offboard. Se esse intervalo for excedido, o programa de comando irá voltar para o último estado da aeronave antes de entrar no modo offboard! */


    while(ros::ok() && !current_state.connected){
        ros::spinOnce();
        rate.sleep();
    }

	/* Antes de publicarmos algo, nós esperamos a conexão a ser estabelecida entre a MAVROS e o autopilot. Esse loop se encerrará quando a mensagem for recebida! */

    geometry_msgs::PoseStamped pose;

    pose.pose.position.x = 0;
    pose.pose.position.y = 0;
    pose.pose.position.z = 0;


    //send a few setpoints before starting

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

	if(qrcode == "arm"){
		arm_cmd.request.value = true;

		if( current_state.mode != "OFFBOARD" &&
           	(ros::Time::now() - last_request > ros::Duration(5.0))){
            		if( set_mode_client.call(offb_set_mode) &&
            	   	 offb_set_mode.response.mode_sent){
                		ROS_INFO("Offboard enabled");
           		}
          		last_request = ros::Time::now();
        	}

		else {
           	 	if( !current_state.armed &&
                	(ros::Time::now() - last_request > ros::Duration(5.0))){
                		if( arming_client.call(arm_cmd) &&
                    		arm_cmd.response.success){
                   			 ROS_INFO("Vehicle armed");
				         if(qrcode == "arm")
					 	ROS_INFO("armed");
                		}
              		  last_request = ros::Time::now();
          	        }
        	}
	}

	else{
		arm_cmd.request.value = false;
		if( current_state.mode != "OFFBOARD" &&
           	(ros::Time::now() - last_request > ros::Duration(5.0))){
            		if( set_mode_client.call(offb_set_mode) &&
            	   	 offb_set_mode.response.mode_sent){
                		ROS_INFO("Offboard enabled");
           		}
          		last_request = ros::Time::now();
        	}

		else {
           	 	if( current_state.armed &&
                	(ros::Time::now() - last_request > ros::Duration(5.0))){
                		if( arming_client.call(arm_cmd) &&
                    		arm_cmd.response.success){
                   			 ROS_INFO("Vehicle disarmed");
				         if(qrcode != "arm")
					 	ROS_INFO("disarmed");
                		}
              		  last_request = ros::Time::now();
          	        }
        	}
        }


	local_pos_pub.publish(pose);

        ros::spinOnce();
        rate.sleep();
    }

    return 0;
}
