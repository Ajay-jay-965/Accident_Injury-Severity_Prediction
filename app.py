# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:35:30 2021

@author: surya
"""
from flask import Flask, request, render_template
from flask_cors import cross_origin
#import sklearn
#import tensorflow as tf
import numpy as np  
#import pandas as pd
#from tensorflow import keras
#from keras.models import Sequential
#from keras.layers import Dense,Activation
from keras.models import load_model


app = Flask(__name__)
model = load_model('fmodel72.h5')



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        
        
        
        Age = int(request.form["AGE"])
        Alcohol_result = int(request.form["ALCOHOL_TEST_RESULT"])
        drug_result = int(request.form["DRUG_TEST_RESULT"])

        Sex = request.form["SEX"]
        if(Sex=='Male'):
            Male = 1
            Female = 0
            Unknown = 0
            
        elif (Sex=='Female'):
            Male = 0
            Female = 1
            Unknown = 0
            
        elif (Sex=='Unknown'):
            Male = 0
            Female = 0
            Unknown = 1
                
        else:
            Male = 0
            Female = 0
            Unknown = 0

                  
        person_type = request.form["PERSON_TYPE"]
        if(person_type=='Driver'):
            Driver=1
            Passenger_of_a_Motor_Vehicle_in_Transport=0
            Pedestrian=0
            Bicyclist=0
            Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport=0
            Occupant_of_a_Motor_Vehicle_Not_in_Transport=0
            Other_Pedestrian=0
            Occupant_of_a_Non_Motor_Vehicle_Transport_Device=0
            Other_Cyclist=0
            Unknown_Type_of_Non_Motorist=0
         
        elif(person_type=='Passenger_of_a_Motor_Vehicle_in_Transport'):
            Driver=0
            Passenger_of_a_Motor_Vehicle_in_Transport=1
            Pedestrian=0
            Bicyclist=0
            Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport=0
            Occupant_of_a_Motor_Vehicle_Not_in_Transport=0
            Other_Pedestrian=0
            Occupant_of_a_Non_Motor_Vehicle_Transport_Device=0
            Other_Cyclist=0
            Unknown_Type_of_Non_Motorist=0    
            
        elif(person_type=='Pedestrian'):
            Driver=0
            Passenger_of_a_Motor_Vehicle_in_Transport=0
            Pedestrian=1
            Bicyclist=0
            Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport=0
            Occupant_of_a_Motor_Vehicle_Not_in_Transport=0
            Other_Pedestrian=0
            Occupant_of_a_Non_Motor_Vehicle_Transport_Device=0
            Other_Cyclist=0
            Unknown_Type_of_Non_Motorist=0 
            
        elif(person_type=='Bicyclist'):
            Driver=0
            Passenger_of_a_Motor_Vehicle_in_Transport=0
            Pedestrian=0
            Bicyclist=1
            Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport=0
            Occupant_of_a_Motor_Vehicle_Not_in_Transport=0
            Other_Pedestrian=0
            Occupant_of_a_Non_Motor_Vehicle_Transport_Device=0
            Other_Cyclist=0
            Unknown_Type_of_Non_Motorist=0
            
        elif(person_type=='Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport'):
            Driver=0
            Passenger_of_a_Motor_Vehicle_in_Transport=0
            Pedestrian=0
            Bicyclist=0
            Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport=1
            Occupant_of_a_Motor_Vehicle_Not_in_Transport=0
            Other_Pedestrian=0
            Occupant_of_a_Non_Motor_Vehicle_Transport_Device=0
            Other_Cyclist=0
            Unknown_Type_of_Non_Motorist=0
            
        elif(person_type=='Occupant_of_a_Motor_Vehicle_Not_in_Transport'):
            Driver=0
            Passenger_of_a_Motor_Vehicle_in_Transport=0
            Pedestrian=0
            Bicyclist=0
            Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport=0
            Occupant_of_a_Motor_Vehicle_Not_in_Transport=1
            Other_Pedestrian=0
            Occupant_of_a_Non_Motor_Vehicle_Transport_Device=0
            Other_Cyclist=0
            Unknown_Type_of_Non_Motorist=0
            
        elif(person_type=='Other_Pedestrian'):
            Driver=0
            Passenger_of_a_Motor_Vehicle_in_Transport=0
            Pedestrian=0
            Bicyclist=0
            Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport=0
            Occupant_of_a_Motor_Vehicle_Not_in_Transport=0
            Other_Pedestrian=1
            Occupant_of_a_Non_Motor_Vehicle_Transport_Device=0
            Other_Cyclist=0
            Unknown_Type_of_Non_Motorist=0
            
        elif(person_type=='Occupant_of_a_Non_Motor_Vehicle_Transport_Device'):
            Driver=0
            Passenger_of_a_Motor_Vehicle_in_Transport=0
            Pedestrian=0
            Bicyclist=0
            Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport=0
            Occupant_of_a_Motor_Vehicle_Not_in_Transport=0
            Other_Pedestrian=0
            Occupant_of_a_Non_Motor_Vehicle_Transport_Device=1
            Other_Cyclist=0
            Unknown_Type_of_Non_Motorist=0    
            
        elif(person_type=='Other_Cyclist'):
            Driver=0
            Passenger_of_a_Motor_Vehicle_in_Transport=0
            Pedestrian=0
            Bicyclist=0
            Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport=0
            Occupant_of_a_Motor_Vehicle_Not_in_Transport=0
            Other_Pedestrian=0
            Occupant_of_a_Non_Motor_Vehicle_Transport_Device=0
            Other_Cyclist=1
            Unknown_Type_of_Non_Motorist=0
            
        elif(person_type=='Unknown_Type_of_Non_Motorist'):
            Driver=0
            Passenger_of_a_Motor_Vehicle_in_Transport=0
            Pedestrian=0
            Bicyclist=0
            Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport=0
            Occupant_of_a_Motor_Vehicle_Not_in_Transport=0
            Other_Pedestrian=0
            Occupant_of_a_Non_Motor_Vehicle_Transport_Device=0
            Other_Cyclist=0
            Unknown_Type_of_Non_Motorist=1 
                    
        else:
            Driver=0
            Passenger_of_a_Motor_Vehicle_in_Transport=0
            Pedestrian=0
            Bicyclist=0
            Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport=0
            Occupant_of_a_Motor_Vehicle_Not_in_Transport=0
            Other_Pedestrian=0
            Occupant_of_a_Non_Motor_Vehicle_Transport_Device=0
            Other_Cyclist=0
            Unknown_Type_of_Non_Motorist=0     
                                 
        seating_pos = request.form['SEATING_POSITION']
        if(seating_pos=='Front_Seat_Drivers_Side'):
            Front_Seat_Drivers_Side=1
            Front_Seat_Right_Side=0
            Non_Motorist=0
            Second_Seat_Right_Side=0
            Second_Seat_Left_Side=0
            Second_Seat_Middle=0
            Unknown=0
            Other_Passenger_in_enclosed_cargo_area=0
            Front_Seat_Middle=0
            Other_Passenger_in_unenclosed_cargo_area=0
            
        elif(seating_pos=='Front_Seat_Right_Side'):
            Front_Seat_Drivers_Side=0
            Front_Seat_Right_Side=1
            Non_Motorist=0
            Second_Seat_Right_Side=0
            Second_Seat_Left_Side=0
            Second_Seat_Middle=0
            Unknown=0
            Other_Passenger_in_enclosed_cargo_area=0
            Front_Seat_Middle=0
            Other_Passenger_in_unenclosed_cargo_area=0    
        
    
        elif(seating_pos=='Non_Motorist'):
            Front_Seat_Drivers_Side=0
            Front_Seat_Right_Side=0
            Non_Motorist=1
            Second_Seat_Right_Side=0
            Second_Seat_Left_Side=0
            Second_Seat_Middle=0
            Unknown=0
            Other_Passenger_in_enclosed_cargo_area=0
            Front_Seat_Middle=0
            Other_Passenger_in_unenclosed_cargo_area=0

        elif(seating_pos=='Second_Seat_Right_Side'):
            Front_Seat_Drivers_Side=0
            Front_Seat_Right_Side=0
            Non_Motorist=0
            Second_Seat_Right_Side=1
            Second_Seat_Left_Side=0
            Second_Seat_Middle=0
            Unknown=0
            Other_Passenger_in_enclosed_cargo_area=0
            Front_Seat_Middle=0
            Other_Passenger_in_unenclosed_cargo_area=0

        elif(seating_pos=='Second_Seat_Left_Side'):
            Front_Seat_Drivers_Side=0
            Front_Seat_Right_Side=0
            Non_Motorist=0
            Second_Seat_Right_Side=0
            Second_Seat_Left_Side=1
            Second_Seat_Middle=0
            Unknown=0
            Other_Passenger_in_enclosed_cargo_area=0
            Front_Seat_Middle=0
            Other_Passenger_in_unenclosed_cargo_area=0

        elif(seating_pos=='Second_Seat_Middle'):
            Front_Seat_Drivers_Side=0
            Front_Seat_Right_Side=0
            Non_Motorist=0
            Second_Seat_Right_Side=0
            Second_Seat_Left_Side=0
            Second_Seat_Middle=1
            Unknown=0
            Other_Passenger_in_enclosed_cargo_area=0
            Front_Seat_Middle=0
            Other_Passenger_in_unenclosed_cargo_area=0

        elif(seating_pos=='Unknown'):
            Front_Seat_Drivers_Side=0
            Front_Seat_Right_Side=0
            Non_Motorist=0
            Second_Seat_Right_Side=0
            Second_Seat_Left_Side=0
            Second_Seat_Middle=0
            Unknown=1
            Other_Passenger_in_enclosed_cargo_area=0
            Front_Seat_Middle=0
            Other_Passenger_in_unenclosed_cargo_area=0

        elif(seating_pos=='Other_Passenger_in_enclosed_cargo_area'):
            Front_Seat_Drivers_Side=0
            Front_Seat_Right_Side=0
            Non_Motorist=0
            Second_Seat_Right_Side=0
            Second_Seat_Left_Side=0
            Second_Seat_Middle=0
            Unknown=0
            Other_Passenger_in_enclosed_cargo_area=1
            Front_Seat_Middle=0
            Other_Passenger_in_unenclosed_cargo_area=0
            
        elif(seating_pos=='Front_Seat_Middle'):
            Front_Seat_Drivers_Side=0
            Front_Seat_Right_Side=0
            Non_Motorist=0
            Second_Seat_Right_Side=0
            Second_Seat_Left_Side=0
            Second_Seat_Middle=0
            Unknown=0
            Other_Passenger_in_enclosed_cargo_area=0
            Front_Seat_Middle=1
            Other_Passenger_in_unenclosed_cargo_area=0
            
        elif(seating_pos=='Other_Passenger_in_unenclosed_cargo_area'):
            Front_Seat_Drivers_Side=0
            Front_Seat_Right_Side=0
            Non_Motorist=0
            Second_Seat_Right_Side=0
            Second_Seat_Left_Side=0
            Second_Seat_Middle=0
            Unknown=0
            Other_Passenger_in_enclosed_cargo_area=0
            Front_Seat_Middle=0
            Other_Passenger_in_unenclosed_cargo_area=1
            
        else:
            Front_Seat_Drivers_Side=0
            Front_Seat_Right_Side=0
            Non_Motorist=0
            Second_Seat_Right_Side=0
            Second_Seat_Left_Side=0
            Second_Seat_Middle=0
            Unknown=0
            Other_Passenger_in_enclosed_cargo_area=0
            Front_Seat_Middle=0
            Other_Passenger_in_unenclosed_cargo_area=0    


        restraint_sys = request.form["RESTRAINT_SYSTEM_USE"]
        if (restraint_sys == 'None_Used'):
            None_Used=1
            Lap_and_Shoulder_Belt=0
            Unknown=0
            Restraint_Used_Type_Unknown=0
            Lap_Belt=0
            Motorcycle_Helmet=0
            Child_Safety_Seat=0
            Shoulder_Belt=0
            Safety_Belt_Used_Improperly=0
            Child_Safety_Seat_Used_Improperly=0
        
        elif (restraint_sys == 'Lap_and_Shoulder_Belt'):
            None_Used=0
            Lap_and_Shoulder_Belt=1
            Unknown=0
            Restraint_Used_Type_Unknown=0
            Lap_Belt=0
            Motorcycle_Helmet=0
            Child_Safety_Seat=0
            Shoulder_Belt=0
            Safety_Belt_Used_Improperly=0
            Child_Safety_Seat_Used_Improperly=0

        elif (restraint_sys == 'Unknown'):
            None_Used=0
            Lap_and_Shoulder_Belt=0
            Unknown=1
            Restraint_Used_Type_Unknown=0
            Lap_Belt=0
            Motorcycle_Helmet=0
            Child_Safety_Seat=0
            Shoulder_Belt=0
            Safety_Belt_Used_Improperly=0
            Child_Safety_Seat_Used_Improperly=0

        elif (restraint_sys == 'Restraint_Used_Type_Unknown'):
            None_Used=0
            Lap_and_Shoulder_Belt=0
            Unknown=0
            Restraint_Used_Type_Unknown=1
            Lap_Belt=0
            Motorcycle_Helmet=0
            Child_Safety_Seat=0
            Shoulder_Belt=0
            Safety_Belt_Used_Improperly=0
            Child_Safety_Seat_Used_Improperly=0

        elif (restraint_sys == 'Lap_Belt'):
            None_Used=0
            Lap_and_Shoulder_Belt=0
            Unknown=0
            Restraint_Used_Type_Unknown=0
            Lap_Belt=1
            Motorcycle_Helmet=0
            Child_Safety_Seat=0
            Shoulder_Belt=0
            Safety_Belt_Used_Improperly=0
            Child_Safety_Seat_Used_Improperly=0

        elif (restraint_sys == 'Motorcycle_Helmet'):
            None_Used=0
            Lap_and_Shoulder_Belt=0
            Unknown=0
            Restraint_Used_Type_Unknown=0
            Lap_Belt=0
            Motorcycle_Helmet=1
            Child_Safety_Seat=0
            Shoulder_Belt=0
            Safety_Belt_Used_Improperly=0
            Child_Safety_Seat_Used_Improperly=0
            
        elif (restraint_sys == 'Child_Safety_Seat'):
            None_Used=0
            Lap_and_Shoulder_Belt=0
            Unknown=0
            Restraint_Used_Type_Unknown=0
            Lap_Belt=0
            Motorcycle_Helmet=0
            Child_Safety_Seat=1
            Shoulder_Belt=0
            Safety_Belt_Used_Improperly=0
            Child_Safety_Seat_Used_Improperly=0
    
        elif (restraint_sys == 'Shoulder_Belt'):
            None_Used=0
            Lap_and_Shoulder_Belt=0
            Unknown=0
            Restraint_Used_Type_Unknown=0
            Lap_Belt=0
            Motorcycle_Helmet=0
            Child_Safety_Seat=0
            Shoulder_Belt=1
            Safety_Belt_Used_Improperly=0
            Child_Safety_Seat_Used_Improperly=0
        
        elif (restraint_sys == 'Safety_Belt_Used_Improperly'):
            None_Used=0
            Lap_and_Shoulder_Belt=0
            Unknown=0
            Restraint_Used_Type_Unknown=0
            Lap_Belt=0
            Motorcycle_Helmet=0
            Child_Safety_Seat=0
            Shoulder_Belt=0
            Safety_Belt_Used_Improperly=1
            Child_Safety_Seat_Used_Improperly=0

        elif (restraint_sys == 'Child_Safety_Seat_Used_Improperly'):
            None_Used=0
            Lap_and_Shoulder_Belt=0
            Unknown=0
            Restraint_Used_Type_Unknown=0
            Lap_Belt=0
            Motorcycle_Helmet=0
            Child_Safety_Seat=0
            Shoulder_Belt=0
            Safety_Belt_Used_Improperly=0
            Child_Safety_Seat_Used_Improperly=1
        
        else:
            None_Used=0
            Lap_and_Shoulder_Belt=0
            Unknown=0
            Restraint_Used_Type_Unknown=0
            Lap_Belt=0
            Motorcycle_Helmet=0
            Child_Safety_Seat=0
            Shoulder_Belt=0
            Safety_Belt_Used_Improperly=0
            Child_Safety_Seat_Used_Improperly=0
        
                
        air_bag = request.form["AIR_BAG_AVAILABILITY"]
        if (air_bag == 'Air_Bag_Not_Available_for_this_Seat'):
            Air_Bag_Not_Available_for_this_Seat=1
            Deployed_Air_Bag_from_Front=0
            Air_Bag_Available_but_Not_Deployed=0
            Air_Bag_Available_Deployment_Not_Known=0
            Non_Motorist=0
            Unknown=0
            Deployed_Air_Bag_Multiple_Directions=0
            Deployed_Air_Bag_from_Side=0
            Deployed_Air_Bag_Direction_Unknown=0
            Air_Bag_Available_and_Switched_Off=0
            
        elif (air_bag == 'Deployed_Air_Bag_from_Front'):
            Air_Bag_Not_Available_for_this_Seat=0
            Deployed_Air_Bag_from_Front=1
            Air_Bag_Available_but_Not_Deployed=0
            Air_Bag_Available_Deployment_Not_Known=0
            Non_Motorist=0
            Unknown=0
            Deployed_Air_Bag_Multiple_Directions=0
            Deployed_Air_Bag_from_Side=0
            Deployed_Air_Bag_Direction_Unknown=0
            Air_Bag_Available_and_Switched_Off=0
            
        elif (air_bag == 'Air_Bag_Available_but_Not_Deployed'):
            Air_Bag_Not_Available_for_this_Seat=0
            Deployed_Air_Bag_from_Front=0
            Air_Bag_Available_but_Not_Deployed=1
            Air_Bag_Available_Deployment_Not_Known=0
            Non_Motorist=0
            Unknown=0
            Deployed_Air_Bag_Multiple_Directions=0
            Deployed_Air_Bag_from_Side=0
            Deployed_Air_Bag_Direction_Unknown=0
            Air_Bag_Available_and_Switched_Off=0
            
        elif (air_bag == 'Air_Bag_Available_Deployment_Not_Known'):
            Air_Bag_Not_Available_for_this_Seat=0
            Deployed_Air_Bag_from_Front=0
            Air_Bag_Available_but_Not_Deployed=0
            Air_Bag_Available_Deployment_Not_Known=1
            Non_Motorist=0
            Unknown=0
            Deployed_Air_Bag_Multiple_Directions=0
            Deployed_Air_Bag_from_Side=0
            Deployed_Air_Bag_Direction_Unknown=0
            Air_Bag_Available_and_Switched_Off=0
            
        elif (air_bag == 'Non_Motorist'):
            Air_Bag_Not_Available_for_this_Seat=0
            Deployed_Air_Bag_from_Front=0
            Air_Bag_Available_but_Not_Deployed=0
            Air_Bag_Available_Deployment_Not_Known=0
            Non_Motorist=1
            Unknown=0
            Deployed_Air_Bag_Multiple_Directions=0
            Deployed_Air_Bag_from_Side=0
            Deployed_Air_Bag_Direction_Unknown=0
            Air_Bag_Available_and_Switched_Off=0
            
        elif (air_bag == 'Unknown'):
            Air_Bag_Not_Available_for_this_Seat=0
            Deployed_Air_Bag_from_Front=0
            Air_Bag_Available_but_Not_Deployed=0
            Air_Bag_Available_Deployment_Not_Known=0
            Non_Motorist=0
            Unknown=1
            Deployed_Air_Bag_Multiple_Directions=0
            Deployed_Air_Bag_from_Side=0
            Deployed_Air_Bag_Direction_Unknown=0
            Air_Bag_Available_and_Switched_Off=0
            
        elif (air_bag == 'Deployed_Air_Bag_Multiple_Directions'):
            Air_Bag_Not_Available_for_this_Seat=0
            Deployed_Air_Bag_from_Front=0
            Air_Bag_Available_but_Not_Deployed=0
            Air_Bag_Available_Deployment_Not_Known=0
            Non_Motorist=0
            Unknown=0
            Deployed_Air_Bag_Multiple_Directions=1
            Deployed_Air_Bag_from_Side=0
            Deployed_Air_Bag_Direction_Unknown=0
            Air_Bag_Available_and_Switched_Off=0
            
        elif (air_bag == 'Deployed_Air_Bag_from_Side'):
            Air_Bag_Not_Available_for_this_Seat=0
            Deployed_Air_Bag_from_Front=0
            Air_Bag_Available_but_Not_Deployed=0
            Air_Bag_Available_Deployment_Not_Known=0
            Non_Motorist=0
            Unknown=0
            Deployed_Air_Bag_Multiple_Directions=0
            Deployed_Air_Bag_from_Side=1
            Deployed_Air_Bag_Direction_Unknown=0
            Air_Bag_Available_and_Switched_Off=0
            
        elif (air_bag == 'Deployed_Air_Bag_Direction_Unknown'):
            Air_Bag_Not_Available_for_this_Seat=0
            Deployed_Air_Bag_from_Front=0
            Air_Bag_Available_but_Not_Deployed=0
            Air_Bag_Available_Deployment_Not_Known=0
            Non_Motorist=0
            Unknown=0
            Deployed_Air_Bag_Multiple_Directions=0
            Deployed_Air_Bag_from_Side=0
            Deployed_Air_Bag_Direction_Unknown=1
            Air_Bag_Available_and_Switched_Off=0
            
        elif (air_bag == 'Air_Bag_Available_and_Switched_Off'):
            Air_Bag_Not_Available_for_this_Seat=0
            Deployed_Air_Bag_from_Front=1
            Air_Bag_Available_but_Not_Deployed=0
            Air_Bag_Available_Deployment_Not_Known=0
            Non_Motorist=0
            Unknown=0
            Deployed_Air_Bag_Multiple_Directions=0
            Deployed_Air_Bag_from_Side=0
            Deployed_Air_Bag_Direction_Unknown=0
            Air_Bag_Available_and_Switched_Off=1
            
        else:
            Air_Bag_Not_Available_for_this_Seat=0
            Deployed_Air_Bag_from_Front=0
            Air_Bag_Available_but_Not_Deployed=0
            Air_Bag_Available_Deployment_Not_Known=0
            Non_Motorist=0
            Unknown=0
            Deployed_Air_Bag_Multiple_Directions=0
            Deployed_Air_Bag_from_Side=0
            Deployed_Air_Bag_Direction_Unknown=0
            Air_Bag_Available_and_Switched_Off=0    
            
        '''Not_Ejected,Totally_Ejected,Partially_Ejected,Unknown'''
        
        ejection = request.form['EJECTION']
        if (ejection == 'Not_Ejected'):
            Not_Ejected =1 
            Totally_Ejected=0
            Partially_Ejected=0
            Unknown=0
            
        elif (ejection == 'Totally_Ejected'):
            Not_Ejected =0
            Totally_Ejected=1
            Partially_Ejected=0
            Unknown=0
            
        elif (ejection == 'Partially_Ejected'):
            Not_Ejected =0
            Totally_Ejected=0
            Partially_Ejected=1
            Unknown=0
            
        elif (ejection == 'Unknown'):
            Not_Ejected =0
            Totally_Ejected=0
            Partially_Ejected=0
            Unknown=1
            
        else:
            Not_Ejected =0
            Totally_Ejected=0
            Partially_Ejected=0
            Unknown=0
               
        non_motorist = request.form["NON_MOTORIST_LOCATION"]
        if (non_motorist == 'Not_Applicable_Vehicle_Occupant'):
            Not_Applicable_Vehicle_Occupant=1
            Non_Intersection_On_Roadway_Crosswalk_not_Available=0
            Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Non_Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_On_Road_Shoulder=0
            Intersection_In_Crosswalk=0
            Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_Other_Not_a_Roadway=0
            Intersection_On_Roadway_Crosswalk_not_Available=0
            
        elif (non_motorist == 'Non_Intersection_On_Roadway_Crosswalk_not_Available'):
            Not_Applicable_Vehicle_Occupant=0
            Non_Intersection_On_Roadway_Crosswalk_not_Available=1
            Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Non_Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_On_Road_Shoulder=0
            Intersection_In_Crosswalk=0
            Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_Other_Not_a_Roadway=0
            Intersection_On_Roadway_Crosswalk_not_Available=0
            
        elif (non_motorist == 'Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown'):
            Not_Applicable_Vehicle_Occupant=0
            Non_Intersection_On_Roadway_Crosswalk_not_Available=0
            Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown=1
            Non_Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_On_Road_Shoulder=0
            Intersection_In_Crosswalk=0
            Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_Other_Not_a_Roadway=0
            Intersection_On_Roadway_Crosswalk_not_Available=0
            
        elif (non_motorist == 'Non_Intersection_On_Roadway_Not_in_Crosswalk'):
            Not_Applicable_Vehicle_Occupant=0
            Non_Intersection_On_Roadway_Crosswalk_not_Available=0
            Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Non_Intersection_On_Roadway_Not_in_Crosswalk=1
            Non_Intersection_On_Road_Shoulder=0
            Intersection_In_Crosswalk=0
            Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_Other_Not_a_Roadway=0
            Intersection_On_Roadway_Crosswalk_not_Available=0
            
        elif (non_motorist == 'Non_Intersection_On_Road_Shoulder'):
            Not_Applicable_Vehicle_Occupant=0
            Non_Intersection_On_Roadway_Crosswalk_not_Available=0
            Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Non_Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_On_Road_Shoulder=1
            Intersection_In_Crosswalk=0
            Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_Other_Not_a_Roadway=0
            Intersection_On_Roadway_Crosswalk_not_Available=0
            
        elif (non_motorist == 'Intersection_In_Crosswalk'):
            Not_Applicable_Vehicle_Occupant=0
            Non_Intersection_On_Roadway_Crosswalk_not_Available=0
            Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Non_Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_On_Road_Shoulder=0
            Intersection_In_Crosswalk=1
            Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_Other_Not_a_Roadway=0
            Intersection_On_Roadway_Crosswalk_not_Available=0
            
        elif (non_motorist == 'Intersection_On_Roadway_Crosswalk_Availability_Unknown'):
            Not_Applicable_Vehicle_Occupant=0
            Non_Intersection_On_Roadway_Crosswalk_not_Available=0
            Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Non_Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_On_Road_Shoulder=0
            Intersection_In_Crosswalk=0
            Intersection_On_Roadway_Crosswalk_Availability_Unknown=1
            Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_Other_Not_a_Roadway=0
            Intersection_On_Roadway_Crosswalk_not_Available=0
            
        elif (non_motorist == 'Intersection_On_Roadway_Not_in_Crosswalk'):
            Not_Applicable_Vehicle_Occupant=0
            Non_Intersection_On_Roadway_Crosswalk_not_Available=0
            Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Non_Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_On_Road_Shoulder=0
            Intersection_In_Crosswalk=0
            Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Intersection_On_Roadway_Not_in_Crosswalk=1
            Non_Intersection_Other_Not_a_Roadway=0
            Intersection_On_Roadway_Crosswalk_not_Available=0
        
        elif (non_motorist == 'Non_Intersection_Other_Not_a_Roadway'):
            Not_Applicable_Vehicle_Occupant=0
            Non_Intersection_On_Roadway_Crosswalk_not_Available=0
            Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Non_Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_On_Road_Shoulder=0
            Intersection_In_Crosswalk=0
            Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_Other_Not_a_Roadway=1
            Intersection_On_Roadway_Crosswalk_not_Available=0
        
        elif (non_motorist == 'Intersection_On_Roadway_Crosswalk_not_Available'):
            Not_Applicable_Vehicle_Occupant=0
            Non_Intersection_On_Roadway_Crosswalk_not_Available=0
            Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Non_Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_On_Road_Shoulder=0
            Intersection_In_Crosswalk=0
            Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_Other_Not_a_Roadway=0
            Intersection_On_Roadway_Crosswalk_not_Available=1
            
        else:
            Not_Applicable_Vehicle_Occupant=0
            Non_Intersection_On_Roadway_Crosswalk_not_Available=0
            Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Non_Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_On_Road_Shoulder=0
            Intersection_In_Crosswalk=0
            Intersection_On_Roadway_Crosswalk_Availability_Unknown=0
            Intersection_On_Roadway_Not_in_Crosswalk=0
            Non_Intersection_Other_Not_a_Roadway=0
            Intersection_On_Roadway_Crosswalk_not_Available=0 
            
            
        police_report_alco = request.form['POLICE_REPORTED_ALCOHOL_INVOLVEMENT']  
        if (police_report_alco=='Not_reported'):
            Not_reported=1
            No=0
            Unknown=0
            Yes=0
            
        elif (police_report_alco=='No'):
            Not_reported=0
            No=1
            Unknown=0
            Yes=0
            
        elif (police_report_alco=='Unknown'):
            Not_reported=0
            No=0
            Unknown=1
            Yes=0
            
        elif (police_report_alco=='Yes'):
            Not_reported=0
            No=0
            Unknown=0
            Yes=1
        
        else:
            Not_reported=0
            No=0
            Unknown=0
            Yes=0
                               
           
        alcohol_test_type = request.form['ALCOHOL_TEST_TYPE']
        if (alcohol_test_type=='Not_Tested_for_Alcohol'):
            Not_Tested_for_Alcohol=1
            Whole_Blood=0
            Unknown=0
            Breath_BAC=0
            Other_Test_Type=0
            Urine=0
            Vitreous=0
            Blood_Plasma_or_Serum=0
            Liver=0
            Blood_Clot=0
        
        elif (alcohol_test_type=='Whole_Blood'):
            Not_Tested_for_Alcohol=0
            Whole_Blood=1
            Unknown=0
            Breath_BAC=0
            Other_Test_Type=0
            Urine=0
            Vitreous=0
            Blood_Plasma_or_Serum=0
            Liver=0
            Blood_Clot=0
        
        elif (alcohol_test_type=='Unknown'):
            Not_Tested_for_Alcohol=0
            Whole_Blood=0
            Unknown=1
            Breath_BAC=0
            Other_Test_Type=0
            Urine=0
            Vitreous=0
            Blood_Plasma_or_Serum=0
            Liver=0
            Blood_Clot=0
        
        elif (alcohol_test_type=='Breath_BAC'):
            Not_Tested_for_Alcohol=0
            Whole_Blood=0
            Unknown=0
            Breath_BAC=1
            Other_Test_Type=0
            Urine=0
            Vitreous=0
            Blood_Plasma_or_Serum=0
            Liver=0
            Blood_Clot=0
            
        elif (alcohol_test_type=='Other_Test_Type'):
            Not_Tested_for_Alcohol=0
            Whole_Blood=0
            Unknown=0
            Breath_BAC=0
            Other_Test_Type=1
            Urine=0
            Vitreous=0
            Blood_Plasma_or_Serum=0
            Liver=0
            Blood_Clot=0
            
        elif (alcohol_test_type=='Urine'):
            Not_Tested_for_Alcohol=0
            Whole_Blood=0
            Unknown=0
            Breath_BAC=0
            Other_Test_Type=0
            Urine=1
            Vitreous=0
            Blood_Plasma_or_Serum=0
            Liver=0
            Blood_Clot=0
            
        elif (alcohol_test_type=='Vitreous'):
            Not_Tested_for_Alcohol=0
            Whole_Blood=0
            Unknown=0
            Breath_BAC=0
            Other_Test_Type=0
            Urine=0
            Vitreous=1
            Blood_Plasma_or_Serum=0
            Liver=0
            Blood_Clot=0
               
            
        elif (alcohol_test_type=='Blood_Plasma_or_Serum'):
            Not_Tested_for_Alcohol=0
            Whole_Blood=0
            Unknown=0
            Breath_BAC=0
            Other_Test_Type=0
            Urine=0
            Vitreous=0
            Blood_Plasma_or_Serum=1
            Liver=0
            Blood_Clot=0
            
        elif (alcohol_test_type=='Liver'):
            Not_Tested_for_Alcohol=0
            Whole_Blood=0
            Unknown=0
            Breath_BAC=0
            Other_Test_Type=0
            Urine=0
            Vitreous=0
            Blood_Plasma_or_Serum=0
            Liver=1
            Blood_Clot=0
            
        elif (alcohol_test_type=='Blood_Clot'):
            Not_Tested_for_Alcohol=0
            Whole_Blood=0
            Unknown=0
            Breath_BAC=0
            Other_Test_Type=0
            Urine=0
            Vitreous=0
            Blood_Plasma_or_Serum=0
            Liver=0
            Blood_Clot=1
        
        '''Not_Reported,No_Drugs,Reported_Unknown,Drugs_Involved'''
        
        police_drug_report = request.form['POLICE_REPORTED_DRUG_INVOLVEMENT']
        if (police_drug_report=='Not_Reported'):
            Not_Reported=1
            No_Drugs=0
            Reported_Unknown=0
            Drugs_Involved=0
        
        elif (police_drug_report=='No_Drugs'):
            Not_Reported=0
            No_Drugs=1
            Reported_Unknown=0
            Drugs_Involved=0
            
        elif (police_drug_report=='Reported_Unknown'):
            Not_Reported=0
            No_Drugs=0
            Reported_Unknown=1
            Drugs_Involved=0
            
        elif (police_drug_report=='Drugs_Involved'):
            Not_Reported=0
            No_Drugs=0
            Reported_Unknown=0
            Drugs_Involved=1
        
        else:
            Not_Reported=0
            No_Drugs=0
            Reported_Unknown=0
            Drugs_Involved=0
            
                
        drug_test_type = request.form['DRUG_TEST_TYPE']
        if (drug_test_type=='Not_Tested_for_Drugs'):
            Not_Tested_for_Drugs=1
            Blood_Test=0
            Unknown_if_Tested_for_Drugs=0
            Urine_Test=0
            Both_Blood_and_Urine=0
            Unknown_Test_Type=0
            Other_Type_Test=0
        
        elif (drug_test_type=='Blood_Test'):
            Not_Tested_for_Drugs=0
            Blood_Test=1
            Unknown_if_Tested_for_Drugs=0
            Urine_Test=0
            Both_Blood_and_Urine=0
            Unknown_Test_Type=0
            Other_Type_Test=0
        
        elif (drug_test_type=='Unknown_if_Tested_for_Drugs'):
            Not_Tested_for_Drugs=0
            Blood_Test=0
            Unknown_if_Tested_for_Drugs=1
            Urine_Test=0
            Both_Blood_and_Urine=0
            Unknown_Test_Type=0
            Other_Type_Test=0
            
        elif (drug_test_type=='Urine_Test'):
            Not_Tested_for_Drugs=0
            Blood_Test=0
            Unknown_if_Tested_for_Drugs=0
            Urine_Test=1
            Both_Blood_and_Urine=0
            Unknown_Test_Type=0
            Other_Type_Test=0
            
        elif (drug_test_type=='Both_Blood_and_Urine'):
            Not_Tested_for_Drugs=0
            Blood_Test=0
            Unknown_if_Tested_for_Drugs=0
            Urine_Test=0
            Both_Blood_and_Urine=1
            Unknown_Test_Type=0
            Other_Type_Test=0
            
        elif (drug_test_type=='Unknown_Test_Type'):
            Not_Tested_for_Drugs=0
            Blood_Test=0
            Unknown_if_Tested_for_Drugs=0
            Urine_Test=0
            Both_Blood_and_Urine=0
            Unknown_Test_Type=1
            Other_Type_Test=0
        
        elif (drug_test_type=='Other_Type_Test'):
            Not_Tested_for_Drugs=0
            Blood_Test=0
            Unknown_if_Tested_for_Drugs=0
            Urine_Test=0
            Both_Blood_and_Urine=0
            Unknown_Test_Type=0
            Other_Type_Test=1
        
        else:
            Not_Tested_for_Drugs=0
            Blood_Test=0
            Unknown_if_Tested_for_Drugs=0
            Urine_Test=0
            Both_Blood_and_Urine=0
            Unknown_Test_Type=0
            Other_Type_Test=0
          
        #Yes,No,Unknown,
       
        hospital_taken =request.form['TAKEN_TO_HOSPITAL']
        if (hospital_taken=='Yes'):
            Yes=1
            No=0
            Unknown=0
            
        elif (hospital_taken=='N0'):
            Yes=0
            No=1
            Unknown=0
            
        elif (hospital_taken=='Unknown'):
            Yes=0
            No=0
            Unknown=1
        
        else:
            Yes=0
            No=0
            Unknown=1
            
            
        related_factor = request.form['RELATED_FACTOR_PERSON_LEVEL']
        if(related_factor=='Not_Applicable_Driver'):
            Not_Applicable_Driver=1
            Improper_Crossing_or_Roadway=0
            Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway=0
            Running_into_Road=0
            Not_Visible=0
            Failure_to_Yield_Right_of_Way=0
            Unknown=0
            Inattentive=0
            Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe=0
            Interfering_with_Driver=0
            
        elif(related_factor=='Improper_Crossing_or_Roadway'):
            Not_Applicable_Driver=0
            Improper_Crossing_or_Roadway=1
            Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway=0
            Running_into_Road=0
            Not_Visible=0
            Failure_to_Yield_Right_of_Way=0
            Unknown=0
            Inattentive=0
            Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe=0
            Interfering_with_Driver=0
            
        elif(related_factor=='Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway'):
            Not_Applicable_Driver=0
            Improper_Crossing_or_Roadway=0
            Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway=1
            Running_into_Road=0
            Not_Visible=0
            Failure_to_Yield_Right_of_Way=0
            Unknown=0
            Inattentive=0
            Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe=0
            Interfering_with_Driver=0
           
        elif(related_factor=='Running_into_Road'):
            Not_Applicable_Driver=0
            Improper_Crossing_or_Roadway=0
            Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway=0
            Running_into_Road=1
            Not_Visible=0
            Failure_to_Yield_Right_of_Way=0
            Unknown=0
            Inattentive=0
            Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe=0
            Interfering_with_Driver=0
            
        elif(related_factor=='Not_Visible'):
            Not_Applicable_Driver=0
            Improper_Crossing_or_Roadway=0
            Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway=0
            Running_into_Road=0
            Not_Visible=1
            Failure_to_Yield_Right_of_Way=0
            Unknown=0
            Inattentive=0
            Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe=0
            Interfering_with_Driver=0
            
        elif(related_factor=='Failure_to_Yield_Right_of_Way'):
            Not_Applicable_Driver=0
            Improper_Crossing_or_Roadway=0
            Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway=0
            Running_into_Road=0
            Not_Visible=0
            Failure_to_Yield_Right_of_Way=1
            Unknown=0
            Inattentive=0
            Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe=0
            Interfering_with_Driver=0
            
        elif(related_factor=='Unknown'):
            Not_Applicable_Driver=0
            Improper_Crossing_or_Roadway=0
            Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway=0
            Running_into_Road=0
            Not_Visible=0
            Failure_to_Yield_Right_of_Way=0
            Unknown=1
            Inattentive=0
            Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe=0
            Interfering_with_Driver=0
           
        elif(related_factor=='Inattentive'):
            Not_Applicable_Driver=0
            Improper_Crossing_or_Roadway=0
            Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway=0
            Running_into_Road=0
            Not_Visible=0
            Failure_to_Yield_Right_of_Way=0
            Unknown=0
            Inattentive=1
            Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe=0
            Interfering_with_Driver=0
            
        elif(related_factor=='Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe'):
            Not_Applicable_Driver=0
            Improper_Crossing_or_Roadway=0
            Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway=0
            Running_into_Road=0
            Not_Visible=0
            Failure_to_Yield_Right_of_Way=0
            Unknown=0
            Inattentive=0
            Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe=1
            Interfering_with_Driver=0
            
        elif(related_factor=='Interfering_with_Driver'):
            Not_Applicable_Driver=0
            Improper_Crossing_or_Roadway=0
            Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway=0
            Running_into_Road=0
            Not_Visible=0
            Failure_to_Yield_Right_of_Way=0
            Unknown=0
            Inattentive=0
            Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe=0
            Interfering_with_Driver=1
        
        else:
            Not_Applicable_Driver=0
            Improper_Crossing_or_Roadway=0
            Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway=0
            Running_into_Road=0
            Not_Visible=0
            Failure_to_Yield_Right_of_Way=0
            Unknown=0
            Inattentive=0
            Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe=0
            Interfering_with_Driver=0
        
        
        
        prediction=model.predict([[
             Age,
             Alcohol_result,
             drug_result,
        
             Male,
             Female,
             Unknown,
             
             Driver,
            Passenger_of_a_Motor_Vehicle_in_Transport,
            Pedestrian,
            Bicyclist,
            Unknown_Occupant_Type_in_a_Motor_Vehicle_in_Transport,
            Occupant_of_a_Motor_Vehicle_Not_in_Transport,
            Other_Pedestrian,
            Occupant_of_a_Non_Motor_Vehicle_Transport_Device,
            Other_Cyclist,
            Unknown_Type_of_Non_Motorist,
            
             Front_Seat_Drivers_Side,
             Front_Seat_Right_Side,
             Non_Motorist,
             Second_Seat_Right_Side,
             Second_Seat_Left_Side,
             Second_Seat_Middle,
             Unknown,
             Other_Passenger_in_enclosed_cargo_area,
             Front_Seat_Middle,
             Other_Passenger_in_unenclosed_cargo_area,
            
             None_Used,
             Lap_and_Shoulder_Belt,
             Unknown,
             Restraint_Used_Type_Unknown,
             Lap_Belt,
             Motorcycle_Helmet,
             Child_Safety_Seat,
             Shoulder_Belt,
             Safety_Belt_Used_Improperly,
             Child_Safety_Seat_Used_Improperly,
             
             Air_Bag_Not_Available_for_this_Seat,
             Deployed_Air_Bag_from_Front,
             Air_Bag_Available_but_Not_Deployed,
             Air_Bag_Available_Deployment_Not_Known,
             Non_Motorist,
             Unknown,
             Deployed_Air_Bag_Multiple_Directions,
             Deployed_Air_Bag_from_Side,
             Deployed_Air_Bag_Direction_Unknown,
             Air_Bag_Available_and_Switched_Off,
             
             Not_Ejected,
             Totally_Ejected,
             Partially_Ejected,
             Unknown,
             
             Not_Applicable_Vehicle_Occupant,
             Non_Intersection_On_Roadway_Crosswalk_not_Available,
             Non_Intersection_On_Roadway_Crosswalk_Availability_Unknown,
             Non_Intersection_On_Roadway_Not_in_Crosswalk,
             Non_Intersection_On_Road_Shoulder,
             Intersection_In_Crosswalk,
             Intersection_On_Roadway_Crosswalk_Availability_Unknown,
             Intersection_On_Roadway_Not_in_Crosswalk,
             Non_Intersection_Other_Not_a_Roadway,
             Intersection_On_Roadway_Crosswalk_not_Available,
             
             Not_reported,
             No,
             Unknown,
             Yes,
            
             Not_Tested_for_Alcohol,
             Whole_Blood,
             Unknown,
             Breath_BAC,
             Other_Test_Type,
             Urine,
             Vitreous,
             Blood_Plasma_or_Serum,
             Liver,
             Blood_Clot,
             
             Not_Reported,
             No_Drugs,
             Reported_Unknown,
             Drugs_Involved,
             
             Not_Tested_for_Drugs,
             Blood_Test,
             Unknown_if_Tested_for_Drugs,
             Urine_Test,
             Both_Blood_and_Urine,
             Unknown_Test_Type,
             Other_Type_Test,
            
             Yes,
             No,
             Unknown,
             
             Not_Applicable_Driver,
            Improper_Crossing_or_Roadway,
            Walking_or_Riding_with_or_Against_Traffic_or_Playing_in_Roadway,
            Running_into_Road,
            Not_Visible,
            Failure_to_Yield_Right_of_Way,
            Unknown,
            Inattentive,
            Failure_to_Obey_Traffic_Sign_Traffic_Officers_Failure_to_Observe,
            Interfering_with_Driver,
        ]])

        output = [np.argmax(i) for i in prediction]
    
        categories=['Died prior to accident',
                               'Fatal Injury',
                               'Incapaciting Injury',
                               'Injured Severity Unknown',
                               'No Injury',
                               'Non-Incapaciting Evident Injury',
                               'Possible Injury',
                               'Unknown'
                        ]
        
        output=categories[output[0]]
        

        return render_template('home.html',prediction_text="The Injury Severity is: {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)


