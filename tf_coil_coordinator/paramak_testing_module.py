"""
The module contains testing functions for Paramak use. It calculates the 
"""
from tf_coil_coordinator import find_points
from math import pi

def surface_area(lower_left,middle_right,thickness,extrusion_length,test=False,XZ_face_only=False,extrusion_area_only=False):
    """
    Function calculates the total surface area of the TF coil from the coordinates given in the find_points function
    """
    ### Define the basic parameters for the TF coil using the analyse argument for find_points
    base, height, inner_rad, outter_rad = find_points(lower_left,middle_right,thickness,test=False,line_type=False,analyse=True)
    
    # The surface area of the face in XZ plane is divisible into 5 segments
    base_segment_area = thickness * (base - inner_rad)
    vertical_segment_area = thickness * (height - (inner_rad * 2))
    corner_area = (pi/4) * (outter_rad**2 - inner_rad**2)
    
    total_face_area = base_segment_area*2 + vertical_segment_area + corner_area*2

    # The surface area of the planes in YZ plane
    contour_length = inner_rad * (pi - 8) + pi * outter_rad + 2 * (2*base + thickness + height)
    extrusion_area = contour_length * extrusion_length
 
    total_bounding_surface = total_face_area*2 + extrusion_area
    
    ### pytest.approx() good to approximate values

    if test == True:
        print("Self testing:\nCalculated parameters:\nbase: {}\nheight: {}\ninner radius: {}\noutter radius: {}\nContour length: {}".format(base,height,inner_rad,outter_rad,contour_length))

    if XZ_face_only == True:
        if test == True:
            print("Face area = {}".format(total_face_area))
        return total_face_area
    
    elif extrusion_area_only == True:
        if test == True:
            print("Extrusion area = {}".format(extrusion_area))
        return extrusion_area

    else:
        if test == True:
            print("Total Surface area = {}".format(total_bounding_surface))
        return total_bounding_surface


def volume(lower_left,middle_right,thickness,extrusion_length,test=False):
    """
    The function calculates the volume from the given coordinates used for parametarising the component in find_points function in core module
    it takes an additional variable for extrusion length which is the thickness of the coil
    """
    face_area = surface_area(lower_left,middle_right,thickness,extrusion_length,test=False,XZ_face_only=True)
    
    if test == True:
        print("Self testing:\nArea of the XZ plane face:\n", face_area)

    total_shape_volume = face_area * extrusion_length

    return total_shape_volume

if __name__ == "__main__":
    print("Area testing:")
    surface_area((50,0), (100,100), 20, 10, test=True)
    print("\nVolume testing:")
    volume((50,0), (100,100), 20, 10, test=True)
    