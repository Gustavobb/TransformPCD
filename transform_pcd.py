import numpy as np

class Quaternion:
    def __init__(self, qi, qj, qk, qr):
        self.qi = qi
        self.qj = qj
        self.qk = qk
        self.qr = qr

    def get_matrix(self):
        return np.matrix([
            [1 - 2 * (self.qj ** 2 + self.qk ** 2), 2 * (self.qi * self.qj - self.qk * self.qr), 2 * (self.qi * self.qk + self.qj * self.qr), 0], 
            [2 * (self.qi * self.qj + self.qk * self.qr), 1 - 2 * (self.qi ** 2 + self.qk ** 2), 2 * (self.qj * self.qk - self.qi * self.qr), 0],
            [2 * (self.qi * self.qk - self.qj * self.qr), 2 * (self.qj * self.qk + self.qi * self.qr), 1 - 2 * (self.qi ** 2 + self.qj ** 2), 0],
            [0, 0, 0, 1]
        ])

class Translation:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_matrix(self):
        return np.matrix([
            [1, 0, 0, self.x],
            [0, 1, 0, self.y],
            [0, 0, 1, self.z],
            [0, 0, 0, 1]
        ])

class EuclidianTransform:
    def __init__(self, translation, quaternion):
        self.t = translation
        self.q = quaternion

    def get_matrix(self):
        return self.t.get_matrix() * self.q.get_matrix()

def transform_and_save_pcd(euclidianTransform, file_path, save_path):
    transform_matrix = euclidianTransform.get_matrix()
    print("\nEuclidian Transform Process Started")

    with open(save_path, 'w') as save_file:
        with open(file_path, 'r') as read_file:
            print('Reading file...')
            for i in range(11):
                save_file.write(read_file.readline())

            print('Transforming...')
            for line in read_file:
                atributes = line.split(' ')
                x = float(atributes[0])
                y = float(atributes[1])
                z = float(atributes[2])
                w = 1.0

                point = np.matrix([[x], [y], [z], [w]])
                transformed_point = transform_matrix * point
                save_file.write(str(transformed_point[0, 0]) + ' ' + str(transformed_point[1, 0]) + ' ' + str(transformed_point[2, 0]) + ' '.join(atributes[2:]))
    
    print('Done!')

def transform_and_return_array(euclidianTransform, file_path):
    transform_matrix = euclidianTransform.get_matrix()
    return_array = []
    print("\nEuclidian Transform Process Started")

    with open(file_path, 'r') as read_file:
        print('Reading file...')
        for i in range(11):
            read_file.readline()

        print('Transforming...')
        for line in read_file:
            atributes = line.split(' ')
            x = float(atributes[0])
            y = float(atributes[1])
            z = float(atributes[2])
            w = 1.0

            point = np.matrix([[x], [y], [z], [w]])
            transformed_point = transform_matrix * point
            return_array += [[transformed_point[0, 0], transformed_point[1, 0], transformed_point[2, 0]]]
    
    print('Done!')
    return np.array(return_array)