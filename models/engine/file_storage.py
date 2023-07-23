def reload(self):
    """Loads storage dictionary from file"""
    from models.base_model import BaseModel
    from models.user import User
    from models.place import Place
    from models.state import State
    from models.city import City
    from models.amenity import Amenity
    from models.review import Review

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    try:
        with open(self.__file_path, 'r') as f:
            temp = json.load(f)
            for key, val in temp.items():
                cls_name = val['__class__']
                if cls_name in classes:
                    self.__objects[key] = classes[cls_name](**val)
    except FileNotFoundError:
        pass

