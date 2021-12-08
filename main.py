import transform_pcd

def main():
    # usage example:
    # python3 main.py

    # get the path to the pcd file
    file_path = r'C:\Users\gubeb\Documents\TransformPCD\pcd_test.pcd'

    # create a quaternion 
    q = transform_pcd.Quaternion(0.000, 0.707, 0.000, 0.707)

    # create a translation vector
    t = transform_pcd.Translation(0, 0, 6)

    # create a euclidian transform
    euclidian_transform = transform_pcd.EuclidianTransform(t, q)

    # transform the point cloud and save it
    transform_pcd.transform_and_save_pcd(euclidian_transform, file_path, r'C:\Users\gubeb\Documents\TransformPCD\pcd_test_result.pcd')

    # or transform the point cloud and get the array of points
    points = transform_pcd.transform_and_return_array(euclidian_transform, file_path)
    print(points)

if __name__ == "__main__":
    main()