from src.controllers.profiles_controller import profile
from src.controllers.user_controller import auth
from src.controllers.profile_images_controller import profile_images


registerable_controllers = [
    auth,
    profile,
    profile_images,

]       