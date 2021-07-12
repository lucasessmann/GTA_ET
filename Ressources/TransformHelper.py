import numpy as np
import pandas as pd 
from tqdm import tqdm

def apply_perspective_transform_matrix(matrix, img_size=(4096,4096), pixel_coords = None, dataframe = None, df_x_name = "", df_y_name = "", transform_x_name="transformed_map_x", transform_y_name="transformed_map_y"):
    '''
    matrix: perspective transform matrix generated with cv2.getPerspectiveTransform()
    img_size: Size of the background image. Needed, for y values since the projection generates y values starting from the top.
    pixel_coords: Pixel coordinates in source space to project into target space. Can be list of pixels.
    dataframe: Dataframe holding the source space pixel data. 
    df_x_name: Column name used for x pixel coordinates.
    df_y_name: Column name used for y pixel coordinates.
    transform_x_name: Generated column name used for x coordinates in target space.
    transform_y_name: Generated column name used for y coordinates in target space.
    Compare https://docs.opencv.org/4.5.2/da/d54/group__imgproc__transform.html#ga20f62aa3235d869c9956436c870893ae 
    '''
    
    print("Calculating Perspective Transform...")

    # Dataframe not provided 
    if dataframe is None:
    
        # One pixel passed 
        if len(np.shape(pixel_coords)) == 1:

            # Apply matrix 
            result = matrix.dot(np.float32([pixel_coords[0],pixel_coords[1],1]))

            # Remove scalar factor, generate y value starting at the bottom 
            result[0] = result[0] / result[2]
            result[1] = result[1] / result[2]
            result[1] = img_size[1] - result[1]

            return (result[0],result[1])

        # List of pixels
        else:

            # Define method from above again to be able to apply faster to list slices
            def apply_transform(arg):

                result = matrix.dot(np.float32([arg[0],arg[1],1]))
                result[0] = result[0] / result[2]
                result[1] = result[1] / result[2]
                result[1] = img_size[1] - result[1]
                return np.array([result[0],result[1]])

            # Apply to each row in the passed pixel list 
            return np.apply_along_axis(apply_transform,1,pixel_coords)
    
    # Dataframe provided 
    else:

        # Progress bar 
        tqdm.pandas()
        
        # Init transformed columns
        dataframe[transform_x_name] = np.NAN
        dataframe[transform_y_name] = np.NAN
     
        # Define method from above again to be able to apply faster to dataframe rows
        def apply_transform(arg):
            
            # Calculate transform
            result = matrix.dot(np.float32([arg[df_x_name],arg[df_y_name],1]))
            result[0] = result[0] / result[2]
            result[1] = result[1] / result[2]
            result[1] = img_size[1] - result[1]
            
            # Add result to dataframe slice
            arg[transform_x_name] = result[0]
            arg[transform_y_name] = result[1]
            
            return arg
        
            
        # Apply transform 
        dataframe = dataframe.progress_apply(lambda row: apply_transform(row), axis=1)
                                    
        return dataframe
