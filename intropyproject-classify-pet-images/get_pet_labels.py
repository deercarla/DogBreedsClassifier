#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: de Erausquin, Carla
# DATE CREATED: 20/05/2024
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
import os
import logging
# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    # 0) Configure logging:
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # 1) Getting the images names:
    try:
        dog_images_names = os.listdir(image_dir)
    except FileNotFoundError:
        logger.error(f"Error: File '{image_dir}' not found.")

    # 2) Defining aux function that gets the dog breed from file name:
    def get_dog_breed_from_file_name(file_name):
        # Getting the file name as lower:
        file_name_lower_list = file_name.lower().split('_')

        # Deleting the .image_type and number unwanted parts:
        breed_parts = file_name_lower_list[:-1]

        # Keeping what is important (dog breed):
        breed_name = [' '.join(breed_parts)]
        return breed_name

    # 3) Creating dict:
    dog_images_names_dict = {file_name: get_dog_breed_from_file_name(file_name) for file_name in dog_images_names}

    return dog_images_names_dict