import cv2

def does_intersect():
    return True

def get_neighbors(anchor_key, dictionary, neighborhood_coordinates):
    neighbors = []
    for key, value in dictionary.items():
        if key != anchor_key:
            row_min = value["segment_info"]["row_min"]
            row_max = value["segment_info"]["row_max"]
            column_min = value["segment_info"]["column_min"]
            column_max = value["segment_info"]["column_max"]

            if((neighborhood_coordinates[0] <= row_min <= neighborhood_coordinates[1])\
                or (neighborhood_coordinates[0] <= row_max <= neighborhood_coordinates[1]))\
                and ((neighborhood_coordinates[2] <= column_min <= neighborhood_coordinates[3])\
                or (neighborhood_coordinates[2] <= column_max <= neighborhood_coordinates[3])):
                    neighbors.append(key)
    return neighbors

def get_neighborhood_area(img_coordinates, k, value):
    print("img_coordinates", img_coordinates)
    # neighborhood row/column min/max
    neighborhood_row_min = max(value["segment_info"]["row_min"] - k, img_coordinates[0])
    neighborhood_row_max = min(value["segment_info"]["row_max"] + k, img_coordinates[1])
    neighborhood_column_min = max(value["segment_info"]["column_min"] - k, img_coordinates[2])
    neighborhood_column_max = min(value["segment_info"]["column_max"] + k, img_coordinates[3])

    return [neighborhood_row_min, neighborhood_row_max, neighborhood_column_min, neighborhood_column_max]

def analyze_proximity(dictionary, image_file):
    k = 100 # proximity factor
    img = cv2.imread(image_file)

    # image row/column min/max
    img_row_min = 0
    img_row_max = img.shape[0] - 1
    img_column_min = 0
    img_column_max = img.shape[1] - 1
    img_coordinates = [img_row_min, img_row_max, img_column_min, img_column_max]

    for key, value in dictionary.items():
        print("key: ", key)
        print("content:", value["segment_info"]["content"])
        neighborhood_coordinates = get_neighborhood_area(img_coordinates, k, value)
        print("neighborhood_coordinates", neighborhood_coordinates)
        neighbors = get_neighbors(key, dictionary, neighborhood_coordinates)
        print("neighbors: ", neighbors)
