from src.controllers.profiles_controller import profile
from src.controllers.user_controller import auth
from src.controllers.profile_images_controller import profile_images
from src.controllers.contract_controller import contract
from src.controllers.engagement_controller import engagement
from src.controllers.message_controller import message


registerable_controllers = [
    auth,
    profile,
    profile_images,
    contract,
    message,
    engagement

]       