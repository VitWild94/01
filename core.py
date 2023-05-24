import vk_api
from config import acces_token
from vk_api.exceptions import ApiError


class VkTools():
    def __init__(self, token):
        self.ext_api = vk_api.VkApi(token=token)

    def get_profile_info(self, user_id):
        try:
            info = self.ext_api.method('users.get',
                                       {
                                           'user_id': user_id,
                                           'fields': 'bdate,city,sex,relation'
                                       }
                                       )

        except ApiError:
            return

        return info

    def user_serch(self, city_id, age_from, age_to, sex, offset=None):
        try:
            profiles = self.ext_api.method('users.serch',
                                           {
                                               'city_id': city_id,
                                               'aga_from': age_from,
                                               'age_to': age_to,
                                               'sex': sex,
                                               'count': 1000,
                                               'offset': offset
                                           }
                                           )

        except ApiError:
            return

        profiles = profiles['items']

        result = []
        for profile in profiles:
            if profile['is_closed'] == False:
                result.append({'name': profile['first_name'] + ' ' + profile['last_name'],
                               'if': profiles['id']
                               })
        return result

    def photos_get(self, user_id):
        photos = self.ext_api.method('photos.get',
                                     {'album_id': 'profile',
                                      'owner_id': user_id
                                      }

                                     )
        try:
            photos = photos['items']
        except KeyError:
            return

        result = []
        for num, photo in enumerate(photos):
            result.append({'owner_id': photo['owner_id'],
                           'id': photo['id']
                           })
            if num == 2:
                break

        return result


if __name__ == '__main__':
    tools = VkTools(acces_token)

    info = tools.get_profile_info(626122609)
    if info:
        ptint(tools.get_profile_info(626122609))
    else:
        pass
    print(tools.get_profile_info(626122609))
    profiles = tools.user_serch(1, 20, 40, 1)
    print(profiles)

    photos = tools.photos_get(626122609)
    print(photos)